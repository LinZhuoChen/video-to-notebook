from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.db.session import connect, init_db
from video_to_notebook.explain.prompt_io import (
    apply_explain_results,
    collect_explain_prompts,
)


def _seed(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 2, 'L2', 'https://www.youtube.com/watch?v=abc', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 100.0, 160.0, 'vector basics text')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 1, 1, 160.0, 220.0, 'scalar mul text')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (1, 'linear-algebra', 'Linear Algebra', 'Vectors etc.', 'seed')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (2, 'scalar-multiplication', 'Scalar Multiplication', 'seed')"
        )
        conn.execute(
            "INSERT INTO concept_aliases (concept_id, alias) "
            "VALUES (1, 'linalg')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )
        # Chunk 2 mentions both — gives a co-occurrence for "related_concepts"
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (2, 1, 0.85, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (2, 2, 0.85, 'haiku:v1')"
        )


def test_collect_returns_concept_and_occurrences(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_explain_prompts(db_path=db, concept_slug="linear-algebra")
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "explain_prompts"
    assert envelope["concept"]["canonical_name"] == "Linear Algebra"
    assert envelope["concept"]["aliases"] == ["linalg"]
    assert len(envelope["occurrences"]) == 2
    # co-occurrence pulls scalar-multiplication
    related_slugs = [r["slug"] for r in envelope["related_concepts"]]
    assert "scalar-multiplication" in related_slugs


def test_collect_unknown_concept_raises(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    with pytest.raises(ValueError, match="no concept"):
        collect_explain_prompts(db_path=db, concept_slug="does-not-exist")


def test_apply_writes_fragment_and_db_row(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    src = tmp_path / "frag.html"
    src.write_text("<article>test</article>", encoding="utf-8")
    state = tmp_path / "state"
    state.mkdir()
    dst = apply_explain_results(
        db_path=db,
        state_dir=state,
        results={
            "schema_version": "1",
            "kind": "explain_results",
            "concept_slug": "linear-algebra",
            "explainer": "claude-code-max:v2",
            "html_fragment_path": str(src),
        },
    )
    assert dst == "linear-algebra.html"
    assert (state / "concepts" / "linear-algebra.html").is_file()
    with connect(db) as conn:
        row = conn.execute(
            "SELECT html_fragment, explainer FROM concept_explanations"
        ).fetchone()
    assert row == ("linear-algebra.html", "claude-code-max:v2")


def test_apply_is_upsertable(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    src = tmp_path / "frag.html"
    src.write_text("<article>v1</article>", encoding="utf-8")
    state = tmp_path / "state"
    state.mkdir()
    base = {
        "schema_version": "1",
        "kind": "explain_results",
        "concept_slug": "linear-algebra",
        "html_fragment_path": str(src),
    }
    apply_explain_results(db_path=db, state_dir=state, results=base | {"explainer": "v1"})
    src.write_text("<article>v2</article>", encoding="utf-8")
    apply_explain_results(db_path=db, state_dir=state, results=base | {"explainer": "v2"})
    with connect(db) as conn:
        rows = conn.execute("SELECT COUNT(*), explainer FROM concept_explanations").fetchone()
    assert rows == (1, "v2")  # second run overwrote, didn't duplicate


def test_apply_rejects_wrong_schema(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    src = tmp_path / "frag.html"
    src.write_text("x", encoding="utf-8")
    state = tmp_path / "state"
    state.mkdir()
    with pytest.raises(ValueError, match="schema_version"):
        apply_explain_results(
            db_path=db,
            state_dir=state,
            results={
                "schema_version": "999",
                "kind": "explain_results",
                "concept_slug": "linear-algebra",
                "html_fragment_path": str(src),
            },
        )


def test_apply_rejects_missing_fragment(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    state = tmp_path / "state"
    state.mkdir()
    with pytest.raises(FileNotFoundError):
        apply_explain_results(
            db_path=db,
            state_dir=state,
            results={
                "schema_version": "1",
                "kind": "explain_results",
                "concept_slug": "linear-algebra",
                "html_fragment_path": "/nonexistent",
            },
        )
