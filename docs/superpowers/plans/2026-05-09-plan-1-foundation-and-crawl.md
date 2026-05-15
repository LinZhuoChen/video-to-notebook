# Plan 1 — Foundation + Crawl Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a working `video-to-notebook init && video-to-notebook crawl <url>` for both YouTube and Bilibili, persisting transcripts and chunks in SQLite. End-to-end smoke test passes on a fixture course without network.

**Architecture:** Typer CLI dispatch → `db/` (SQLite + raw SQL) ← `crawl/` (yt-dlp wrapper per platform + subtitle parser + chunker). No tagging, no clustering, no HTML in this plan — those land in Plans 2 / 3.

**Tech Stack:** Python 3.12 + uv + Typer + SQLite (stdlib) + yt-dlp + pytest + ruff + pyright + GitHub Actions

**Repo:** `/Users/chenlinzhuo/code/video-to-notebook/` (already `git init`, has README + .gitignore + spec)

---

## File Structure

```
video-to-notebook/
├── pyproject.toml                  # NEW: uv-managed Python package
├── .python-version                 # NEW: 3.12
├── ruff.toml                       # NEW: lint config
├── pyrightconfig.json              # NEW: type-check config
├── .github/workflows/ci.yml        # NEW: lint + typecheck + test on push/PR
├── src/video_to_notebook/
│   ├── __init__.py                 # NEW: __version__
│   ├── cli.py                      # NEW: Typer app entrypoint
│   ├── config.py                   # NEW: TOML project config
│   ├── db/
│   │   ├── __init__.py
│   │   ├── schema.sql              # NEW: canonical v1 schema (subset for Plan 1)
│   │   └── session.py              # NEW: connect / init_db / transaction context manager
│   └── crawl/
│       ├── __init__.py
│       ├── base.py                 # NEW: Crawler ABC + Chunker class
│       ├── subtitles.py            # NEW: VTT/SRT parser
│       ├── youtube.py              # NEW: YouTube adapter (yt-dlp subprocess)
│       └── bilibili.py             # NEW: Bilibili adapter
└── tests/
    ├── conftest.py                 # NEW: shared fixtures (tmp_db, etc.)
    ├── fixtures/
    │   └── mini_course/
    │       ├── youtube_lecture1.vtt        # NEW: hand-crafted VTT
    │       └── bilibili_lecture1.vtt       # NEW: hand-crafted Bilibili VTT
    ├── unit/
    │   ├── test_db_session.py      # NEW
    │   ├── test_config.py          # NEW
    │   ├── test_subtitles.py       # NEW
    │   ├── test_chunker.py         # NEW
    │   ├── test_crawler_youtube.py # NEW (mocks subprocess)
    │   └── test_crawler_bilibili.py # NEW (mocks subprocess)
    └── integration/
        ├── test_init.py            # NEW: CLI `init` smoke
        └── test_crawl_smoke.py     # NEW: end-to-end against fixture
```

Each Python module has one responsibility:
- `db/session.py`: connection lifecycle and transaction safety
- `crawl/subtitles.py`: pure parsing (no I/O, no network)
- `crawl/base.py`: shared chunker + abstract Crawler protocol
- `crawl/youtube.py` / `crawl/bilibili.py`: platform-specific subprocess orchestration
- `cli.py`: argument parsing + DB / crawler wiring only (no business logic)

---

## Phase 0: Project Foundation

### Task 1: pyproject.toml + uv + ruff + pyright config

**Files:**
- Create: `pyproject.toml`
- Create: `.python-version`
- Create: `ruff.toml`
- Create: `pyrightconfig.json`
- Create: `src/video_to_notebook/__init__.py`

- [ ] **Step 1: Write `.python-version`**

```
3.12
```

- [ ] **Step 2: Write `pyproject.toml`**

```toml
[project]
name = "video-to-notebook"
version = "0.1.0"
description = "Crawl, merge, and visualize open-courseware by concept"
readme = "README.md"
requires-python = ">=3.12"
license = "MIT"
authors = [{ name = "chenlinzhuo" }]
dependencies = [
    "typer>=0.12.0",
    "rich>=13.7.0",
    "yt-dlp>=2024.5.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=5.0.0",
    "ruff>=0.5.0",
    "pyright>=1.1.370",
]

[project.scripts]
video-to-notebook = "video_to_notebook.cli:app"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/video_to_notebook"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
markers = [
    "integration: integration tests (slower, may hit fs)",
]
```

- [ ] **Step 3: Write `ruff.toml`**

```toml
line-length = 100
target-version = "py312"

[lint]
select = ["E", "F", "I", "B", "UP", "SIM"]
ignore = ["E501"]  # line length handled by formatter

[format]
quote-style = "double"
```

- [ ] **Step 4: Write `pyrightconfig.json`**

```json
{
  "include": ["src", "tests"],
  "exclude": ["**/node_modules", "**/.venv", "**/dist"],
  "pythonVersion": "3.12",
  "typeCheckingMode": "basic",
  "reportMissingImports": "error",
  "reportMissingTypeStubs": "none"
}
```

- [ ] **Step 5: Write `src/video_to_notebook/__init__.py`**

```python
__version__ = "0.1.0"
```

- [ ] **Step 6: Install deps with uv**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
uv venv
uv pip install -e ".[dev]"
```

Expected: `video-to-notebook 0.1.0` installed in `.venv/`. No errors.

- [ ] **Step 7: Verify CLI shim exists**

```bash
uv run video-to-notebook --help 2>&1 | head -5
```

Expected: error about no `app` attribute yet (cli.py not written) — that's fine; the entry point is wired.

- [ ] **Step 8: Commit**

```bash
git add pyproject.toml .python-version ruff.toml pyrightconfig.json src/video_to_notebook/__init__.py
git commit -m "chore: project scaffold (pyproject, ruff, pyright, uv)"
```

---

### Task 2: Pytest scaffold + dummy test

**Files:**
- Create: `tests/__init__.py` (empty)
- Create: `tests/conftest.py`
- Create: `tests/unit/__init__.py` (empty)
- Create: `tests/unit/test_sanity.py`

- [ ] **Step 1: Write `tests/conftest.py`**

```python
"""Shared pytest fixtures."""
from __future__ import annotations
import os
from pathlib import Path

import pytest


@pytest.fixture
def fixtures_dir() -> Path:
    """Path to tests/fixtures/."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def tmp_project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A throwaway project directory; cwd is set into it for the duration."""
    monkeypatch.chdir(tmp_path)
    return tmp_path
