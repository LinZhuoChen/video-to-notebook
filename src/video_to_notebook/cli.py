"""Typer-based CLI entrypoint."""
from __future__ import annotations

import importlib.metadata
import shutil
import sys
from enum import StrEnum
from pathlib import Path
from urllib.parse import urlparse

import anthropic
import typer

from video_to_notebook.build.runner import run_build
from video_to_notebook.cluster.embedding import Embedder
from video_to_notebook.cluster.llm_review import Reviewer
from video_to_notebook.cluster.prompt_io import (
    apply_cluster_results,
    collect_cluster_prompts,
)
from video_to_notebook.cluster.runner import run_cluster
from video_to_notebook.config import (
    CONFIG_FILENAME,
    PROJECT_MARKER,
    ProjectNotInitializedError,
    find_project_root,
)
from video_to_notebook.crawl.bilibili import BilibiliCrawler
from video_to_notebook.crawl.exceptions import BilibiliCookieError, PlaylistFetchError
from video_to_notebook.crawl.runner import CrawlReport, _CrawlerLike, run_crawl
from video_to_notebook.crawl.youtube import YouTubeCrawler
from video_to_notebook.curriculum.prompt_io import (
    apply_curriculum_results,
    collect_curriculum_prompts,
)
from video_to_notebook.db.session import init_db
from video_to_notebook.explain.prompt_io import (
    apply_explain_results,
    collect_explain_prompts,
)
from video_to_notebook.inflow import (
    cluster_paths,
    curriculum_paths,
    emit_hint,
    explain_paths,
    read_decisions,
    synthesize_paths,
    tag_paths,
    warn_print_prompts_deprecated,
    write_envelope,
)
from video_to_notebook.synthesize.prompt_io import (
    apply_synthesize_results,
    collect_synthesize_prompts,
)
from video_to_notebook.tag.claude_tagger import ClaudeTagger
from video_to_notebook.tag.ontology import load_ontology
from video_to_notebook.tag.prompt_io import apply_tag_results, collect_tag_prompts
from video_to_notebook.tag.runner import run_tag

app = typer.Typer(
    help="Crawl and merge open-courseware into an interactive concept-anchored site.",
    no_args_is_help=True,
    add_completion=False,
)


def course_merger_shim() -> None:
    """v1.x back-compat entry point — forwards to `video-to-notebook`.

    Prints a one-line deprecation notice to stderr, then dispatches to the
    real Typer app so existing scripts that call `course-merger ...` keep
    working. Scheduled for removal in v3.0.0.
    """
    print(
        "warning: `course-merger` is deprecated and will be removed in v3.0.0; "
        "use `video-to-notebook` instead.",
        file=sys.stderr,
    )
    app()


DEFAULT_CONFIG_TOML = """\
# video-to-notebook project config

# tagger_model = "claude-haiku-4-5"
# cluster_review_model = "claude-sonnet-4-6"
"""


def _reject_mutually_exclusive(**flags: bool) -> None:
    """Exit 1 if two or more of the given boolean flags are set.

    Keys must be the public flag spellings (e.g. ``apply``, ``use_api``);
    the error message prints them with leading ``--`` and underscores
    replaced by hyphens.
    """
    active = [name for name, is_set in flags.items() if is_set]
    if len(active) >= 2:
        rendered = ", ".join(f"--{n.replace('_', '-')}" for n in active)
        typer.echo(f"error: mutually exclusive flags: {rendered}", err=True)
        raise typer.Exit(code=1)


