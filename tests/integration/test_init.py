from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app

runner = CliRunner()


@pytest.mark.integration
def test_init_creates_state_dir(tmp_project: Path):
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0, result.stdout

    assert (tmp_project / ".video-to-notebook").is_dir()
    assert (tmp_project / ".video-to-notebook" / "db.sqlite").is_file()
    assert (tmp_project / ".video-to-notebook" / "config.toml").is_file()


@pytest.mark.integration
def test_init_refuses_to_overwrite(tmp_project: Path):
    runner.invoke(app, ["init"])
    result = runner.invoke(app, ["init"])
    assert result.exit_code != 0
    assert "already initialized" in result.stdout.lower()


@pytest.mark.integration
def test_init_force_reinitializes(tmp_project: Path):
    runner.invoke(app, ["init"])
    sentinel = tmp_project / ".video-to-notebook" / "leftover.txt"
    sentinel.write_text("stale")

    result = runner.invoke(app, ["init", "--force"])
    assert result.exit_code == 0, result.stdout
    assert not sentinel.exists()