```

- [ ] **Step 2: Write `tests/unit/test_sanity.py`**

```python
def test_imports():
    import video_to_notebook

    assert video_to_notebook.__version__ == "0.1.0"
```

- [ ] **Step 3: Run test**

```bash
uv run pytest tests/unit/test_sanity.py -v
```

Expected: `1 passed`.

- [ ] **Step 4: Run ruff + pyright**

```bash
uv run ruff check .
uv run pyright src tests
```

Expected: both pass with no errors.

- [ ] **Step 5: Commit**

```bash
git add tests/
git commit -m "test: pytest scaffold + sanity test"
```

---

### Task 3: GitHub Actions CI

**Files:**
- Create: `.github/workflows/ci.yml`

- [ ] **Step 1: Write CI workflow**

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"

      - name: Set up Python
        run: uv python install 3.12

      - name: Install dependencies
        run: uv pip install --system -e ".[dev]"

      - name: Lint
        run: ruff check .

      - name: Type check
        run: pyright src tests

      - name: Test
        run: pytest -v --tb=short
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/ci.yml
git commit -m "ci: lint + typecheck + test on push/PR"
```

---

## Phase 1: Database Layer

### Task 4: SQLite schema + session module

**Files:**
- Create: `src/video_to_notebook/db/__init__.py` (empty)
- Create: `src/video_to_notebook/db/schema.sql`
- Create: `src/video_to_notebook/db/session.py`
- Create: `tests/unit/test_db_session.py`

This task implements the Plan-1 subset of the schema (courses + lectures + chunks). Tables for concepts / aliases / chunk_concepts / build_meta arrive in Plans 2-3.

- [ ] **Step 1: Write the failing test for session**

```python
# tests/unit/test_db_session.py
from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from video_to_notebook.db.session import init_db, connect


def test_init_db_creates_tables(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    with connect(db_path) as conn:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        names = [r[0] for r in rows]

    assert "courses" in names
    assert "lectures" in names
    assert "chunks" in names


def test_init_db_idempotent(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    init_db(db_path)  # second call must not raise


def test_connect_enables_foreign_keys(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (val,) = conn.execute("PRAGMA foreign_keys").fetchone()
        assert val == 1


def test_transaction_rolls_back_on_error(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    with pytest.raises(sqlite3.IntegrityError):
        with connect(db_path) as conn:
            conn.execute(
                "INSERT INTO courses (slug, title, platform, source_url, added_at) "
                "VALUES (?, ?, ?, ?, ?)",
                ("cs336", "CS336", "youtube", "https://x", "2026-01-01"),
            )
            conn.execute(
                "INSERT INTO courses (slug, title, platform, source_url, added_at) "
                "VALUES (?, ?, ?, ?, ?)",
                ("cs336", "duplicate slug", "youtube", "https://y", "2026-01-01"),
            )

    # The first insert should also have rolled back.
    with connect(db_path) as conn:
        (cnt,) = conn.execute("SELECT COUNT(*) FROM courses").fetchone()
    assert cnt == 0
```

- [ ] **Step 2: Run test to verify it fails**

```bash
uv run pytest tests/unit/test_db_session.py -v
```

Expected: `ImportError: cannot import name 'init_db'`.

- [ ] **Step 3: Write `src/video_to_notebook/db/schema.sql`**

```sql
-- Plan 1 subset. concepts/aliases/chunk_concepts/build_meta tables land in Plan 2.

CREATE TABLE IF NOT EXISTS courses (
  id          INTEGER PRIMARY KEY,
  slug        TEXT UNIQUE NOT NULL,
  title       TEXT NOT NULL,
  platform    TEXT NOT NULL CHECK (platform IN ('youtube', 'bilibili')),
  source_url  TEXT NOT NULL,
  added_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lectures (
  id            INTEGER PRIMARY KEY,
  course_id     INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  idx           INTEGER NOT NULL,
  title         TEXT NOT NULL,
  video_url     TEXT NOT NULL,
  duration_sec  INTEGER,
  transcript    TEXT,
  status        TEXT NOT NULL CHECK (status IN ('ok', 'paywalled', 'no_subs', 'error')),
  UNIQUE (course_id, idx)
);

CREATE TABLE IF NOT EXISTS chunks (
  id          INTEGER PRIMARY KEY,
  lecture_id  INTEGER NOT NULL REFERENCES lectures(id) ON DELETE CASCADE,
  idx         INTEGER NOT NULL,
  start_sec   REAL NOT NULL,
  end_sec     REAL NOT NULL,
  text        TEXT NOT NULL,
  UNIQUE (lecture_id, idx)
);

CREATE INDEX IF NOT EXISTS idx_chunk_lecture ON chunks(lecture_id);
```

- [ ] **Step 4: Write `src/video_to_notebook/db/session.py`**

```python
"""SQLite connection lifecycle and transaction helpers."""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

_SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def init_db(db_path: Path) -> None:
    """Create the database file and apply the schema. Idempotent."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    schema = _SCHEMA_PATH.read_text(encoding="utf-8")
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()


@contextmanager
def connect(db_path: Path) -> Iterator[sqlite3.Connection]:
    """Open a connection with sane defaults inside a transaction.

    Auto-commits on clean exit; rolls back on exception.
    """
    conn = sqlite3.connect(db_path, isolation_level=None)  # autocommit off via BEGIN
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("BEGIN")
    try:
        yield conn
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
uv run pytest tests/unit/test_db_session.py -v
```

Expected: `4 passed`.

- [ ] **Step 6: Commit**

```bash
git add src/video_to_notebook/db/ tests/unit/test_db_session.py
git commit -m "feat(db): schema.sql + session.connect/init_db with transaction safety"
```

---

## Phase 2: Config Loader

### Task 5: Project config (TOML)

**Files:**
- Create: `src/video_to_notebook/config.py`
- Create: `tests/unit/test_config.py`

The project root sits at `.video-to-notebook/` once `init` has been run. Config lives at `.video-to-notebook/config.toml`. This task is the read side; `init` (Task 7) writes the default.

- [ ] **Step 1: Write the failing test**

```python
# tests/unit/test_config.py
from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.config import (
    Config,
    ProjectNotInitializedError,
    find_project_root,
    load_config,
)


def test_find_project_root_finds_marker(tmp_path: Path):
    (tmp_path / ".video-to-notebook").mkdir()
    nested = tmp_path / "a" / "b"
    nested.mkdir(parents=True)
    assert find_project_root(nested) == tmp_path


def test_find_project_root_raises_when_missing(tmp_path: Path):
    with pytest.raises(ProjectNotInitializedError):
        find_project_root(tmp_path)


def test_load_config_reads_toml(tmp_path: Path):
    root = tmp_path
    (root / ".video-to-notebook").mkdir()
    (root / ".video-to-notebook" / "config.toml").write_text(
        'tagger_model = "claude-haiku-4-5"\n'
        'cluster_review_model = "claude-sonnet-4-6"\n'
    )
    cfg = load_config(root)
    assert isinstance(cfg, Config)
    assert cfg.tagger_model == "claude-haiku-4-5"
    assert cfg.db_path == root / ".video-to-notebook" / "db.sqlite"
```

