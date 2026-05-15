from __future__ import annotations

from video_to_notebook.build.writers import (
    write_concept_md,
    write_course_md,
    write_lecture_md,
)


def test_write_concept_md_includes_frontmatter():
    md = write_concept_md(
        concept={
            "slug": "self-attention",
            "canonical_name": "Self-Attention",
            "description": "SA desc",
            "ontology_source": "seed",
            "occurrence_count": 5,
            "aliases": ["SA", "self attention"],
        },
        occurrences=[
            {
                "course_slug": "cs336",
                "lecture_idx": 2,
                "lecture_title": "L2",
                "video_url": "https://yt/v",
                "start_sec": 10.5,
                "end_sec": 30.0,
                "text": "hello",
                "confidence": 0.9,
            }
        ],
    )

    assert md.startswith("---\n")
    # Astro 5 reserves `slug`; it must NOT appear in frontmatter
    frontmatter_block = md.split("---", 2)[1]
    assert "\nslug:" not in frontmatter_block
    assert 'canonical_name: Self-Attention' in md
    assert 'occurrence_count: 5' in md
    assert "cs336" in md  # body mentions the course
    assert "10" in md  # timestamp surfaced


def test_write_concept_md_empty_occurrences():
    md = write_concept_md(
        concept={
            "slug": "x",
            "canonical_name": "X",
            "description": "",
            "ontology_source": "seed",
            "occurrence_count": 0,
            "aliases": [],
        },
        occurrences=[],
    )
    assert md.startswith("---\n")
    assert "occurrence_count: 0" in md


def test_write_course_md_lists_lectures():
    md = write_course_md(
        course={
            "slug": "cs336",
            "title": "CS336",
            "platform": "youtube",
            "source_url": "https://yt/p",
            "lecture_count": 2,
        },
        lectures=[
            {"idx": 1, "title": "Intro", "video_url": "https://yt/v1", "duration_sec": 600},
            {"idx": 2, "title": "Attention", "video_url": "https://yt/v2", "duration_sec": 1200},
        ],
    )
    # Astro 5 reserves `slug` — must not be in frontmatter
    frontmatter_block = md.split("---", 2)[1]
    assert "\nslug:" not in frontmatter_block
    assert 'title: CS336' in md
    assert 'lecture_count: 2' in md
    assert "Intro" in md
    assert "Attention" in md


def test_write_lecture_md_serializes_chunks_into_frontmatter():
    md = write_lecture_md(
        course={"slug": "cs336"},
        lecture={
            "id": 7,
            "idx": 2,
            "title": "Attention",
            "video_url": "https://yt/v2",
            "duration_sec": 1200,
        },
        chunks=[
            {
                "id": 1, "idx": 0, "start_sec": 0, "end_sec": 60,
                "text": "self attention is great",
                "concept_slugs": ["self-attention"],
            },
            {
                "id": 2, "idx": 1, "start_sec": 60, "end_sec": 120,
                "text": "multi head",
                "concept_slugs": ["mha"],
            },
        ],
    )
    # Astro 5 reserves `slug` — it's auto-derived from filename, not in frontmatter
    frontmatter_block = md.split("---", 2)[1]
    assert "\nslug:" not in frontmatter_block
    assert 'course_slug: cs336' in md
    assert 'idx: 2' in md
    assert 'chunks:' in md
    assert 'concept_slugs:' in md
    assert "self attention" in md
