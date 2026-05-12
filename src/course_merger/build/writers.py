"""Pure functions that turn dict rows into Astro-content-collection Markdown."""
from __future__ import annotations

from typing import Any

import yaml


def _frontmatter(data: dict[str, Any]) -> str:
    body = yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, default_flow_style=False
    )
    return f"---\n{body}---\n"


def write_concept_md(*, concept: dict[str, Any], occurrences: list[dict[str, Any]]) -> str:
    fm = {
        "slug": concept["slug"],
        "canonical_name": concept["canonical_name"],
        "description": concept.get("description", ""),
        "ontology_source": concept["ontology_source"],
        "aliases": concept.get("aliases", []),
        "occurrence_count": concept["occurrence_count"],
    }
    body_lines = [f"# {concept['canonical_name']}", ""]
    if concept.get("description"):
        body_lines += [concept["description"], ""]
    body_lines.append(
        f"**{len(occurrences)} occurrence{'s' if len(occurrences) != 1 else ''}** across courses:"
    )
    body_lines.append("")
    for o in occurrences:
        ts = int(o["start_sec"])
        body_lines.append(
            f"- **{o['course_slug']}** L{o['lecture_idx']} ({o['lecture_title']}) "
            f"@ {ts}s — {o['text'][:120]}"
        )
    return _frontmatter(fm) + "\n".join(body_lines) + "\n"


def write_course_md(*, course: dict[str, Any], lectures: list[dict[str, Any]]) -> str:
    fm = {
        "slug": course["slug"],
        "title": course["title"],
        "platform": course["platform"],
        "source_url": course["source_url"],
        "lecture_count": course["lecture_count"],
    }
    body_lines = [f"# {course['title']}", "", f"_{course['platform']}_", ""]
    body_lines.append("## Lectures")
    for lec in lectures:
        dur = ""
        if lec.get("duration_sec"):
            mins = lec["duration_sec"] // 60
            dur = f" · {mins} min"
        body_lines.append(f"- L{lec['idx']}: {lec['title']}{dur}")
    return _frontmatter(fm) + "\n".join(body_lines) + "\n"


def write_lecture_md(
    *, course: dict[str, Any], lecture: dict[str, Any], chunks: list[dict[str, Any]]
) -> str:
    fm = {
        "slug": f"{course['slug']}--{lecture['idx']}",
        "course_slug": course["slug"],
        "idx": lecture["idx"],
        "title": lecture["title"],
        "video_url": lecture["video_url"],
        "duration_sec": lecture.get("duration_sec"),
        "chunks": [
            {
                "idx": c["idx"],
                "start_sec": c["start_sec"],
                "end_sec": c["end_sec"],
                "text": c["text"],
                "concept_slugs": c.get("concept_slugs", []),
            }
            for c in chunks
        ],
    }
    body = f"# {lecture['title']}\n\nSee the structured chunks above.\n"
    return _frontmatter(fm) + body
