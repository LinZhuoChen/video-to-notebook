"""Bridge: SQLite concept_explanations + .course-merger/concepts fragments →
site/src/content/concept-explainers.

Astro reads these at build time for the rich /concepts/<slug>/ entries.
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


def write_concept_explainer_assets(
    *,
    db_path: Path,
    state_dir: Path,
    site_dir: Path,
) -> None:
    """Emit site/src/content/concept-explainers/<lang>/{manifest.json + <slug>.html}.

    Builds per-language because the synthesised HTML prose itself is in
    one language. The Astro site picks zh/ or en/ at build time from
    PUBLIC_LANGUAGE.
    """
    lang = _read_project_language(db_path)
    target = site_dir / "src" / "content" / "concept-explainers" / lang
    target.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, Any]] = []
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT c.slug, c.canonical_name, ce.html_fragment, ce.generated_at,
                   ce.explainer
            FROM concept_explanations ce
            JOIN concepts c ON c.id = ce.concept_id
            ORDER BY c.canonical_name
            """
        ).fetchall()

    for slug, name, frag, generated_at, explainer in rows:
        entries.append({
            "slug": slug,
            "canonical_name": name,
            "html_fragment": frag,
            "generated_at": generated_at,
            "explainer": explainer,
        })
        src = state_dir / "concepts" / frag
        if src.is_file():
            shutil.copyfile(src, target / frag)

    manifest = {
        "schema_version": MANIFEST_VERSION,
        "explainers": entries,
    }
    (target / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
