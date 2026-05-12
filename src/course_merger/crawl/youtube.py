"""YouTube adapter: shells out to yt-dlp for playlist enumeration and subtitle download."""
from __future__ import annotations

import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


class YouTubeCrawler:
    platform = "youtube"

    def __init__(self, _work_dir: Path | None = None) -> None:
        self._work_dir = _work_dir  # tests inject a tmp dir; production uses tempdir

    # ---- playlist enumeration -------------------------------------------------

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
        entries: list[dict] = []
        for line in result.stdout.strip().splitlines():
            parts = line.split("|", 2)
            if len(parts) != 3:
                continue
            raw_idx, video_id, title = parts
            try:
                idx = int(raw_idx)
            except ValueError:
                # Single video case: playlist_index is "NA"; treat as idx=1.
                idx = 1
            entries.append(
                {
                    "idx": idx,
                    "video_id": video_id.strip(),
                    "title": title.strip(),
                    "video_url": f"https://www.youtube.com/watch?v={video_id.strip()}",
                }
            )
        return entries

    # ---- subtitle download ----------------------------------------------------

    def download_subtitle_vtt(
        self,
        video_url: str,
        lang_priority: list[str],
        cookies_from: str | None,
    ) -> str | None:
        """Try `--write-subs` then `--write-auto-subs`. Return raw VTT or None."""
        for write_flag in ("--write-subs", "--write-auto-subs"):
            for lang in lang_priority:
                with self._workspace() as work:
                    prefix = work / "sub"
                    cmd = ["yt-dlp"]
                    if cookies_from:
                        cmd += ["--cookies-from-browser", cookies_from]
                    cmd += [
                        write_flag,
                        "--skip-download",
                        "--sub-format", "vtt",
                        "--sub-lang", lang,
                        "--no-playlist",
                        "-o", str(prefix),
                        video_url,
                    ]
                    subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=120)
                    for candidate in work.glob("sub*.vtt"):
                        return candidate.read_text(encoding="utf-8")
        return None

    # ---- helpers --------------------------------------------------------------

    @contextmanager
    def _workspace(self) -> Iterator[Path]:
        if self._work_dir is not None:
            yield self._work_dir
        else:
            with tempfile.TemporaryDirectory() as td:
                yield Path(td)