def _load_project_state_dir() -> Path:
    """Resolve the active project's state dir (``<root>/.video-to-notebook``)."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1) from e
    return root / PROJECT_MARKER


@app.command("init")
def init_cmd(
    force: bool = typer.Option(
        False, "--force", help="Wipe existing state and reinitialize."
    ),
    language: str = typer.Option(
        "zh", "--language",
        help="Output language for generated chapters / concept pages / site UI. "
             "Choices: 'zh' (中文), 'en' (English). Default: zh.",
    ),
) -> None:
    """Initialize a video-to-notebook project in the current directory."""
    if language not in ("zh", "en"):
        typer.echo(f"error: --language must be 'zh' or 'en', got {language!r}")
        raise typer.Exit(code=1)

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
    db_path = state_dir / "db.sqlite"
    init_db(db_path)

    # Persist language choice in build_meta (single source of truth).
    from video_to_notebook.db.session import connect
    with connect(db_path) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO build_meta (key, value) VALUES (?, ?)",
            ("language", language),
        )

    (state_dir / CONFIG_FILENAME).write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")

    typer.echo(f"initialized video-to-notebook project at {cwd} (language: {language})")


@app.command("version")
def version_cmd() -> None:
    """Show the installed video-to-notebook version."""
    try:
        ver = importlib.metadata.version("video-to-notebook")
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


class CookieBrowser(StrEnum):
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
        help="Browser to extract cookies from (one of edge/chrome/firefox/safari/brave/opera). "
             "On macOS, Chrome v10-encrypted cookies need Keychain access; if --cookies-from-browser "
             "chrome silently fails, fall back to --cookies-file.",
    ),
    cookies_file: Path | None = typer.Option(
        None,
        "--cookies-file",
        help="Path to a Netscape-format cookies.txt (export from a browser extension like "
             "'Get cookies.txt LOCALLY'). Most portable cookie source — works around macOS "
             "Keychain restrictions and bilibili anti-scraping that breaks --cookies-from-browser. "
             "Wins over --cookies-from when both are passed.",
        exists=True,
        dir_okay=False,
    ),
    whisper: bool = typer.Option(
        False,
        "--whisper/--no-whisper",
        help="Fall back to Whisper transcription when a video has no published "
             "subtitles. Needs `pip install video-to-notebook[whisper]`.",
    ),
    whisper_backend: str | None = typer.Option(
        None,
        "--whisper-backend",
        help="Force a Whisper backend ('mlx-whisper' or 'faster-whisper'). "
             "Default: mlx-whisper on macOS, faster-whisper elsewhere.",
    ),
    whisper_model: str | None = typer.Option(
        None,
        "--whisper-model",
        help="Whisper model id. mlx default: 'mlx-community/whisper-large-v3-turbo' "
             "(~800MB, ~2× real-time, simplified-zh + punctuation). "
             "faster-whisper default: 'small'. For absolute best accuracy try "
             "'mlx-community/whisper-large-v3-mlx' on mlx or 'large-v3' on faster-whisper.",
    ),
    whisper_lang: str | None = typer.Option(
        None,
        "--whisper-lang",
        help="ISO-639 language code hint for Whisper (e.g. 'en', 'zh'). "
             "Default: auto-detect.",
    ),
) -> None:
    """Crawl a course (single video or playlist) into the local DB."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1) from e

    platform = _detect_platform(url)
    crawler: _CrawlerLike
    if platform == "bilibili":
        crawler = BilibiliCrawler()
        default_lang = ["ai-zh", "ai-en"]
    else:
        crawler = YouTubeCrawler()
        default_lang = ["en"]

    course_slug = name or _slug_from_url(url)

    transcriber = None
    if whisper:
        from video_to_notebook.crawl.transcribe import build_transcriber
        try:
            transcriber = build_transcriber(
                backend=whisper_backend,
                model=whisper_model,
                language=whisper_lang,
            )
        except (ValueError, ImportError) as e:
            typer.echo(f"--whisper setup failed: {e}")
            raise typer.Exit(code=5) from e
        typer.echo(f"whisper fallback enabled: backend={transcriber.backend} model={transcriber.model}")

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
            cookies_file=cookies_file,
            transcriber=transcriber,
        )
    except BilibiliCookieError as e:
        typer.echo(f"bilibili cookies missing: {e}")
        raise typer.Exit(code=2) from e
    except PlaylistFetchError as e:
        typer.echo(f"playlist fetch failed: {e}")
        raise typer.Exit(code=4) from e

    whisper_note = f", {report.lectures_whisper} via whisper" if report.lectures_whisper else ""
    typer.echo(
        f"done: {report.lectures_ok} ok{whisper_note}, "
        f"{report.lectures_no_subs} no-subs, {report.lectures_error} errors "
        f"(course: {report.course_slug})"
    )
    if report.lectures_error:
        raise typer.Exit(code=3)


