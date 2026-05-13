"""Orchestrate: ensure site → query DB → write Markdown content → optional astro build."""
from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

from course_merger.build.concept_writer import write_concept_explainer_assets
from course_merger.build.queries import (
    all_concepts_with_counts,
    all_courses_with_lecture_counts,
    chunks_for_lecture,
    concept_occurrences,
    lectures_for_course,
)
from course_merger.build.template_copy import ensure_site_dir
from course_merger.build.textbook_writer import write_textbook_assets
from course_merger.build.writers import (
    write_concept_md,
    write_course_md,
    write_lecture_md,
)
from course_merger.db.session import connect


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


def _run_astro_build(site_dir: Path) -> int:
    if not (site_dir / "node_modules").is_dir():
        subprocess.run(["npm", "install", "--silent"], cwd=site_dir, check=False)
    result = subprocess.run(["npm", "run", "build"], cwd=site_dir, check=False)
    return result.returncode


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

    state_dir = project_root / ".course-merger"
    write_textbook_assets(db_path=db_path, state_dir=state_dir, site_dir=site_dir)
    write_concept_explainer_assets(db_path=db_path, state_dir=state_dir, site_dir=site_dir)

    npm_code: int | None = None
    if npm_build:
        npm_code = _run_astro_build(site_dir)

    return BuildReport(
        courses_written=len(courses),
        lectures_written=lectures_written,
        concepts_written=len(concepts),
        npm_exit_code=npm_code,
    )
