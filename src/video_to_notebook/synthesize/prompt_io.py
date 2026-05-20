"""Per-chapter synthesizer: collect prompts (chapter spec + source chunks),
apply results (HTML fragment file → state_dir/textbook/N.html).

v4 (May 2026) additions vs v3:
  • Chunk preprocessing: dedupe triplicated YouTube auto-caption lines;
    filter sponsor/intro chunks; chronological-order primary sort.
  • Apply-step depth gate: weighted-body floor, structural-element
    counts, extraction-coverage check. Refuses --apply if any HARD
    RULE (see prompts.py) is unmet.
  • decisions.json now carries an `extraction` field with the Phase 1
    JSON; the apply step diffs Phase 1 items vs HTML to verify
    "every extracted item shows up in the chapter" (HARD RULE 2).
"""
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from video_to_notebook.db.session import connect
from video_to_notebook.synthesize.prompts import (
    get_synthesize_style_guide,
)


SCHEMA_VERSION = "1"
DEFAULT_SYNTHESIZER_ID = "claude-code-max:v1"


# ───────────────────────────────────────────────────────────────────────
# Chunk preprocessing (Phase 0 in v4 prompt design)
# ───────────────────────────────────────────────────────────────────────

# YouTube auto-captions triplicate every line ("hello hello hello", "below
# below below"); these patterns collapse any phrase or single word that
# repeats 2+ times in a row. Tolerant of whitespace between repeats.
_PHRASE_REPEAT = re.compile(r"(.{8,}?)(?:[\s]+\1){1,}", re.DOTALL)
_WORD_REPEAT = re.compile(r"\b(\w{2,})(?:[\s]+\1\b){1,}")
_WHITESPACE_RUN = re.compile(r"\s+")

# Phrases that mark a chunk as Vizuara sponsor/intro boilerplate. The
# "Invido AI luxury watch" pitch + Dr. Raj's standard intro both have
# multiple distinctive markers — match any one of them → sponsor.
_SPONSOR_MARKERS = (
    "invido",
    "luxury watch",
    "hyper realistic video",
    "engineering team they have built",
    "create high quality ai videos from just text prompts",
    "create highquality ai videos",
    "graduated with a phd in",
    "co-founders of vizuara",  # standard Dr. Raj intro
    "ai startup in india",  # sponsor pitch tail
    "job openings at the moment",  # sponsor pitch tail
    "i'm posting more details in the description",  # sponsor pitch tail
    "you can join their amazing team",  # sponsor pitch tail
    "i resonate with them",  # sponsor pitch tail
)

# Phrases that mark a chunk as pure greeting / course-meta chatter
# (these aren't always sponsor, but contribute no pedagogy).
_INTRO_MARKERS = (
    "welcome to this lecture in the build deep",
    "welcome to this next lecture in the build deep",
    "in the previous lecture we",  # often followed by recap-only
)


def _preprocess_chunk_text(text: str) -> str:
    """Collapse triplicated phrases AND single-word repeats + normalise whitespace.

    Idempotent. Safe to call repeatedly.
    """
    # Multi-pass collapse — sometimes the auto-caption repeats 4× and one
    # pass leaves a 2× residue. Run phrase + word patterns alternately.
    prev = None
    cur = text
    for _ in range(4):
        if cur == prev:
            break
        prev = cur
        cur = _PHRASE_REPEAT.sub(r"\1", cur)
        cur = _WORD_REPEAT.sub(r"\1", cur)
    cur = _WHITESPACE_RUN.sub(" ", cur).strip()
    return cur


