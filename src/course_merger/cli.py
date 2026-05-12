"""Typer-based CLI entrypoint."""
from __future__ import annotations

import importlib.metadata
import shutil
from enum import Enum
from pathlib import Path
from urllib.parse import urlparse

import typer

from course_merger.config import CONFIG_FILENAME, PROJECT_MARKER, ProjectNotInitializedError, find_project_root
from course_merger.crawl.bilibili import BilibiliCookieError, BilibiliCrawler
from course_merger.crawl.runner import CrawlReport, _CrawlerLike, run_crawl
from course_merger.crawl.youtube import YouTubeCrawler
from course_merger.db.session import init_db

app = typer.Typer(
    help="Crawl and merge open-courseware into an interactive concept-anchored site.",
    no_args_is_help=True,
    add_completion=False,
)


DEFAULT_CONFIG_TOML = """\
# course-merger project config

# tagger_model = "claude-haiku-4-5"
# cluster_review_model = "claude-sonnet-4-6"
"""


@app.command("init")
def init_cmd(
    force: bool = typer.Option(
        False, "--force", help="Wipe existing state and reinitialize."
    ),
) -> None:
    """Initialize a course-merger project in the current directory."""
    cwd = Path.cwd()
    state_dir = cwd / PROJECT_MARKER

    if state_dir.exists():
        if not force:
            typer.echo(
                f"error: {PROJECT_MARKER}/ already initialized at {cwd}. "
                "Use --force to overwrite."
            )
            raise typer.Exit(code=1)
        shutil.rmtree(state_dir)

    state_dir.mkdir(parents=True)
    init_db(state_dir / "db.sqlite")
    (state_dir / CONFIG_FILENAME).write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")

    typer.echo(f"initialized course-merger project at {cwd}")


@app.command("version")
def version_cmd() -> None:
    """Show the installed course-merger version."""
    try:
        ver = importlib.metadata.version("course-merger")
    except importlib.metadata.PackageNotFoundError:
        ver = "unknown"
    typer.echo(ver)


def _detect_platform(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    if "bilibili.com" in host or "b23.tv" in host:
        return "bilibili"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    raise typer.BadParameter(f"Unrecognized platform for URL: {url}")


class CookieBrowser(str, Enum):
    edge = "edge"
    chrome = "chrome"
    firefox = "firefox"
    safari = "safari"
    brave = "brave"
    opera = "opera"


def _slug_from_url(url: str) -> str:
    """Derive a short, meaningful slug from a video URL.

    Prefers the playlist ID (?list=) or video ID (?v=, /video/BVxxx),
    falls back to a hash of the URL.
    """
    import hashlib
    import re
    from urllib.parse import parse_qs, urlparse

    parsed = urlparse(url)
    qs = parse_qs(parsed.query)

    # Prefer playlist id
    if "list" in qs:
        return _normalize_slug(qs["list"][0])
    # Then YouTube ?v=
    if "v" in qs:
        return _normalize_slug(qs["v"][0])
    # Then Bilibili /video/BVxxx/ path
    m = re.search(r"/video/([A-Za-z0-9_-]+)", parsed.path)
    if m:
        return _normalize_slug(m.group(1))
    # Fallback: short hash
    return "course-" + hashlib.sha1(url.encode()).hexdigest()[:8]


def _normalize_slug(text: str) -> str:
    """Lowercase, replace non-alphanumeric with single hyphens, strip ends."""
    import re
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    return s.strip("-") or "course"


@app.command("crawl")
def crawl_cmd(
    url: str = typer.Argument(..., help="Video or playlist URL"),
    name: str | None = typer.Option(
        None, "--name", help="Course slug (defaults to a slug derived from the URL)."
    ),
    lang: list[str] | None = typer.Option(
        None,
        "--lang",
        help="Subtitle language priority list. "
        "Defaults: YouTube=[en], Bilibili=[ai-zh, ai-en].",
    ),
    cookies_from: CookieBrowser | None = typer.Option(
        None,
        "--cookies-from",
        help="Browser to extract cookies from (required for Bilibili).",
    ),
) -> None:
    """Crawl a course (single video or playlist) into the local DB."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1)

    platform = _detect_platform(url)
    crawler: _CrawlerLike
    if platform == "bilibili":
        crawler = BilibiliCrawler()
        default_lang = ["ai-zh", "ai-en"]
    else:
        crawler = YouTubeCrawler()
        default_lang = ["en"]

    course_slug = name or _slug_from_url(url)

    db_path = root / PROJECT_MARKER / "db.sqlite"
    try:
        report: CrawlReport = run_crawl(
            db_path=db_path,
            crawler=crawler,
            url=url,
            course_slug=course_slug,
            course_title=name or course_slug,
            lang_priority=lang or default_lang,
            cookies_from=cookies_from.value if cookies_from else None,
        )
    except BilibiliCookieError as e:
        typer.echo(f"bilibili cookies missing: {e}")
        raise typer.Exit(code=2)

    typer.echo(
        f"done: {report.lectures_ok} ok, "
        f"{report.lectures_no_subs} no-subs, {report.lectures_error} errors "
        f"(course: {report.course_slug})"
    )
    if report.lectures_error:
        raise typer.Exit(code=3)