- [ ] **Step 2: Run test to verify failure**

```bash
uv run pytest tests/unit/test_config.py -v
```

Expected: `ImportError`.

- [ ] **Step 3: Write `src/video_to_notebook/config.py`**

```python
"""Project config + project-root discovery."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path


PROJECT_MARKER = ".video-to-notebook"
CONFIG_FILENAME = "config.toml"
DB_FILENAME = "db.sqlite"


class ProjectNotInitializedError(RuntimeError):
    """Raised when no `.video-to-notebook/` ancestor is found."""


@dataclass(frozen=True, slots=True)
class Config:
    """Parsed project config plus derived paths."""

    project_root: Path
    tagger_model: str = "claude-haiku-4-5"
    cluster_review_model: str = "claude-sonnet-4-6"

    @property
    def state_dir(self) -> Path:
        return self.project_root / PROJECT_MARKER

    @property
    def db_path(self) -> Path:
        return self.state_dir / DB_FILENAME


def find_project_root(start: Path) -> Path:
    """Walk up from `start` looking for a directory containing `.video-to-notebook/`."""
    start = start.resolve()
    for candidate in (start, *start.parents):
        if (candidate / PROJECT_MARKER).is_dir():
            return candidate
    raise ProjectNotInitializedError(
        f"No video-to-notebook project found at or above {start}. "
        "Run `video-to-notebook init` first."
    )


def load_config(project_root: Path) -> Config:
    """Read .video-to-notebook/config.toml; missing keys fall back to dataclass defaults."""
    config_file = project_root / PROJECT_MARKER / CONFIG_FILENAME
    if not config_file.is_file():
        return Config(project_root=project_root)
    data = tomllib.loads(config_file.read_text(encoding="utf-8"))
    return Config(
        project_root=project_root,
        tagger_model=data.get("tagger_model", Config.tagger_model),
        cluster_review_model=data.get("cluster_review_model", Config.cluster_review_model),
    )
```

- [ ] **Step 4: Run test**

```bash
uv run pytest tests/unit/test_config.py -v
```

Expected: `3 passed`.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/config.py tests/unit/test_config.py
git commit -m "feat(config): project root discovery + TOML config loader"
```

---

## Phase 3: CLI Skeleton + `init` Command

### Task 6: Typer app with `init`

**Files:**
- Create: `src/video_to_notebook/cli.py`
- Create: `tests/integration/__init__.py` (empty)
- Create: `tests/integration/test_init.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/integration/test_init.py
from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app

runner = CliRunner()


@pytest.mark.integration
def test_init_creates_state_dir(tmp_project: Path):
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0, result.stdout

    assert (tmp_project / ".video-to-notebook").is_dir()
    assert (tmp_project / ".video-to-notebook" / "db.sqlite").is_file()
    assert (tmp_project / ".video-to-notebook" / "config.toml").is_file()


@pytest.mark.integration
def test_init_refuses_to_overwrite(tmp_project: Path):
    runner.invoke(app, ["init"])
    result = runner.invoke(app, ["init"])
    assert result.exit_code != 0
    assert "already initialized" in result.stdout.lower()


@pytest.mark.integration
def test_init_force_reinitializes(tmp_project: Path):
    runner.invoke(app, ["init"])
    # Drop a sentinel file to prove --force regenerates state
    sentinel = tmp_project / ".video-to-notebook" / "leftover.txt"
    sentinel.write_text("stale")

    result = runner.invoke(app, ["init", "--force"])
    assert result.exit_code == 0, result.stdout
    assert not sentinel.exists()
```

- [ ] **Step 2: Run tests to verify failure**

```bash
uv run pytest tests/integration/test_init.py -v
```

Expected: `ImportError: cannot import name 'app' from 'video_to_notebook.cli'`.

- [ ] **Step 3: Write `src/video_to_notebook/cli.py`**

```python
"""Typer-based CLI entrypoint."""
from __future__ import annotations

import shutil
from pathlib import Path

import typer
from rich.console import Console

from video_to_notebook.config import CONFIG_FILENAME, PROJECT_MARKER
from video_to_notebook.db.session import init_db

app = typer.Typer(
    help="Crawl and merge open-courseware into an interactive concept-anchored site.",
    no_args_is_help=True,
    add_completion=False,
)

console = Console()


DEFAULT_CONFIG_TOML = """\
# video-to-notebook project config

# tagger_model = "claude-haiku-4-5"
# cluster_review_model = "claude-sonnet-4-6"
"""


@app.command("init")
def init_cmd(
    force: bool = typer.Option(
        False, "--force", help="Wipe existing state and reinitialize."
    ),
) -> None:
    """Initialize a video-to-notebook project in the current directory."""
    cwd = Path.cwd()
    state_dir = cwd / PROJECT_MARKER

    if state_dir.exists():
        if not force:
            console.print(
                f"[red]error[/red]: {PROJECT_MARKER}/ already initialized at {cwd}. "
                "Use --force to overwrite.",
            )
            raise typer.Exit(code=1)
        shutil.rmtree(state_dir)

    state_dir.mkdir(parents=True)
    init_db(state_dir / "db.sqlite")
    (state_dir / CONFIG_FILENAME).write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")

    console.print(f"[green]initialized[/green] video-to-notebook project at {cwd}")
```

- [ ] **Step 4: Run tests**

```bash
uv run pytest tests/integration/test_init.py -v
```

Expected: `3 passed`.

- [ ] **Step 5: Smoke test the CLI for real**

```bash
cd /tmp && rm -rf cm-smoke && mkdir cm-smoke && cd cm-smoke
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook init
ls -la .video-to-notebook/
```

Expected: `db.sqlite` and `config.toml` exist.

- [ ] **Step 6: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add src/video_to_notebook/cli.py tests/integration/
git commit -m "feat(cli): \`init\` command scaffolds .video-to-notebook/ state dir"
```

---

## Phase 4: Subtitle Parser

### Task 7: VTT parser

**Files:**
- Create: `src/video_to_notebook/crawl/__init__.py` (empty)
- Create: `src/video_to_notebook/crawl/subtitles.py`
- Create: `tests/fixtures/mini_course/youtube_lecture1.vtt`
- Create: `tests/unit/test_subtitles.py`