def _is_sponsor_chunk(text: str) -> bool:
    """True if chunk is dominated by sponsor / intro boilerplate."""
    low = text.lower()
    for marker in _SPONSOR_MARKERS:
        if marker in low:
            return True
    # Heuristic: a chunk whose first 400 chars look like a greeting with
    # no technical content is treated as intro noise.
    head = low[:400]
    intro_hits = sum(1 for m in _INTRO_MARKERS if m in head)
    technical_terms = sum(
        1
        for t in (
            "attention",
            "embedding",
            "softmax",
            "matrix",
            "vector",
            "transformer",
            "kv",
            "cache",
            "head",
            "layer",
            "mlp",
            "ffn",
            "moe",
            "expert",
            "router",
            "rope",
            "rotary",
            "deepseek",
            "mla",
            "latent",
            "mha",
            "mqa",
            "gqa",
            "grpo",
            "ppo",
            "rl",
            "lora",
            "sft",
            "quantization",
            "fp8",
            "mtp",
            "注意力",
            "嵌入",
            "矩阵",
            "向量",
            "缓存",
            "潜",
            "专家",
            "推理",
            "训练",
            "梯度",
        )
        if t in low
    )
    if intro_hits >= 1 and technical_terms <= 1 and len(text) < 800:
        return True
    return False


def _select_chunks(
    conn, primary: str, all_slugs: list[str], cap: int
) -> list[dict]:
    """Round-robin chunk selection across lectures, ordered by primary-concept
    coverage and chronological lecture order.

    v4 changes from v3:
      • Apply `_preprocess_chunk_text` before any other logic (collapse
        triplicates, normalise whitespace).
      • Filter sponsor / intro chunks BEFORE selection — they're noise.
      • Primary sort = chronological by lecture_idx (not alphabetical
        course_slug) to interleave the two courses properly. The
        alphabetical-course_slug bias was a known v3 bug.
      • Sort chunks within lecture by start_sec (true narrative order),
        not chunk_idx, in case chunk_idx ordering is corrupted.
    """
    # 1. Count primary-concept hits per lecture (deep-coverage signal).
    primary_hits: dict[int, int] = dict(
        conn.execute(
            """
            SELECT chunks.lecture_id, COUNT(*)
            FROM chunk_concepts cc
            JOIN chunks ON chunks.id = cc.chunk_id
            JOIN concepts ON concepts.id = cc.concept_id
            WHERE concepts.slug = ?
            GROUP BY chunks.lecture_id
            """,
            (primary,),
        ).fetchall()
    )

    # 2. Pull every candidate chunk (any of the chapter's slugs).
    placeholders = ",".join("?" for _ in all_slugs)
    rows = conn.execute(
        f"""
        SELECT DISTINCT chunks.id, chunks.lecture_id, chunks.idx,
               chunks.start_sec, chunks.text,
               courses.slug, lectures.idx, lectures.title, lectures.video_url
        FROM chunks
        JOIN chunk_concepts cc ON cc.chunk_id = chunks.id
        JOIN concepts ON concepts.id = cc.concept_id
        JOIN lectures ON lectures.id = chunks.lecture_id
        JOIN courses ON courses.id = lectures.course_id
        WHERE concepts.slug IN ({placeholders})
        """,
        all_slugs,
    ).fetchall()

    # 3. Preprocess + filter sponsor chunks BEFORE bucketing.
    by_lecture: dict[int, list[dict]] = defaultdict(list)
    n_filtered_sponsor = 0
    for r in rows:
        raw_text = r[4]
        clean_text = _preprocess_chunk_text(raw_text)
        if _is_sponsor_chunk(clean_text):
            n_filtered_sponsor += 1
            continue
        if len(clean_text) < 80:
            # Too short to be pedagogically substantive
            continue
        by_lecture[r[1]].append(
            {
                "chunk_id": r[0],
                "lecture_id": r[1],
                "chunk_idx": r[2],
                "start_sec": r[3] or 0,
                "text": clean_text,
                "raw_text": raw_text,
                "course_slug": r[5],
                "lecture_idx": r[6],
                "lecture_title": r[7],
                "video_url": r[8],
            }
        )

    # 4. Sort chunks within each lecture by (start_sec, chunk_idx) —
    #    true narrative order so the lecturer's story flows.
    for lid in by_lecture:
        by_lecture[lid].sort(key=lambda c: (c["start_sec"], c["chunk_idx"]))

    # 5. Order lectures: most primary-concept coverage first, then by
    #    chronological lecture_idx (NOT alphabetical course_slug).
    #    For ties on coverage, prefer the course-lecture pair that
    #    naturally comes first in the curriculum.
    lecture_order = sorted(
        by_lecture.keys(),
        key=lambda lid: (
            -primary_hits.get(lid, 0),
            by_lecture[lid][0]["lecture_idx"],  # chronological, not alphabetic
            by_lecture[lid][0]["course_slug"],
        ),
    )

    # 6. Allocation: round-robin breadth, then depth.
    #    Pass 1: 1 chunk per lecture, in coverage order
    #    Pass 2+: pour the rest into the deepest-coverage lectures
    picked: list[dict] = []
    positions: dict[int, int] = {lid: 0 for lid in lecture_order}

    for lid in lecture_order:
        if len(picked) >= cap:
            break
        if positions[lid] < len(by_lecture[lid]):
            picked.append(by_lecture[lid][positions[lid]])
            positions[lid] += 1

    for lid in lecture_order:
        while len(picked) < cap and positions[lid] < len(by_lecture[lid]):
            picked.append(by_lecture[lid][positions[lid]])
            positions[lid] += 1

    return [
        {
            k: c[k]
            for k in (
                "chunk_id",
                "course_slug",
                "lecture_idx",
                "lecture_title",
                "video_url",
                "start_sec",
                "text",
            )
        }
        for c in picked
    ]


