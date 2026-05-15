"""Per-chapter synthesizer: collect prompts (chapter spec + source chunks),
apply results (HTML fragment file → state_dir/textbook/N.html)."""
from __future__ import annotations

import json
import shutil
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from video_to_notebook.db.session import connect
from video_to_notebook.synthesize.prompts import (
    get_synthesize_style_guide,
)


def _get_language(conn) -> str:
    """Read 'language' from build_meta; default 'zh' if unset (legacy projects)."""
    row = conn.execute(
        "SELECT value FROM build_meta WHERE key='language'"
    ).fetchone()
    return row[0] if row else "zh"

SCHEMA_VERSION = "1"
DEFAULT_SYNTHESIZER_ID = "claude-code-max:v1"


def _select_chunks(conn, primary: str, all_slugs: list[str], cap: int) -> list[dict]:
    """Round-robin chunk selection across lectures, ordered by primary-concept
    coverage. SQL stays trivial; ranking lives in Python.

    Why not pure SQL: round-robin + per-lecture-score ranking is awkward as
    a single SQL with CTEs / window functions, and the data scale (≤ a few
    thousand chunks) makes Python sorting trivially fast.
    """
    # 1. Count primary-concept hits per lecture (deep-coverage signal).
    primary_hits: dict[int, int] = dict(conn.execute(
        """
        SELECT chunks.lecture_id, COUNT(*)
        FROM chunk_concepts cc
        JOIN chunks ON chunks.id = cc.chunk_id
        JOIN concepts ON concepts.id = cc.concept_id
        WHERE concepts.slug = ?
        GROUP BY chunks.lecture_id
        """,
        (primary,),
    ).fetchall())

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

    # 3. Bucket by lecture, sorted within each lecture by chunk.idx
    #    (preserves temporal order so the lecturer's narrative flows).
    by_lecture: dict[int, list[dict]] = defaultdict(list)
    for r in rows:
        by_lecture[r[1]].append({
            "chunk_id": r[0],
            "lecture_id": r[1],
            "chunk_idx": r[2],
            "start_sec": r[3],
            "text": r[4],
            "course_slug": r[5],
            "lecture_idx": r[6],
            "lecture_title": r[7],
            "video_url": r[8],
        })
    for lid in by_lecture:
        by_lecture[lid].sort(key=lambda c: c["chunk_idx"])

    # 4. Order lectures: most primary-concept coverage first.
    #    Lectures not in primary_hits (zero coverage) come last.
    lecture_order = sorted(
        by_lecture.keys(),
        key=lambda lid: (-primary_hits.get(lid, 0),
                         by_lecture[lid][0]["course_slug"],
                         by_lecture[lid][0]["lecture_idx"]),
    )

    # 5. Allocation: ONE pass of round-robin for breadth (a single chunk
    #    from each lecture, in coverage order), then remaining budget
    #    goes to the deepest-coverage lecture for narrative depth.
    #    Rationale: a chapter primarily reflects its dominant lecture's
    #    pedagogy; round-robin alone over-dilutes when there's a clear
    #    primary source.
    picked: list[dict] = []
    positions: dict[int, int] = {lid: 0 for lid in lecture_order}

    # Pass 1: breadth — 1 chunk per lecture, in primary-coverage order.
    for lid in lecture_order:
        if len(picked) >= cap:
            break
        if positions[lid] < len(by_lecture[lid]):
            picked.append(by_lecture[lid][positions[lid]])
            positions[lid] += 1

    # Pass 2+: depth — pour the rest into lectures in coverage order,
    # advancing each until exhausted before moving on.
    for lid in lecture_order:
        while len(picked) < cap and positions[lid] < len(by_lecture[lid]):
            picked.append(by_lecture[lid][positions[lid]])
            positions[lid] += 1

    # Strip internal-only fields before returning.
    return [
        {k: c[k] for k in
         ("chunk_id", "course_slug", "lecture_idx", "lecture_title",
          "video_url", "start_sec", "text")}
        for c in picked
    ]


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


def apply_synthesize_results(
    *,
    db_path: Path,
    state_dir: Path,
    results: dict[str, Any],
) -> None:
    """Read the synthesized HTML fragment, copy into state_dir/textbook/N.html,
    update curriculum_chapters row."""
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

    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT id FROM curriculum_chapters WHERE order_idx = ?",
            (chapter_order_idx,),
        ).fetchone()
        if row is None:
            raise ValueError(f"no chapter at order_idx={chapter_order_idx}")

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
