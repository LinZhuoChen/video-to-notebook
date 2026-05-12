from __future__ import annotations

import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from course_merger.crawl.youtube import YouTubeCrawler


def _fake_completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    return subprocess.CompletedProcess(args=[], returncode=returncode, stdout=stdout, stderr=stderr)


def test_list_playlist_parses_flat_output():
    fake_stdout = "1|abc123|Lecture 1: Intro\n2|def456|Lecture 2: Transformers\n"
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)) as mock:
        entries = YouTubeCrawler().list_playlist("https://youtube.com/playlist?list=PLX")

    assert entries == [
        {"idx": 1, "video_id": "abc123", "title": "Lecture 1: Intro",
         "video_url": "https://www.youtube.com/watch?v=abc123"},
        {"idx": 2, "video_id": "def456", "title": "Lecture 2: Transformers",
         "video_url": "https://www.youtube.com/watch?v=def456"},
    ]
    cmd = mock.call_args.args[0]
    assert "--flat-playlist" in cmd
    assert "%(playlist_index)s|%(id)s|%(title)s" in cmd


def test_list_playlist_single_video_wraps_to_one_entry():
    fake_stdout = "NA|xyz789|Single Talk\n"
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)):
        entries = YouTubeCrawler().list_playlist("https://www.youtube.com/watch?v=xyz789")
    assert len(entries) == 1
    assert entries[0]["idx"] == 1
    assert entries[0]["video_id"] == "xyz789"


def test_download_subtitle_vtt_returns_none_when_no_subs(tmp_path: Path):
    with patch("subprocess.run", return_value=_fake_completed(returncode=0)):
        result = YouTubeCrawler(_work_dir=tmp_path).download_subtitle_vtt(
            "https://www.youtube.com/watch?v=xyz", lang_priority=["en"], cookies_from=None
        )
    assert result is None


def test_download_subtitle_vtt_reads_file(tmp_path: Path):
    crawler = YouTubeCrawler(_work_dir=tmp_path)
    vtt_path = tmp_path / "sub.en.vtt"
    vtt_path.write_text("WEBVTT\n\nfake content")

    def fake_run(cmd, *_args, **_kwargs):
        return _fake_completed()

    with patch("subprocess.run", side_effect=fake_run):
        result = crawler.download_subtitle_vtt(
            "https://www.youtube.com/watch?v=xyz", lang_priority=["en"], cookies_from=None
        )
    assert result is not None
    assert result.startswith("WEBVTT")


from course_merger.crawl.exceptions import PlaylistFetchError


def test_list_playlist_raises_on_nonzero_returncode():
    fake_run = _fake_completed(stderr="ERROR: Video unavailable", returncode=1)
    with patch("subprocess.run", return_value=fake_run):
        with pytest.raises(PlaylistFetchError) as exc:
            YouTubeCrawler().list_playlist("https://www.youtube.com/playlist?list=invalid")
    assert "Video unavailable" in str(exc.value)
