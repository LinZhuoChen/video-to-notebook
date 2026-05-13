"""In-session tag mode: collect prompts as JSON, apply decisions back to DB.

Lets Claude Max subscribers run tag inside a Claude Code conversation without
a separate Anthropic API key. The conversation flow:
  1. `course-merger tag --print-prompts ...` emits envelope to stdout
  2. Claude (conversation agent) produces decisions JSON
  3. `course-merger tag --apply-results decisions.json` writes to DB
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from course_merger.db.session import connect
from course_merger.tag.ontology import Ontology
from course_merger.tag.runner import TagReport, _untagged_chunks_query

SCHEMA_VERSION = "1"
DEFAULT_TAGGER_MODEL_ID = "claude-code-max:v1"

_MIN_CONFIDENCE = 0.5
_PROPOSED_PREFIX = "proposed:"

_TAGGER_INSTRUCTIONS = (
    "For each chunk, return 1-3 concept tags. Each tag's `slug` is either "
    "(a) one of the ontology_slugs in the envelope, or "
    "(b) prefixed `proposed:` to coin a new concept (use sparingly, "
    "<=1 per chunk). Each tag needs a `confidence` in [0.0, 1.0]; "
    "values below 0.5 are dropped. Slugs must be kebab-case English even "
    "if the chunk is Chinese or mixed-language."
)


def collect_tag_prompts(
    *,
    db_path: Path,
    ontology: Ontology,
    course_slug: str | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    sql, params = _untagged_chunks_query(course_slug)
    with connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
    if limit is not None:
        rows = rows[:limit]
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "tag_prompts",
        "ontology_slugs": [c.slug for c in ontology.concepts],
        "instructions": _TAGGER_INSTRUCTIONS,
        "chunks": [{"chunk_id": r[0], "text": r[1]} for r in rows],
    }


def apply_tag_results(
    *,
    db_path: Path,
    ontology: Ontology,
    results: dict[str, Any],
) -> TagReport:
    if results.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"tag results schema_version {results.get('schema_version')!r} "
            f"is not supported (expected {SCHEMA_VERSION!r})"
        )
    if results.get("kind") != "tag_results":
        raise ValueError(
            f"tag results kind {results.get('kind')!r} is not 'tag_results'"
        )

    tagger_model_id = results.get("tagger_model_id", DEFAULT_TAGGER_MODEL_ID)
    raw_results = results.get("results", []) or []

    chunks_tagged = 0
    tags_known_written = 0
    tags_proposed_written = 0

    with connect(db_path) as conn:
        for entry in raw_results:
            chunk_id = entry.get("chunk_id")
            if chunk_id is None:
                continue
            chunks_tagged += 1

            for tag in entry.get("tags") or []:
                slug = tag.get("slug", "")
                confidence = float(tag.get("confidence", 0.0))
                if confidence < _MIN_CONFIDENCE:
                    continue
                is_proposed = slug.startswith(_PROPOSED_PREFIX)
                clean_slug = slug[len(_PROPOSED_PREFIX):] if is_proposed else slug
                if not clean_slug:
                    continue

                if is_proposed:
                    conn.execute(
                        "INSERT OR IGNORE INTO proposed_tags "
                        "(chunk_id, raw_tag, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, clean_slug, confidence, tagger_model_id),
                    )
                    tags_proposed_written += 1
                else:
                    concept = conn.execute(
                        "SELECT id FROM concepts WHERE slug = ?", (clean_slug,)
                    ).fetchone()
                    if concept is None:
                        conn.execute(
                            "INSERT OR IGNORE INTO proposed_tags "
                            "(chunk_id, raw_tag, confidence, tagger_model) "
                            "VALUES (?, ?, ?, ?)",
                            (chunk_id, clean_slug, confidence, tagger_model_id),
                        )
                        tags_proposed_written += 1
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO chunk_concepts "
                        "(chunk_id, concept_id, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, concept[0], confidence, tagger_model_id),
                    )
                    tags_known_written += 1

    return TagReport(
        chunks_tagged=chunks_tagged,
        tags_known_written=tags_known_written,
        tags_proposed_written=tags_proposed_written,
        parse_failures=0,
    )
