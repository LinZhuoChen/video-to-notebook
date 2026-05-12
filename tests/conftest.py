"""Shared pytest fixtures."""
from __future__ import annotations
from pathlib import Path

import pytest


@pytest.fixture
def fixtures_dir() -> Path:
    """Path to tests/fixtures/."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def tmp_project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A throwaway project directory; cwd is set into it for the duration."""
    monkeypatch.chdir(tmp_path)
    return tmp_path