def _get_language(conn) -> str:
    """Read 'language' from build_meta; default 'zh' if unset (legacy projects)."""
    row = conn.execute(
        "SELECT value FROM build_meta WHERE key='language'"
    ).fetchone()
    return row[0] if row else "zh"


def collect_synthesize_prompts(
    *,
    db_path: Path,
    chapter_order_idx: int,
    max_source_chunks: int = 20,
) -> dict[str, Any]:
    """Build the envelope for synthesizing chapter N: chapter spec + relevant chunks."""
    with connect(db_path) as conn:
        chapter_row = conn.execute(
            """
            SELECT order_idx, module, title, blurb, primary_concept_slug,
                   related_concept_slugs
            FROM curriculum_chapters WHERE order_idx = ?
            """,
            (chapter_order_idx,),
        ).fetchone()
        if chapter_row is None:
            raise ValueError(f"no chapter at order_idx={chapter_order_idx}")

        order_idx, module, title, blurb, primary, related_json = chapter_row
        related = json.loads(related_json) if related_json else []
        all_slugs = [primary] + related

        source_chunks = _select_chunks(conn, primary, all_slugs, max_source_chunks)
        language = _get_language(conn)

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "synthesize_prompts",
        "chapter": {
            "order_idx": order_idx,
            "module": module,
            "title": title,
            "blurb": blurb,
            "primary_concept_slug": primary,
            "related_concept_slugs": related,
        },
        "source_chunks": source_chunks,
        "style_guide": get_synthesize_style_guide(language),
        "language": language,
        "output_path_hint": f".course-merger/textbook/{order_idx}.html",
    }


# ───────────────────────────────────────────────────────────────────────
# Depth-gate verification (Phase 2 in v4 prompt design)
# ───────────────────────────────────────────────────────────────────────


def _count_weighted_body(html: str) -> int:
    """Weighted body length: zh chars + en words × 2, after stripping
    code/svg/style/script tags.
    """
    cleaned = re.sub(r"<svg[^>]*>.*?</svg>", "", html, flags=re.S)
    cleaned = re.sub(r"<pre[^>]*>.*?</pre>", "", cleaned, flags=re.S)
    cleaned = re.sub(r"<style[^>]*>.*?</style>", "", cleaned, flags=re.S)
    cleaned = re.sub(r"<script[^>]*>.*?</script>", "", cleaned, flags=re.S)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    zh_chars = sum(1 for ch in cleaned if "一" <= ch <= "鿿")
    en_words = len(re.findall(r"\b[a-zA-Z][a-zA-Z\-]+\b", cleaned))
    return zh_chars + en_words * 2


