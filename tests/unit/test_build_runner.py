from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from course_merger.build.runner import BuildReport, run_build
from course_merger.db.session import connect, init_db


def _seed_full(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://yt/p', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'attention is all')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'attention', 'Attention', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )


def test_run_build_writes_content_files(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed_full(db)

    with patch("course_merger.build.runner._run_astro_build") as mock_npm:
        mock_npm.return_value = 0
        report = run_build(project_root=tmp_path, db_path=db, npm_build=True)

    assert isinstance(report, BuildReport)
    assert report.courses_written == 1
    assert report.lectures_written == 1
    assert report.concepts_written == 1

    site = tmp_path / "site"
    # Note singular directory names — matches Astro 5 content collection convention
    assert (site / "src" / "content" / "course" / "cs336.md").is_file()
    assert (site / "src" / "content" / "lecture" / "cs336--1.md").is_file()
    assert (site / "src" / "content" / "concept" / "attention.md").is_file()
    assert mock_npm.called


def test_run_build_skips_npm_when_disabled(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed_full(db)

    with patch("course_merger.build.runner._run_astro_build") as mock_npm:
        run_build(project_root=tmp_path, db_path=db, npm_build=False)
    assert not mock_npm.called


def test_run_build_incremental_only_dirty(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed_full(db)
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (2, 'other', 'Other', 'seed')"
        )
        conn.execute(
            "INSERT INTO build_meta (key, value) VALUES ('dirty_concepts', '[\"attention\"]')"
        )

    with patch("course_merger.build.runner._run_astro_build") as mock_npm:
        mock_npm.return_value = 0
        report = run_build(
            project_root=tmp_path, db_path=db, npm_build=False, incremental=True
        )

    assert report.concepts_written == 1
    site = tmp_path / "site"
    assert (site / "src" / "content" / "concept" / "attention.md").is_file()
    assert not (site / "src" / "content" / "concept" / "other.md").is_file()
