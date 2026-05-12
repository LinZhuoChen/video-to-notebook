from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from course_merger.db.session import connect, init_db
from course_merger.tag.claude_tagger import Tag, TagResult
from course_merger.tag.ontology import load_ontology
from course_merger.tag.runner import TagReport, run_tag


def _seed_one_course_with_chunks(db_path: Path, n_chunks: int = 3) -> int | None:
    """Insert a course + 1 lecture + N chunks. Return lecture_id."""
    init_db(db_path)
    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("c1", "Course 1", "youtube", "https://x", "2026-05-09"),
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, ?, ?, ?, ?, 'ok')",
            (course_id, 1, "L1", "https://yt/v1", "transcript text"),
        )
        lecture_id = cur.lastrowid
        for i in range(n_chunks):
            conn.execute(
                "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
                "VALUES (?, ?, ?, ?, ?)",
                (lecture_id, i, i * 10.0, (i + 1) * 10.0, f"chunk text {i}"),
            )
    return lecture_id


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def _fake_tagger(canned: list[TagResult]):
    m = MagicMock()
    m.tag_chunk.side_effect = canned
    m.tagger_model_id = "claude-haiku-4-5:v1"
    return m


def test_run_tag_writes_chunk_concepts_for_known_tags(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=2)

    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )

    tagger = _fake_tagger([
        TagResult(tags=(Tag(slug="self-attention", confidence=0.9, is_proposed=False),)),
        TagResult(tags=()),
    ])

    report = run_tag(db_path=db_path, tagger=tagger, ontology=onto)

    assert isinstance(report, TagReport)
    assert report.chunks_tagged == 2
    assert report.tags_known_written == 1
    assert report.tags_proposed_written == 0

    with connect(db_path) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 1


def test_run_tag_writes_proposed_tags_separately(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=1)

    tagger = _fake_tagger([
        TagResult(tags=(Tag(slug="rotary-positional-encoding", confidence=0.8, is_proposed=True),)),
    ])

    run_tag(db_path=db_path, tagger=tagger, ontology=onto)

    with connect(db_path) as conn:
        rows = conn.execute(
            "SELECT raw_tag, confidence FROM proposed_tags"
        ).fetchall()
    assert rows == [("rotary-positional-encoding", 0.8)]


def test_run_tag_skips_already_tagged_chunks(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=2)

    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'SA', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'old-model:v0')"
        )

    tagger = _fake_tagger([
        TagResult(tags=(Tag(slug="self-attention", confidence=0.9, is_proposed=False),)),
    ])

    run_tag(db_path=db_path, tagger=tagger, ontology=onto)

    # Only chunk 2 should have been processed (chunk 1 already had a row).
    assert tagger.tag_chunk.call_count == 1


def test_run_tag_respects_course_filter(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=2)

    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c2', 'Course 2', 'youtube', 'https://y', '2026-05-09')"
        )
        c2_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'https://yt/v2', 't', 'ok')",
            (c2_id,),
        )
        l2_id = cur.lastrowid
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'c2 chunk')",
            (l2_id,),
        )

    tagger = _fake_tagger([TagResult(tags=())] * 10)

    run_tag(db_path=db_path, tagger=tagger, ontology=onto, course_slug="c1")

    # Only c1's 2 chunks should be processed.
    assert tagger.tag_chunk.call_count == 2


def test_run_tag_respects_limit(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=10)

    tagger = _fake_tagger([TagResult(tags=())] * 10)

    run_tag(db_path=db_path, tagger=tagger, ontology=onto, limit=3)

    assert tagger.tag_chunk.call_count == 3