def _count_structural_elements(html: str) -> dict[str, int]:
    """Count the structural elements HARD RULE 3 cares about."""
    return {
        "h2": len(re.findall(r"<h2[^>]*>", html)),
        "callout_quote": len(
            re.findall(r'<(?:div|blockquote)[^>]*class="[^"]*callout-quote', html)
        ),
        "deriv_step": len(re.findall(r'<div[^>]*class="[^"]*deriv-step', html)),
        "pre_code_py": len(
            re.findall(r"<pre[^>]*>\s*<code[^>]*python", html)
        ),
        "callout_neutral": len(
            re.findall(
                r'<div[^>]*class="[^"]*callout\s+callout-(info|note|warning|tip)', html
            )
        ),
        "svg": len(re.findall(r"<svg[^>]*viewBox", html)),
        "svg_animated": len(
            re.findall(r"@keyframes\s+\w+", html)
        ),  # any keyframes block anywhere counts
        "iframe": len(re.findall(r"<iframe[^>]*src=", html)),
        "takeaways_ul_items": _count_takeaways(html),
    }


def _count_takeaways(html: str) -> int:
    """Count items in the takeaways block (last ul.takeaways)."""
    m = re.search(
        r'<ul[^>]*class="[^"]*takeaways[^"]*"[^>]*>(.*?)</ul>', html, re.S
    )
    if not m:
        return 0
    return len(re.findall(r"<li", m.group(1)))


def _check_extraction_coverage(
    html: str, extraction: dict[str, Any]
) -> list[str]:
    """Verify every Phase 1 extraction item shows up in the HTML.

    Returns a list of missing-item descriptions (empty list = all present).
    Uses loose substring matching; a stricter version could parse the
    HTML to require quotes to be inside callout-quote blocks, etc.
    """
    missing: list[str] = []
    html_lower = html.lower()

    for i, q in enumerate(extraction.get("lecturer_verbatim_quotes", []) or []):
        target = q.get("quote_in_target_lang", "") or ""
        # Match the first 30 chars (rough fingerprint) to avoid trivial
        # rewordings counting as misses
        fingerprint = re.sub(r"\s+", " ", target).strip()[:30].lower()
        if not fingerprint:
            continue
        if fingerprint not in html_lower:
            missing.append(f"lecturer_quote #{i}: {fingerprint!r} not found")

    for i, d in enumerate(extraction.get("derivation_steps", []) or []):
        eq = (d.get("equation_latex", "") or "").strip()
        if not eq:
            continue
        # Strip braces and dollar signs for matching
        eq_clean = re.sub(r"[$\\\\{}]", "", eq)[:20]
        if eq_clean.lower() not in html_lower:
            missing.append(f"derivation_step #{i}: equation {eq!r} not found")

    for i, m in enumerate(extraction.get("metaphors", []) or []):
        phr = (m.get("lecturer_phrasing", "") or "")[:20]
        if not phr:
            continue
        if phr.lower() not in html_lower:
            missing.append(f"metaphor #{i}: {phr!r} not found")

    for i, n in enumerate(
        extraction.get("concrete_numerical_examples", []) or []
    ):
        val = (n.get("value", "") or n if isinstance(n, str) else n.get("value", ""))
        if not val:
            continue
        if val.lower() not in html_lower:
            missing.append(f"concrete_number #{i}: {val!r} not found")

    for i, mc in enumerate(
        extraction.get("common_misconceptions_lecturer_called_out", []) or []
    ):
        misc = (mc.get("misconception", "") or "")[:20]
        if not misc:
            continue
        if misc.lower() not in html_lower:
            missing.append(f"misconception #{i}: {misc!r} not found")

    return missing