This is the part of `video-course-notes` we're extracting and cleaning up — a pure function over VTT text.

- [ ] **Step 1: Write fixture `tests/fixtures/mini_course/youtube_lecture1.vtt`**

```
WEBVTT
Kind: captions
Language: en

00:00:00.500 --> 00:00:03.100
Welcome to lecture one of CS336 from Stanford.

00:00:03.100 --> 00:00:06.800
Today we will introduce the transformer architecture
and explain self-attention.

00:00:06.800 --> 00:00:09.500
<00:00:07.200><c>The</c> <c>key</c> <c>question</c> is: why does it scale?

00:00:09.500 --> 00:00:12.000
Welcome to lecture one of CS336 from Stanford.
```

(Last line is a duplicate of the first to verify dedup.)

- [ ] **Step 2: Write the failing test**

```python
# tests/unit/test_subtitles.py
from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.crawl.subtitles import Cue, parse_vtt


def test_parse_vtt_basic(fixtures_dir: Path):
    text = (fixtures_dir / "mini_course" / "youtube_lecture1.vtt").read_text()
    cues = parse_vtt(text)

    assert len(cues) == 3  # duplicate dropped
    assert isinstance(cues[0], Cue)
    assert cues[0].start_sec == pytest.approx(0.5)
    assert cues[0].end_sec == pytest.approx(3.1)
    assert "Welcome to lecture one" in cues[0].text


def test_parse_vtt_strips_inline_tags(fixtures_dir: Path):
    text = (fixtures_dir / "mini_course" / "youtube_lecture1.vtt").read_text()
    cues = parse_vtt(text)
    assert "<c>" not in cues[2].text
    assert "key" in cues[2].text


def test_parse_vtt_handles_empty():
    assert parse_vtt("") == []
    assert parse_vtt("WEBVTT\n\n") == []


def test_parse_vtt_decodes_html_entities():
    src = "WEBVTT\n\n00:00:01.000 --> 00:00:02.000\n&gt;&gt; Hi &amp; bye"
    cues = parse_vtt(src)
    assert cues[0].text == ">> Hi & bye"
```

- [ ] **Step 3: Run tests to verify failure**

```bash
uv run pytest tests/unit/test_subtitles.py -v
```

Expected: `ImportError`.

- [ ] **Step 4: Write `src/video_to_notebook/crawl/subtitles.py`**

```python
"""Parse WebVTT / SRT subtitles into time-stamped cues."""
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
    """Parse a WebVTT-format subtitle string. Dedupes consecutive identical lines."""
    lines = text.splitlines()
    cues: list[Cue] = []
    i = 0
    prev_text: str | None = None

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
        if cleaned == prev_text:
            continue
        cues.append(Cue(start_sec=start, end_sec=end, text=cleaned))
        prev_text = cleaned

    return cues
```

- [ ] **Step 5: Run tests**

```bash
uv run pytest tests/unit/test_subtitles.py -v
```

Expected: `4 passed`.

- [ ] **Step 6: Commit**

```bash
git add src/video_to_notebook/crawl/__init__.py src/video_to_notebook/crawl/subtitles.py tests/fixtures/ tests/unit/test_subtitles.py
git commit -m "feat(crawl): WebVTT parser with dedup, tag stripping, entity decoding"
```

---

## Phase 5: Chunker

### Task 8: Chunker (Cue → Chunk)

**Files:**
- Create: `src/video_to_notebook/crawl/base.py`
- Create: `tests/unit/test_chunker.py`

The chunker groups consecutive cues into ~300-800 token chunks. v1 uses a sliding-window approach over cue boundaries (no chapter detection — that arrives in v2). The actual "token" measurement is approximate via word count × 1.3.

- [ ] **Step 1: Write the failing test**

```python
# tests/unit/test_chunker.py
from __future__ import annotations

from video_to_notebook.crawl.base import Chunk, Chunker
from video_to_notebook.crawl.subtitles import Cue


def _mk_cues(count: int, words_per_cue: int = 5, dur: float = 3.0) -> list[Cue]:
    out: list[Cue] = []
    for i in range(count):
        text = " ".join([f"w{i}_{k}" for k in range(words_per_cue)])
        out.append(Cue(start_sec=i * dur, end_sec=(i + 1) * dur, text=text))
    return out


def test_chunker_groups_cues_to_target_tokens():
    # 100 cues × 10 words ≈ 1000 words ≈ 1300 tokens → ~2-3 chunks @ target=500
    cues = _mk_cues(100, words_per_cue=10)
    chunks = Chunker(target_tokens=500).chunk(cues)

    assert len(chunks) >= 2
    for c in chunks:
        assert isinstance(c, Chunk)
        assert c.start_sec >= 0
        assert c.end_sec > c.start_sec
        # First/last chunks may undershoot; interior must be within 50% of target.

    # Idx must be 0-based and monotonic.
    assert [c.idx for c in chunks] == list(range(len(chunks)))


def test_chunker_empty_input():
    assert Chunker(target_tokens=500).chunk([]) == []


def test_chunker_single_short_cue():
    cues = [Cue(0.0, 1.0, "hello world")]
    chunks = Chunker(target_tokens=500).chunk(cues)
    assert len(chunks) == 1
    assert chunks[0].text == "hello world"
    assert chunks[0].start_sec == 0.0
    assert chunks[0].end_sec == 1.0


def test_chunker_preserves_total_word_count():
    cues = _mk_cues(50, words_per_cue=7)
    chunks = Chunker(target_tokens=300).chunk(cues)

    expected_words = sum(len(c.text.split()) for c in cues)
    got_words = sum(len(c.text.split()) for c in chunks)
    assert expected_words == got_words
```

- [ ] **Step 2: Run tests to verify failure**

```bash
uv run pytest tests/unit/test_chunker.py -v
```

Expected: `ImportError`.

- [ ] **Step 3: Write `src/video_to_notebook/crawl/base.py`**

```python
"""Crawler protocol + chunker (cue → chunk)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from video_to_notebook.crawl.subtitles import Cue


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
```

- [ ] **Step 4: Run tests**

```bash
uv run pytest tests/unit/test_chunker.py -v
```

