"""Project config + project-root discovery."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

PROJECT_MARKER = ".video-to-notebook"
CONFIG_FILENAME = "config.toml"
DB_FILENAME = "db.sqlite"


class ProjectNotInitializedError(RuntimeError):
    """Raised when no `.video-to-notebook/` ancestor is found."""


@dataclass(frozen=True, slots=True)
class Config:
    """Parsed project config plus derived paths."""

    project_root: Path
    tagger_model: str = "claude-haiku-4-5"
    cluster_review_model: str = "claude-sonnet-4-6"

    @property
    def state_dir(self) -> Path:
        return self.project_root / PROJECT_MARKER

    @property
    def db_path(self) -> Path:
        return self.state_dir / DB_FILENAME


def find_project_root(start: Path) -> Path:
    """Walk up from `start` looking for `.video-to-notebook/`.

    Note: v1.x used `.course-merger/`. Existing v1 projects must be
    migrated with `mv .course-merger .video-to-notebook`. See CHANGELOG
    v2.0.0 for the migration note.
    """
    start = start.resolve()
    for candidate in (start, *start.parents):
        if (candidate / PROJECT_MARKER).is_dir():
            return candidate
        # Helpful diagnostic for users upgrading from v1.x:
        if (candidate / ".course-merger").is_dir():
            raise ProjectNotInitializedError(
                f"Found legacy `.course-merger/` at {candidate}. "
                f"This is a v1.x project. Migrate with:\n"
                f"  mv {candidate}/.course-merger {candidate}/{PROJECT_MARKER}\n"
                f"then re-run the command. (See CHANGELOG v2.0.0.)"
            )
    raise ProjectNotInitializedError(
        f"No video-to-notebook project found at or above {start}. "
        "Run `video-to-notebook init` first."
    )


def load_config(project_root: Path) -> Config:
    """Read .video-to-notebook/config.toml; missing keys fall back to dataclass defaults."""
    config_file = project_root / PROJECT_MARKER / CONFIG_FILENAME
    if not config_file.is_file():
        return Config(project_root=project_root)
    data = tomllib.loads(config_file.read_text(encoding="utf-8"))
    return Config(
        project_root=project_root,
        tagger_model=data.get("tagger_model", Config.tagger_model),
        cluster_review_model=data.get("cluster_review_model", Config.cluster_review_model),
    )