def _verify_depth(
    *,
    html: str,
    extraction: dict[str, Any] | None,
    is_overview: bool,
    language: str,
) -> list[str]:
    """Run all HARD RULE checks; return list of failures (empty = pass)."""
    failures: list[str] = []

    # HARD RULE 6 — weighted body floor
    weighted = _count_weighted_body(html)
    if language == "zh":
        floor = 4000 if is_overview else 5000
    else:
        floor = 2500 if is_overview else 3000
    if weighted < floor:
        failures.append(
            f"HARD RULE 6 (weighted body): {weighted} < floor {floor}"
        )

    # HARD RULE 3 — structural elements
    elem = _count_structural_elements(html)
    overview_min_h2 = 8
    full_min_h2 = 10
    min_h2 = overview_min_h2 if is_overview else full_min_h2
    if elem["h2"] < min_h2:
        failures.append(f"HARD RULE 3a (top-level sections): {elem['h2']} < {min_h2}")
    min_quotes = 3 if is_overview else 5
    if elem["callout_quote"] < min_quotes:
        failures.append(
            f"HARD RULE 3b (callout-quote): {elem['callout_quote']} < {min_quotes}"
        )
    min_callouts = 3 if is_overview else 5
    if elem["callout_neutral"] < min_callouts:
        failures.append(
            f"HARD RULE 3e (callout info/note/warning/tip): "
            f"{elem['callout_neutral']} < {min_callouts}"
        )
    min_svg = 1 if is_overview else 2
    if elem["svg"] < min_svg:
        failures.append(f"HARD RULE 3f / 5a (svg): {elem['svg']} < {min_svg}")
    if not is_overview and elem["svg_animated"] < 1:
        failures.append(
            f"HARD RULE 5b (animated svg @keyframes): {elem['svg_animated']} < 1"
        )
    if elem["iframe"] < 1:
        failures.append(f"HARD RULE 3g (iframe embedded clip): {elem['iframe']} < 1")
    if not (5 <= elem["takeaways_ul_items"] <= 7):
        failures.append(
            f"HARD RULE 3h (takeaways block 5-7 items): "
            f"{elem['takeaways_ul_items']} items"
        )

    # HARD RULE 2 — extraction coverage (only if extraction was provided)
    if extraction is not None and not extraction.get(
        "BLOCKED_INSUFFICIENT_INPUT"
    ):
        missing = _check_extraction_coverage(html, extraction)
        if missing:
            # Cap the report to first 8 to keep messages readable
            shown = missing[:8]
            extra = (
                f" (+ {len(missing) - 8} more)" if len(missing) > 8 else ""
            )
            failures.append(
                "HARD RULE 2 (extraction coverage): items missing from HTML: "
                + "; ".join(shown)
                + extra
            )

        # HARD RULE 1c — Phase 1 minimum items
        audit = extraction.get("chunk_coverage_audit", {}) or {}
        total = audit.get("total_substantive_chunks", 0)
        with_items = audit.get("chunks_with_extracted_items", 0)
        if total > 0:
            coverage = with_items / total
            min_coverage = 0.80 if is_overview else 0.90
            if coverage < min_coverage:
                failures.append(
                    f"HARD RULE 1a (chunk coverage): {coverage:.2f} < {min_coverage}"
                )
        # Check skipped chunks have non-empty reasons
        for skip in audit.get("chunks_without_extracted_items", []) or []:
            reason = (skip.get("reason_skipped", "") or "").strip()
            if not reason:
                failures.append(
                    f"HARD RULE 1b (skipped chunk needs reason): chunk_id="
                    f"{skip.get('chunk_id', '?')}"
                )
        # Total Phase 1 items
        total_items = (
            len(extraction.get("lecturer_verbatim_quotes", []) or [])
            + len(extraction.get("metaphors", []) or [])
            + len(extraction.get("derivation_steps", []) or [])
            + len(extraction.get("concrete_numerical_examples", []) or [])
            + len(extraction.get("asides", []) or [])
            + len(
                extraction.get("common_misconceptions_lecturer_called_out", [])
                or []
            )
        )
        min_total = 15 if is_overview else 25
        if total_items < min_total:
            failures.append(
                f"HARD RULE 1c (Phase 1 total items): {total_items} < {min_total}"
            )

    return failures


