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
# They must therefore be excluded from the overlay-sync rewrap (so
# upgrading the CLI never blows away the user's synthesized content).
#
# Each prefix corresponds to one of the five data-derived collections:
#   - course / lecture / concept          → Markdown written by build.runner
#   - textbook / concept-explainers       → HTML fragments + manifest written
#                                           by textbook_writer / concept_writer
#
# Note: first-init does NOT exclude these — the template ships with
# empty placeholder JSON manifests (curriculum.json / manifest.json)
# that Astro's static imports require. The template-cleanliness invariant
# (see ``tests/unit/test_template_copy.py``) guarantees no demo HTML or
# Markdown ever lives in these subtrees within the source tree, so a
# first-init copytree only ever pulls in those empty placeholders.
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
    """True if `rel` is inside a project-owned subtree."""
    return any(rel == p or p in rel.parents for p in _PROJECT_OWNED_PREFIXES)


def ensure_site_dir(project_root: Path) -> Path:
    """Return ``<project_root>/site``, syncing bundled template files on every call.

    On first use this is a full copy of the (intentionally clean) template.
    On subsequent calls we overlay-sync the template's ``src/`` and config
    files into the project, preserving ``node_modules/``, ``dist/``,
    ``.astro/``, and the project-owned content subtrees (so re-builds and
    CLI upgrades never blow away the user's synthesized content).
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
    """Copy `src` to `site`, excluding only transient build / dep dirs."""
    shutil.copytree(
        src, site,
        ignore=shutil.ignore_patterns(*_TRANSIENT_DIRS),
    )


def _overlay_sync(src: Path, site: Path) -> None:
    """Walk `src`; copy each file into `site` unless it's transient or project-owned.

    Project-owned subtrees are never touched on overlay-sync — they belong
    to the user's project state. The textbook / concept-explainer writers
    rewrite the JSON manifests from SQLite on every ``build``, so freshness
    is guaranteed without overlay-sync's help.
    """
    walker = src.walk() if hasattr(src, "walk") else _walk(src)
    for root, dirs, files in walker:
        rel = root.relative_to(src)
        if any(part in _TRANSIENT_DIRS for part in rel.parts):
            dirs[:] = []
            continue
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
