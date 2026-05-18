"""Whisper-based audio→subtitle fallback for videos without published captions.

The crawler tries `yt-dlp --write-subs` and `--write-auto-subs` first; when both
return nothing this module steps in: yt-dlp downloads the audio track, Whisper
transcribes it, and the result is formatted as a WebVTT string so the existing
`parse_vtt` → chunker → DB pipeline keeps working unchanged.

Two backends, both optional dependencies:
  * `mlx-whisper` (Apple Silicon, faster on M-series)
  * `faster-whisper` (cross-platform CPU/GPU fallback)

Install with `pip install video-to-notebook[whisper]` to pick up whichever is
appropriate for the host. The runner only invokes a transcriber when one is
explicitly passed, so the import surface stays zero for users who don't need it.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True, slots=True)
class Segment:
    start_sec: float
    end_sec: float
    text: str


class Transcriber(Protocol):
    """Audio file → list of timestamped segments. Backends are interchangeable."""

    backend: str
    model: str
    language: str | None

    def transcribe(self, audio_path: Path) -> list[Segment]: ...


# ---- VTT formatting ----------------------------------------------------------


def _format_timestamp(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms == 1000:
        ms = 0
        s += 1
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def segments_to_vtt(segments: list[Segment]) -> str:
    """Render whisper segments as a WebVTT document the existing parser eats."""
    lines = ["WEBVTT", ""]
    for seg in segments:
        text = seg.text.strip()
        if not text:
            continue
        lines.append(f"{_format_timestamp(seg.start_sec)} --> {_format_timestamp(seg.end_sec)}")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


# ---- Audio download ----------------------------------------------------------


class AudioDownloadError(RuntimeError):
    pass


def download_audio(
    video_url: str,
    *,
    cookies_from: str | None,
    work_dir: Path,
    audio_format: str = "m4a",
    timeout: int = 600,
) -> Path:
    """yt-dlp --extract-audio. Returns the path to the downloaded audio file."""
    out_template = work_dir / "audio.%(ext)s"
    cmd = ["yt-dlp"]
    if cookies_from:
        cmd += ["--cookies-from-browser", cookies_from]
    cmd += [
        "--extract-audio",
        "--audio-format", audio_format,
        "--audio-quality", "0",
        "--no-playlist",
        "-o", str(out_template),
        video_url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=timeout)
    if result.returncode != 0:
        last_err = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "no error message"
        raise AudioDownloadError(
            f"yt-dlp audio download failed for {video_url} (exit {result.returncode}): {last_err}"
        )
    # yt-dlp normalises the final extension to audio_format
    audio_file = work_dir / f"audio.{audio_format}"
    if not audio_file.exists():
        # Sometimes yt-dlp picks a different extension; pick whatever ended up there.
        matches = list(work_dir.glob("audio.*"))
        if not matches:
            raise AudioDownloadError(
                f"yt-dlp succeeded but no audio file was produced in {work_dir}"
            )
        audio_file = matches[0]
    return audio_file


@contextmanager
def _workspace(explicit_dir: Path | None) -> Iterator[Path]:
    if explicit_dir is not None:
        explicit_dir.mkdir(parents=True, exist_ok=True)
        yield explicit_dir
    else:
        with tempfile.TemporaryDirectory(prefix="v2n-whisper-") as td:
            yield Path(td)


# ---- Backends ----------------------------------------------------------------


class MlxWhisperTranscriber:
    """Apple Silicon backend. Lazy-imports mlx_whisper on first transcribe()."""

    backend = "mlx-whisper"

    def __init__(self, model: str = "mlx-community/whisper-small-mlx", language: str | None = None) -> None:
        self.model = model
        self.language = language

    def transcribe(self, audio_path: Path) -> list[Segment]:
        try:
            import mlx_whisper  # type: ignore[import-untyped]
        except ImportError as e:
            raise ImportError(
                "mlx-whisper not installed. `pip install video-to-notebook[whisper]` on macOS, "
                "or pass --whisper-backend faster-whisper to use the cross-platform fallback."
            ) from e

        kwargs: dict = {"path_or_hf_repo": self.model}
        if self.language:
            kwargs["language"] = self.language
        result = mlx_whisper.transcribe(str(audio_path), **kwargs)
        return [
            Segment(
                start_sec=float(seg["start"]),
                end_sec=float(seg["end"]),
                text=str(seg["text"]),
            )
            for seg in result.get("segments", [])
        ]


class FasterWhisperTranscriber:
    """Cross-platform CPU/GPU backend. Lazy-imports faster_whisper."""

    backend = "faster-whisper"

    def __init__(
        self,
        model: str = "small",
        language: str | None = None,
        compute_type: str = "int8",
    ) -> None:
        self.model = model
        self.language = language
        self.compute_type = compute_type
        self._model_obj = None

    def _ensure_model(self):
        if self._model_obj is not None:
            return self._model_obj
        try:
            from faster_whisper import WhisperModel  # type: ignore[import-untyped]
        except ImportError as e:
            raise ImportError(
                "faster-whisper not installed. `pip install video-to-notebook[whisper]` or "
                "`pip install faster-whisper`."
            ) from e
        self._model_obj = WhisperModel(self.model, compute_type=self.compute_type)
        return self._model_obj

    def transcribe(self, audio_path: Path) -> list[Segment]:
        model = self._ensure_model()
        kwargs: dict = {}
        if self.language:
            kwargs["language"] = self.language
        segments, _info = model.transcribe(str(audio_path), **kwargs)
        return [
            Segment(start_sec=float(s.start), end_sec=float(s.end), text=str(s.text))
            for s in segments
        ]


# ---- Factory + orchestrator --------------------------------------------------


_DEFAULT_BACKEND_BY_PLATFORM = {
    "darwin": "mlx-whisper",
}


def build_transcriber(
    *,
    backend: str | None = None,
    model: str | None = None,
    language: str | None = None,
) -> Transcriber:
    """Pick mlx-whisper on macOS, faster-whisper elsewhere; explicit `backend` overrides."""
    chosen = backend or _DEFAULT_BACKEND_BY_PLATFORM.get(sys.platform, "faster-whisper")
    if chosen == "mlx-whisper":
        return MlxWhisperTranscriber(
            model=model or "mlx-community/whisper-small-mlx",
            language=language,
        )
    if chosen == "faster-whisper":
        return FasterWhisperTranscriber(
            model=model or "small",
            language=language,
        )
    raise ValueError(
        f"unknown whisper backend {chosen!r}. Use 'mlx-whisper' or 'faster-whisper'."
    )


def transcribe_video_to_vtt(
    *,
    video_url: str,
    cookies_from: str | None,
    transcriber: Transcriber,
    work_dir: Path | None = None,
) -> str | None:
    """Download audio, run Whisper, return a VTT string. Returns None on download failure."""
    try:
        with _workspace(work_dir) as work:
            audio_path = download_audio(
                video_url, cookies_from=cookies_from, work_dir=work
            )
            segments = transcriber.transcribe(audio_path)
            if not segments:
                return None
            return segments_to_vtt(segments)
    except AudioDownloadError:
        return None
