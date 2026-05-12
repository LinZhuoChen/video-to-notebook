"""Typer-based CLI entrypoint."""
from __future__ import annotations

import importlib.metadata
import shutil
from pathlib import Path

import typer

from course_merger.config import CONFIG_FILENAME, PROJECT_MARKER
from course_merger.db.session import init_db

app = typer.Typer(
    help="Crawl and merge open-courseware into an interactive concept-anchored site.",
    no_args_is_help=True,
    add_completion=False,
)


DEFAULT_CONFIG_TOML = """\
# course-merger project config

# tagger_model = "claude-haiku-4-5"
# cluster_review_model = "claude-sonnet-4-6"
"""


@app.command("init")
def init_cmd(
    force: bool = typer.Option(
        False, "--force", help="Wipe existing state and reinitialize."
    ),
) -> None:
    """Initialize a course-merger project in the current directory."""
    cwd = Path.cwd()
    state_dir = cwd / PROJECT_MARKER

    if state_dir.exists():
        if not force:
            typer.echo(
                f"error: {PROJECT_MARKER}/ already initialized at {cwd}. "
                "Use --force to overwrite."
            )
            raise typer.Exit(code=1)
        shutil.rmtree(state_dir)

    state_dir.mkdir(parents=True)
    init_db(state_dir / "db.sqlite")
    (state_dir / CONFIG_FILENAME).write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")

    typer.echo(f"initialized course-merger project at {cwd}")


@app.command("version")
def version_cmd() -> None:
    """Show the installed course-merger version."""
    try:
        ver = importlib.metadata.version("course-merger")
    except importlib.metadata.PackageNotFoundError:
        ver = "unknown"
    typer.echo(ver)