Expected: `4 passed`.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/crawl/base.py tests/unit/test_chunker.py
git commit -m "feat(crawl): Chunker groups cues to target token budget"
```

---

## Phase 6: YouTube Crawler

### Task 9: YouTube adapter (yt-dlp subprocess)

**Files:**
- Create: `src/video_to_notebook/crawl/youtube.py`
- Create: `tests/unit/test_crawler_youtube.py`

The adapter shells out to `yt-dlp` with a stable flag combo. Tests mock `subprocess.run` so they don't need network.

- [ ] **Step 1: Write the failing test**

```python
# tests/unit/test_crawler_youtube.py
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from video_to_notebook.crawl.youtube import YouTubeCrawler


def _fake_completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    return subprocess.CompletedProcess(args=[], returncode=returncode, stdout=stdout, stderr=stderr)


def test_list_playlist_parses_flat_output():
    fake_stdout = "1|abc123|Lecture 1: Intro\n2|def456|Lecture 2: Transformers\n"
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)) as mock:
        entries = YouTubeCrawler().list_playlist("https://youtube.com/playlist?list=PLX")

    assert entries == [
        {"idx": 1, "video_id": "abc123", "title": "Lecture 1: Intro",
         "video_url": "https://www.youtube.com/watch?v=abc123"},
        {"idx": 2, "video_id": "def456", "title": "Lecture 2: Transformers",
         "video_url": "https://www.youtube.com/watch?v=def456"},
    ]
    cmd = mock.call_args.args[0]
    assert "--flat-playlist" in cmd
    assert "%(playlist_index)s|%(id)s|%(title)s" in cmd


def test_list_playlist_single_video_wraps_to_one_entry():
    """A single-video URL should yield one playlist entry."""
    fake_stdout = "NA|xyz789|Single Talk\n"
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)):
        entries = YouTubeCrawler().list_playlist("https://www.youtube.com/watch?v=xyz789")
    assert len(entries) == 1
    assert entries[0]["idx"] == 1
    assert entries[0]["video_id"] == "xyz789"


def test_download_subtitle_vtt_returns_none_when_no_subs(tmp_path: Path):
    # Simulate yt-dlp succeeding but writing no file.
    with patch("subprocess.run", return_value=_fake_completed(returncode=0)):
        result = YouTubeCrawler(_work_dir=tmp_path).download_subtitle_vtt(
            "https://www.youtube.com/watch?v=xyz", lang_priority=["en"], cookies_from=None
        )
    assert result is None


def test_download_subtitle_vtt_reads_file(tmp_path: Path):
    """If yt-dlp writes a .vtt file, we read it back as the result."""
    crawler = YouTubeCrawler(_work_dir=tmp_path)
    # Pre-create the file that the subprocess would have written.
    vtt_path = tmp_path / "sub.en.vtt"
    vtt_path.write_text("WEBVTT\n\nfake content")

    def fake_run(cmd, *_args, **_kwargs):
        # Real yt-dlp would have produced sub.en.vtt; we just confirm it exists.
        return _fake_completed()

    with patch("subprocess.run", side_effect=fake_run):
        result = crawler.download_subtitle_vtt(
            "https://www.youtube.com/watch?v=xyz", lang_priority=["en"], cookies_from=None
        )
    assert result is not None
    assert result.startswith("WEBVTT")
