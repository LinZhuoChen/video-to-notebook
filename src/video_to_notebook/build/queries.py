"""Read-only SELECT queries against the v2 DB; return plain dicts."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from video_to_notebook.db.session import connect


def all_courses_with_lecture_counts(db_path: Path) -> list[dict[str, Any]]:
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT courses.id, courses.slug, courses.title, courses.platform,
                   courses.source_url, courses.added_at,
                   COUNT(lectures.id) FILTER (WHERE lectures.status = 'ok') AS lecture_count
            FROM courses
            LEFT JOIN lectures ON lectures.course_id = courses.id
            GROUP BY courses.id
            ORDER BY courses.slug
            """
        ).fetchall()
    return [
        {
            "id": r[0],
            "slug": r[1],
            "title": r[2],
            "platform": r[3],
            "source_url": r[4],
            "added_at": r[5],
            "lecture_count": r[6],
        }
        for r in rows
    ]


def lectures_for_course(db_path: Path, course_slug: str) -> list[dict[str, Any]]:
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT lectures.id, lectures.idx, lectures.title, lectures.video_url,
                   lectures.duration_sec
            FROM lectures
            JOIN courses ON courses.id = lectures.course_id
            WHERE courses.slug = ? AND lectures.status = 'ok'
            ORDER BY lectures.idx
            """,
            (course_slug,),
        ).fetchall()
    return [
        {
            "id": r[0],
            "idx": r[1],
            "title": r[2],
            "video_url": r[3],
            "duration_sec": r[4],
        }
        for r in rows
    ]


def chunks_for_lecture(db_path: Path, *, lecture_id: int) -> list[dict[str, Any]]:
    with connect(db_path) as conn:
        chunk_rows = conn.execute(
            "SELECT id, idx, start_sec, end_sec, text FROM chunks WHERE lecture_id = ? ORDER BY idx",
            (lecture_id,),
        ).fetchall()
        if not chunk_rows:
            return []
        chunk_ids = [r[0] for r in chunk_rows]
        placeholders = ",".join("?" for _ in chunk_ids)
        concept_rows = conn.execute(
            f"""
            SELECT chunk_concepts.chunk_id, concepts.slug
            FROM chunk_concepts
            JOIN concepts ON concepts.id = chunk_concepts.concept_id
            WHERE chunk_concepts.chunk_id IN ({placeholders})
            ORDER BY concepts.slug
            """,
            chunk_ids,
        ).fetchall()
    concept_map: dict[int, list[str]] = {}
    for chunk_id, slug in concept_rows:
        concept_map.setdefault(chunk_id, []).append(slug)
    return [
        {
            "id": r[0],
            "idx": r[1],
            "start_sec": r[2],
            "end_sec": r[3],
            "text": r[4],
            "concept_slugs": concept_map.get(r[0], []),
        }
        for r in chunk_rows
    ]


def all_concepts_with_counts(db_path: Path) -> list[dict[str, Any]]:
    with connect(db_path) as conn:
        concept_rows = conn.execute(
            """
            SELECT concepts.id, concepts.slug, concepts.canonical_name,
                   COALESCE(concepts.description, ''),
                   concepts.ontology_source,
                   COUNT(chunk_concepts.chunk_id) AS occurrence_count
            FROM concepts
            LEFT JOIN chunk_concepts ON chunk_concepts.concept_id = concepts.id
            GROUP BY concepts.id
            ORDER BY concepts.canonical_name
            """
        ).fetchall()
        alias_rows = conn.execute(
            "SELECT concept_id, alias FROM concept_aliases ORDER BY alias"
        ).fetchall()
    aliases_map: dict[int, list[str]] = {}
    for cid, alias in alias_rows:
        aliases_map.setdefault(cid, []).append(alias)
    return [
        {
            "id": r[0],
            "slug": r[1],
            "canonical_name": r[2],
            "description": r[3],
            "ontology_source": r[4],
            "occurrence_count": r[5],
            "aliases": aliases_map.get(r[0], []),
        }
        for r in concept_rows
    ]


def concept_occurrences(db_path: Path, concept_slug: str) -> list[dict[str, Any]]:
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT courses.slug, lectures.idx, lectures.title, lectures.video_url,
                   chunks.start_sec, chunks.end_sec, chunks.text, chunk_concepts.confidence
            FROM chunk_concepts
            JOIN concepts ON concepts.id = chunk_concepts.concept_id
            JOIN chunks ON chunks.id = chunk_concepts.chunk_id
            JOIN lectures ON lectures.id = chunks.lecture_id
            JOIN courses ON courses.id = lectures.course_id
            WHERE concepts.slug = ?
            ORDER BY courses.slug, lectures.idx, chunks.idx
            """,
            (concept_slug,),
        ).fetchall()
    return [
        {
            "course_slug": r[0],
            "lecture_idx": r[1],
            "lecture_title": r[2],
            "video_url": r[3],
            "start_sec": r[4],
            "end_sec": r[5],
            "text": r[6],
            "confidence": r[7],
        }
        for r in rows
    ]