@app.command("tag")
def tag_cmd(
    ontology: Path = typer.Option(
        ..., "--ontology", help="Path to ontology YAML.", exists=True, dir_okay=False
    ),
    model: str = typer.Option(
        "claude-haiku-4-5", "--model", help="Claude model id (--use-api only)."
    ),
    course: str | None = typer.Option(
        None, "--course", help="Only tag chunks of this course slug."
    ),
    limit: int | None = typer.Option(
        None, "--limit", help="Max chunks to process this run."
    ),
    apply: bool = typer.Option(
        False, "--apply",
        help="Read decisions from the default path and write tags to DB.",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Read decisions JSON from an explicit path and write to DB.",
    ),
    use_api: bool = typer.Option(
        False, "--use-api",
        help="Opt in to the Anthropic-SDK path (requires ANTHROPIC_API_KEY).",
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="DEPRECATED — printing prompts is now the default. Will be removed.",
    ),
) -> None:
    """Assign concept tags to chunks.

    Default mode writes an in-session prompt envelope to
    ``<state_dir>/prompts/tag.json`` and exits, expecting an agent to write
    decisions to the sibling ``.decisions.json`` and re-invoke with --apply.
    Pass --use-api to call Claude Haiku directly instead.
    """
    _reject_mutually_exclusive(
        apply=apply,
        apply_results=apply_results is not None,
        use_api=use_api,
    )
    if print_prompts:
        if apply or apply_results is not None or use_api:
            typer.echo(
                "error: --print-prompts cannot be combined with --apply / "
                "--apply-results / --use-api",
                err=True,
            )
            raise typer.Exit(code=1)
        warn_print_prompts_deprecated()

    state_dir = _load_project_state_dir()
    onto = load_ontology(ontology)
    db_path = state_dir / "db.sqlite"

    if use_api:
        client = anthropic.Anthropic()
        tagger = ClaudeTagger(client=client, model=model, ontology=onto)
        report = run_tag(
            db_path=db_path, tagger=tagger, ontology=onto,
            course_slug=course, limit=limit,
        )
        typer.echo(
            f"done: {report.chunks_tagged} chunks tagged, "
            f"{report.tags_known_written} known tags, "
            f"{report.tags_proposed_written} proposed tags, "
            f"{report.parse_failures} parse failures"
        )
        return

    prompts_path, decisions_path = tag_paths(state_dir)

    if apply or apply_results is not None:
        src = apply_results if apply_results is not None else decisions_path
        try:
            results = read_decisions(src)
        except FileNotFoundError as e:
            typer.echo(f"error: {e}", err=True)
            raise typer.Exit(code=1) from e
        report = apply_tag_results(db_path=db_path, ontology=onto, results=results)
        typer.echo(
            f"done (in-session): {report.chunks_tagged} chunks tagged, "
            f"{report.tags_known_written} known tags, "
            f"{report.tags_proposed_written} proposed tags"
        )
        return

    envelope = collect_tag_prompts(
        db_path=db_path, ontology=onto, course_slug=course, limit=limit,
    )
    write_envelope(prompts_path, envelope)
    emit_hint(
        prompts_path=prompts_path,
        decisions_path=decisions_path,
        size_summary=f"{len(envelope['chunks'])} chunks",
        next_command=f"video-to-notebook tag --ontology {ontology} --apply",
    )


