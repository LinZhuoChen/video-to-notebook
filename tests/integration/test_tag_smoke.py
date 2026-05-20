from __future__ import annotations

import json
import shutil
from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.db.session import connect
from video_to_notebook.inflow import tag_paths
from video_to_notebook.tag.claude_tagger import Tag, TagResult

runner = CliRunner()


def _seed_one_chunk(db: Path, *, chunk_text: str = "self-attention is key.") -> None:
    """Insert the minimal rows (course → lecture → chunk → concept) used by every smoke test."""
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-09')"
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'https://yt/v1', 'about self-attention', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, ?)",
            (lecture_id, chunk_text),
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )


@pytest.mark.integration
def test_tag_use_api_end_to_end(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_one_chunk(db)

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    fake_result = TagResult(
        tags=(Tag(slug="self-attention", confidence=0.95, is_proposed=False),)
    )
    with (
        patch(
            "video_to_notebook.tag.claude_tagger.ClaudeTagger.tag_chunk",
            return_value=fake_result,
        ),
        patch("anthropic.Anthropic", return_value=object()),
    ):
        result = runner.invoke(
            app,
            ["tag", "--ontology", str(ont_path), "--model", "claude-haiku-4-5", "--use-api"],
        )

    assert result.exit_code == 0, result.output
    assert "chunks tagged" in result.stdout.lower() or "1 tagged" in result.stdout.lower()

    with connect(db) as conn:
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_cc == 1


@pytest.mark.integration
def test_tag_default_writes_prompts_file(tmp_project: Path, fixtures_dir: Path):
    """New default: ``tag`` (no flags) writes the prompts envelope to disk and exits."""
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'hello world')"
        )

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path)])
    assert result.exit_code == 0, result.output
    assert result.stdout == ""  # stdout is clean; hints go to stderr

    prompts_path, decisions_path = tag_paths(tmp_project / ".video-to-notebook")
    assert prompts_path.is_file()
    assert not decisions_path.exists()
    envelope = json.loads(prompts_path.read_text())
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "tag_prompts"
    assert len(envelope["chunks"]) == 1
    assert envelope["chunks"][0]["text"] == "hello world"


@pytest.mark.integration
def test_tag_errors_when_not_initialized(tmp_project: Path, fixtures_dir: Path):
    result = runner.invoke(
        app, ["tag", "--ontology", str(fixtures_dir / "ontology.yaml")]
    )
    assert result.exit_code != 0
    assert "init" in result.output.lower()


@pytest.mark.integration
def test_tag_apply_default_path(tmp_project: Path, fixtures_dir: Path):
    """``tag --apply`` reads from the default decisions path."""
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_one_chunk(db, chunk_text="self attention.")

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    _, decisions_path = tag_paths(tmp_project / ".video-to-notebook")
    decisions_path.parent.mkdir(parents=True, exist_ok=True)
    decisions_path.write_text(json.dumps({
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [{"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.9}]}],
    }))

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path), "--apply"])
    assert result.exit_code == 0, result.output
    assert "1 known tags" in result.stdout

    with connect(db) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 1


@pytest.mark.integration
def test_tag_apply_results_explicit_path(tmp_project: Path, fixtures_dir: Path):
    """``tag --apply-results <path>`` still honors an explicit decisions path."""
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    _seed_one_chunk(db, chunk_text="self attention.")

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    results_path = tmp_project / "results.json"
    results_path.write_text(json.dumps({
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [{"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.9}]}],
    }))

    result = runner.invoke(
        app,
        ["tag", "--ontology", str(ont_path), "--apply-results", str(results_path)],
    )
    assert result.exit_code == 0, result.output
    assert "1 known tags" in result.stdout


@pytest.mark.integration
def test_tag_apply_without_decisions_file_errors(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path), "--apply"])
    assert result.exit_code != 0
    assert "decisions file not found" in result.output.lower()


@pytest.mark.integration
@pytest.mark.parametrize(
    "flags",
    [
        ["--apply", "--apply-results", "FAKE"],
        ["--apply", "--use-api"],
        ["--apply-results", "FAKE", "--use-api"],
    ],
)
def test_tag_mutual_exclusion(tmp_project: Path, fixtures_dir: Path, flags: list[str]):
    runner.invoke(app, ["init"])
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)
    # Replace placeholder FAKE with an actual (empty) file so typer doesn't reject earlier.
    fake_path = tmp_project / "fake.json"
    fake_path.write_text("{}")
    expanded = [str(fake_path) if f == "FAKE" else f for f in flags]

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path), *expanded])
    assert result.exit_code != 0
    assert "mutually exclusive" in result.output.lower()


@pytest.mark.integration
def test_tag_print_prompts_is_deprecated_noop(tmp_project: Path, fixtures_dir: Path):
    """``--print-prompts`` is a no-op alias that warns but otherwise behaves as default."""
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'hi')"
        )

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path), "--print-prompts"])
    assert result.exit_code == 0, result.output
    assert "deprecated" in result.output.lower()
    prompts_path, _ = tag_paths(tmp_project / ".video-to-notebook")
    assert prompts_path.is_file()


@pytest.mark.integration
def test_tag_print_prompts_with_apply_errors(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    result = runner.invoke(
        app,
        ["tag", "--ontology", str(ont_path), "--print-prompts", "--apply"],
    )
    assert result.exit_code != 0
    assert "cannot be combined" in result.output.lower()
