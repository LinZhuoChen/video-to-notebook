"""Bilibili adapter: yt-dlp with cookies (required) and ?p=N playlist pagination."""
from __future__ import annotations

import re
import subprocess
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from course_merger.crawl.exceptions import BilibiliCookieError, PlaylistFetchError

__all__ = ["BilibiliCookieError", "BilibiliCrawler", "PlaylistFetchError"]

_P_PARAM_RE = re.compile(r"\?p=\d+")


def _ep_url(base_url: str, idx: int) -> str:
    """Inject ?p=N into a Bilibili base URL, replacing any existing ?p=."""
    if _P_PARAM_RE.search(base_url):
        return _P_PARAM_RE.sub(f"?p={idx}", base_url)
    sep = "&" if "?" in base_url else "?"
    return f"{base_url}{sep}p={idx}"


class BilibiliCrawler:
    platform = "bilibili"

    def __init__(self, _work_dir: Path | None = None) -> None:
        self._work_dir = _work_dir

    def list_playlist(self, url: str) -> list[dict]:
        cmd = [
            "yt-dlp",
            "--flat-playlist",
            "--no-download",
            "--print",
            "%(playlist_index)s|%(id)s|%(title)s",
            url,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=120)
        if result.returncode != 0:
            last_err = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "no error message"
            raise PlaylistFetchError(
                f"yt-dlp failed for {url} (exit {result.returncode}): {last_err}"
            )
        entries: list[dict] = []
        for line in result.stdout.strip().splitlines():
            parts = line.split("|", 2)
            if len(parts) != 3:
                continue
            raw_idx, video_id, title = parts
            try:
                idx = int(raw_idx)
            except ValueError:
                idx = 1
            entries.append(
                {
                    "idx": idx,
                    "video_id": video_id.strip(),
                    "title": title.strip(),
                    "video_url": _ep_url(url, idx),
                }
            )
        return entries

    def download_subtitle_vtt(
        self,
        video_url: str,
        lang_priority: list[str],
        cookies_from: str | None,
    ) -> str | None:
        if not cookies_from:
            raise BilibiliCookieError(
                "Bilibili requires a logged-in browser. Pass --cookies-from edge|chrome|firefox."
            )

        for lang in lang_priority:
            with self._workspace() as work:
                prefix = work / "sub"
                cmd = [
                    "yt-dlp",
                    "--cookies-from-browser", cookies_from,
                    "--write-subs",
                    "--skip-download",
                    "--sub-format", "vtt",
                    "--sub-lang", lang,
                    "--no-playlist",
                    "-o", str(prefix),
                    video_url,
                ]
                result = subprocess.run(
                    cmd, capture_output=True, text=True, check=False, timeout=120
                )
                if "403" in result.stderr or "401" in result.stderr:
                    raise BilibiliCookieError(
                        f"Bilibili rejected cookies from `{cookies_from}`. "
                        "Log in to bilibili.com in that browser and retry."
                    )
                for candidate in work.glob("sub*.vtt"):
                    return candidate.read_text(encoding="utf-8")
        return None

    @contextmanager
    def _workspace(self) -> Iterator[Path]:
        if self._work_dir is not None:
            yield self._work_dir
        else:
            with tempfile.TemporaryDirectory() as td:
                yield Path(td)
