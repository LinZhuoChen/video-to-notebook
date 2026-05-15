from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.build.queries import (
    all_concepts_with_counts,
    all_courses_with_lecture_counts,
    chunks_for_lecture,
    concept_occurrences,
    lectures_for_course,
)
from video_to_notebook.db.session import connect, init_db


@pytest.fixture
def seeded_db(tmp_path: Path) -> Path:
    db = tmp_path / "db.sqlite"
    init_db(db)
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://yt/p', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status, duration_sec) "
            "VALUES (1, 1, 1, 'L1: Intro', 'https://yt/v1', 'transcript A', 'ok', 3600)"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status, duration_sec) "
            "VALUES (2, 1, 2, 'L2: Attention', 'https://yt/v2', 'transcript B', 'ok', 3000)"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'hello world')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 2, 0, 0, 60, 'self attention explained')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (3, 2, 1, 60, 120, 'multi head attention')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (1, 'self-attention', 'Self-Attention', 'SA desc', 'seed')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (2, 'mha', 'Multi-Head Attention', 'MHA desc', 'discovered')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (2, 1, 0.9, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (3, 2, 0.85, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO concept_aliases (concept_id, alias) VALUES (1, 'SA')"
        )
    return db


def test_all_courses(seeded_db):
    courses = all_courses_with_lecture_counts(seeded_db)
    assert len(courses) == 1
    c = courses[0]
    assert c["slug"] == "cs336"
    assert c["title"] == "CS336"
    assert c["lecture_count"] == 2
    assert c["platform"] == "youtube"


def test_lectures_for_course(seeded_db):
    lectures = lectures_for_course(seeded_db, "cs336")
    assert len(lectures) == 2
    assert lectures[0]["idx"] == 1
    assert lectures[0]["title"] == "L1: Intro"
    assert lectures[1]["idx"] == 2


def test_chunks_for_lecture(seeded_db):
    chunks = chunks_for_lecture(seeded_db, lecture_id=2)
    assert len(chunks) == 2
    assert chunks[0]["text"] == "self attention explained"
    assert chunks[0]["concept_slugs"] == ["self-attention"]
    assert chunks[1]["concept_slugs"] == ["mha"]


def test_all_concepts_with_counts(seeded_db):
    concepts = all_concepts_with_counts(seeded_db)
    assert len(concepts) == 2
    by_slug = {c["slug"]: c for c in concepts}
    assert by_slug["self-attention"]["occurrence_count"] == 1
    assert by_slug["self-attention"]["aliases"] == ["SA"]
    assert by_slug["mha"]["occurrence_count"] == 1
    assert by_slug["mha"]["aliases"] == []


def test_concept_occurrences(seeded_db):
    occ = concept_occurrences(seeded_db, "self-attention")
    assert len(occ) == 1
    row = occ[0]
    assert row["course_slug"] == "cs336"
    assert row["lecture_idx"] == 2
    assert row["lecture_title"] == "L2: Attention"
    assert row["start_sec"] == 0
    assert "self attention" in row["text"]


def test_concept_occurrences_missing_concept(seeded_db):
    assert concept_occurrences(seeded_db, "nonexistent") == []
