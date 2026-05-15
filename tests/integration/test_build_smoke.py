from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_build_cli_writes_content(tmp_project: Path):
    runner.invoke(app, ["init"])

    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://yt/p', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'hello attention')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'attention', 'Attention', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )

    # Skip npm build for the smoke test (no Node guaranteed in all CI)
    result = runner.invoke(app, ["build", "--no-npm"])
    assert result.exit_code == 0, result.stdout

    site = tmp_project / "site"
    # NOTE: singular directory names per Astro 5 content collection convention
    assert (site / "src" / "content" / "course" / "cs336.md").is_file()
    assert (site / "src" / "content" / "concept" / "attention.md").is_file()


@pytest.mark.integration
def test_build_errors_when_not_initialized(tmp_project: Path):
    result = runner.invoke(app, ["build", "--no-npm"])
    assert result.exit_code != 0
    assert "init" in result.stdout.lower()
