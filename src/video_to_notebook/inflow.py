"""Shared helpers for the in-session prompt/decision flow.

All five LLM-driven commands (tag, cluster, curriculum, synthesize, explain)
default to writing a JSON envelope under ``<state_dir>/prompts/`` and exiting,
expecting an in-session agent (Claude Code, Codex, ...) to write a decisions
file at the sibling ``<step>.decisions.json`` path and re-invoke the same
command with ``--apply``.

This module is the single source of truth for those paths, for the atomic
envelope write, and for the stderr hint format. It deliberately depends only
on the stdlib so it can be reused from tests without pulling in Typer.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

PROMPTS_DIRNAME = "prompts"


# ---------------------------------------------------------------------------
# Path helpers — one function per command, returning (prompts, decisions).
# ---------------------------------------------------------------------------


def prompts_dir(state_dir: Path) -> Path:
    return state_dir / PROMPTS_DIRNAME


def tag_paths(state_dir: Path) -> tuple[Path, Path]:
    base = prompts_dir(state_dir)
    return base / "tag.json", base / "tag.decisions.json"


def cluster_paths(state_dir: Path) -> tuple[Path, Path]:
    base = prompts_dir(state_dir)
    return base / "cluster.json", base / "cluster.decisions.json"


def curriculum_paths(state_dir: Path) -> tuple[Path, Path]:
    base = prompts_dir(state_dir)
    return base / "curriculum.json", base / "curriculum.decisions.json"


def synthesize_paths(state_dir: Path, chapter: int) -> tuple[Path, Path]:
    base = prompts_dir(state_dir) / "synthesize"
    return base / f"chapter-{chapter}.json", base / f"chapter-{chapter}.decisions.json"


def explain_paths(state_dir: Path, concept_slug: str) -> tuple[Path, Path]:
    base = prompts_dir(state_dir) / "explain"
    return base / f"{concept_slug}.json", base / f"{concept_slug}.decisions.json"


# ---------------------------------------------------------------------------
# I/O — atomic write + friendly read.
# ---------------------------------------------------------------------------


def write_envelope(path: Path, envelope: dict[str, Any]) -> None:
    """Atomically serialize ``envelope`` to ``path`` as pretty-printed JSON.

    Creates parent directories on demand. Writes to a tempfile in the parent
    directory and then ``os.replace``s — same-filesystem, so atomic on POSIX.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent,
    )
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(envelope, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        os.replace(tmp, path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def read_decisions(path: Path) -> dict[str, Any]:
    """Load a decisions JSON file. Raises ``FileNotFoundError`` if missing."""
    if not path.is_file():
        raise FileNotFoundError(
            f"decisions file not found: {path}\n"
            "Hint: re-run the command without --apply to regenerate the "
            "prompts envelope, then write your decisions to this path."
        )
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Stderr formatting — keep messages identical across commands.
# ---------------------------------------------------------------------------


def emit_hint(
    *,
    prompts_path: Path,
    decisions_path: Path,
    size_summary: str,
    next_command: str,
) -> None:
    """Print the standard three-line in-session hint to stderr."""
    print(f"prompts written: {prompts_path} ({size_summary})", file=sys.stderr)
    print(f"→ write decisions to: {decisions_path}", file=sys.stderr)
    print(f"→ then: {next_command}", file=sys.stderr)


def warn_print_prompts_deprecated() -> None:
    """One-line deprecation notice for the legacy ``--print-prompts`` flag."""
    print(
        "warning: --print-prompts is deprecated and will be removed in a future "
        "release; printing prompts is now the default.",
        file=sys.stderr,
    )
