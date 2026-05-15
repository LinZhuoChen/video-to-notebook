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


def ensure_site_dir(project_root: Path) -> Path:
    """Return <project_root>/site, syncing bundled template files on every call.

    On first use this is a full copy. On subsequent calls we overlay-sync the
    template's `src/` and config files into the project (preserving
    `node_modules/`, `dist/`, `.astro/`, and anything outside the template).

    This means upgrading course-merger automatically picks up new template
    files (e.g. `src/i18n.ts`) without forcing the user to re-init.
    """
    site = project_root / "site"
    src = _bundled_template_root()
    if not src.is_dir():
        raise FileNotFoundError(
            f"bundled template-site not found at {src}; reinstall course-merger?"
        )

    if not site.is_dir():
        shutil.copytree(
            src, site,
            ignore=shutil.ignore_patterns("node_modules", "dist", ".astro"),
        )
        return site

    # Overlay-sync: copy each file from template into site, overwriting
    # existing copies but never deleting user-added files. Skip the heavy
    # dirs the template ships without.
    for root, dirs, files in src.walk() if hasattr(src, "walk") else _walk(src):
        rel = root.relative_to(src)
        # Skip well-known transient dirs.
        if any(part in {"node_modules", "dist", ".astro"} for part in rel.parts):
            dirs[:] = []
            continue
        dst_dir = site / rel
        dst_dir.mkdir(parents=True, exist_ok=True)
        for name in files:
            src_file = root / name
            dst_file = dst_dir / name
            shutil.copyfile(src_file, dst_file)

    return site


def _walk(root: Path):
    """Fallback for Python < 3.12 where Path.walk doesn't exist."""
    import os
    for dirpath, dirnames, filenames in os.walk(root):
        yield Path(dirpath), dirnames, filenames