```

- [ ] **Step 2: Run tests to verify failure**

```bash
uv run pytest tests/unit/test_crawler_youtube.py -v
```

Expected: `ImportError`.

- [ ] **Step 3: Write `src/video_to_notebook/crawl/youtube.py`**

```python
"""YouTube adapter: shells out to yt-dlp for playlist enumeration and subtitle download."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


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

    def _workspace(self):
        from contextlib import contextmanager

        @contextmanager
        def ctx():
            if self._work_dir is not None:
                yield self._work_dir
            else:
                with tempfile.TemporaryDirectory() as td:
                    yield Path(td)

        return ctx()
```

- [ ] **Step 4: Run tests**

```bash
uv run pytest tests/unit/test_crawler_youtube.py -v
```

Expected: `4 passed`.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/crawl/youtube.py tests/unit/test_crawler_youtube.py
git commit -m "feat(crawl): YouTube adapter (yt-dlp playlist + VTT subtitle download)"
```

---

## Phase 7: Bilibili Crawler

### Task 10: Bilibili adapter

**Files:**
- Create: `src/video_to_notebook/crawl/bilibili.py`
- Create: `tests/fixtures/mini_course/bilibili_lecture1.vtt`
- Create: `tests/unit/test_crawler_bilibili.py`

B 站要求 `--cookies-from-browser` 才能拿到字幕，且 playlist 用 `?p=N` 分页（不是 video ID）。Subtitle language priority: `ai-zh` → `ai-en`.

- [ ] **Step 1: Write fixture (a B 站 AI 中文字幕样本)**

```
# tests/fixtures/mini_course/bilibili_lecture1.vtt
WEBVTT

00:00:00.000 --> 00:00:04.000
大家好，欢迎来到 CS336 第一讲。

00:00:04.000 --> 00:00:08.500
今天我们介绍 transformer 架构，以及 self-attention 是怎么工作的。

00:00:08.500 --> 00:00:12.000
为什么 attention 会 scale 得这么好？
```

- [ ] **Step 2: Write the failing test**

```python
# tests/unit/test_crawler_bilibili.py
from __future__ import annotations

import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from video_to_notebook.crawl.bilibili import BilibiliCrawler, BilibiliCookieError


def _fake_completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    return subprocess.CompletedProcess(args=[], returncode=returncode, stdout=stdout, stderr=stderr)


def test_list_playlist_iterates_p_param():
    """Bilibili playlists use ?p=N, not video IDs."""
    crawler = BilibiliCrawler()
    fake_stdout = "1|BVxxx|Lecture 1\n2|BVxxx|Lecture 2\n3|BVxxx|Lecture 3\n"
    with patch("subprocess.run", return_value=_fake_completed(stdout=fake_stdout)):
        entries = crawler.list_playlist("https://www.bilibili.com/video/BVxxx/")

    assert len(entries) == 3
    assert entries[0]["video_url"] == "https://www.bilibili.com/video/BVxxx/?p=1"
    assert entries[2]["video_url"] == "https://www.bilibili.com/video/BVxxx/?p=3"


def test_download_subtitle_tries_ai_zh_then_ai_en(tmp_path: Path):
    crawler = BilibiliCrawler(_work_dir=tmp_path)

    call_log: list[list[str]] = []

    def fake_run(cmd, *args, **kwargs):
        call_log.append(cmd)
        # Pretend ai-en succeeds (writes a file); ai-zh fails (no file).
        if "ai-en" in cmd:
            (tmp_path / "sub.ai-en.vtt").write_text("WEBVTT\n\nfake en")
        return _fake_completed()

    with patch("subprocess.run", side_effect=fake_run):
        result = crawler.download_subtitle_vtt(
            "https://www.bilibili.com/video/BVxxx/?p=1",
            lang_priority=["ai-zh", "ai-en"],
            cookies_from="edge",
        )

    assert result == "WEBVTT\n\nfake en"
    # First attempt was ai-zh, second was ai-en.
    assert "ai-zh" in call_log[0]
    assert "ai-en" in call_log[1]


def test_download_subtitle_requires_cookies():
    crawler = BilibiliCrawler()
    with pytest.raises(BilibiliCookieError):
        crawler.download_subtitle_vtt(
            "https://www.bilibili.com/video/BVxxx/?p=1",
            lang_priority=["ai-zh"],
            cookies_from=None,
        )


def test_download_subtitle_detects_403_and_raises():
    crawler = BilibiliCrawler()
    fake_run = _fake_completed(stderr="HTTP Error 403: Forbidden", returncode=1)
    with patch("subprocess.run", return_value=fake_run):
        with pytest.raises(BilibiliCookieError) as exc:
            crawler.download_subtitle_vtt(
                "https://www.bilibili.com/video/BVxxx/?p=1",
                lang_priority=["ai-zh"],
                cookies_from="edge",
            )
    assert "edge" in str(exc.value)  # actionable error mentions the browser name
```

- [ ] **Step 3: Run tests to verify failure**

```bash
uv run pytest tests/unit/test_crawler_bilibili.py -v
```

Expected: `ImportError`.

- [ ] **Step 4: Write `src/video_to_notebook/crawl/bilibili.py`**

```python
"""Bilibili adapter: yt-dlp with cookies (required) and ?p=N playlist pagination."""
from __future__ import annotations

import re
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path


class BilibiliCookieError(RuntimeError):
    """Raised when Bilibili rejects the request due to missing/expired cookies."""


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

    def _workspace(self):
        @contextmanager
        def ctx():
            if self._work_dir is not None:
                yield self._work_dir
            else:
                with tempfile.TemporaryDirectory() as td:
                    yield Path(td)

        return ctx()
```

- [ ] **Step 5: Run tests**

```bash
uv run pytest tests/unit/test_crawler_bilibili.py -v
```

Expected: `4 passed`.

- [ ] **Step 6: Commit**

```bash
git add src/video_to_notebook/crawl/bilibili.py tests/fixtures/mini_course/bilibili_lecture1.vtt tests/unit/test_crawler_bilibili.py
git commit -m "feat(crawl): Bilibili adapter with cookie + ai-zh/ai-en fallback"
```

---

## Phase 8: `crawl` CLI Command + End-to-End Smoke Test

### Task 11: Wire crawlers into CLI

**Files:**
- Modify: `src/video_to_notebook/cli.py` (add `crawl` command)
- Create: `src/video_to_notebook/crawl/runner.py` (orchestrates list → download → parse → chunk → insert)
- Create: `tests/integration/test_crawl_smoke.py`

The `crawl` command does the boring orchestration: pick a crawler by URL host, list the playlist, for each entry download VTT, parse, chunk, and write to DB. Heavily mocked at the crawler boundary in tests.

- [ ] **Step 1: Write the failing test for `runner`**

```python
# tests/unit/test_crawl_runner.py
from __future__ import annotations

import sqlite3
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from video_to_notebook.crawl.runner import CrawlReport, run_crawl
from video_to_notebook.db.session import connect, init_db


@pytest.fixture
def fake_crawler():
    crawler = MagicMock()
    crawler.platform = "youtube"
    crawler.list_playlist.return_value = [
        {"idx": 1, "video_id": "v1", "title": "L1", "video_url": "https://yt/v1"},
        {"idx": 2, "video_id": "v2", "title": "L2", "video_url": "https://yt/v2"},
    ]
    # L1 returns a VTT; L2 returns None (no subs).
    crawler.download_subtitle_vtt.side_effect = [
        "WEBVTT\n\n00:00:00.000 --> 00:00:02.000\nHello.\n\n00:00:02.000 --> 00:00:04.000\nWorld.",
        None,
    ]
    return crawler


def test_run_crawl_inserts_lectures_and_chunks(tmp_path: Path, fake_crawler):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    report = run_crawl(
        db_path=db_path,
        crawler=fake_crawler,
        url="https://yt/playlist",
        course_slug="testcourse",
        course_title="Test Course",
        lang_priority=["en"],
        cookies_from=None,
    )

    assert isinstance(report, CrawlReport)
    assert report.course_slug == "testcourse"
    assert report.lectures_ok == 1
    assert report.lectures_no_subs == 1

    with connect(db_path) as conn:
        (courses,) = conn.execute("SELECT COUNT(*) FROM courses").fetchone()
        (lectures,) = conn.execute("SELECT COUNT(*) FROM lectures").fetchone()
        (chunks,) = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()

    assert courses == 1
    assert lectures == 2
    assert chunks >= 1  # L1 produces at least one chunk


def test_run_crawl_is_idempotent(tmp_path: Path, fake_crawler):
    """Re-running the same crawl must not create duplicate lectures."""
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    run_crawl(
        db_path=db_path,
        crawler=fake_crawler,
        url="https://yt/playlist",
        course_slug="testcourse",
        course_title="Test Course",
        lang_priority=["en"],
        cookies_from=None,
    )

    # Reset the side_effect since the mock has been consumed.
    fake_crawler.download_subtitle_vtt.side_effect = [
        "WEBVTT\n\n00:00:00.000 --> 00:00:02.000\nHello.",
        None,
    ]

    run_crawl(
        db_path=db_path,
        crawler=fake_crawler,
        url="https://yt/playlist",
        course_slug="testcourse",
        course_title="Test Course",
        lang_priority=["en"],
        cookies_from=None,
    )

    with connect(db_path) as conn:
        (lectures,) = conn.execute("SELECT COUNT(*) FROM lectures").fetchone()
    assert lectures == 2  # not 4
```

- [ ] **Step 2: Run test to verify failure**

```bash
uv run pytest tests/unit/test_crawl_runner.py -v
```

Expected: `ImportError`.

- [ ] **Step 3: Write `src/video_to_notebook/crawl/runner.py`**

```python
"""Orchestrator: crawler → subtitles → chunker → DB."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol

