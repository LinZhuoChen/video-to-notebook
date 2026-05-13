from __future__ import annotations

import json
from pathlib import Path

import pytest

from course_merger.db.session import connect, init_db
from course_merger.tag.ontology import load_ontology
from course_merger.tag.prompt_io import (
    apply_tag_results,
    collect_tag_prompts,
)
from course_merger.tag.runner import TagReport


def _seed(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'https://x', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'self attention is great')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 1, 1, 60, 120, 'rotary embedding is RoPE')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'self-attention', 'Self-Attention', 'seed')"
        )


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def test_collect_returns_only_untagged(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'previous:v1')"
        )

    envelope = collect_tag_prompts(db_path=db, ontology=onto)

    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "tag_prompts"
    assert "self-attention" in envelope["ontology_slugs"]
    chunk_ids = [c["chunk_id"] for c in envelope["chunks"]]
    assert chunk_ids == [2]


def test_collect_respects_limit_and_course(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_tag_prompts(db_path=db, ontology=onto, limit=1)
    assert len(envelope["chunks"]) == 1

    envelope_all = collect_tag_prompts(db_path=db, ontology=onto, course_slug="c1")
    assert len(envelope_all["chunks"]) == 2

    envelope_none = collect_tag_prompts(db_path=db, ontology=onto, course_slug="nonexistent")
    assert envelope_none["chunks"] == []


def test_collect_includes_full_chunk_text(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_tag_prompts(db_path=db, ontology=onto)
    texts = [c["text"] for c in envelope["chunks"]]
    assert any("self attention" in t for t in texts)


def test_apply_writes_chunk_concepts_for_known_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [
            {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.95}]},
            {"chunk_id": 2, "tags": []},
        ],
    }
    report = apply_tag_results(db_path=db, ontology=onto, results=results)

    assert isinstance(report, TagReport)
    assert report.chunks_tagged == 2
    assert report.tags_known_written == 1
    with connect(db) as conn:
        rows = conn.execute(
            "SELECT tagger_model FROM chunk_concepts WHERE chunk_id = 1"
        ).fetchall()
    assert rows == [("claude-code-max:v1",)]


def test_apply_writes_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [
            {"chunk_id": 2, "tags": [{"slug": "proposed:rotary-embedding", "confidence": 0.7}]},
        ],
    }
    apply_tag_results(db_path=db, ontology=onto, results=results)
    with connect(db) as conn:
        rows = conn.execute("SELECT raw_tag, tagger_model FROM proposed_tags").fetchall()
    assert rows == [("rotary-embedding", "claude-code-max:v1")]


def test_apply_filters_low_confidence(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [
            {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.3}]},
        ],
    }
    report = apply_tag_results(db_path=db, ontology=onto, results=results)
    assert report.tags_known_written == 0
    with connect(db) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 0


def test_apply_rejects_wrong_schema_version(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "999",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [],
    }
    with pytest.raises(ValueError, match="schema_version"):
        apply_tag_results(db_path=db, ontology=onto, results=results)


def test_apply_rejects_wrong_kind(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "cluster_results",
        "tagger_model_id": "x",
        "results": [],
    }
    with pytest.raises(ValueError, match="kind"):
        apply_tag_results(db_path=db, ontology=onto, results=results)
