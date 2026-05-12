"""Orchestrator: crawler → subtitles → chunker → DB."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol

from course_merger.crawl.base import Chunker
from course_merger.crawl.bilibili import BilibiliCookieError
from course_merger.crawl.subtitles import parse_vtt
from course_merger.db.session import connect


class _CrawlerLike(Protocol):
    platform: str

    def list_playlist(self, url: str) -> list[dict]: ...

    def download_subtitle_vtt(
        self, video_url: str, lang_priority: list[str], cookies_from: str | None
    ) -> str | None: ...


@dataclass(frozen=True, slots=True)
class CrawlReport:
    course_slug: str
    lectures_ok: int
    lectures_no_subs: int
    lectures_error: int

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
    target_tokens: int = 500,
) -> CrawlReport:
    """Crawl a course and persist into the DB. Idempotent on (course_slug, lecture.idx)."""

    now = datetime.now(timezone.utc).isoformat()
    entries = crawler.list_playlist(url)
    chunker = Chunker(target_tokens=target_tokens)

    ok = 0
    no_subs = 0
    error = 0

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
                    entry["video_url"], lang_priority, cookies_from
                )
            except BilibiliCookieError:
                raise
            except Exception:
                conn.execute(
                    "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
                    "VALUES (?, ?, ?, ?, NULL, 'error')",
                    (course_id, entry["idx"], entry["title"], entry["video_url"]),
                )
                error += 1
                continue

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

    return CrawlReport(
        course_slug=course_slug,
        lectures_ok=ok,
        lectures_no_subs=no_subs,
        lectures_error=error,
    )
