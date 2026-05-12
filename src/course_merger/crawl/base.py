"""Crawler protocol + chunker (cue → chunk)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from course_merger.crawl.subtitles import Cue


@dataclass(frozen=True, slots=True)
class Chunk:
    idx: int
    start_sec: float
    end_sec: float
    text: str


# 1 word ≈ 1.3 tokens for English (rough; languages with subword splits differ).
_WORD_TO_TOKEN_RATIO = 1.3


def _approx_tokens(text: str) -> int:
    return int(len(text.split()) * _WORD_TO_TOKEN_RATIO)


class Chunker:
    """Group consecutive cues until ~target_tokens accumulated, then emit a chunk."""

    def __init__(self, target_tokens: int = 500) -> None:
        if target_tokens < 50:
            raise ValueError("target_tokens too small; minimum is 50")
        self.target_tokens = target_tokens

    def chunk(self, cues: list[Cue]) -> list[Chunk]:
        if not cues:
            return []

        out: list[Chunk] = []
        buf_texts: list[str] = []
        buf_start = cues[0].start_sec
        buf_end = cues[0].end_sec
        buf_tokens = 0
        idx = 0

        for cue in cues:
            cue_tokens = _approx_tokens(cue.text)
            if buf_tokens and buf_tokens + cue_tokens > self.target_tokens:
                out.append(
                    Chunk(idx=idx, start_sec=buf_start, end_sec=buf_end, text=" ".join(buf_texts))
                )
                idx += 1
                buf_texts = []
                buf_start = cue.start_sec
                buf_tokens = 0
            buf_texts.append(cue.text)
            buf_end = cue.end_sec
            buf_tokens += cue_tokens

        if buf_texts:
            out.append(
                Chunk(idx=idx, start_sec=buf_start, end_sec=buf_end, text=" ".join(buf_texts))
            )

        return out


class Crawler(Protocol):
    """Per-platform adapter.

    Implementations are NOT required to inherit from this — duck typing is fine,
    Protocol exists for static type checks.
    """

    platform: str  # "youtube" | "bilibili"

    def list_playlist(self, url: str) -> list[dict]:
        """Return a list of {idx, title, video_url} for each entry."""
        ...

    def download_subtitle_vtt(
        self, video_url: str, lang_priority: list[str], cookies_from: str | None
    ) -> str | None:
        """Return the raw VTT text, or None if no subs are available."""
        ...
