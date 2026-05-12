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
    pkg = resources.files("course_merger") / "_template_site"
    return Path(str(pkg))


def ensure_site_dir(project_root: Path) -> Path:
    """Return <project_root>/site, copying the bundled template on first use.

    Subsequent calls leave the directory untouched (idempotent), so user edits
    and node_modules survive.
    """
    site = project_root / "site"
    if site.is_dir():
        return site

    src = _bundled_template_root()
    if not src.is_dir():
        raise FileNotFoundError(
            f"bundled template-site not found at {src}; reinstall course-merger?"
        )
    shutil.copytree(
        src, site,
        ignore=shutil.ignore_patterns("node_modules", "dist", ".astro"),
    )
    return site
