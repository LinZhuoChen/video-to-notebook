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


def test_parse_vtt_accepts_mm_ss_timestamp_without_hours():
    """WebVTT timestamps may omit hours for clips under 1h. yt-dlp's
    SRT→VTT post-processor emits this short form for short Bilibili
    auto-captions; the parser must accept both shapes.

    Regression: pre-fix the regex was anchored to ``HH:MM:SS.mmm`` and
    silently produced 0 cues for every Bilibili lecture, leaving 31
    'ok' lectures with empty transcripts.
    """
    src = (
        "WEBVTT\n\n"
        "00:02.660 --> 00:03.060\nHello\n\n"
        "00:03.060 --> 00:07.730\n今天来给大家讲一下手写self attention的四重境界\n"
    )
    cues = parse_vtt(src)
    assert len(cues) == 2
    assert cues[0].start_sec == pytest.approx(2.66)
    assert cues[0].end_sec == pytest.approx(3.06)
    assert cues[0].text == "Hello"
    assert cues[1].text == "今天来给大家讲一下手写self attention的四重境界"
    assert cues[1].start_sec == pytest.approx(3.06)
    assert cues[1].end_sec == pytest.approx(7.73)


def test_parse_vtt_accepts_both_timestamp_shapes_in_one_file():
    """Mix the two forms in one file — both styles should parse correctly."""
    src = (
        "WEBVTT\n\n"
        "00:00:01.000 --> 00:00:02.000\nwith hours\n\n"
        "00:05.500 --> 00:06.000\nwithout hours\n"
    )
    cues = parse_vtt(src)
    assert len(cues) == 2
    assert cues[0].start_sec == pytest.approx(1.0)
    assert cues[1].start_sec == pytest.approx(5.5)


def test_parse_vtt_inner_timestamp_strip_handles_short_form():
    """The inner-timestamp stripper (``<00:00:07.200>`` style karaoke
    markers used by YouTube) also has to tolerate the short form."""
    src = (
        "WEBVTT\n\n"
        "00:05.000 --> 00:06.000\nstart<00:05.500>word<00:06.000>end\n"
    )
    cues = parse_vtt(src)
    assert len(cues) == 1
    assert "<" not in cues[0].text
    assert ">" not in cues[0].text
    assert cues[0].text == "startwordend"
