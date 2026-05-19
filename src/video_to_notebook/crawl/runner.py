"""Orchestrator: crawler → subtitles (or Whisper fallback) → chunker → DB."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol

from video_to_notebook.crawl.base import Chunker
from video_to_notebook.crawl.exceptions import BilibiliCookieError, PlaylistFetchError
from video_to_notebook.crawl.subtitles import parse_vtt
from video_to_notebook.crawl.transcribe import Transcriber, transcribe_video_to_vtt
from video_to_notebook.db.session import connect


class _CrawlerLike(Protocol):
    platform: str

    def list_playlist(
        self,
        url: str,
        cookies_from: str | None = None,
        cookies_file: Path | None = None,
    ) -> list[dict]: ...

    def download_subtitle_vtt(
        self,
        video_url: str,
        lang_priority: list[str],
        cookies_from: str | None,
        cookies_file: Path | None = None,
    ) -> str | None: ...


@dataclass(frozen=True, slots=True)
class CrawlReport:
    course_slug: str
    lectures_ok: int
    lectures_no_subs: int
    lectures_error: int
    lectures_whisper: int = 0  # subset of lectures_ok that came from Whisper

    @property
    def total(self) -> int:
        return self.lectures_ok + self.lectures_no_subs + self.lectures_error


def run_crawl(
    *,
    db_path: Path,
    crawler: _CrawlerLike,
    url: str,
    course_slug: str,
    course_title: str,
    lang_priority: list[str],
    cookies_from: str | None,
    cookies_file: Path | None = None,
    target_tokens: int = 500,
    transcriber: Transcriber | None = None,
) -> CrawlReport:
    """Crawl a course and persist into the DB. Idempotent on (course_slug, lecture.idx).

    If `transcriber` is provided, lectures without published subtitles fall back
    to audio download + Whisper transcription instead of being recorded as
    `no_subs`. The CrawlReport's `lectures_whisper` counter tracks how many.
    """

    now = datetime.now(UTC).isoformat()
    entries = crawler.list_playlist(url, cookies_from=cookies_from, cookies_file=cookies_file)
    chunker = Chunker(target_tokens=target_tokens)

    ok = 0
    no_subs = 0
    error = 0
    whisper_count = 0

    with connect(db_path) as conn:
        course_row = conn.execute(
            "SELECT id FROM courses WHERE slug = ?", (course_slug,)
        ).fetchone()
        if course_row is None:
            cur = conn.execute(
                "INSERT INTO courses (slug, title, platform, source_url, added_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (course_slug, course_title, crawler.platform, url, now),
            )
            course_id = cur.lastrowid
        else:
            course_id = course_row[0]

        for entry in entries:
            existing = conn.execute(
                "SELECT id, status FROM lectures WHERE course_id = ? AND idx = ?",
                (course_id, entry["idx"]),
            ).fetchone()
            if existing is not None:
                _, status = existing
                if status == "ok":
                    ok += 1
                elif status == "no_subs":
                    no_subs += 1
                else:
                    error += 1
                continue

            try:
                vtt = crawler.download_subtitle_vtt(
                    entry["video_url"],
                    lang_priority,
                    cookies_from,
                    cookies_file=cookies_file,
                )
            except BilibiliCookieError:
                raise
            except PlaylistFetchError:
                raise
            except Exception:
                conn.execute(
                    "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
                    "VALUES (?, ?, ?, ?, NULL, 'error')",
                    (course_id, entry["idx"], entry["title"], entry["video_url"]),
                )
                error += 1
                continue

            from_whisper = False
            if vtt is None and transcriber is not None:
                vtt = transcribe_video_to_vtt(
                    video_url=entry["video_url"],
                    cookies_from=cookies_from,
                    cookies_file=cookies_file,
                    transcriber=transcriber,
                )
                from_whisper = vtt is not None

            if vtt is None:
                conn.execute(
                    "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
                    "VALUES (?, ?, ?, ?, NULL, 'no_subs')",
                    (course_id, entry["idx"], entry["title"], entry["video_url"]),
                )
                no_subs += 1
                continue

            cues = parse_vtt(vtt)
            full_transcript = "\n".join(c.text for c in cues)
            cur = conn.execute(
                "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
                "VALUES (?, ?, ?, ?, ?, 'ok')",
                (course_id, entry["idx"], entry["title"], entry["video_url"], full_transcript),
            )
            lecture_id = cur.lastrowid

            for chunk in chunker.chunk(cues):
                conn.execute(
                    "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (lecture_id, chunk.idx, chunk.start_sec, chunk.end_sec, chunk.text),
                )
            ok += 1
            if from_whisper:
                whisper_count += 1

    return CrawlReport(
        course_slug=course_slug,
        lectures_ok=ok,
        lectures_no_subs=no_subs,
        lectures_error=error,
        lectures_whisper=whisper_count,
    )
