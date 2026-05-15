from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.curriculum.prompt_io import (
    apply_curriculum_results,
    collect_curriculum_prompts,
)
from video_to_notebook.db.session import connect, init_db


def _seed(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'self attention here')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 1, 1, 60, 120, 'vector basics')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (1, 'self-attention', 'Self-Attention', 'desc', 'seed'),"
            "(2, 'linear-algebra', 'Linear Algebra', 'desc2', 'discovered')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1'),(2, 2, 0.85, 'haiku:v1')"
        )


def test_collect_returns_only_concepts_with_chunks(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_curriculum_prompts(db_path=db)
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "curriculum_prompts"
    slugs = {c["slug"] for c in envelope["concepts"]}
    assert slugs == {"self-attention", "linear-algebra"}


def test_collect_includes_sample_chunks(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_curriculum_prompts(db_path=db)
    assert "linear-algebra" in envelope["concept_chunks"]
    assert "vector basics" in envelope["concept_chunks"]["linear-algebra"][0]["text"]


def test_collect_caps_sample_chunks_per_concept(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    # Add 10 more chunks all tagged self-attention
    with connect(db) as conn:
        for i in range(3, 13):
            conn.execute(
                "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
                "VALUES (?, 1, ?, ?, ?, ?)",
                (i, i + 10, i * 60.0, (i + 1) * 60.0, f"attention chunk {i}"),
            )
            conn.execute(
                "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
                "VALUES (?, 1, 0.9, 'haiku:v1')",
                (i,),
            )

    envelope = collect_curriculum_prompts(db_path=db, samples_per_concept=3)
    assert len(envelope["concept_chunks"]["self-attention"]) <= 3


def test_apply_writes_chapters_to_db(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "curriculum_results",
        "designer": "claude-code-max:v1",
        "chapters": [
            {
                "order_idx": 1,
                "module": "Module 1: Foundations",
                "title": "什么是向量",
                "blurb": "向量是带方向的位移。",
                "primary_concept_slug": "linear-algebra",
                "related_concept_slugs": [],
            },
            {
                "order_idx": 2,
                "module": "Module 2: Attention",
                "title": "注意力机制",
                "blurb": "Self-attention 的直觉。",
                "primary_concept_slug": "self-attention",
                "related_concept_slugs": ["linear-algebra"],
            },
        ],
    }
    n = apply_curriculum_results(db_path=db, results=results)
    assert n == 2
    with connect(db) as conn:
        rows = conn.execute(
            "SELECT order_idx, title, primary_concept_slug, status "
            "FROM curriculum_chapters ORDER BY order_idx"
        ).fetchall()
    assert rows == [
        (1, "什么是向量", "linear-algebra", "planned"),
        (2, "注意力机制", "self-attention", "planned"),
    ]


def test_apply_replaces_existing_chapters(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    base = {
        "schema_version": "1",
        "kind": "curriculum_results",
        "designer": "claude-code-max:v1",
        "chapters": [
            {
                "order_idx": 1,
                "module": "M1",
                "title": "Old title",
                "blurb": "b",
                "primary_concept_slug": "linear-algebra",
                "related_concept_slugs": [],
            }
        ],
    }
    apply_curriculum_results(db_path=db, results=base)
    base["chapters"][0]["title"] = "New title"
    apply_curriculum_results(db_path=db, results=base)
    with connect(db) as conn:
        rows = conn.execute(
            "SELECT title FROM curriculum_chapters WHERE order_idx = 1"
        ).fetchall()
    assert rows == [("New title",)]


def test_apply_rejects_wrong_schema(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "999",
        "kind": "curriculum_results",
        "designer": "x",
        "chapters": [],
    }
    with pytest.raises(ValueError, match="schema_version"):
        apply_curriculum_results(db_path=db, results=results)


def test_apply_rejects_unknown_concept_slug(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "curriculum_results",
        "designer": "claude-code-max:v1",
        "chapters": [
            {
                "order_idx": 1,
                "module": "M1",
                "title": "Ch1",
                "blurb": "b",
                "primary_concept_slug": "nonexistent-slug",
                "related_concept_slugs": [],
            }
        ],
    }
    with pytest.raises(ValueError, match="primary_concept_slug.*unknown"):
        apply_curriculum_results(db_path=db, results=results)
