from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.db.session import connect, init_db
from video_to_notebook.synthesize.prompt_io import (
    apply_synthesize_results,
    collect_synthesize_prompts,
)


def _seed(db_path: Path) -> int:
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
        # Use a realistic-length chunk so it passes the v4 preprocessing
        # filter (min 80 chars, after sponsor/intro detection).
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 268.4, 320.0, "
            "'A vector is a list of numbers with both magnitude and direction. "
            "We use vectors to represent positions, velocities, forces, and in "
            "machine learning the embedding of a token in some d-dimensional "
            "space. The dot product of two vectors measures their alignment.')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'linear-algebra', 'Linear Algebra', 'discovered')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO curriculum_chapters "
            "(order_idx, module, title, blurb, primary_concept_slug, "
            "related_concept_slugs, curriculum_designer, status) "
            "VALUES (1, 'Module 1', '什么是向量', '向量是带方向的位移。', "
            "'linear-algebra', '[]', 'claude-code-max:v1', 'planned')"
        )
    return 1


def test_collect_returns_chapter_and_chunks(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_synthesize_prompts(db_path=db, chapter_order_idx=1)
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "synthesize_prompts"
    assert envelope["chapter"]["title"] == "什么是向量"
    assert envelope["chapter"]["primary_concept_slug"] == "linear-algebra"
    assert len(envelope["source_chunks"]) == 1
    assert envelope["source_chunks"][0]["start_sec"] == 268.4
    assert envelope["source_chunks"][0]["video_url"] == "https://www.youtube.com/watch?v=abc"


def test_collect_unknown_chapter_raises(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    with pytest.raises(ValueError, match="no chapter at order_idx"):
        collect_synthesize_prompts(db_path=db, chapter_order_idx=999)


def test_apply_writes_fragment_and_marks_chapter(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    fragment = tmp_path / "fragment.html"
    fragment.write_text("<article><h1>Hi</h1></article>")

    state_dir = tmp_path / ".video-to-notebook"
    state_dir.mkdir(parents=True, exist_ok=True)

    results = {
        "schema_version": "1",
        "kind": "synthesize_results",
        "synthesizer": "claude-code-max:v1",
        "chapter_order_idx": 1,
        "html_fragment_path": str(fragment),
    }
    apply_synthesize_results(
        db_path=db, state_dir=state_dir, results=results,
        skip_depth_gate=True,  # legacy tests verify apply-flow contract, not depth
    )

    # The file is copied into <state_dir>/textbook/<order>.html
    dst = state_dir / "textbook" / "1.html"
    assert dst.is_file()
    assert "<h1>Hi</h1>" in dst.read_text()

    # And the DB row was updated
    with connect(db) as conn:
        (status, path) = conn.execute(
            "SELECT status, synthesized_path FROM curriculum_chapters "
            "WHERE order_idx = 1"
        ).fetchone()
    assert status == "synthesized"
    assert path == "1.html"


def test_apply_rejects_wrong_schema(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    fragment = tmp_path / "f.html"
    fragment.write_text("<article></article>")
    state_dir = tmp_path / ".video-to-notebook"
    state_dir.mkdir()

    with pytest.raises(ValueError, match="schema_version"):
        apply_synthesize_results(
            db_path=db, state_dir=state_dir,
            results={
                "schema_version": "999",
                "kind": "synthesize_results",
                "synthesizer": "x",
                "chapter_order_idx": 1,
                "html_fragment_path": str(fragment),
            },
        )


def test_apply_rejects_missing_fragment(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    state_dir = tmp_path / ".video-to-notebook"
    state_dir.mkdir()

    with pytest.raises(FileNotFoundError):
        apply_synthesize_results(
            db_path=db, state_dir=state_dir,
            results={
                "schema_version": "1",
                "kind": "synthesize_results",
                "synthesizer": "claude-code-max:v1",
                "chapter_order_idx": 1,
                "html_fragment_path": "/nonexistent/path.html",
            },
        )


def test_apply_rejects_chapter_not_planned(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed(db)
    fragment = tmp_path / "f.html"
    fragment.write_text("<article></article>")
    state_dir = tmp_path / ".video-to-notebook"
    state_dir.mkdir()

    with pytest.raises(ValueError, match="no chapter at order_idx"):
        apply_synthesize_results(
            db_path=db, state_dir=state_dir,
            results={
                "schema_version": "1",
                "kind": "synthesize_results",
                "synthesizer": "claude-code-max:v1",
                "chapter_order_idx": 999,
                "html_fragment_path": str(fragment),
            },
        )