@app.command("cluster")
def cluster_cmd(
    ontology: Path = typer.Option(
        ..., "--ontology", help="Path to ontology YAML.", exists=True, dir_okay=False
    ),
    review_model: str = typer.Option(
        "claude-sonnet-4-6", "--review-model",
        help="Claude model for review (--use-api only).",
    ),
    threshold: float = typer.Option(
        0.75, "--threshold", help="Cosine similarity threshold for merging proposed tags."
    ),
    apply: bool = typer.Option(
        False, "--apply",
        help="Read decisions from the default path and write cluster results to DB.",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Read decisions JSON from an explicit path. The file must contain both "
        "`_prompts_envelope` and `decisions_envelope` (or top-level decisions).",
    ),
    use_api: bool = typer.Option(
        False, "--use-api",
        help="Opt in to the Anthropic-SDK path (requires ANTHROPIC_API_KEY).",
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="DEPRECATED — printing prompts is now the default. Will be removed.",
    ),
) -> None:
    """Review near-duplicate proposed tags and decide merge / create / reject.

    Default mode writes an in-session prompt envelope to
    ``<state_dir>/prompts/cluster.json`` and exits. Pass --use-api to call
    Claude Sonnet directly instead.
    """
    _reject_mutually_exclusive(
        apply=apply,
        apply_results=apply_results is not None,
        use_api=use_api,
    )
    if print_prompts:
        if apply or apply_results is not None or use_api:
            typer.echo(
                "error: --print-prompts cannot be combined with --apply / "
                "--apply-results / --use-api",
                err=True,
            )
            raise typer.Exit(code=1)
        warn_print_prompts_deprecated()

    state_dir = _load_project_state_dir()
    onto = load_ontology(ontology)
    db_path = state_dir / "db.sqlite"
    embedder = Embedder()

    if use_api:
        client = anthropic.Anthropic()
        reviewer = Reviewer(client=client, model=review_model, ontology=onto)
        report = run_cluster(
            db_path=db_path, embedder=embedder, reviewer=reviewer, threshold=threshold,
        )
        typer.echo(
            f"done: {report.clusters_reviewed} clusters reviewed | "
            f"{report.merged} merged, {report.created} created, "
            f"{report.rejected} rejected, {report.ambiguous} ambiguous"
        )
        return

    prompts_path, decisions_path = cluster_paths(state_dir)

    if apply or apply_results is not None:
        src = apply_results if apply_results is not None else decisions_path
        try:
            payload = read_decisions(src)
        except FileNotFoundError as e:
            typer.echo(f"error: {e}", err=True)
            raise typer.Exit(code=1) from e
        prompts = payload.get("_prompts_envelope") or payload.get("prompts")
        decisions = payload.get("decisions_envelope") or payload.get("decisions") or payload
        if prompts is None or "clusters" not in prompts:
            typer.echo(
                "error: decisions JSON must include the original prompts envelope "
                "(under `_prompts_envelope`) and the decisions (under "
                "`decisions_envelope`).",
                err=True,
            )
            raise typer.Exit(code=1)
        report = apply_cluster_results(
            db_path=db_path, ontology=onto, prompts=prompts, decisions=decisions,
        )
        typer.echo(
            f"done (in-session): {report.clusters_reviewed} clusters reviewed | "
            f"{report.merged} merged, {report.created} created, "
            f"{report.rejected} rejected, {report.ambiguous} ambiguous"
        )
        return

    envelope = collect_cluster_prompts(
        db_path=db_path, ontology=onto, embedder=embedder, threshold=threshold,
    )
    write_envelope(prompts_path, envelope)
    emit_hint(
        prompts_path=prompts_path,
        decisions_path=decisions_path,
        size_summary=f"{len(envelope['clusters'])} clusters",
        next_command=f"video-to-notebook cluster --ontology {ontology} --apply",
    )