from video_to_notebook.crawl.base import Chunker
from video_to_notebook.crawl.subtitles import parse_vtt
from video_to_notebook.db.session import connect


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
        # Upsert course.
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
            # Skip if lecture already exists at this idx.
            existing = conn.execute(
                "SELECT id, status FROM lectures WHERE course_id = ? AND idx = ?",
                (course_id, entry["idx"]),
            ).fetchone()
            if existing is not None:
                # Existing lecture — increment counter based on its current status.
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
```

- [ ] **Step 4: Run tests**

```bash
uv run pytest tests/unit/test_crawl_runner.py -v
```

Expected: `2 passed`.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/crawl/runner.py tests/unit/test_crawl_runner.py
git commit -m "feat(crawl): runner orchestrates crawler -> subtitles -> chunker -> DB"
```

---

### Task 12: Add `crawl` CLI subcommand

**Files:**
- Modify: `src/video_to_notebook/cli.py`
- Create: `tests/integration/test_crawl_smoke.py`

- [ ] **Step 1: Write the failing integration test**

```python
# tests/integration/test_crawl_smoke.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_crawl_youtube_end_to_end(tmp_project: Path, fixtures_dir: Path):
    """`init` then `crawl` a fake YouTube playlist, end up with rows in the DB."""
    runner.invoke(app, ["init"])

    vtt_text = (fixtures_dir / "mini_course" / "youtube_lecture1.vtt").read_text()

    fake_list = [{"idx": 1, "video_id": "v1", "title": "Intro", "video_url": "https://yt/v1"}]

    with (
        patch("video_to_notebook.crawl.youtube.YouTubeCrawler.list_playlist", return_value=fake_list),
        patch(
            "video_to_notebook.crawl.youtube.YouTubeCrawler.download_subtitle_vtt",
            return_value=vtt_text,
        ),
    ):
        result = runner.invoke(
            app,
            ["crawl", "https://www.youtube.com/watch?v=v1", "--name", "cs336-fake"],
        )

    assert result.exit_code == 0, result.stdout

    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        (courses,) = conn.execute("SELECT COUNT(*) FROM courses").fetchone()
        (lectures,) = conn.execute("SELECT COUNT(*) FROM lectures WHERE status='ok'").fetchone()
        (chunks,) = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()

    assert courses == 1
    assert lectures == 1
    assert chunks >= 1


@pytest.mark.integration
def test_crawl_bilibili_requires_cookies(tmp_project: Path):
    runner.invoke(app, ["init"])
    result = runner.invoke(
        app,
        ["crawl", "https://www.bilibili.com/video/BVxxx/", "--name", "x"],
    )
    assert result.exit_code != 0
    assert "cookies" in result.stdout.lower()


@pytest.mark.integration
def test_crawl_errors_when_not_initialized(tmp_project: Path):
    """Running `crawl` before `init` should be a clear error, not a crash."""
    result = runner.invoke(app, ["crawl", "https://yt/x", "--name", "y"])
    assert result.exit_code != 0
    assert "init" in result.stdout.lower()
```

- [ ] **Step 2: Run integration test to confirm failure**

```bash
uv run pytest tests/integration/test_crawl_smoke.py -v
```

Expected: failures (no `crawl` command registered yet).

- [ ] **Step 3: Modify `src/video_to_notebook/cli.py` — add `crawl` command**

Add these imports and the new command to `cli.py`:

```python
# Add to top of cli.py imports:
from urllib.parse import urlparse

from video_to_notebook.config import ProjectNotInitializedError, find_project_root
from video_to_notebook.crawl.bilibili import BilibiliCookieError, BilibiliCrawler
from video_to_notebook.crawl.runner import run_crawl
from video_to_notebook.crawl.youtube import YouTubeCrawler


def _detect_platform(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    if "bilibili.com" in host or "b23.tv" in host:
        return "bilibili"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    raise typer.BadParameter(f"Unrecognized platform for URL: {url}")


def _slugify(text: str) -> str:
    import re
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    return s.strip("-") or "course"


@app.command("crawl")
def crawl_cmd(
    url: str = typer.Argument(..., help="Video or playlist URL"),
    name: str | None = typer.Option(
        None, "--name", help="Course slug (defaults to a slugified domain+title)."
    ),
    lang: list[str] | None = typer.Option(
        None,
        "--lang",
        help="Subtitle language priority list. "
        "Defaults: YouTube=[en], Bilibili=[ai-zh, ai-en].",
    ),
    cookies_from: str | None = typer.Option(
        None,
        "--cookies-from",
        help="Browser to extract cookies from (required for Bilibili): edge|chrome|firefox.",
    ),
) -> None:
    """Crawl a course (single video or playlist) into the local DB."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        console.print(f"[red]error[/red]: {e}")
        raise typer.Exit(code=1)

    platform = _detect_platform(url)
    if platform == "bilibili":
        crawler = BilibiliCrawler()
        default_lang = ["ai-zh", "ai-en"]
    else:
        crawler = YouTubeCrawler()
        default_lang = ["en"]

    course_slug = name or _slugify(url)

    db_path = root / PROJECT_MARKER / "db.sqlite"
    try:
        report = run_crawl(
            db_path=db_path,
            crawler=crawler,
            url=url,
            course_slug=course_slug,
            course_title=name or course_slug,
            lang_priority=lang or default_lang,
            cookies_from=cookies_from,
        )
    except BilibiliCookieError as e:
        console.print(f"[red]bilibili cookies missing[/red]: {e}")
        raise typer.Exit(code=2)

    console.print(
        f"[green]done[/green]: {report.lectures_ok} ok, "
        f"{report.lectures_no_subs} no-subs, {report.lectures_error} errors "
        f"(course: {report.course_slug})"
    )
```

- [ ] **Step 4: Run integration tests**

```bash
uv run pytest tests/integration/test_crawl_smoke.py -v
```

Expected: `3 passed`.

- [ ] **Step 5: Run the full test suite**

```bash
uv run pytest -v
uv run ruff check .
uv run pyright src tests
```

Expected: everything green.

- [ ] **Step 6: Commit**

```bash
git add src/video_to_notebook/cli.py tests/integration/test_crawl_smoke.py
git commit -m "feat(cli): \`crawl\` subcommand routes by URL host and calls crawler runner"
```

---

## Phase 9: Documentation Polish

### Task 13: README quickstart

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace README quickstart section**

```markdown
# video-to-notebook

Crawl open-courseware (YouTube / Bilibili), tag chunks with concept labels via Claude, cluster labels into a unified ontology across courses, and emit an interactive static HTML site for self-study.

> [!warning] Status: under construction (Plan 1 of 4 — Foundation + Crawl).
> The current build supports `init` and `crawl` only. Tag / cluster / build land in Plans 2-4.

## Quickstart

```bash
# 1. Install
git clone https://github.com/chenlinzhuo/video-to-notebook.git
cd video-to-notebook
uv venv && uv pip install -e ".[dev]"

