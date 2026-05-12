from __future__ import annotations

from pathlib import Path

import pytest

from course_merger.config import (
    Config,
    ProjectNotInitializedError,
    find_project_root,
    load_config,
)


def test_find_project_root_finds_marker(tmp_path: Path):
    (tmp_path / ".course-merger").mkdir()
    nested = tmp_path / "a" / "b"
    nested.mkdir(parents=True)
    assert find_project_root(nested) == tmp_path


def test_find_project_root_raises_when_missing(tmp_path: Path):
    with pytest.raises(ProjectNotInitializedError):
        find_project_root(tmp_path)


def test_load_config_reads_toml(tmp_path: Path):
    root = tmp_path
    (root / ".course-merger").mkdir()
    (root / ".course-merger" / "config.toml").write_text(
        'tagger_model = "claude-haiku-4-5"\n'
        'cluster_review_model = "claude-sonnet-4-6"\n'
    )
    cfg = load_config(root)
    assert isinstance(cfg, Config)
    assert cfg.tagger_model == "claude-haiku-4-5"
    assert cfg.db_path == root / ".course-merger" / "db.sqlite"