@app.command("build")
def build_cmd(
    no_npm: bool = typer.Option(
        False, "--no-npm", help="Only write Markdown content; skip running astro build."
    ),
    incremental: bool = typer.Option(
        False, "--incremental",
        help="Only re-render concepts marked dirty by the most recent cluster run.",
    ),
) -> None:
    """Generate the static site under <project>/site/dist/."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1) from e

    db_path = root / PROJECT_MARKER / "db.sqlite"
    report = run_build(
        project_root=root, db_path=db_path,
        npm_build=not no_npm, incremental=incremental,
    )

    typer.echo(
        f"done: {report.courses_written} courses, "
        f"{report.lectures_written} lectures, "
        f"{report.concepts_written} concepts"
        + (f", astro exit {report.npm_exit_code}" if report.npm_exit_code is not None else "")
    )
    if report.npm_exit_code not in (None, 0):
        raise typer.Exit(code=5)


@app.command("serve")
def serve_cmd() -> None:
    """Run `astro dev` on the project's site directory."""
    import subprocess
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1) from e

    from video_to_notebook.build.template_copy import ensure_site_dir
    site_dir = ensure_site_dir(root)

    if not (site_dir / "node_modules").is_dir():
        typer.echo("running: npm install")
        subprocess.run(["npm", "install", "--silent"], cwd=site_dir, check=False)

    typer.echo(f"running: npm run dev (in {site_dir})")
    subprocess.run(["npm", "run", "dev"], cwd=site_dir, check=False)


@app.command("curriculum")
def curriculum_cmd(
    apply: bool = typer.Option(
        False, "--apply",
        help="Read decisions from the default path and write chapters to DB.",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Read decisions JSON from an explicit path and write to DB.",
    ),
    samples_per_concept: int = typer.Option(
        5, "--samples", help="Sample chunks per concept in the prompts envelope.",
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="DEPRECATED — printing prompts is now the default. Will be removed.",
    ),
) -> None:
    """Design the chapter sequence for the merged textbook.

    Default mode writes an in-session prompt envelope to
    ``<state_dir>/prompts/curriculum.json`` and exits, expecting an agent to
    write decisions to the sibling ``.decisions.json`` and re-invoke with
    --apply. There is no API path for this command.
    """
    _reject_mutually_exclusive(
        apply=apply,
        apply_results=apply_results is not None,
    )
    if print_prompts:
        if apply or apply_results is not None:
            typer.echo(
                "error: --print-prompts cannot be combined with --apply / "
                "--apply-results",
                err=True,
            )
            raise typer.Exit(code=1)
        warn_print_prompts_deprecated()

    state_dir = _load_project_state_dir()
    db_path = state_dir / "db.sqlite"
    prompts_path, decisions_path = curriculum_paths(state_dir)

    if apply or apply_results is not None:
        src = apply_results if apply_results is not None else decisions_path
        try:
            results = read_decisions(src)
        except FileNotFoundError as e:
            typer.echo(f"error: {e}", err=True)
            raise typer.Exit(code=1) from e
        n = apply_curriculum_results(db_path=db_path, results=results)
        typer.echo(f"done: wrote {n} chapters to curriculum_chapters")
        return

    envelope = collect_curriculum_prompts(
        db_path=db_path, samples_per_concept=samples_per_concept,
    )
    write_envelope(prompts_path, envelope)
    emit_hint(
        prompts_path=prompts_path,
        decisions_path=decisions_path,
        size_summary=f"{len(envelope['concepts'])} concepts",
        next_command="video-to-notebook curriculum --apply",
    )


