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


_TIMESTAMP_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})\.(\d{3})"
)
_TAG_RE = re.compile(r"<[^>]+>")
_INNER_TIMESTAMP_RE = re.compile(r"<\d{2}:\d{2}:\d{2}\.\d{3}>")


def _hms_to_sec(h: str, m: str, s: str, ms: str) -> float:
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


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
