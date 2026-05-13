"""Per-concept explainer: collect prompts (concept + occurrences + related),
apply results (HTML fragment file → state_dir/concepts/<slug>.html + DB row)."""
from __future__ import annotations

import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from course_merger.db.session import connect
from course_merger.explain.prompts import (
    EXPLAIN_STYLE_GUIDE,
    EXPLAINER_VERSION,
)

SCHEMA_VERSION = "1"
DEFAULT_EXPLAINER_ID = "claude-code-max:v1"


def _resolve_concept_id(conn, slug: str) -> tuple[int, str, str, list[str]]:
    row = conn.execute(
        """
        SELECT id, canonical_name, COALESCE(description, '')
        FROM concepts WHERE slug = ?
        """,
        (slug,),
    ).fetchone()
    if row is None:
        raise ValueError(f"no concept with slug={slug!r}")
    concept_id, canonical_name, description = row
    alias_rows = conn.execute(
        "SELECT alias FROM concept_aliases WHERE concept_id = ? ORDER BY alias",
        (concept_id,),
    ).fetchall()
    aliases = [r[0] for r in alias_rows]
    return concept_id, canonical_name, description, aliases


def collect_explain_prompts(
    *,
    db_path: Path,
    concept_slug: str,
    max_source_chunks: int = 12,
    max_related: int = 6,
) -> dict[str, Any]:
    """Build the envelope for explaining one concept."""
    with connect(db_path) as conn:
        concept_id, canonical_name, description, aliases = _resolve_concept_id(
            conn, concept_slug,
        )

        chunk_rows = conn.execute(
            """
            SELECT chunks.id, courses.slug, lectures.idx, lectures.title,
                   lectures.video_url, chunks.start_sec, chunks.text
            FROM chunks
            JOIN lectures ON lectures.id = chunks.lecture_id
            JOIN courses ON courses.id = lectures.course_id
            JOIN chunk_concepts cc ON cc.chunk_id = chunks.id
            WHERE cc.concept_id = ?
            ORDER BY cc.confidence DESC, courses.slug, lectures.idx, chunks.idx
            LIMIT ?
            """,
            (concept_id, max_source_chunks),
        ).fetchall()
        occurrences = [
            {
                "chunk_id": r[0],
                "course_slug": r[1],
                "lecture_idx": r[2],
                "lecture_title": r[3],
                "video_url": r[4],
                "start_sec": r[5],
                "text": r[6],
            }
            for r in chunk_rows
        ]

        # Related = other concepts that co-occur in the same chunks, weighted by
        # frequency. Skip the focal concept itself.
        related_rows = conn.execute(
            """
            SELECT c2.slug, c2.canonical_name, COUNT(*) AS shared
            FROM chunk_concepts a
            JOIN chunk_concepts b ON b.chunk_id = a.chunk_id AND b.concept_id != a.concept_id
            JOIN concepts c2 ON c2.id = b.concept_id
            WHERE a.concept_id = ?
            GROUP BY c2.id
            ORDER BY shared DESC, c2.canonical_name
            LIMIT ?
            """,
            (concept_id, max_related),
        ).fetchall()
        related_concepts = [
            {"slug": r[0], "canonical_name": r[1], "co_occurrence": r[2]}
            for r in related_rows
        ]

        # Module hint: pick the curriculum module where this concept is most
        # used as primary_concept_slug, else None.
        mod_row = conn.execute(
            """
            SELECT module FROM curriculum_chapters
            WHERE primary_concept_slug = ?
            LIMIT 1
            """,
            (concept_slug,),
        ).fetchone()
        module_hint = mod_row[0] if mod_row else None

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "explain_prompts",
        "explainer_version": EXPLAINER_VERSION,
        "concept": {
            "slug": concept_slug,
            "canonical_name": canonical_name,
            "description": description,
            "aliases": aliases,
            "module_hint": module_hint,
        },
        "occurrences": occurrences,
        "related_concepts": related_concepts,
        "style_guide": EXPLAIN_STYLE_GUIDE,
        "output_path_hint": f".course-merger/concepts/{concept_slug}.html",
    }


def apply_explain_results(
    *,
    db_path: Path,
    state_dir: Path,
    results: dict[str, Any],
) -> str:
    """Read the explainer HTML fragment, copy into state_dir/concepts/<slug>.html,
    upsert into concept_explanations. Returns the destination filename."""
    if results.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"explain schema_version {results.get('schema_version')!r} unsupported"
        )
    if results.get("kind") != "explain_results":
        raise ValueError(
            f"explain kind {results.get('kind')!r} is not 'explain_results'"
        )

    concept_slug = results["concept_slug"]
    explainer = results.get("explainer", DEFAULT_EXPLAINER_ID)
    src_path = Path(results["html_fragment_path"])
    if not src_path.is_file():
        raise FileNotFoundError(f"html_fragment_path does not exist: {src_path}")

    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT id FROM concepts WHERE slug = ?", (concept_slug,),
        ).fetchone()
        if row is None:
            raise ValueError(f"no concept with slug={concept_slug!r}")
        concept_id = row[0]

        concepts_dir = state_dir / "concepts"
        concepts_dir.mkdir(parents=True, exist_ok=True)
        dst_name = f"{concept_slug}.html"
        dst_path = concepts_dir / dst_name
        shutil.copyfile(src_path, dst_path)

        now = datetime.now(UTC).isoformat()
        conn.execute(
            """
            INSERT INTO concept_explanations
              (concept_id, html_fragment, explainer, generated_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(concept_id) DO UPDATE SET
              html_fragment=excluded.html_fragment,
              explainer=excluded.explainer,
              generated_at=excluded.generated_at
            """,
            (concept_id, dst_name, explainer, now),
        )
    return dst_name
