from __future__ import annotations

import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from video_to_notebook.crawl.bilibili import BilibiliCookieError, BilibiliCrawler
from video_to_notebook.crawl.exceptions import PlaylistFetchError


def _fake_completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    return subprocess.CompletedProcess(args=[], returncode=returncode, stdout=stdout, stderr=stderr)


def test_list_playlist_iterates_p_param():
    """Multi-part single video: shared BV id, episode selected by ?p=N."""
    crawler = BilibiliCrawler()
    fake_stdout = "1|BVxxx|Lecture 1\n2|BVxxx|Lecture 2\n3|BVxxx|Lecture 3\n"
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)):
        entries = crawler.list_playlist("https://www.bilibili.com/video/BVxxx/")

    assert len(entries) == 3
    assert entries[0]["video_url"] == "https://www.bilibili.com/video/BVxxx/?p=1"
    assert entries[2]["video_url"] == "https://www.bilibili.com/video/BVxxx/?p=3"


def test_list_playlist_season_yields_canonical_per_bv_urls():
    """Space season / list URLs return entries with distinct BV ids; each
    entry must resolve to its own canonical https://www.bilibili.com/video/BV<id>/
    page — pointing yt-dlp back at the list URL with ?p=N would just
    re-download the default video (the bug that landed 13 identical
    transcripts in the chuguo-aigc-s3 crawl)."""
    crawler = BilibiliCrawler()
    fake_stdout = (
        "1|BV1YiuaznE3X|Episode 1\n"
        "2|BV1jUgtzSEmW|Episode 2\n"
        "3|BV1Mgh4zJEZV|Episode 3\n"
    )
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)):
        entries = crawler.list_playlist(
            "https://space.bilibili.com/20942052/lists/5853725?type=season"
        )

    assert len(entries) == 3
    assert entries[0]["video_url"] == "https://www.bilibili.com/video/BV1YiuaznE3X/"
    assert entries[1]["video_url"] == "https://www.bilibili.com/video/BV1jUgtzSEmW/"
    assert entries[2]["video_url"] == "https://www.bilibili.com/video/BV1Mgh4zJEZV/"
    # The episode IDs from the season are preserved on the entry dict.
    assert [e["video_id"] for e in entries] == ["BV1YiuaznE3X", "BV1jUgtzSEmW", "BV1Mgh4zJEZV"]


def test_download_subtitle_tries_ai_zh_then_ai_en(tmp_path: Path):
    crawler = BilibiliCrawler(_work_dir=tmp_path)

    call_log: list[list[str]] = []

    def fake_run(cmd, *args, **kwargs):
        call_log.append(cmd)
        if "ai-en" in cmd:
            (tmp_path / "sub.ai-en.vtt").write_text("WEBVTT\n\nfake en")
        return _fake_completed()

    with patch("subprocess.run", side_effect=fake_run):
        result = crawler.download_subtitle_vtt(
            "https://www.bilibili.com/video/BVxxx/?p=1",
            lang_priority=["ai-zh", "ai-en"],
            cookies_from="edge",
        )

    assert result == "WEBVTT\n\nfake en"
    assert "ai-zh" in call_log[0]
    assert "ai-en" in call_log[1]


def test_download_subtitle_requires_cookies():
    crawler = BilibiliCrawler()
    with pytest.raises(BilibiliCookieError):
        crawler.download_subtitle_vtt(
            "https://www.bilibili.com/video/BVxxx/?p=1",
            lang_priority=["ai-zh"],
            cookies_from=None,
        )


def test_download_subtitle_detects_403_and_raises():
    crawler = BilibiliCrawler()
    fake_run = _fake_completed(stderr="HTTP Error 403: Forbidden", returncode=1)
    with (
        patch("subprocess.run", return_value=fake_run),
        pytest.raises(BilibiliCookieError) as exc,
    ):
        crawler.download_subtitle_vtt(
            "https://www.bilibili.com/video/BVxxx/?p=1",
            lang_priority=["ai-zh"],
            cookies_from="edge",
        )
    assert "edge" in str(exc.value)


def test_list_playlist_raises_on_nonzero_returncode():
    fake_run = _fake_completed(stderr="ERROR: BVxxx not found", returncode=1)
    with patch("subprocess.run", return_value=fake_run), pytest.raises(PlaylistFetchError):
        BilibiliCrawler().list_playlist("https://www.bilibili.com/video/BVxxx/")
