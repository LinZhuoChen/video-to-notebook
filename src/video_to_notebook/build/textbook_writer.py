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


def write_textbook_assets(
    *,
    db_path: Path,
    state_dir: Path,
    site_dir: Path,
) -> None:
    """Emit site/src/content/textbook/curriculum.json + chapter HTML fragments."""
    target = site_dir / "src" / "content" / "textbook"
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
