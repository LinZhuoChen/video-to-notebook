from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from video_to_notebook.crawl.runner import CrawlReport, run_crawl
from video_to_notebook.db.session import connect, init_db


@pytest.fixture
def fake_crawler():
    crawler = MagicMock()
    crawler.platform = "youtube"
    crawler.list_playlist.return_value = [
        {"idx": 1, "video_id": "v1", "title": "L1", "video_url": "https://yt/v1"},
        {"idx": 2, "video_id": "v2", "title": "L2", "video_url": "https://yt/v2"},
    ]
    crawler.download_subtitle_vtt.side_effect = [
        "WEBVTT\n\n00:00:00.000 --> 00:00:02.000\nHello.\n\n00:00:02.000 --> 00:00:04.000\nWorld.",
        None,
    ]
    return crawler


def test_run_crawl_inserts_lectures_and_chunks(tmp_path: Path, fake_crawler):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    report = run_crawl(
        db_path=db_path,
        crawler=fake_crawler,
        url="https://yt/playlist",
        course_slug="testcourse",
        course_title="Test Course",
        lang_priority=["en"],
        cookies_from=None,
    )

    assert isinstance(report, CrawlReport)
    assert report.course_slug == "testcourse"
    assert report.lectures_ok == 1
    assert report.lectures_no_subs == 1

    with connect(db_path) as conn:
        (courses,) = conn.execute("SELECT COUNT(*) FROM courses").fetchone()
        (lectures,) = conn.execute("SELECT COUNT(*) FROM lectures").fetchone()
        (chunks,) = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()

    assert courses == 1
    assert lectures == 2
    assert chunks >= 1


def test_run_crawl_is_idempotent(tmp_path: Path, fake_crawler):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    run_crawl(
        db_path=db_path,
        crawler=fake_crawler,
        url="https://yt/playlist",
        course_slug="testcourse",
        course_title="Test Course",
        lang_priority=["en"],
        cookies_from=None,
    )

    fake_crawler.download_subtitle_vtt.side_effect = [
        "WEBVTT\n\n00:00:00.000 --> 00:00:02.000\nHello.",
        None,
    ]

    run_crawl(
        db_path=db_path,
        crawler=fake_crawler,
        url="https://yt/playlist",
        course_slug="testcourse",
        course_title="Test Course",
        lang_priority=["en"],
        cookies_from=None,
    )

    with connect(db_path) as conn:
        (lectures,) = conn.execute("SELECT COUNT(*) FROM lectures").fetchone()
    assert lectures == 2
