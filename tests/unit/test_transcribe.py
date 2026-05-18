"""Tests for the Whisper-fallback module.

Heavy backends (mlx-whisper / faster-whisper) are NOT imported here. We only
test the format-conversion logic, the audio-download error path, and the
end-to-end glue with a fake Transcriber.
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from video_to_notebook.crawl.transcribe import (
    AudioDownloadError,
    Segment,
    _format_timestamp,
    build_transcriber,
    download_audio,
    segments_to_vtt,
    transcribe_video_to_vtt,
)

# ---- _format_timestamp -------------------------------------------------------


def test_format_timestamp_zero():
    assert _format_timestamp(0) == "00:00:00.000"


def test_format_timestamp_sub_second():
    assert _format_timestamp(0.123) == "00:00:00.123"


def test_format_timestamp_compound():
    assert _format_timestamp(3661.5) == "01:01:01.500"


def test_format_timestamp_rounds_ms():
    # 0.001s → 1ms (unambiguous; avoids banker's-rounding edge case at 0.5)
    assert _format_timestamp(0.001) == "00:00:00.001"


def test_format_timestamp_carries_ms_rounding_to_next_second():
    # 0.9995 → 1.000s, ms=0
    assert _format_timestamp(0.9995) == "00:00:01.000"


def test_format_timestamp_negative_clamped():
    assert _format_timestamp(-1) == "00:00:00.000"


# ---- segments_to_vtt ---------------------------------------------------------


def test_segments_to_vtt_basic():
    segs = [
        Segment(start_sec=0.0, end_sec=2.5, text="Hello world."),
        Segment(start_sec=3.0, end_sec=5.75, text="Second line."),
    ]
    vtt = segments_to_vtt(segs)
    assert vtt.startswith("WEBVTT")
    assert "00:00:00.000 --> 00:00:02.500" in vtt
    assert "Hello world." in vtt
    assert "00:00:03.000 --> 00:00:05.750" in vtt
    assert "Second line." in vtt


def test_segments_to_vtt_skips_empty_text():
    segs = [
        Segment(start_sec=0.0, end_sec=1.0, text="  "),
        Segment(start_sec=1.0, end_sec=2.0, text="kept"),
    ]
    vtt = segments_to_vtt(segs)
    # Empty cue should be skipped; only one cue produced.
    cue_lines = [line for line in vtt.splitlines() if "-->" in line]
    assert len(cue_lines) == 1
    assert "kept" in vtt


def test_segments_to_vtt_empty():
    assert segments_to_vtt([]) == "WEBVTT\n"


def test_segments_to_vtt_roundtrips_through_parse_vtt():
    """The whole point of this module: the synthesised VTT must parse cleanly."""
    from video_to_notebook.crawl.subtitles import parse_vtt

    segs = [
        Segment(start_sec=0.0, end_sec=1.5, text="First."),
        Segment(start_sec=2.0, end_sec=4.0, text="Second."),
    ]
    cues = parse_vtt(segments_to_vtt(segs))
    assert [c.text for c in cues] == ["First.", "Second."]
    assert cues[0].start_sec == pytest.approx(0.0)
    assert cues[0].end_sec == pytest.approx(1.5)
    assert cues[1].start_sec == pytest.approx(2.0)


# ---- download_audio ----------------------------------------------------------


def test_download_audio_raises_on_yt_dlp_failure(tmp_path):
    with patch("video_to_notebook.crawl.transcribe.subprocess.run") as mock_run:
        mock_run.return_value = type(
            "R", (), {"returncode": 1, "stderr": "ERROR: video unavailable", "stdout": ""}
        )()
        with pytest.raises(AudioDownloadError, match="exit 1"):
            download_audio("https://example.com/v", cookies_from=None, work_dir=tmp_path)


def test_download_audio_returns_path_on_success(tmp_path):
    expected = tmp_path / "audio.m4a"
    expected.write_bytes(b"fake-audio")

    with patch("video_to_notebook.crawl.transcribe.subprocess.run") as mock_run:
        mock_run.return_value = type(
            "R", (), {"returncode": 0, "stderr": "", "stdout": ""}
        )()
        got = download_audio("https://example.com/v", cookies_from=None, work_dir=tmp_path)

    assert got == expected


def test_download_audio_falls_back_to_glob_when_extension_differs(tmp_path):
    other = tmp_path / "audio.mp3"
    other.write_bytes(b"fake")
    with patch("video_to_notebook.crawl.transcribe.subprocess.run") as mock_run:
        mock_run.return_value = type(
            "R", (), {"returncode": 0, "stderr": "", "stdout": ""}
        )()
        got = download_audio("https://example.com/v", cookies_from=None, work_dir=tmp_path)
    assert got == other


# ---- build_transcriber -------------------------------------------------------


def test_build_transcriber_rejects_unknown_backend():
    with pytest.raises(ValueError, match="unknown whisper backend"):
        build_transcriber(backend="not-a-backend")


def test_build_transcriber_returns_mlx_on_darwin():
    with patch("video_to_notebook.crawl.transcribe.sys.platform", "darwin"):
        t = build_transcriber()
    assert t.backend == "mlx-whisper"
    assert t.model == "mlx-community/whisper-small-mlx"


def test_build_transcriber_returns_faster_elsewhere():
    with patch("video_to_notebook.crawl.transcribe.sys.platform", "linux"):
        t = build_transcriber()
    assert t.backend == "faster-whisper"
    assert t.model == "small"


def test_build_transcriber_respects_explicit_args():
    t = build_transcriber(backend="faster-whisper", model="large-v3", language="zh")
    assert t.backend == "faster-whisper"
    assert t.model == "large-v3"
    assert t.language == "zh"


# ---- transcribe_video_to_vtt -------------------------------------------------


class _FakeTranscriber:
    backend = "fake"
    model = "fake-model"
    language: str | None = None

    def transcribe(self, audio_path: Path) -> list[Segment]:
        assert audio_path.exists()
        return [
            Segment(start_sec=0.0, end_sec=1.0, text="hello"),
            Segment(start_sec=1.5, end_sec=3.0, text="world"),
        ]


def test_transcribe_video_to_vtt_happy_path(tmp_path):
    audio = tmp_path / "audio.m4a"
    audio.write_bytes(b"fake")

    def fake_download(video_url, *, cookies_from, work_dir, **kwargs):
        return audio

    with patch("video_to_notebook.crawl.transcribe.download_audio", fake_download):
        vtt = transcribe_video_to_vtt(
            video_url="https://example.com/v",
            cookies_from=None,
            transcriber=_FakeTranscriber(),
            work_dir=tmp_path,
        )
    assert vtt is not None
    assert "hello" in vtt
    assert "world" in vtt
    assert vtt.startswith("WEBVTT")


def test_transcribe_video_to_vtt_returns_none_on_download_error(tmp_path):
    def boom(*a, **kw):
        raise AudioDownloadError("boom")

    with patch("video_to_notebook.crawl.transcribe.download_audio", boom):
        vtt = transcribe_video_to_vtt(
            video_url="https://example.com/v",
            cookies_from=None,
            transcriber=_FakeTranscriber(),
            work_dir=tmp_path,
        )
    assert vtt is None


def test_transcribe_video_to_vtt_returns_none_when_transcriber_emits_nothing(tmp_path):
    class _Silent:
        backend = "fake"
        model = "fake"
        language: str | None = None

        def transcribe(self, audio_path):
            return []

    audio = tmp_path / "audio.m4a"
    audio.write_bytes(b"fake")

    def fake_download(*a, **kw):
        return audio

    with patch("video_to_notebook.crawl.transcribe.download_audio", fake_download):
        vtt = transcribe_video_to_vtt(
            video_url="https://example.com/v",
            cookies_from=None,
            transcriber=_Silent(),
            work_dir=tmp_path,
        )
    assert vtt is None