def _is_overview_chapter(chapter_order_idx: int, blurb: str | None) -> bool:
    """Identify overview chapters that get a softer floor."""
    if chapter_order_idx == 1:
        return True
    if blurb and any(
        marker in blurb.lower()
        for marker in ("overview", "一览", "概览", "走进", "intro")
    ):
        return True
    return False


def apply_synthesize_results(
    *,
    db_path: Path,
    state_dir: Path,
    results: dict[str, Any],
    skip_depth_gate: bool = False,
) -> None:
    """Read the synthesized HTML fragment, run HARD RULE checks, copy
    into state_dir/textbook/N.html, update curriculum_chapters row.

    v4 change: refuse to apply unless all HARD RULEs pass.
    Pass skip_depth_gate=True to bypass (used for legacy projects /
    explicit user override; not the default).
    """
    if results.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"synthesize schema_version {results.get('schema_version')!r} unsupported"
        )
    if results.get("kind") != "synthesize_results":
        raise ValueError(
            f"synthesize kind {results.get('kind')!r} is not 'synthesize_results'"
        )

    chapter_order_idx = results["chapter_order_idx"]
    synthesizer = results.get("synthesizer", DEFAULT_SYNTHESIZER_ID)
    src_path = Path(results["html_fragment_path"])
    if not src_path.is_file():
        raise FileNotFoundError(f"html_fragment_path does not exist: {src_path}")

    html = src_path.read_text(encoding="utf-8")
    extraction = results.get("extraction")  # may be None on legacy decisions

    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT id, blurb FROM curriculum_chapters WHERE order_idx = ?",
            (chapter_order_idx,),
        ).fetchone()
        if row is None:
            raise ValueError(f"no chapter at order_idx={chapter_order_idx}")
        _, blurb = row
        language = _get_language(conn)

    is_overview = _is_overview_chapter(chapter_order_idx, blurb)

    # ─────────────────────────────────────────────────────────────
    # Gate: refuse --apply if HARD RULEs fail (unless explicit skip)
    # ─────────────────────────────────────────────────────────────
    if not skip_depth_gate:
        # If extraction marks BLOCKED_INSUFFICIENT_INPUT, the agent has
        # signalled a pipeline gap (HARD RULE 1 fallback). Refuse apply
        # and surface the blocking reason to the user.
        if extraction and extraction.get("BLOCKED_INSUFFICIENT_INPUT"):
            raise ValueError(
                f"chapter {chapter_order_idx}: synthesizer signalled "
                f"BLOCKED_INSUFFICIENT_INPUT: {extraction.get('reason', '?')}. "
                f"Fix: {extraction.get('what_to_fix', '?')}"
            )

        failures = _verify_depth(
            html=html,
            extraction=extraction,
            is_overview=is_overview,
            language=language,
        )
        if failures:
            msg_lines = [
                f"chapter {chapter_order_idx}: depth gate FAILED "
                f"({len(failures)} HARD RULE violation(s))",
                "",
            ]
            for f in failures:
                msg_lines.append(f"  • {f}")
            msg_lines.append("")
            msg_lines.append(
                "To bypass (NOT recommended; defeats the purpose of v4): "
                "pass --skip-depth-gate to synthesize --apply."
            )
            raise ValueError("\n".join(msg_lines))

    # ─────────────────────────────────────────────────────────────
    # All gates passed (or skipped) — proceed with apply.
    # ─────────────────────────────────────────────────────────────
    with connect(db_path) as conn:
        textbook_dir = state_dir / "textbook"
        textbook_dir.mkdir(parents=True, exist_ok=True)
        dst_name = f"{chapter_order_idx}.html"
        dst_path = textbook_dir / dst_name
        shutil.copyfile(src_path, dst_path)

        now = datetime.now(UTC).isoformat()
        conn.execute(
            """
            UPDATE curriculum_chapters
            SET status='synthesized',
                synthesized_path=?, synthesized_at=?,
                curriculum_designer=?
            WHERE order_idx = ?
            """,
            (dst_name, now, synthesizer, chapter_order_idx),
        )
