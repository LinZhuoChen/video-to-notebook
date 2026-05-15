from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.crawl.subtitles import Cue, parse_vtt


def test_parse_vtt_basic(fixtures_dir: Path):
    text = (fixtures_dir / "mini_course" / "youtube_lecture1.vtt").read_text()
    cues = parse_vtt(text)

    assert len(cues) == 3  # duplicate dropped
    assert isinstance(cues[0], Cue)
    assert cues[0].start_sec == pytest.approx(0.5)
    assert cues[0].end_sec == pytest.approx(3.1)
    assert "Welcome to lecture one" in cues[0].text


def test_parse_vtt_strips_inline_tags(fixtures_dir: Path):
    text = (fixtures_dir / "mini_course" / "youtube_lecture1.vtt").read_text()
    cues = parse_vtt(text)
    assert "<c>" not in cues[2].text
    assert "key" in cues[2].text


def test_parse_vtt_handles_empty():
    assert parse_vtt("") == []
    assert parse_vtt("WEBVTT\n\n") == []


def test_parse_vtt_decodes_html_entities():
    src = "WEBVTT\n\n00:00:01.000 --> 00:00:02.000\n&gt;&gt; Hi &amp; bye"
    cues = parse_vtt(src)
    assert cues[0].text == ">> Hi & bye"