@app.command("synthesize")
def synthesize_cmd(
    chapter: int = typer.Option(
        ..., "--chapter", help="The order_idx of the chapter to synthesize.",
    ),
    apply: bool = typer.Option(
        False, "--apply",
        help="Read decisions from the default path and copy the HTML fragment into state.",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Read decisions JSON from an explicit path.",
    ),
    max_source_chunks: int = typer.Option(
        20, "--max-chunks", help="Cap source chunks per chapter to control context size.",
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="DEPRECATED — printing prompts is now the default. Will be removed.",
    ),
) -> None:
    """Generate the HTML for one textbook chapter (in-session only).

    Default mode writes an in-session prompt envelope to
    ``<state_dir>/prompts/synthesize/chapter-N.json`` and exits. There is no
    API path for this command.
    """
    _reject_mutually_exclusive(
        apply=apply,
        apply_results=apply_results is not None,
    )
    if print_prompts:
        if apply or apply_results is not None:
            typer.echo(
                "error: --print-prompts cannot be combined with --apply / "
                "--apply-results",
                err=True,
            )
            raise typer.Exit(code=1)
        warn_print_prompts_deprecated()

    state_dir = _load_project_state_dir()
    db_path = state_dir / "db.sqlite"
    prompts_path, decisions_path = synthesize_paths(state_dir, chapter)

    if apply or apply_results is not None:
        src = apply_results if apply_results is not None else decisions_path
        try:
            results = read_decisions(src)
        except FileNotFoundError as e:
            typer.echo(f"error: {e}", err=True)
            raise typer.Exit(code=1) from e
        apply_synthesize_results(db_path=db_path, state_dir=state_dir, results=results)
        typer.echo(
            f"done: synthesized chapter {results['chapter_order_idx']} → "
            f"{state_dir / 'textbook' / (str(results['chapter_order_idx']) + '.html')}"
        )
        return

    envelope = collect_synthesize_prompts(
        db_path=db_path, chapter_order_idx=chapter,
        max_source_chunks=max_source_chunks,
    )
    write_envelope(prompts_path, envelope)
    emit_hint(
        prompts_path=prompts_path,
        decisions_path=decisions_path,
        size_summary=(
            f"chapter {chapter} '{envelope['chapter']['title']}', "
            f"{len(envelope['source_chunks'])} source chunks"
        ),
        next_command=f"video-to-notebook synthesize --chapter {chapter} --apply",
    )


@app.command("explain")
def explain_cmd(
    concept: str = typer.Option(
        ..., "--concept", help="The concept slug to explain (e.g. 'gradient-descent').",
    ),
    apply: bool = typer.Option(
        False, "--apply",
        help="Read decisions from the default path and copy the HTML fragment into state.",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Read decisions JSON from an explicit path.",
    ),
    max_source_chunks: int = typer.Option(
        12, "--max-chunks", help="Cap source chunks for the concept envelope.",
    ),
    max_related: int = typer.Option(
        6, "--max-related", help="Cap related concepts surfaced in the envelope.",
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="DEPRECATED — printing prompts is now the default. Will be removed.",
    ),
) -> None:
    """Generate a rich illustrated explanation for ONE concept (in-session only).

    Default mode writes an in-session prompt envelope to
    ``<state_dir>/prompts/explain/<SLUG>.json`` and exits. There is no API
    path for this command.
    """
    _reject_mutually_exclusive(
        apply=apply,
        apply_results=apply_results is not None,
    )
    if print_prompts:
        if apply or apply_results is not None:
            typer.echo(
                "error: --print-prompts cannot be combined with --apply / "
                "--apply-results",
                err=True,
            )
            raise typer.Exit(code=1)
        warn_print_prompts_deprecated()

    state_dir = _load_project_state_dir()
    db_path = state_dir / "db.sqlite"
    prompts_path, decisions_path = explain_paths(state_dir, concept)

    if apply or apply_results is not None:
        src = apply_results if apply_results is not None else decisions_path
        try:
            results = read_decisions(src)
        except FileNotFoundError as e:
            typer.echo(f"error: {e}", err=True)
            raise typer.Exit(code=1) from e
        dst = apply_explain_results(db_path=db_path, state_dir=state_dir, results=results)
        typer.echo(
            f"done: explained concept '{results['concept_slug']}' → "
            f"{state_dir / 'concepts' / dst}"
        )
        return

    envelope = collect_explain_prompts(
        db_path=db_path, concept_slug=concept,
        max_source_chunks=max_source_chunks, max_related=max_related,
    )
    write_envelope(prompts_path, envelope)
    emit_hint(
        prompts_path=prompts_path,
        decisions_path=decisions_path,
        size_summary=(
            f"concept '{concept}', {len(envelope['occurrences'])} occurrences"
        ),
        next_command=f"video-to-notebook explain --concept {concept} --apply",
    )
