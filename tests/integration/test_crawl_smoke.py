from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from course_merger.cli import app
from course_merger.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_crawl_youtube_end_to_end(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])

    vtt_text = (fixtures_dir / "mini_course" / "youtube_lecture1.vtt").read_text()

    fake_list = [{"idx": 1, "video_id": "v1", "title": "Intro", "video_url": "https://yt/v1"}]

    with (
        patch("course_merger.crawl.youtube.YouTubeCrawler.list_playlist", return_value=fake_list),
        patch(
            "course_merger.crawl.youtube.YouTubeCrawler.download_subtitle_vtt",
            return_value=vtt_text,
        ),
    ):
        result = runner.invoke(
            app,
            ["crawl", "https://www.youtube.com/watch?v=v1", "--name", "cs336-fake"],
        )

    assert result.exit_code == 0, result.stdout

    db = tmp_project / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        (courses,) = conn.execute("SELECT COUNT(*) FROM courses").fetchone()
        (lectures,) = conn.execute("SELECT COUNT(*) FROM lectures WHERE status='ok'").fetchone()
        (chunks,) = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()

    assert courses == 1
    assert lectures == 1
    assert chunks >= 1


@pytest.mark.integration
def test_crawl_bilibili_requires_cookies(tmp_project: Path):
    runner.invoke(app, ["init"])
    # Mock list_playlist to return one entry, so the runner reaches download_subtitle_vtt
    # which raises BilibiliCookieError when cookies_from is None.
    fake_list = [{"idx": 1, "video_id": "BVxxx", "title": "L1",
                  "video_url": "https://www.bilibili.com/video/BVxxx/?p=1"}]
    with patch("course_merger.crawl.bilibili.BilibiliCrawler.list_playlist", return_value=fake_list):
        result = runner.invoke(
            app,
            ["crawl", "https://www.bilibili.com/video/BVxxx/", "--name", "x"],
        )
    assert result.exit_code != 0
    assert "cookies" in result.stdout.lower()


@pytest.mark.integration
def test_crawl_errors_when_not_initialized(tmp_project: Path):
    result = runner.invoke(app, ["crawl", "https://yt/x", "--name", "y"])
    assert result.exit_code != 0
    assert "init" in result.stdout.lower()


@pytest.mark.integration
def test_crawl_exits_nonzero_on_lecture_error(tmp_project: Path):
    runner.invoke(app, ["init"])

    fake_list = [{"idx": 1, "video_id": "v1", "title": "L1", "video_url": "https://yt/v1"}]
    with (
        patch("course_merger.crawl.youtube.YouTubeCrawler.list_playlist", return_value=fake_list),
        patch(
            "course_merger.crawl.youtube.YouTubeCrawler.download_subtitle_vtt",
            side_effect=RuntimeError("boom"),
        ),
    ):
        result = runner.invoke(
            app, ["crawl", "https://www.youtube.com/watch?v=v1", "--name", "broken"]
        )

    assert result.exit_code == 3, result.stdout
