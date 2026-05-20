from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.db.session import connect
from video_to_notebook.inflow import curriculum_paths, explain_paths, synthesize_paths

runner = CliRunner()


def _seed_tagged_chunks(db: Path) -> None:
    """Minimum data so curriculum/synthesize/explain envelopes have content."""
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'https://yt/v1', 'self-attention is key', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'self attention here')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (1, 'self-attention', 'Self-Attention', 'desc', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )


@pytest.mark.integration
def test_curriculum_default_writes_prompts_file(tmp_project: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_tagged_chunks(db)

    result = runner.invoke(app, ["curriculum"])
    assert result.exit_code == 0, result.output
    assert result.stdout == ""

    prompts_path, _ = curriculum_paths(tmp_project / ".video-to-notebook")
    assert prompts_path.is_file()
    envelope = json.loads(prompts_path.read_text())
    assert envelope["kind"] == "curriculum_prompts"
    assert any(c["slug"] == "self-attention" for c in envelope["concepts"])


@pytest.mark.integration
def test_synthesize_default_writes_prompts_file(tmp_project: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_tagged_chunks(db)
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO curriculum_chapters "
            "(order_idx, module, title, blurb, primary_concept_slug, "
            "related_concept_slugs, curriculum_designer) "
            "VALUES (1, 'M1', 'Intro to Attention', 'overview', 'self-attention', "
            "'[]', 'test')"
        )

    result = runner.invoke(app, ["synthesize", "--chapter", "1"])
    assert result.exit_code == 0, result.output
    assert result.stdout == ""

    prompts_path, _ = synthesize_paths(tmp_project / ".video-to-notebook", chapter=1)
    assert prompts_path.is_file()
    envelope = json.loads(prompts_path.read_text())
    assert envelope["kind"] == "synthesize_prompts"
    assert envelope["chapter"]["order_idx"] == 1
    assert envelope["chapter"]["title"] == "Intro to Attention"


@pytest.mark.integration
def test_explain_default_writes_prompts_file(tmp_project: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_tagged_chunks(db)

    result = runner.invoke(app, ["explain", "--concept", "self-attention"])
    assert result.exit_code == 0, result.output
    assert result.stdout == ""

    prompts_path, _ = explain_paths(
        tmp_project / ".video-to-notebook", concept_slug="self-attention"
    )
    assert prompts_path.is_file()
    envelope = json.loads(prompts_path.read_text())
    assert envelope["kind"] == "explain_prompts"
    assert envelope["concept"]["slug"] == "self-attention"


@pytest.mark.integration
def test_curriculum_apply_default_path(tmp_project: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_tagged_chunks(db)

    _, decisions_path = curriculum_paths(tmp_project / ".video-to-notebook")
    decisions_path.parent.mkdir(parents=True, exist_ok=True)
    decisions_path.write_text(json.dumps({
        "schema_version": "1",
        "kind": "curriculum_results",
        "chapters": [
            {
                "order_idx": 1,
                "module": "M1",
                "title": "Attention 101",
                "blurb": "intro",
                "primary_concept_slug": "self-attention",
                "related_concept_slugs": [],
            }
        ],
    }))

    result = runner.invoke(app, ["curriculum", "--apply"])
    assert result.exit_code == 0, result.output
    assert "1 chapters" in result.stdout

    with connect(db) as conn:
        rows = conn.execute(
            "SELECT title FROM curriculum_chapters WHERE order_idx = 1"
        ).fetchall()
    assert rows == [("Attention 101",)]


@pytest.mark.integration
@pytest.mark.parametrize(
    "command,extra",
    [
        ("curriculum", []),
        ("synthesize", ["--chapter", "1"]),
        ("explain", ["--concept", "self-attention"]),
    ],
)
def test_apply_without_decisions_errors(
    tmp_project: Path, command: str, extra: list[str]
):
    runner.invoke(app, ["init"])
    result = runner.invoke(app, [command, *extra, "--apply"])
    assert result.exit_code != 0
    assert "decisions file not found" in result.output.lower()
