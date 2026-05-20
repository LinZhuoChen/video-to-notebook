"""Lazy-copy the bundled Astro template-site into a project."""
from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path


def _bundled_template_root() -> Path:
    # First try the editable / source layout (development mode)
    src_layout = Path(__file__).parent.parent.parent.parent / "template-site"
    if src_layout.is_dir():
        return src_layout
    # Otherwise, packaged form
    pkg = resources.files("video_to_notebook") / "_template_site"
    return Path(str(pkg))


# Subtrees that the *project* owns once it has been initialized — the
# build writers regenerate everything inside these from the SQLite DB.
# They must therefore be excluded from both the first-init copytree
# (so a fresh project never starts with the showcase corpus's content)
# AND from the overlay-sync rewrap (so upgrading the CLI never blows
# away the user's synthesized content).
#
# All five collections are fully derived from the DB:
#   - course / lecture / concept          → Markdown written by build.runner
#   - textbook / concept-explainers       → HTML fragments + manifest written
#                                           by textbook_writer / concept_writer
_PROJECT_OWNED_PREFIXES: tuple[Path, ...] = (
    Path("src") / "content" / "course",
    Path("src") / "content" / "lecture",
    Path("src") / "content" / "concept",
    Path("src") / "content" / "textbook",
    Path("src") / "content" / "concept-explainers",
)


# Build-time / dependency directories that the template ships without —
# never copy or sync these into a project.
_TRANSIENT_DIRS = frozenset({"node_modules", "dist", ".astro"})


def _is_project_owned(rel: Path) -> bool:
    """Is this path inside a project-owned subtree (textbook / concept-explainers)?"""
    return any(rel == p or p in rel.parents for p in _PROJECT_OWNED_PREFIXES)


def ensure_site_dir(project_root: Path) -> Path:
    """Return ``<project_root>/site``, syncing bundled template files on every call.

    On first use this is a full copy. On subsequent calls we overlay-sync the
    template's ``src/`` and config files into the project (preserving
    ``node_modules/``, ``dist/``, ``.astro/``, project-owned content
    subtrees, and anything outside the template).

    "Project-owned" means subtrees the build writers regenerate from SQLite
    (currently textbook and concept-explainers). Demo HTML fragments bundled
    with the template-site are deliberately excluded from both the first-init
    copy and the overlay-sync — otherwise every new project would start with
    the showcase corpus's content and overlay-sync would resurrect deleted
    demo files on every build.
    """
    site = project_root / "site"
    src = _bundled_template_root()
    if not src.is_dir():
        raise FileNotFoundError(
            f"bundled template-site not found at {src}; reinstall course-merger?"
        )

    if not site.is_dir():
        _first_init_copy(src, site)
        return site

    _overlay_sync(src, site)
    return site


def _first_init_copy(src: Path, site: Path) -> None:
    """Copy `src` to `site`, excluding transient dirs and project-owned subtrees."""

    def _ignore(directory: str, names: list[str]) -> list[str]:
        # `directory` is an absolute path from copytree; convert to a path
        # relative to `src` so we can match against `_PROJECT_OWNED_PREFIXES`.
        rel = Path(directory).resolve().relative_to(src.resolve())
        if _is_project_owned(rel):
            # Skip every file in this dir but keep walking so the empty
            # subtree itself is preserved for Astro's content collection.
            return names
        ignored = [n for n in names if n in _TRANSIENT_DIRS]
        # If a child of this dir is a project-owned subtree, skip the demo
        # content inside it but keep the directory itself.
        for n in names:
            if _is_project_owned(rel / n):
                # Don't add to `ignored` — we want copytree to enter this
                # subdir; we'll filter its contents when we get there.
                continue
        return ignored

    shutil.copytree(src, site, ignore=_ignore)


def _overlay_sync(src: Path, site: Path) -> None:
    """Walk `src`; copy every file into `site` unless it's transient or project-owned."""
    walker = src.walk() if hasattr(src, "walk") else _walk(src)
    for root, dirs, files in walker:
        rel = root.relative_to(src)
        # Skip well-known transient dirs.
        if any(part in _TRANSIENT_DIRS for part in rel.parts):
            dirs[:] = []
            continue
        # Skip project-owned content subtrees so user data
        # (curriculum.json, N.html, etc.) is never overwritten by demo files.
        if _is_project_owned(rel):
            dirs[:] = []
            continue
        dst_dir = site / rel
        dst_dir.mkdir(parents=True, exist_ok=True)
        for name in files:
            src_file = root / name
            dst_file = dst_dir / name
            shutil.copyfile(src_file, dst_file)


def _walk(root: Path):
    """Fallback for Python < 3.12 where Path.walk doesn't exist."""
    import os
    for dirpath, dirnames, filenames in os.walk(root):
        yield Path(dirpath), dirnames, filenames
