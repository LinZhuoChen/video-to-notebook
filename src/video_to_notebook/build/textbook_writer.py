"""Bridge: SQLite curriculum + .course-merger/textbook fragments → site/src/content/textbook.

Astro reads these at build time. Manifest format stable across builds so
Astro pages can rely on it via `import.meta.glob`.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from video_to_notebook.db.session import connect

MANIFEST_VERSION = "1"


def _read_project_language(db_path: Path) -> str:
    """Read build_meta.language; default to 'zh' for legacy projects."""
    try:
        with connect(db_path) as conn:
            row = conn.execute(
                "SELECT value FROM build_meta WHERE key='language'"
            ).fetchone()
        if row and row[0] in ("zh", "en"):
            return row[0]
    except Exception:
        pass
    return "zh"


def write_textbook_assets(
    *,
    db_path: Path,
    state_dir: Path,
    site_dir: Path,
) -> None:
    """Emit site/src/content/textbook/<lang>/curriculum.json + chapter HTML fragments.

    The site is built once per language (PUBLIC_LANGUAGE env at Astro build
    time picks zh/ or en/). A bilingual demo therefore needs *both*
    sub-folders populated — typically by running this writer twice from
    two project DBs (one zh, one en), or by editing build_meta.language
    between runs.
    """
    lang = _read_project_language(db_path)
    target = site_dir / "src" / "content" / "textbook" / lang
    target.mkdir(parents=True, exist_ok=True)

    chapters: list[dict[str, Any]] = []
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT order_idx, module, title, blurb, primary_concept_slug,
                   related_concept_slugs, status, synthesized_path
            FROM curriculum_chapters ORDER BY order_idx
            """
        ).fetchall()

    for order, module, title, blurb, primary, related_json, status, frag in rows:
        chapters.append({
            "order_idx": order,
            "module": module,
            "title": title,
            "blurb": blurb,
            "primary_concept_slug": primary,
            "related_concept_slugs": json.loads(related_json or "[]"),
            "status": status,
            "html_fragment": frag,
        })
        if status == "synthesized" and frag:
            src = state_dir / "textbook" / frag
            if src.is_file():
                shutil.copyfile(src, target / frag)

    manifest = {
        "schema_version": MANIFEST_VERSION,
        "chapters": chapters,
    }
    (target / "curriculum.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
