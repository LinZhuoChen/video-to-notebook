"""Orchestrator: load chunks → tag via Claude → write chunk_concepts + proposed_tags."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from course_merger.db.session import connect
from course_merger.tag.claude_tagger import TagResult
from course_merger.tag.ontology import Ontology


class _TaggerLike(Protocol):
    @property
    def tagger_model_id(self) -> str: ...

    def tag_chunk(self, chunk_text: str) -> TagResult: ...


@dataclass(frozen=True, slots=True)
class TagReport:
    chunks_tagged: int
    tags_known_written: int
    tags_proposed_written: int
    parse_failures: int


def _untagged_chunks_query(course_slug: str | None) -> tuple[str, tuple]:
    base = """
        SELECT chunks.id, chunks.text
        FROM chunks
        JOIN lectures ON lectures.id = chunks.lecture_id
        JOIN courses ON courses.id = lectures.course_id
        WHERE NOT EXISTS (SELECT 1 FROM chunk_concepts WHERE chunk_concepts.chunk_id = chunks.id)
        AND NOT EXISTS (SELECT 1 FROM proposed_tags WHERE proposed_tags.chunk_id = chunks.id)
        AND lectures.status = 'ok'
    """
    params: tuple = ()
    if course_slug:
        base += " AND courses.slug = ?"
        params = (course_slug,)
    base += " ORDER BY chunks.id"
    return base, params


def run_tag(
    *,
    db_path: Path,
    tagger: _TaggerLike,
    ontology: Ontology,
    course_slug: str | None = None,
    limit: int | None = None,
) -> TagReport:
    chunks_tagged = 0
    tags_known_written = 0
    tags_proposed_written = 0
    parse_failures = 0

    with connect(db_path) as conn:
        sql, params = _untagged_chunks_query(course_slug)
        chunks = conn.execute(sql, params).fetchall()

        if limit is not None:
            chunks = chunks[:limit]

        for chunk_id, chunk_text in chunks:
            result = tagger.tag_chunk(chunk_text)
            chunks_tagged += 1
            if result.error == "parse_failure":
                parse_failures += 1
                conn.execute(
                    "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
                    "VALUES (?, '__parse_failure__', 0.0, ?)",
                    (chunk_id, tagger.tagger_model_id),
                )
                continue

            for tag in result.tags:
                if tag.is_proposed:
                    conn.execute(
                        "INSERT OR IGNORE INTO proposed_tags "
                        "(chunk_id, raw_tag, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, tag.slug, tag.confidence, tagger.tagger_model_id),
                    )
                    tags_proposed_written += 1
                else:
                    concept = conn.execute(
                        "SELECT id FROM concepts WHERE slug = ?", (tag.slug,)
                    ).fetchone()
                    if concept is None:
                        # Tagger returned a non-proposed slug we don't have a concept for.
                        # Demote to proposed so cluster pass can decide.
                        conn.execute(
                            "INSERT OR IGNORE INTO proposed_tags "
                            "(chunk_id, raw_tag, confidence, tagger_model) "
                            "VALUES (?, ?, ?, ?)",
                            (chunk_id, tag.slug, tag.confidence, tagger.tagger_model_id),
                        )
                        tags_proposed_written += 1
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO chunk_concepts "
                        "(chunk_id, concept_id, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, concept[0], tag.confidence, tagger.tagger_model_id),
                    )
                    tags_known_written += 1

    return TagReport(
        chunks_tagged=chunks_tagged,
        tags_known_written=tags_known_written,
        tags_proposed_written=tags_proposed_written,
        parse_failures=parse_failures,
    )