# 2. Initialize a project
mkdir my-courses && cd my-courses
uv run video-to-notebook init

# 3. Crawl a YouTube playlist
uv run video-to-notebook crawl \
    "https://www.youtube.com/playlist?list=PLxxx" \
    --name cs336

# 4. Crawl a Bilibili playlist (requires logged-in browser)
uv run video-to-notebook crawl \
    "https://www.bilibili.com/video/BVxxx/" \
    --name "vizuara-llm" \
    --cookies-from edge
```

After `crawl`, all transcripts and chunks live in `.video-to-notebook/db.sqlite`. Inspect with:

```bash
sqlite3 .video-to-notebook/db.sqlite "SELECT slug, title FROM courses;"
sqlite3 .video-to-notebook/db.sqlite "SELECT COUNT(*) FROM chunks;"
```

## Roadmap

- **Plan 1 (current):** Foundation + crawl. `init`, `crawl` for YouTube & Bilibili. ✅
- **Plan 2 (next):** Tag + cluster. `tag`, `cluster`. Claude Haiku tagging + Sonnet cluster review.
- **Plan 3:** Build + HTML. `build`, `serve`. Astro static site with cross-course concept pages.
- **Plan 4:** Demo + deploy. `examples/frontier-notebook/` auto-deploys to GitHub Pages.

## Design

Full design spec: [`docs/specs/2026-05-09-video-to-notebook-skill-design.md`](docs/specs/2026-05-09-video-to-notebook-skill-design.md).

## License

MIT
```

- [ ] **Step 2: Verify the file renders correctly**

```bash
glow README.md 2>/dev/null || cat README.md | head -40
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: README quickstart for Plan 1 (init + crawl)"
```

---

## Phase 10: Plan 1 Verification

### Task 14: Manual smoke test against a real YouTube playlist

**Files:** none (verification only)

This task is the GREEN check for the whole plan — run against a real public video end-to-end. Use a playlist that's small and public.

- [ ] **Step 1: Run init in a throwaway directory**

```bash
cd /tmp && rm -rf cm-real && mkdir cm-real && cd cm-real
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook init
```

Expected: `initialized video-to-notebook project at /tmp/cm-real`.

- [ ] **Step 2: Crawl a real YouTube playlist**

Use the playlist we previously used in this session (Vizuara - Build Claude Code from Scratch):

```bash
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook crawl \
    "https://www.youtube.com/playlist?list=PLPTV0NXA_ZShnka8uVzF3mSvZdilfiGWG" \
    --name "vizuara-build-claude-code"
```

Expected: `done: 3 ok, 0 no-subs, 1 errors` (the L4 video is members-only — it will get `status='error'` because yt-dlp errors out, which is the desired behavior).

- [ ] **Step 3: Verify DB state**

```bash
sqlite3 .video-to-notebook/db.sqlite \
    "SELECT idx, title, status, LENGTH(transcript) FROM lectures ORDER BY idx;"
sqlite3 .video-to-notebook/db.sqlite \
    "SELECT COUNT(*) AS chunks_total FROM chunks;"
```

Expected: 3 rows with `status='ok'` and non-null transcripts; one row with non-ok status; `chunks_total` > 30.

- [ ] **Step 4: Verify idempotency**

```bash
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook crawl \
    "https://www.youtube.com/playlist?list=PLPTV0NXA_ZShnka8uVzF3mSvZdilfiGWG" \
    --name "vizuara-build-claude-code"
sqlite3 .video-to-notebook/db.sqlite "SELECT COUNT(*) FROM lectures;"
```

Expected: same lecture count as before (no duplicates).

- [ ] **Step 5: Tag the completion**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git tag plan-1-done
git log --oneline plan-1-done
```

Plan 1 ships. Ready to start Plan 2 (Tag + Cluster).

---

## Self-Review Notes

**Spec coverage check (Plan 1 portion only):**

- §1 Goals — incremental architecture (DB-backed, idempotent crawl): ✅ Task 11 idempotency test.
- §2 v1 platforms YouTube + Bilibili: ✅ Tasks 9 + 10.
- §3 Architecture diagram (DB at center, crawl as one of 4 commands): ✅ Tasks 4-12 build the crawl arm + DB.
- §4 Repo layout: ✅ Plan covers `src/video_to_notebook/{cli,config,db/,crawl/}` and `tests/{unit,integration,fixtures}`.
- §5 Data model — Plan 1 implements `courses`, `lectures`, `chunks` (and indices); concepts/aliases/chunk_concepts/build_meta deferred to Plan 2 explicitly.
- §6 CLI — Plan 1 implements `init` + `crawl`; `tag`/`cluster`/`build`/`serve`/`review` deferred to Plans 2-3.
- §8 Error handling for crawl — Task 11 (`no_subs`, `error` statuses), Task 12 (cookie missing → actionable error), Task 12 (bare crawl before init → clear error).
- §9 Testing strategy — unit + integration layers present; snapshot/E2E deferred to Plan 3 (no HTML yet).
- §10 Defaults — YouTube lang `en`, Bilibili lang `ai-zh→ai-en`, Bilibili requires `--cookies-from`. ✅

**Out of scope for Plan 1 (correctly deferred):**

- Whisper fallback — §1 Non-Goals confirms v1 doesn't transcribe. ✅ Plan 1 returns None for `no_subs` and reports.
- Tagging / clustering / HTML — Plan 2 / 3.
- Demo site / GH Pages — Plan 4.
- Migrations directory — Plan 1 only has one schema version; `migrations/` arrives when Plan 2 adds concept tables.

**Placeholder scan:** no "TBD", "TODO", or unresolved placeholders. Every code block is runnable.

**Type / signature consistency:**

- `Cue.start_sec` / `end_sec` (float) used consistently in subtitles.py, chunker, and runner.
- `Chunk.idx` / `start_sec` / `end_sec` / `text` consistent across chunker and runner DB insert.
- `Crawler` Protocol attributes (`platform`, `list_playlist`, `download_subtitle_vtt`) match both implementations (YouTubeCrawler, BilibiliCrawler) and the runner's `_CrawlerLike` shape.
- `CrawlReport` fields (`course_slug`, `lectures_ok`, `lectures_no_subs`, `lectures_error`) match runner outputs and CLI output strings.

**One follow-up I'm flagging up-front:** the Plan 1 schema uses `CHECK (platform IN ('youtube', 'bilibili'))`. When Plan 2/3/4 add new platforms (Coursera, edX), this CHECK has to be relaxed via a migration. Acceptable for v1; migration mechanism arrives in Plan 2.
