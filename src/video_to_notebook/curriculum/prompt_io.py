"""In-session curriculum design: collect prompts as JSON, apply chapters to DB."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from video_to_notebook.curriculum.prompts import (
    get_curriculum_instructions,
)
from video_to_notebook.db.session import connect


def _get_language(conn) -> str:
    row = conn.execute(
        "SELECT value FROM build_meta WHERE key='language'"
    ).fetchone()
    return row[0] if row else "zh"


SCHEMA_VERSION = "1"
DEFAULT_DESIGNER_ID = "claude-code-max:v1"


def collect_curriculum_prompts(
    *,
    db_path: Path,
    samples_per_concept: int = 5,
) -> dict[str, Any]:
    """Build the envelope: every concept with chunks + sample chunks per concept."""
    with connect(db_path) as conn:
        concept_rows = conn.execute(
            """
            SELECT concepts.slug, concepts.canonical_name,
                   COALESCE(concepts.description, ''),
                   COUNT(DISTINCT cc.chunk_id) AS occurrences,
                   GROUP_CONCAT(DISTINCT courses.slug) AS course_slugs
            FROM concepts
            JOIN chunk_concepts cc ON cc.concept_id = concepts.id
            JOIN chunks ON chunks.id = cc.chunk_id
            JOIN lectures ON lectures.id = chunks.lecture_id
            JOIN courses ON courses.id = lectures.course_id
            GROUP BY concepts.id
            HAVING occurrences > 0
            ORDER BY occurrences DESC
            """
        ).fetchall()

        concepts: list[dict[str, Any]] = []
        concept_chunks: dict[str, list[dict[str, Any]]] = {}
        for slug, name, desc, occurrences, courses_csv in concept_rows:
            concepts.append({
                "slug": slug,
                "canonical_name": name,
                "description": desc,
                "occurrence_count": occurrences,
                "courses": sorted((courses_csv or "").split(",")) if courses_csv else [],
            })

            chunks = conn.execute(
                """
                SELECT courses.slug, lectures.idx, chunks.text
                FROM chunks
                JOIN lectures ON lectures.id = chunks.lecture_id
                JOIN courses ON courses.id = lectures.course_id
                JOIN chunk_concepts cc ON cc.chunk_id = chunks.id
                JOIN concepts ON concepts.id = cc.concept_id
                WHERE concepts.slug = ?
                ORDER BY courses.slug, lectures.idx, chunks.idx
                LIMIT ?
                """,
                (slug, samples_per_concept),
            ).fetchall()
            concept_chunks[slug] = [
                {"course_slug": c, "lecture_idx": idx, "text": t}
                for c, idx, t in chunks
            ]

        language = _get_language(conn)

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "curriculum_prompts",
        "concepts": concepts,
        "concept_chunks": concept_chunks,
        "instructions": get_curriculum_instructions(language),
        "language": language,
    }


def apply_curriculum_results(
    *,
    db_path: Path,
    results: dict[str, Any],
) -> int:
    """Validate and write chapters into curriculum_chapters. Returns count written.

    Re-applying replaces any existing chapter at the same order_idx.
    """
    if results.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"curriculum schema_version {results.get('schema_version')!r} unsupported "
            f"(expected {SCHEMA_VERSION!r})"
        )
    if results.get("kind") != "curriculum_results":
        raise ValueError(
            f"curriculum kind {results.get('kind')!r} is not 'curriculum_results'"
        )

    designer = results.get("designer", DEFAULT_DESIGNER_ID)
    chapters = results.get("chapters", []) or []

    with connect(db_path) as conn:
        known = {r[0] for r in conn.execute("SELECT slug FROM concepts").fetchall()}
        for ch in chapters:
            slug = ch.get("primary_concept_slug", "")
            if slug not in known:
                raise ValueError(
                    f"chapter {ch.get('order_idx')}: primary_concept_slug "
                    f"{slug!r} unknown"
                )

        n_written = 0
        for ch in chapters:
            conn.execute(
                "INSERT INTO curriculum_chapters "
                "(order_idx, module, title, blurb, primary_concept_slug, "
                "related_concept_slugs, curriculum_designer, status) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, 'planned') "
                "ON CONFLICT(order_idx) DO UPDATE SET "
                "module=excluded.module, title=excluded.title, blurb=excluded.blurb, "
                "primary_concept_slug=excluded.primary_concept_slug, "
                "related_concept_slugs=excluded.related_concept_slugs, "
                "curriculum_designer=excluded.curriculum_designer",
                (
                    ch["order_idx"],
                    ch["module"],
                    ch["title"],
                    ch["blurb"],
                    ch["primary_concept_slug"],
                    json.dumps(ch.get("related_concept_slugs", [])),
                    designer,
                ),
            )
            n_written += 1

    return n_written
