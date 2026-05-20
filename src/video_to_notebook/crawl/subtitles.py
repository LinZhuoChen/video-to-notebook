"""Parse WebVTT subtitles into time-stamped cues."""
from __future__ import annotations

import html
import re
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Cue:
    start_sec: float
    end_sec: float
    text: str


# WebVTT timestamps come in two shapes:
#   MM:SS.mmm           (hours omitted when total duration < 1h — the
#                        WebVTT spec allows this; yt-dlp's SRT→VTT
#                        converter produces this shape for short clips,
#                        including Bilibili's ai-zh auto-captions on
#                        ~10-30 min videos).
#   HH:MM:SS.mmm        (hours always present — YouTube's auto-captions
#                        use this regardless of duration).
# The regex must accept both. The hours group is optional with a
# non-capturing wrapper so the parser can default the hour component
# to "0" when it's missing.
_HMS_RE = r"(?:(\d{2,}):)?(\d{2}):(\d{2})\.(\d{3})"
_TIMESTAMP_RE = re.compile(rf"{_HMS_RE}\s*-->\s*{_HMS_RE}")
_TAG_RE = re.compile(r"<[^>]+>")
_INNER_TIMESTAMP_RE = re.compile(r"<(?:\d{2,}:)?\d{2}:\d{2}\.\d{3}>")


def _hms_to_sec(h: str | None, m: str, s: str, ms: str) -> float:
    return (int(h) if h else 0) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse_vtt(text: str) -> list[Cue]:
    """Parse a WebVTT-format subtitle string.

    Dedupes globally: any cue whose text exactly matches an earlier cue's
    text is dropped. This handles yt-dlp's repeated-line auto-caption
    quirk well; rare cost is that legitimately repeated phrases get
    consolidated into one cue.
    """
    lines = text.splitlines()
    cues: list[Cue] = []
    i = 0
    seen_texts: set[str] = set()

    while i < len(lines):
        line = lines[i].strip()
        ts = _TIMESTAMP_RE.match(line)
        if not ts:
            i += 1
            continue

        start = _hms_to_sec(ts.group(1), ts.group(2), ts.group(3), ts.group(4))
        end = _hms_to_sec(ts.group(5), ts.group(6), ts.group(7), ts.group(8))

        # Collect text lines until blank or next timestamp.
        i += 1
        text_buf: list[str] = []
        while i < len(lines):
            t = lines[i]
            if not t.strip():
                break
            if _TIMESTAMP_RE.match(t.strip()):
                break
            text_buf.append(t)
            i += 1

        raw = "\n".join(text_buf)
        # Strip inline timestamps like <00:00:07.200>, then strip tags.
        raw = _INNER_TIMESTAMP_RE.sub("", raw)
        raw = _TAG_RE.sub("", raw)
        cleaned = html.unescape(raw).strip()
        if not cleaned:
            continue
        if cleaned in seen_texts:
            continue
        seen_texts.add(cleaned)
        cues.append(Cue(start_sec=start, end_sec=end, text=cleaned))

    return cues
