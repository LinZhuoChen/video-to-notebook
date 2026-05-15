"""Orchestrate: ensure site → query DB → write Markdown content → optional astro build."""
from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

from video_to_notebook.build.concept_writer import write_concept_explainer_assets
from video_to_notebook.build.queries import (
    all_concepts_with_counts,
    all_courses_with_lecture_counts,
    chunks_for_lecture,
    concept_occurrences,
    lectures_for_course,
)
from video_to_notebook.build.template_copy import ensure_site_dir
from video_to_notebook.build.textbook_writer import write_textbook_assets
from video_to_notebook.build.writers import (
    write_concept_md,
    write_course_md,
    write_lecture_md,
)
from video_to_notebook.db.session import connect


@dataclass(frozen=True, slots=True)
class BuildReport:
    courses_written: int
    lectures_written: int
    concepts_written: int
    npm_exit_code: int | None


def _dirty_concepts(db_path: Path) -> set[str] | None:
    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT value FROM build_meta WHERE key='dirty_concepts'"
        ).fetchone()
    if not row:
        return None
    try:
        return set(json.loads(row[0]))
    except (json.JSONDecodeError, TypeError):
        return None


def _run_astro_build(site_dir: Path, language: str = "zh") -> int:
    if not (site_dir / "node_modules").is_dir():
        subprocess.run(["npm", "install", "--silent"], cwd=site_dir, check=False)
    # Pass site language to Astro via env var. Vite/Astro pick up
    # `PUBLIC_LANGUAGE` and expose it as `import.meta.env.PUBLIC_LANGUAGE`,
    # which i18n.ts reads to select the dictionary.
    env = {**os.environ, "PUBLIC_LANGUAGE": language}
    result = subprocess.run(["npm", "run", "build"], cwd=site_dir, check=False, env=env)
    return result.returncode


def _get_site_language(db_path: Path) -> str:
    """Read site language from build_meta; default 'zh' for legacy projects."""
    import sqlite3
    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            "SELECT value FROM build_meta WHERE key='language'"
        ).fetchone()
    return row[0] if row else "zh"


def run_build(
    *,
    project_root: Path,
    db_path: Path,
    npm_build: bool = True,
    incremental: bool = False,
) -> BuildReport:
    site_dir = ensure_site_dir(project_root)
    content_dir = site_dir / "src" / "content"

    # Ensure target dirs exist (singular per Astro 5 content collection convention)
    for sub in ("course", "lecture", "concept"):
        (content_dir / sub).mkdir(parents=True, exist_ok=True)

    courses = all_courses_with_lecture_counts(db_path)
    for course in courses:
        md = write_course_md(course=course, lectures=lectures_for_course(db_path, course["slug"]))
        (content_dir / "course" / f"{course['slug']}.md").write_text(md, encoding="utf-8")

    lectures_written = 0
    for course in courses:
        for lec in lectures_for_course(db_path, course["slug"]):
            md = write_lecture_md(
                course=course,
                lecture=lec,
                chunks=chunks_for_lecture(db_path, lecture_id=lec["id"]),
            )
            slug = f"{course['slug']}--{lec['idx']}"
            (content_dir / "lecture" / f"{slug}.md").write_text(md, encoding="utf-8")
            lectures_written += 1

    all_concepts = all_concepts_with_counts(db_path)
    dirty = _dirty_concepts(db_path) if incremental else None
    if dirty is not None:
        concepts = [c for c in all_concepts if c["slug"] in dirty]
    else:
        concepts = all_concepts

    for concept in concepts:
        md = write_concept_md(
            concept=concept,
            occurrences=concept_occurrences(db_path, concept["slug"]),
        )
        (content_dir / "concept" / f"{concept['slug']}.md").write_text(md, encoding="utf-8")

    from video_to_notebook.config import PROJECT_MARKER
    state_dir = project_root / PROJECT_MARKER
    write_textbook_assets(db_path=db_path, state_dir=state_dir, site_dir=site_dir)
    write_concept_explainer_assets(db_path=db_path, state_dir=state_dir, site_dir=site_dir)

    npm_code: int | None = None
    if npm_build:
        language = _get_site_language(db_path)
        npm_code = _run_astro_build(site_dir, language=language)

    return BuildReport(
        courses_written=len(courses),
        lectures_written=lectures_written,
        concepts_written=len(concepts),
        npm_exit_code=npm_code,
    )
