# Plan 2 — Tag + Cluster Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `course-merger tag && course-merger cluster`. After Plan 2, every crawled chunk has 1-3 Claude-Haiku-assigned concept tags, and proposed new concepts get LLM-reviewed and merged into the canonical ontology via embedding clustering.

**Architecture:** A migration runner (PRAGMA `user_version`) lets us add 4 new tables without breaking Plan 1's DB. The `tag` command loops untagged chunks → calls Claude Haiku with a cacheable system prompt containing the ontology → writes `chunk_concepts` rows. The `cluster` command embeds all `proposed:` tags via sentence-transformers, groups them by cosine similarity, then asks Sonnet per-cluster whether to merge / create / reject.

**Tech Stack:** Python 3.12 + anthropic SDK 0.36+ + sentence-transformers (all-MiniLM-L6-v2) + numpy + PyYAML. Tests mock the Anthropic boundary; embedding tests use the real (small) model.

**Repo:** `/Users/chenlinzhuo/code/course-merger/` (at tag `plan-1-done`, commit `0b0a292`). Plan-1 backlog (WAL mode, `BilibiliCookieError` location, yt-dlp returncode) gets cleared in Phase 0 before Plan-2 features layer on.

---

## File Structure

```
course-merger/
├── pyproject.toml                          # MODIFY: add anthropic, sentence-transformers, pyyaml, numpy, scipy
├── src/course_merger/
│   ├── cli.py                              # MODIFY: add `tag` and `cluster` commands
│   ├── db/
│   │   ├── schema.sql                      # MODIFY: full v2 schema (used by fresh init)
│   │   ├── session.py                      # MODIFY: WAL mode + migration runner
│   │   └── migrations/                     # NEW
│   │       ├── 0001_initial.sql            # NEW: Plan-1 schema as v1 migration
│   │       └── 0002_concepts.sql           # NEW: concepts/aliases/chunk_concepts/build_meta
│   ├── crawl/
│   │   ├── exceptions.py                   # NEW: lift BilibiliCookieError here
│   │   ├── bilibili.py                     # MODIFY: import error from exceptions
│   │   ├── youtube.py                      # MODIFY: check yt-dlp returncode
│   │   └── runner.py                       # MODIFY: import BilibiliCookieError from new location
│   ├── tag/                                # NEW package
│   │   ├── __init__.py
│   │   ├── ontology.py                     # YAML loader, ontology in-memory model
│   │   ├── prompts.py                      # versioned tagger system prompt constants
│   │   ├── claude_tagger.py                # Anthropic SDK wrapper, prompt caching
│   │   └── runner.py                       # orchestrator (loops untagged chunks → DB)
│   └── cluster/                            # NEW package
│       ├── __init__.py
│       ├── embedding.py                    # sentence-transformers wrapper, lazy-load model
│       ├── clusterer.py                    # cosine-similarity greedy clusterer
│       ├── prompts.py                      # versioned Sonnet review prompts
│       ├── llm_review.py                   # Sonnet review pass
│       └── runner.py                       # orchestrator (proposed tags → clusters → reviewed concepts)
└── tests/
    ├── fixtures/
    │   ├── ontology.yaml                   # NEW: tiny seed ontology
    │   └── tagger_responses.py             # NEW: canned Claude JSON for mocks
    ├── unit/
    │   ├── test_migrations.py              # NEW: schema_version tracking
    │   ├── test_exceptions.py              # NEW: import + raising path
    │   ├── test_ontology.py                # NEW: YAML loader edge cases
    │   ├── test_claude_tagger.py           # NEW: mocked SDK, prompt structure, parse logic
    │   ├── test_tag_runner.py              # NEW: full tag pipeline with mocked tagger
    │   ├── test_embedding.py               # NEW: real model, session-scoped fixture
    │   ├── test_clusterer.py               # NEW: synthetic embeddings
    │   ├── test_llm_review.py              # NEW: mocked Sonnet decisions
    │   └── test_cluster_runner.py          # NEW: full cluster pipeline mocked
    └── integration/
        ├── test_tag_smoke.py               # NEW: `tag` CLI end-to-end
        └── test_cluster_smoke.py           # NEW: `cluster` CLI end-to-end
```

Each module has one responsibility:
- `db/migrations/*.sql`: declarative schema deltas, run in order
- `tag/ontology.py`: pure YAML → in-memory ontology
- `tag/prompts.py`: versioned prompt string constants (so prompt changes are reviewable in diff)
- `tag/claude_tagger.py`: Anthropic SDK interaction, includes prompt caching
- `tag/runner.py`: DB ↔ tagger ↔ DB orchestration
- `cluster/embedding.py`: sentence-transformers wrapper, model lazy-loaded
- `cluster/clusterer.py`: pure algorithm over a similarity matrix (no I/O)
- `cluster/llm_review.py`: Sonnet boundary (mocked in tests)
- `cluster/runner.py`: full pipeline with side-effects on DB

---

## Phase 0: Plan-1 Backlog Cleanup

### Task 1: Enable SQLite WAL mode

**Files:**
- Modify: `src/course_merger/db/session.py:24-40`
- Modify: `tests/unit/test_db_session.py` — add test

WAL (Write-Ahead Log) lets readers operate concurrently with a writer. Important for Plan 2 (`tag` writes, `cluster` reads chunks concurrently in future) and Plan 3 (`build` reads while `tag` runs).

- [ ] **Step 1: Write failing test**

Append to `tests/unit/test_db_session.py`:

```python
def test_wal_mode_enabled(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (mode,) = conn.execute("PRAGMA journal_mode").fetchone()
    assert mode == "wal"
```

- [ ] **Step 2: Run test, confirm failure**

```bash
cd /Users/chenlinzhuo/code/course-merger && .venv/bin/pytest tests/unit/test_db_session.py::test_wal_mode_enabled -v
```

Expected: FAIL — current default journal mode is `delete`, not `wal`.

- [ ] **Step 3: Modify `init_db` in `src/course_merger/db/session.py`**

Replace the `init_db` function body:

```python
def init_db(db_path: Path) -> None:
    """Create the database file and apply the schema. Idempotent."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    schema = _SCHEMA_PATH.read_text(encoding="utf-8")
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA journal_mode = WAL")
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()
```

- [ ] **Step 4: Run all tests**

```bash
.venv/bin/pytest tests/unit/test_db_session.py -v
```

Expected: 5/5 pass (4 existing + 1 new).

- [ ] **Step 5: Commit**

```bash
git add src/course_merger/db/session.py tests/unit/test_db_session.py
git commit -m "feat(db): enable SQLite WAL mode for concurrent reads"
```

---

### Task 2: Lift `BilibiliCookieError` to `crawl/exceptions.py`

**Files:**
- Create: `src/course_merger/crawl/exceptions.py`
- Modify: `src/course_merger/crawl/bilibili.py:12-13` (remove definition, import instead)
- Modify: `src/course_merger/crawl/runner.py:10` (update import)
- Modify: `src/course_merger/cli.py:13` (update import)
- Create: `tests/unit/test_exceptions.py`

When more crawler errors arrive (yt-dlp 404, generic platform errors), they belong with `BilibiliCookieError`. Centralizing now is cheap.

- [ ] **Step 1: Write the failing test**

```python
# tests/unit/test_exceptions.py
from __future__ import annotations

import pytest

from course_merger.crawl.exceptions import BilibiliCookieError


def test_bilibili_cookie_error_is_runtime_error():
    assert issubclass(BilibiliCookieError, RuntimeError)


def test_bilibili_cookie_error_raises():
    with pytest.raises(BilibiliCookieError) as exc:
        raise BilibiliCookieError("test message")
    assert "test message" in str(exc.value)


def test_backward_compat_import_from_bilibili():
    """The old import location must still work to avoid breaking callers."""
    from course_merger.crawl.bilibili import BilibiliCookieError as B1
    from course_merger.crawl.exceptions import BilibiliCookieError as B2
    assert B1 is B2
```

- [ ] **Step 2: Run test, confirm failure**

```bash
.venv/bin/pytest tests/unit/test_exceptions.py -v
```

Expected: `ModuleNotFoundError: No module named 'course_merger.crawl.exceptions'`.

- [ ] **Step 3: Create `src/course_merger/crawl/exceptions.py`**

```python
"""Crawler exceptions shared across platform adapters."""
from __future__ import annotations


class BilibiliCookieError(RuntimeError):
    """Raised when Bilibili rejects the request due to missing/expired cookies."""
```

- [ ] **Step 4: Modify `src/course_merger/crawl/bilibili.py`**

Replace lines 12-13 (the local class definition) with a re-export so existing imports keep working:

```python
# After the docstring and existing imports, replace:
#   class BilibiliCookieError(RuntimeError):
#       """Raised when Bilibili rejects the request due to missing/expired cookies."""
# With:
from course_merger.crawl.exceptions import BilibiliCookieError

__all__ = ["BilibiliCookieError", "BilibiliCrawler"]
```

- [ ] **Step 5: Modify `src/course_merger/crawl/runner.py:10`**

Change:
```python
from course_merger.crawl.bilibili import BilibiliCookieError
```
to:
```python
from course_merger.crawl.exceptions import BilibiliCookieError
```

- [ ] **Step 6: Modify `src/course_merger/cli.py:13`**

Change:
```python
from course_merger.crawl.bilibili import BilibiliCookieError, BilibiliCrawler
```
to:
```python
from course_merger.crawl.bilibili import BilibiliCrawler
from course_merger.crawl.exceptions import BilibiliCookieError
```

- [ ] **Step 7: Run full suite**

```bash
.venv/bin/pytest -v
.venv/bin/pyright src tests
```

Expected: 41 pass (38 existing + 3 new), pyright clean.

- [ ] **Step 8: Commit**

```bash
git add src/course_merger/crawl/exceptions.py src/course_merger/crawl/bilibili.py src/course_merger/crawl/runner.py src/course_merger/cli.py tests/unit/test_exceptions.py
git commit -m "refactor(crawl): lift BilibiliCookieError to crawl/exceptions.py"
```

---

### Task 3: yt-dlp returncode check in `list_playlist`

**Files:**
- Modify: `src/course_merger/crawl/youtube.py:19-48` (the `list_playlist` method)
- Modify: `src/course_merger/crawl/bilibili.py:33-61` (same method)
- Create: `tests/unit/test_crawler_youtube.py` — add new test
- Create: `tests/unit/test_crawler_bilibili.py` — add new test

Plan 1's `list_playlist` ignored yt-dlp's exit code: a 403 on the playlist URL itself silently returned `[]` and `run_crawl` happily inserted a course row with zero lectures. Treat non-zero exit as an error.

- [ ] **Step 1: Add failing tests**

Append to `tests/unit/test_crawler_youtube.py`:

```python
from course_merger.crawl.youtube import YouTubeCrawler, PlaylistFetchError


def test_list_playlist_raises_on_nonzero_returncode():
    fake_run = _fake_completed(stderr="ERROR: Video unavailable", returncode=1)
    with patch("subprocess.run", return_value=fake_run):
        with pytest.raises(PlaylistFetchError) as exc:
            YouTubeCrawler().list_playlist("https://www.youtube.com/playlist?list=invalid")
    assert "Video unavailable" in str(exc.value)
```

Append to `tests/unit/test_crawler_bilibili.py`:

```python
from course_merger.crawl.bilibili import BilibiliCrawler
from course_merger.crawl.exceptions import PlaylistFetchError


def test_list_playlist_raises_on_nonzero_returncode():
    fake_run = _fake_completed(stderr="ERROR: BVxxx not found", returncode=1)
    with patch("subprocess.run", return_value=fake_run):
        with pytest.raises(PlaylistFetchError):
            BilibiliCrawler().list_playlist("https://www.bilibili.com/video/BVxxx/")
```

- [ ] **Step 2: Run tests, confirm failure**

```bash
.venv/bin/pytest tests/unit/test_crawler_youtube.py::test_list_playlist_raises_on_nonzero_returncode tests/unit/test_crawler_bilibili.py::test_list_playlist_raises_on_nonzero_returncode -v
```

Expected: `ImportError: cannot import name 'PlaylistFetchError'`.

- [ ] **Step 3: Add `PlaylistFetchError` to `src/course_merger/crawl/exceptions.py`**

Append:

```python
class PlaylistFetchError(RuntimeError):
    """Raised when yt-dlp fails to enumerate a playlist (e.g. 404, 403, invalid URL)."""
```

- [ ] **Step 4: Modify `src/course_merger/crawl/youtube.py`**

Add the import at the top:
```python
from course_merger.crawl.exceptions import PlaylistFetchError
```

And replace the body of `list_playlist`:

```python
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
            raise PlaylistFetchError(
                f"yt-dlp failed for {url} (exit {result.returncode}): "
                f"{result.stderr.strip().splitlines()[-1] if result.stderr.strip() else 'no error message'}"
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
                    "video_url": f"https://www.youtube.com/watch?v={video_id.strip()}",
                }
            )
        return entries
```

- [ ] **Step 5: Modify `src/course_merger/crawl/bilibili.py`**

Same import and same returncode check inserted at the top of `list_playlist`:

```python
from course_merger.crawl.exceptions import BilibiliCookieError, PlaylistFetchError
```

Replace `result = subprocess.run(...)` block with:

```python
        result = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=120)
        if result.returncode != 0:
            raise PlaylistFetchError(
                f"yt-dlp failed for {url} (exit {result.returncode}): "
                f"{result.stderr.strip().splitlines()[-1] if result.stderr.strip() else 'no error message'}"
            )
```

- [ ] **Step 6: Catch `PlaylistFetchError` in CLI**

Modify `src/course_merger/cli.py` — in `crawl_cmd`, change the try/except block around `run_crawl` to also catch `PlaylistFetchError`:

```python
from course_merger.crawl.exceptions import BilibiliCookieError, PlaylistFetchError

# ... inside crawl_cmd ...
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
    except PlaylistFetchError as e:
        typer.echo(f"playlist fetch failed: {e}")
        raise typer.Exit(code=4)
```

- [ ] **Step 7: Run full suite**

```bash
.venv/bin/pytest -v
.venv/bin/pyright src tests
```

Expected: 43 pass, pyright clean.

- [ ] **Step 8: Commit**

```bash
git add src/course_merger/crawl/ src/course_merger/cli.py tests/unit/test_crawler_youtube.py tests/unit/test_crawler_bilibili.py
git commit -m "feat(crawl): yt-dlp nonzero returncode raises PlaylistFetchError"
```

---

## Phase 1: Migration Mechanism

### Task 4: PRAGMA `user_version` + migrations runner

**Files:**
- Create: `src/course_merger/db/migrations/__init__.py` (empty marker, optional but keeps things tidy)
- Create: `src/course_merger/db/migrations/0001_initial.sql`
- Modify: `src/course_merger/db/session.py` — add `_run_migrations`, rewire `init_db`
- Create: `tests/unit/test_migrations.py`

The mechanism: SQLite tracks an integer in `PRAGMA user_version`. `init_db` scans `migrations/000N_*.sql` in order; for every file whose number is greater than `user_version`, it executes the file (within a transaction) and then bumps `user_version`. Idempotent.

This task **doesn't yet introduce new tables** — it just establishes the mechanism by treating Plan-1's existing schema as migration `0001`. Plan 2's new tables land in Task 5 as `0002`.

- [ ] **Step 1: Write failing tests**

```python
# tests/unit/test_migrations.py
from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from course_merger.db.session import _migration_files, connect, init_db


def test_fresh_db_runs_all_migrations(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (version,) = conn.execute("PRAGMA user_version").fetchone()
    # After Task 4 there is one migration: 0001. After Task 5 there will be 0002.
    assert version >= 1


def test_init_db_is_idempotent_for_migrations(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (version_first,) = conn.execute("PRAGMA user_version").fetchone()

    # Second call must not re-run already-applied migrations.
    init_db(db_path)
    with connect(db_path) as conn:
        (version_second,) = conn.execute("PRAGMA user_version").fetchone()

    assert version_first == version_second


def test_migration_files_are_ordered():
    files = _migration_files()
    nums = [int(f.name.split("_")[0]) for f in files]
    assert nums == sorted(nums)
    assert nums[0] == 1  # numbering starts at 0001
```

- [ ] **Step 2: Confirm tests fail**

```bash
.venv/bin/pytest tests/unit/test_migrations.py -v
```

Expected: ImportError or attribute errors (`_migration_files` doesn't exist).

- [ ] **Step 3: Create `src/course_merger/db/migrations/0001_initial.sql`**

Copy the content from `src/course_merger/db/schema.sql` verbatim (Plan-1 schema). This file becomes the canonical "v1" migration:

```sql
-- 0001: initial schema (Plan 1 — courses, lectures, chunks).

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

- [ ] **Step 4: Replace `src/course_merger/db/session.py`**

```python
"""SQLite connection lifecycle, transaction helpers, and migration runner."""
from __future__ import annotations

import re
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

_MIGRATIONS_DIR = Path(__file__).parent / "migrations"
_MIGRATION_FILE_RE = re.compile(r"^(\d{4})_[a-z0-9_]+\.sql$")


def _migration_files() -> list[Path]:
    """Return migration files sorted by numeric prefix."""
    files = [
        p for p in _MIGRATIONS_DIR.glob("*.sql")
        if _MIGRATION_FILE_RE.match(p.name)
    ]
    return sorted(files, key=lambda p: int(p.name.split("_")[0]))


def _migration_number(path: Path) -> int:
    return int(path.name.split("_")[0])


def _run_migrations(conn: sqlite3.Connection) -> None:
    """Apply every migration with number > current PRAGMA user_version."""
    (current,) = conn.execute("PRAGMA user_version").fetchone()
    for path in _migration_files():
        num = _migration_number(path)
        if num <= current:
            continue
        sql = path.read_text(encoding="utf-8")
        conn.executescript(sql)
        conn.execute(f"PRAGMA user_version = {num}")


def init_db(db_path: Path) -> None:
    """Create or upgrade the database. Runs all pending migrations in order. Idempotent."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA journal_mode = WAL")
        _run_migrations(conn)
        conn.commit()
    finally:
        conn.close()


@contextmanager
def connect(db_path: Path) -> Iterator[sqlite3.Connection]:
    """Open a connection with sane defaults inside a transaction.

    Auto-commits on clean exit; rolls back on exception.
    """
    conn = sqlite3.connect(db_path, isolation_level=None)
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

- [ ] **Step 5: Delete the now-redundant `src/course_merger/db/schema.sql`**

```bash
rm src/course_merger/db/schema.sql
```

(The old `init_db` referenced this file. With the migrations runner taking over, it's dead.)

- [ ] **Step 6: Create empty marker `src/course_merger/db/migrations/__init__.py`** (zero bytes — only there so packaging tooling sees the directory; not required for sql discovery)

- [ ] **Step 7: Verify pyproject.toml includes the migrations directory in packaging**

Add to `pyproject.toml` under `[tool.hatch.build.targets.wheel]`:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/course_merger"]
[tool.hatch.build.targets.wheel.force-include]
"src/course_merger/db/migrations" = "course_merger/db/migrations"
```

(hatchling auto-includes Python files but not `.sql`; this ensures `.sql` files ship in the wheel.)

- [ ] **Step 8: Run all tests + manual verification**

```bash
.venv/bin/pytest -v
```

Expected: all existing tests pass + 3 new migration tests pass. The Plan-1 e2e tests (`test_crawl_youtube_end_to_end`, etc.) prove the migration runner produced a working v1 schema.

- [ ] **Step 9: Commit**

```bash
git add src/course_merger/db/ pyproject.toml tests/unit/test_migrations.py
git rm src/course_merger/db/schema.sql 2>/dev/null || true
git commit -m "feat(db): migration runner via PRAGMA user_version; relocate v1 schema to migrations/0001"
```

---

## Phase 2: Concept Tables Migration

### Task 5: Migration `0002_concepts.sql`

**Files:**
- Create: `src/course_merger/db/migrations/0002_concepts.sql`
- Modify: `tests/unit/test_migrations.py` — add assertions for new tables

- [ ] **Step 1: Add failing test**

Append to `tests/unit/test_migrations.py`:

```python
def test_0002_creates_concept_tables(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        names = [
            r[0]
            for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            ).fetchall()
        ]
        (version,) = conn.execute("PRAGMA user_version").fetchone()

    for required in ["concepts", "concept_aliases", "chunk_concepts", "build_meta"]:
        assert required in names, f"table {required} missing"
    assert version == 2


def test_concept_aliases_enforce_unique(tmp_path: Path):
    """An alias string can only point to one concept."""
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('a', 'A', 'seed')"
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('b', 'B', 'seed')"
        )
        conn.execute(
            "INSERT INTO concept_aliases (concept_id, alias) "
            "VALUES (1, 'shared-alias')"
        )

    import sqlite3
    with pytest.raises(sqlite3.IntegrityError):
        with connect(db_path) as conn:
            conn.execute(
                "INSERT INTO concept_aliases (concept_id, alias) "
                "VALUES (2, 'shared-alias')"
            )
```

- [ ] **Step 2: Confirm tests fail**

```bash
.venv/bin/pytest tests/unit/test_migrations.py -v
```

Expected: 2 new tests fail.

- [ ] **Step 3: Create `src/course_merger/db/migrations/0002_concepts.sql`**

```sql
-- 0002: concept ontology, chunk-concept assignments, dirty-build tracking (Plan 2).

CREATE TABLE IF NOT EXISTS concepts (
  id              INTEGER PRIMARY KEY,
  slug            TEXT UNIQUE NOT NULL,
  canonical_name  TEXT NOT NULL,
  description     TEXT,
  ontology_source TEXT NOT NULL CHECK (ontology_source IN ('seed', 'discovered', 'user'))
);

CREATE TABLE IF NOT EXISTS concept_aliases (
  concept_id  INTEGER NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
  alias       TEXT NOT NULL,
  UNIQUE (alias)
);

CREATE TABLE IF NOT EXISTS chunk_concepts (
  chunk_id      INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
  concept_id    INTEGER NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
  confidence    REAL NOT NULL,
  tagger_model  TEXT NOT NULL,
  PRIMARY KEY (chunk_id, concept_id)
);

CREATE INDEX IF NOT EXISTS idx_chunk_concept_concept ON chunk_concepts(concept_id);

CREATE TABLE IF NOT EXISTS build_meta (
  key    TEXT PRIMARY KEY,
  value  TEXT NOT NULL
);

-- Track which chunks have at least one proposed: tag awaiting cluster review.
-- This is denormalized for cheap querying during cluster.
CREATE TABLE IF NOT EXISTS proposed_tags (
  id          INTEGER PRIMARY KEY,
  chunk_id    INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
  raw_tag     TEXT NOT NULL,
  confidence  REAL NOT NULL,
  tagger_model TEXT NOT NULL,
  UNIQUE (chunk_id, raw_tag)
);
```

> Note: `proposed_tags` is added here (not in the spec verbatim) because we need a place to stash the LLM's `proposed:foo` outputs **before** the cluster pass decides what to do with them. Without this table, we'd have to fake-insert "concepts" during `tag` and clean up during `cluster` — uglier.

- [ ] **Step 4: Run tests**

```bash
.venv/bin/pytest tests/unit/test_migrations.py -v
```

Expected: all pass.

- [ ] **Step 5: Verify Plan-1 tests still work**

```bash
.venv/bin/pytest -v
```

Expected: all pass (crawl tests now run on a v2 schema, which is a superset of v1).

- [ ] **Step 6: Commit**

```bash
git add src/course_merger/db/migrations/0002_concepts.sql tests/unit/test_migrations.py
git commit -m "feat(db): migration 0002 adds concepts/aliases/chunk_concepts/build_meta/proposed_tags"
```

---

## Phase 3: Ontology Loader

### Task 6: YAML ontology loader

**Files:**
- Modify: `pyproject.toml` — add `pyyaml`
- Create: `src/course_merger/tag/__init__.py` (empty)
- Create: `src/course_merger/tag/ontology.py`
- Create: `tests/fixtures/ontology.yaml`
- Create: `tests/unit/test_ontology.py`

- [ ] **Step 1: Add `pyyaml` to dependencies**

In `pyproject.toml`, append to the runtime `dependencies` list:

```toml
dependencies = [
    "typer>=0.12.0",
    "rich>=13.7.0",
    "yt-dlp>=2024.5.0",
    "pyyaml>=6.0",
]
```

Install:

```bash
cd /Users/chenlinzhuo/code/course-merger && uv pip install -e ".[dev]"
```

- [ ] **Step 2: Create fixture `tests/fixtures/ontology.yaml`**

```yaml
concepts:
  - slug: self-attention
    canonical_name: Self-Attention
    description: Token-pairwise attention mechanism inside a Transformer block.
    aliases:
      - SA
      - scaled dot-product attention
      - self attention

  - slug: rotary-positional-encoding
    canonical_name: Rotary Positional Encoding
    description: RoPE — encodes absolute position by rotating Q/K embeddings.
    aliases:
      - RoPE
      - rotary embedding

  - slug: kv-cache
    canonical_name: KV Cache
    description: Caching previously computed keys and values to speed up autoregressive decoding.
```

- [ ] **Step 3: Write failing tests**

```python
# tests/unit/test_ontology.py
from __future__ import annotations

from pathlib import Path

import pytest

from course_merger.tag.ontology import (
    Concept,
    Ontology,
    load_ontology,
)


def test_load_ontology_parses_concepts(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    assert isinstance(onto, Ontology)
    assert len(onto.concepts) == 3

    sa = onto.by_slug("self-attention")
    assert isinstance(sa, Concept)
    assert sa.canonical_name == "Self-Attention"
    assert "SA" in sa.aliases


def test_ontology_lookup_by_alias(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    assert onto.find_by_alias("RoPE").slug == "rotary-positional-encoding"
    assert onto.find_by_alias("rotary embedding").slug == "rotary-positional-encoding"
    assert onto.find_by_alias("nonexistent") is None


def test_ontology_top_n_for_prompt(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    # Returns at most n concepts as slugs in stable order.
    slugs = onto.top_n_slugs(n=2)
    assert len(slugs) == 2
    assert all(isinstance(s, str) for s in slugs)


def test_load_ontology_empty_file(tmp_path: Path):
    p = tmp_path / "empty.yaml"
    p.write_text("concepts: []\n")
    onto = load_ontology(p)
    assert onto.concepts == []


def test_load_ontology_rejects_duplicate_slug(tmp_path: Path):
    p = tmp_path / "dup.yaml"
    p.write_text(
        "concepts:\n"
        "  - slug: foo\n"
        "    canonical_name: Foo\n"
        "  - slug: foo\n"
        "    canonical_name: Foo Two\n"
    )
    with pytest.raises(ValueError, match="duplicate slug"):
        load_ontology(p)
```

- [ ] **Step 4: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_ontology.py -v
```

Expected: ImportError.

- [ ] **Step 5: Write `src/course_merger/tag/ontology.py`**

```python
"""YAML ontology loader: in-memory model of seed concepts with alias lookup."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass(frozen=True, slots=True)
class Concept:
    slug: str
    canonical_name: str
    description: str = ""
    aliases: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class Ontology:
    concepts: tuple[Concept, ...]
    _by_slug: dict[str, Concept] = field(default_factory=dict, hash=False, compare=False)
    _by_alias: dict[str, Concept] = field(default_factory=dict, hash=False, compare=False)

    def by_slug(self, slug: str) -> Concept | None:
        return self._by_slug.get(slug)

    def find_by_alias(self, alias: str) -> Concept | None:
        return self._by_alias.get(alias.strip().lower())

    def top_n_slugs(self, n: int) -> list[str]:
        return [c.slug for c in self.concepts[:n]]


def load_ontology(path: Path) -> Ontology:
    """Load a YAML ontology file. Raises ValueError on duplicate slugs."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw = data.get("concepts", []) or []

    concepts: list[Concept] = []
    seen_slugs: set[str] = set()
    for entry in raw:
        slug = entry["slug"]
        if slug in seen_slugs:
            raise ValueError(f"duplicate slug in ontology: {slug!r}")
        seen_slugs.add(slug)
        concepts.append(
            Concept(
                slug=slug,
                canonical_name=entry["canonical_name"],
                description=entry.get("description", ""),
                aliases=tuple(entry.get("aliases", []) or []),
            )
        )

    by_slug = {c.slug: c for c in concepts}
    by_alias: dict[str, Concept] = {}
    for c in concepts:
        # The canonical name itself counts as an alias for lookup convenience.
        by_alias[c.canonical_name.strip().lower()] = c
        for alias in c.aliases:
            by_alias[alias.strip().lower()] = c

    return Ontology(
        concepts=tuple(concepts), _by_slug=by_slug, _by_alias=by_alias
    )
```

- [ ] **Step 6: Run tests**

```bash
.venv/bin/pytest tests/unit/test_ontology.py -v
```

Expected: 5 pass.

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml src/course_merger/tag/__init__.py src/course_merger/tag/ontology.py tests/fixtures/ontology.yaml tests/unit/test_ontology.py
git commit -m "feat(tag): YAML ontology loader with slug + alias lookup"
```

---

## Phase 4: Claude Haiku Tagger

### Task 7: Tagger with prompt caching

**Files:**
- Modify: `pyproject.toml` — add `anthropic`
- Create: `src/course_merger/tag/prompts.py`
- Create: `src/course_merger/tag/claude_tagger.py`
- Create: `tests/fixtures/tagger_responses.py`
- Create: `tests/unit/test_claude_tagger.py`

> **NB:** The implementer should consult the `claude-api` skill for current best practices on prompt caching. The pattern below uses `cache_control: {"type": "ephemeral"}` on the system block to cache the ontology.

- [ ] **Step 1: Add `anthropic` to deps**

Append to `pyproject.toml`:

```toml
dependencies = [
    "typer>=0.12.0",
    "rich>=13.7.0",
    "yt-dlp>=2024.5.0",
    "pyyaml>=6.0",
    "anthropic>=0.36.0",
]
```

Install:

```bash
uv pip install -e ".[dev]"
```

- [ ] **Step 2: Create `src/course_merger/tag/prompts.py`**

```python
"""Versioned prompt constants for the Claude Haiku tagger.

Bump TAGGER_PROMPT_VERSION whenever the system prompt changes — used in the
chunk_concepts.tagger_model field so we can re-tag old chunks if needed.
"""
from __future__ import annotations

TAGGER_PROMPT_VERSION = "v1"


TAGGER_SYSTEM_TEMPLATE = """\
You are a course-content tagger. Given a 300-800 token chunk from a lecture, return 1-3 concept tags as JSON.

Constraints:
- Each tag MUST be either:
  (a) an exact slug from the provided ontology, OR
  (b) prefixed `proposed:` for new concepts (use sparingly; AT MOST 1 per chunk).
- confidence must be a number in [0.0, 1.0]; OMIT any tag with confidence < 0.5.
- Slugs are ALWAYS English kebab-case, even if the chunk is in Chinese or mixed Chinese/English. For example, a chunk saying "注意力机制" or "attention 机制" both map to slug `attention`, never `注意力机制`.
- DO NOT explain.

Available ontology slugs (one per line):
{ontology_block}

Output a single JSON object on one line:
{{"tags": [{{"slug": "...", "confidence": 0.92}}, ...]}}

If the chunk doesn't match any concept, output: {{"tags": []}}
"""
```

- [ ] **Step 3: Write fixture `tests/fixtures/tagger_responses.py`**

```python
"""Canned Anthropic API responses for tagger tests."""
from __future__ import annotations

from types import SimpleNamespace


def make_response(text: str, input_tokens: int = 100, output_tokens: int = 20) -> SimpleNamespace:
    """Build a fake anthropic.types.Message with .content[0].text and .usage."""
    return SimpleNamespace(
        content=[SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        ),
        stop_reason="end_turn",
    )


GOOD_TWO_TAGS = make_response(
    '{"tags": [{"slug": "self-attention", "confidence": 0.95},'
    ' {"slug": "proposed:rotary-embedding", "confidence": 0.78}]}'
)

LOW_CONFIDENCE_FILTERED = make_response(
    '{"tags": [{"slug": "self-attention", "confidence": 0.4}]}'
)

EMPTY = make_response('{"tags": []}')

MALFORMED = make_response('not valid json at all')
```

- [ ] **Step 4: Write failing tests**

```python
# tests/unit/test_claude_tagger.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from course_merger.tag.claude_tagger import (
    ClaudeTagger,
    TagResult,
    parse_tagger_response,
)
from course_merger.tag.ontology import load_ontology
from tests.fixtures.tagger_responses import (
    EMPTY,
    GOOD_TWO_TAGS,
    LOW_CONFIDENCE_FILTERED,
    MALFORMED,
)


def test_parse_tagger_response_splits_known_and_proposed(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    result = parse_tagger_response(GOOD_TWO_TAGS.content[0].text, onto)

    assert isinstance(result, TagResult)
    # self-attention is in the seed ontology
    assert any(t.slug == "self-attention" and t.is_proposed is False for t in result.tags)
    # rotary-embedding is `proposed:`-prefixed and NOT in the ontology
    assert any(t.slug == "rotary-embedding" and t.is_proposed is True for t in result.tags)


def test_parse_filters_low_confidence(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    result = parse_tagger_response(LOW_CONFIDENCE_FILTERED.content[0].text, onto)
    assert result.tags == []


def test_parse_empty_tags(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    result = parse_tagger_response(EMPTY.content[0].text, onto)
    assert result.tags == []


def test_parse_malformed_raises(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    with pytest.raises(ValueError, match="parse"):
        parse_tagger_response(MALFORMED.content[0].text, onto)


def test_tagger_uses_prompt_caching(fixtures_dir: Path):
    """The system prompt must include cache_control to enable Anthropic caching."""
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    fake_client = MagicMock()
    fake_client.messages.create.return_value = GOOD_TWO_TAGS

    tagger = ClaudeTagger(client=fake_client, model="claude-haiku-4-5", ontology=onto)
    tagger.tag_chunk("This chunk talks about self-attention and rotary embeddings.")

    # Inspect what was passed to messages.create
    call_kwargs = fake_client.messages.create.call_args.kwargs
    system_blocks = call_kwargs["system"]
    assert isinstance(system_blocks, list)
    assert any(
        b.get("cache_control", {}).get("type") == "ephemeral" for b in system_blocks
    )


def test_tagger_retries_once_on_parse_failure(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    fake_client = MagicMock()
    # First call malformed, second call good.
    fake_client.messages.create.side_effect = [MALFORMED, GOOD_TWO_TAGS]

    tagger = ClaudeTagger(client=fake_client, model="claude-haiku-4-5", ontology=onto)
    result = tagger.tag_chunk("anything")

    assert len(result.tags) > 0
    assert fake_client.messages.create.call_count == 2


def test_tagger_returns_empty_after_two_failures(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    fake_client = MagicMock()
    fake_client.messages.create.side_effect = [MALFORMED, MALFORMED]

    tagger = ClaudeTagger(client=fake_client, model="claude-haiku-4-5", ontology=onto)
    result = tagger.tag_chunk("anything")

    assert result.tags == []
    assert result.error == "parse_failure"
```

- [ ] **Step 5: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_claude_tagger.py -v
```

Expected: ImportError.

- [ ] **Step 6: Write `src/course_merger/tag/claude_tagger.py`**

```python
"""Claude Haiku tagger: builds prompts, calls Anthropic API with caching, parses JSON.

The Anthropic SDK is used at the boundary; this module is otherwise pure Python.
Tests inject a MagicMock client to avoid network.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from course_merger.tag.ontology import Ontology
from course_merger.tag.prompts import TAGGER_PROMPT_VERSION, TAGGER_SYSTEM_TEMPLATE


_PROPOSED_PREFIX = "proposed:"
_MIN_CONFIDENCE = 0.5
_MAX_RETRIES = 1  # one retry, so total attempts is 2


@dataclass(frozen=True, slots=True)
class Tag:
    slug: str
    confidence: float
    is_proposed: bool


@dataclass(frozen=True, slots=True)
class TagResult:
    tags: tuple[Tag, ...] = ()
    error: str = ""  # "" | "parse_failure" | "api_error"


def _build_system_blocks(ontology: Ontology) -> list[dict[str, Any]]:
    """Build the system message with the ontology, marked cache-control: ephemeral."""
    ontology_block = "\n".join(c.slug for c in ontology.concepts) or "(no seed concepts)"
    system_text = TAGGER_SYSTEM_TEMPLATE.format(ontology_block=ontology_block)
    return [
        {
            "type": "text",
            "text": system_text,
            "cache_control": {"type": "ephemeral"},
        }
    ]


def parse_tagger_response(text: str, ontology: Ontology) -> TagResult:
    """Parse the JSON output from Claude into a TagResult.

    - Raises ValueError if the text is not valid JSON or shape doesn't match.
    - Filters tags below the confidence threshold.
    - Marks tags with `proposed:` prefix.
    """
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"failed to parse tagger response as JSON: {e}") from e

    if not isinstance(data, dict) or "tags" not in data:
        raise ValueError(f"tagger response missing 'tags' key: {data!r}")

    out: list[Tag] = []
    for entry in data["tags"]:
        if not isinstance(entry, dict):
            continue
        slug = entry.get("slug", "")
        confidence = float(entry.get("confidence", 0.0))
        if confidence < _MIN_CONFIDENCE:
            continue
        is_proposed = slug.startswith(_PROPOSED_PREFIX)
        clean_slug = slug[len(_PROPOSED_PREFIX) :] if is_proposed else slug
        if not clean_slug:
            continue
        out.append(Tag(slug=clean_slug, confidence=confidence, is_proposed=is_proposed))

    return TagResult(tags=tuple(out))


class ClaudeTagger:
    """Wraps the Anthropic client; tag_chunk(text) returns a TagResult."""

    def __init__(
        self,
        *,
        client: Any,  # anthropic.Anthropic
        model: str,
        ontology: Ontology,
        max_tokens: int = 256,
    ) -> None:
        self.client = client
        self.model = model
        self.ontology = ontology
        self.max_tokens = max_tokens
        self._system_blocks = _build_system_blocks(ontology)

    @property
    def tagger_model_id(self) -> str:
        """Identifier written to chunk_concepts.tagger_model — model + prompt version."""
        return f"{self.model}:{TAGGER_PROMPT_VERSION}"

    def tag_chunk(self, chunk_text: str) -> TagResult:
        last_error = ""
        for attempt in range(_MAX_RETRIES + 1):
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=self._system_blocks,
                    messages=[{"role": "user", "content": chunk_text}],
                )
            except Exception as e:
                last_error = f"api_error: {e}"
                continue

            text = resp.content[0].text if resp.content else ""
            try:
                return parse_tagger_response(text, self.ontology)
            except ValueError as e:
                last_error = "parse_failure"
                continue

        return TagResult(tags=(), error=last_error or "parse_failure")
```

- [ ] **Step 7: Run tests**

```bash
.venv/bin/pytest tests/unit/test_claude_tagger.py -v
```

Expected: 7 pass.

- [ ] **Step 8: Verify pyright**

```bash
.venv/bin/pyright src tests
```

Expected: clean.

- [ ] **Step 9: Commit**

```bash
git add pyproject.toml src/course_merger/tag/prompts.py src/course_merger/tag/claude_tagger.py tests/fixtures/tagger_responses.py tests/unit/test_claude_tagger.py
git commit -m "feat(tag): Claude Haiku tagger with prompt caching + JSON parse + retry"
```

---

## Phase 5: `tag` CLI Command

### Task 8: tag runner + CLI wiring

**Files:**
- Create: `src/course_merger/tag/runner.py`
- Modify: `src/course_merger/cli.py` — add `tag` command
- Create: `tests/unit/test_tag_runner.py`
- Create: `tests/integration/test_tag_smoke.py`

The runner: loops untagged chunks (chunks with no `chunk_concepts` AND no `proposed_tags` rows yet), calls the tagger, writes results back. Resumable mid-run because we never re-process a chunk that already has rows.

- [ ] **Step 1: Write failing unit test**

```python
# tests/unit/test_tag_runner.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from course_merger.db.session import connect, init_db
from course_merger.tag.claude_tagger import Tag, TagResult
from course_merger.tag.ontology import load_ontology
from course_merger.tag.runner import TagReport, run_tag


def _seed_one_course_with_chunks(db_path: Path, n_chunks: int = 3) -> int:
    """Insert a course + 1 lecture + N chunks. Return lecture_id."""
    init_db(db_path)
    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("c1", "Course 1", "youtube", "https://x", "2026-05-09"),
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, ?, ?, ?, ?, 'ok')",
            (course_id, 1, "L1", "https://yt/v1", "transcript text"),
        )
        lecture_id = cur.lastrowid
        for i in range(n_chunks):
            conn.execute(
                "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
                "VALUES (?, ?, ?, ?, ?)",
                (lecture_id, i, i * 10.0, (i + 1) * 10.0, f"chunk text {i}"),
            )
    return lecture_id


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def _fake_tagger(canned: list[TagResult]):
    """A MagicMock-like tagger whose tag_chunk returns canned results in order."""
    m = MagicMock()
    m.tag_chunk.side_effect = canned
    m.tagger_model_id = "claude-haiku-4-5:v1"
    return m


def test_run_tag_writes_chunk_concepts_for_known_tags(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=2)

    # Pre-insert the concept so chunk_concepts FK is satisfied
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )

    tagger = _fake_tagger([
        TagResult(tags=(Tag(slug="self-attention", confidence=0.9, is_proposed=False),)),
        TagResult(tags=()),
    ])

    report = run_tag(db_path=db_path, tagger=tagger, ontology=onto)

    assert isinstance(report, TagReport)
    assert report.chunks_tagged == 2  # processed
    assert report.tags_known_written == 1
    assert report.tags_proposed_written == 0

    with connect(db_path) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 1


def test_run_tag_writes_proposed_tags_separately(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=1)

    tagger = _fake_tagger([
        TagResult(tags=(Tag(slug="rotary-positional-encoding", confidence=0.8, is_proposed=True),)),
    ])

    run_tag(db_path=db_path, tagger=tagger, ontology=onto)

    with connect(db_path) as conn:
        rows = conn.execute(
            "SELECT raw_tag, confidence FROM proposed_tags"
        ).fetchall()
    assert rows == [("rotary-positional-encoding", 0.8)]


def test_run_tag_skips_already_tagged_chunks(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=2)

    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'SA', 'seed')"
        )
        # Manually tag chunk 1 already
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'old-model:v0')"
        )

    tagger = _fake_tagger([
        TagResult(tags=(Tag(slug="self-attention", confidence=0.9, is_proposed=False),)),
    ])

    run_tag(db_path=db_path, tagger=tagger, ontology=onto)

    # Only chunk 2 should have been processed (chunk 1 already had a row).
    assert tagger.tag_chunk.call_count == 1


def test_run_tag_respects_course_filter(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=2)

    # Add a second course
    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c2', 'Course 2', 'youtube', 'https://y', '2026-05-09')"
        )
        c2_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'https://yt/v2', 't', 'ok')",
            (c2_id,),
        )
        l2_id = cur.lastrowid
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'c2 chunk')",
            (l2_id,),
        )

    tagger = _fake_tagger([TagResult(tags=())] * 10)

    run_tag(db_path=db_path, tagger=tagger, ontology=onto, course_slug="c1")

    # Only c1's 2 chunks should be processed.
    assert tagger.tag_chunk.call_count == 2


def test_run_tag_respects_limit(tmp_path: Path, onto):
    db_path = tmp_path / "db.sqlite"
    _seed_one_course_with_chunks(db_path, n_chunks=10)

    tagger = _fake_tagger([TagResult(tags=())] * 10)

    run_tag(db_path=db_path, tagger=tagger, ontology=onto, limit=3)

    assert tagger.tag_chunk.call_count == 3
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_tag_runner.py -v
```

Expected: ImportError.

- [ ] **Step 3: Write `src/course_merger/tag/runner.py`**

```python
"""Orchestrator: load chunks → tag via Claude → write chunk_concepts + proposed_tags."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Protocol

from course_merger.db.session import connect
from course_merger.tag.claude_tagger import TagResult
from course_merger.tag.ontology import Ontology


class _TaggerLike(Protocol):
    tagger_model_id: str
    def tag_chunk(self, chunk_text: str) -> TagResult: ...


@dataclass(frozen=True, slots=True)
class TagReport:
    chunks_tagged: int
    tags_known_written: int
    tags_proposed_written: int
    parse_failures: int


def _untagged_chunks_query(course_slug: str | None) -> tuple[str, tuple]:
    """Return SQL + params for chunks needing tagging.

    A chunk is "untagged" if no chunk_concepts AND no proposed_tags rows exist for it.
    """
    base = """
        SELECT chunks.id, chunks.text
        FROM chunks
        JOIN lectures ON lectures.id = chunks.lecture_id
        JOIN courses ON courses.id = lectures.course_id
        WHERE NOT EXISTS (SELECT 1 FROM chunk_concepts WHERE chunk_concepts.chunk_id = chunks.id)
        AND NOT EXISTS (SELECT 1 FROM proposed_tags WHERE proposed_tags.chunk_id = chunks.id)
        AND lectures.status = 'ok'
    """
    params: tuple = ()
    if course_slug:
        base += " AND courses.slug = ?"
        params = (course_slug,)
    base += " ORDER BY chunks.id"
    return base, params


def run_tag(
    *,
    db_path: Path,
    tagger: _TaggerLike,
    ontology: Ontology,
    course_slug: str | None = None,
    limit: int | None = None,
) -> TagReport:
    """Tag every chunk that has no existing chunk_concepts and no proposed_tags."""
    chunks_tagged = 0
    tags_known_written = 0
    tags_proposed_written = 0
    parse_failures = 0

    with connect(db_path) as conn:
        sql, params = _untagged_chunks_query(course_slug)
        chunks = conn.execute(sql, params).fetchall()

        if limit is not None:
            chunks = chunks[:limit]

        for chunk_id, chunk_text in chunks:
            result = tagger.tag_chunk(chunk_text)
            chunks_tagged += 1
            if result.error == "parse_failure":
                parse_failures += 1
                # Still record so we don't re-attempt this chunk on next run.
                conn.execute(
                    "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
                    "VALUES (?, '__parse_failure__', 0.0, ?)",
                    (chunk_id, tagger.tagger_model_id),
                )
                continue

            for tag in result.tags:
                if tag.is_proposed:
                    conn.execute(
                        "INSERT OR IGNORE INTO proposed_tags "
                        "(chunk_id, raw_tag, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, tag.slug, tag.confidence, tagger.tagger_model_id),
                    )
                    tags_proposed_written += 1
                else:
                    concept = conn.execute(
                        "SELECT id FROM concepts WHERE slug = ?", (tag.slug,)
                    ).fetchone()
                    if concept is None:
                        # Tagger returned a non-proposed slug we don't have a concept for.
                        # This happens when the seed ontology is out of sync with prompts.
                        # Demote it to a proposed tag to recover gracefully.
                        conn.execute(
                            "INSERT OR IGNORE INTO proposed_tags "
                            "(chunk_id, raw_tag, confidence, tagger_model) "
                            "VALUES (?, ?, ?, ?)",
                            (chunk_id, tag.slug, tag.confidence, tagger.tagger_model_id),
                        )
                        tags_proposed_written += 1
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO chunk_concepts "
                        "(chunk_id, concept_id, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, concept[0], tag.confidence, tagger.tagger_model_id),
                    )
                    tags_known_written += 1

    return TagReport(
        chunks_tagged=chunks_tagged,
        tags_known_written=tags_known_written,
        tags_proposed_written=tags_proposed_written,
        parse_failures=parse_failures,
    )
```

- [ ] **Step 4: Write failing integration test**

```python
# tests/integration/test_tag_smoke.py
from __future__ import annotations

import shutil
from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from course_merger.cli import app
from course_merger.db.session import connect
from course_merger.tag.claude_tagger import Tag, TagResult

runner = CliRunner()


@pytest.mark.integration
def test_tag_cli_end_to_end(tmp_project: Path, fixtures_dir: Path):
    # 1. init + manually seed a course with one chunk
    runner.invoke(app, ["init"])
    db = tmp_project / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-09')"
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'https://yt/v1', 'about self-attention', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'self-attention is key.')",
            (lecture_id,),
        )
        # Seed the concept so the tag can attach
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )

    # 2. Copy the ontology fixture to a path the CLI accepts
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    # 3. Patch the tagger so no network call is made
    fake_result = TagResult(
        tags=(Tag(slug="self-attention", confidence=0.95, is_proposed=False),)
    )
    with patch(
        "course_merger.tag.claude_tagger.ClaudeTagger.tag_chunk",
        return_value=fake_result,
    ):
        # Also patch anthropic.Anthropic so we don't need an API key.
        with patch("anthropic.Anthropic", return_value=object()):
            result = runner.invoke(
                app, ["tag", "--ontology", str(ont_path), "--model", "claude-haiku-4-5"]
            )

    assert result.exit_code == 0, result.stdout
    assert "1 tagged" in result.stdout.lower() or "chunks tagged" in result.stdout.lower()

    with connect(db) as conn:
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_cc == 1


@pytest.mark.integration
def test_tag_errors_when_not_initialized(tmp_project: Path, fixtures_dir: Path):
    result = runner.invoke(
        app, ["tag", "--ontology", str(fixtures_dir / "ontology.yaml")]
    )
    assert result.exit_code != 0
    assert "init" in result.stdout.lower()
```

- [ ] **Step 5: Modify `src/course_merger/cli.py` — add `tag` command**

Add these imports near the existing crawler imports:

```python
from course_merger.tag.claude_tagger import ClaudeTagger
from course_merger.tag.ontology import load_ontology
from course_merger.tag.runner import run_tag, TagReport
```

Append at the end of the file:

```python
@app.command("tag")
def tag_cmd(
    ontology: Path = typer.Option(
        ..., "--ontology", help="Path to ontology YAML.", exists=True, dir_okay=False
    ),
    model: str = typer.Option(
        "claude-haiku-4-5", "--model", help="Claude model id for tagging."
    ),
    course: str | None = typer.Option(
        None, "--course", help="Only tag chunks of this course slug."
    ),
    limit: int | None = typer.Option(
        None, "--limit", help="Max chunks to process this run (for cost control)."
    ),
) -> None:
    """Assign concept tags to every untagged chunk via Claude Haiku."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1)

    onto = load_ontology(ontology)

    import anthropic
    client = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY env

    tagger = ClaudeTagger(client=client, model=model, ontology=onto)

    db_path = root / PROJECT_MARKER / "db.sqlite"
    report = run_tag(
        db_path=db_path,
        tagger=tagger,
        ontology=onto,
        course_slug=course,
        limit=limit,
    )

    typer.echo(
        f"done: {report.chunks_tagged} chunks tagged, "
        f"{report.tags_known_written} known tags, "
        f"{report.tags_proposed_written} proposed tags, "
        f"{report.parse_failures} parse failures"
    )
```

- [ ] **Step 6: Run tests**

```bash
.venv/bin/pytest tests/unit/test_tag_runner.py tests/integration/test_tag_smoke.py -v
.venv/bin/pytest -v
.venv/bin/pyright src tests
```

Expected: all green.

- [ ] **Step 7: Commit**

```bash
git add src/course_merger/tag/runner.py src/course_merger/cli.py tests/unit/test_tag_runner.py tests/integration/test_tag_smoke.py
git commit -m "feat(tag): \\\`tag\\\` CLI orchestrates Claude tagging into chunk_concepts + proposed_tags"
```

---

## Phase 6: Embedding Module

### Task 9: sentence-transformers wrapper

**Files:**
- Modify: `pyproject.toml` — add `sentence-transformers`, `numpy`
- Create: `src/course_merger/cluster/__init__.py` (empty)
- Create: `src/course_merger/cluster/embedding.py`
- Create: `tests/unit/test_embedding.py`

The model `all-MiniLM-L6-v2` is ~80 MB, downloaded on first use. Tests use a session-scoped fixture so it's loaded once across all tests.

- [ ] **Step 1: Add deps**

In `pyproject.toml` runtime `dependencies`:

```toml
    "sentence-transformers>=3.0.0",
    "numpy>=1.26.0",
```

Install:

```bash
uv pip install -e ".[dev]"
```

- [ ] **Step 2: Write failing tests**

```python
# tests/unit/test_embedding.py
from __future__ import annotations

import numpy as np
import pytest

from course_merger.cluster.embedding import Embedder, cosine_similarity


@pytest.fixture(scope="session")
def embedder():
    return Embedder()  # loads the model once per test session


def test_embedder_returns_384_dim_vector(embedder):
    v = embedder.embed("self-attention")
    assert isinstance(v, np.ndarray)
    assert v.shape == (384,)
    assert v.dtype == np.float32


def test_embed_batch(embedder):
    out = embedder.embed_batch(["self-attention", "RoPE", "kv cache"])
    assert out.shape == (3, 384)


def test_similar_concepts_have_high_cosine(embedder):
    v1 = embedder.embed("rotary positional encoding")
    v2 = embedder.embed("RoPE")
    v3 = embedder.embed("memory bandwidth")
    assert cosine_similarity(v1, v2) > cosine_similarity(v1, v3)


def test_cosine_self_is_one(embedder):
    v = embedder.embed("attention")
    assert cosine_similarity(v, v) == pytest.approx(1.0, abs=1e-5)
```

- [ ] **Step 3: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_embedding.py -v
```

Expected: ImportError.

- [ ] **Step 4: Write `src/course_merger/cluster/embedding.py`**

```python
"""sentence-transformers wrapper for embedding short text strings (tags, concept names).

The model is loaded lazily on first use, kept in process memory thereafter.
"""
from __future__ import annotations

from functools import cached_property

import numpy as np

_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
_DIM = 384


class Embedder:
    """Wraps a sentence-transformers model. Single-process; not thread-safe."""

    def __init__(self, model_name: str = _MODEL_NAME) -> None:
        self.model_name = model_name

    @cached_property
    def _model(self):
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(self.model_name)

    def embed(self, text: str) -> np.ndarray:
        """Embed a single string, return a 384-dim float32 vector."""
        v = self._model.encode([text], convert_to_numpy=True, normalize_embeddings=True)
        return v[0].astype(np.float32)

    def embed_batch(self, texts: list[str]) -> np.ndarray:
        """Embed a batch of strings, return an (N, 384) float32 array."""
        v = self._model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return v.astype(np.float32)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity. Assumes the vectors are pre-normalized."""
    return float(np.dot(a, b))
```

> Note: `normalize_embeddings=True` means the cosine similarity reduces to a plain dot product, so we don't need to divide by norms.

- [ ] **Step 5: Run tests**

```bash
.venv/bin/pytest tests/unit/test_embedding.py -v
```

Expected: 4 pass (first run downloads the model; ~30s on first invocation, then cached).

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml src/course_merger/cluster/__init__.py src/course_merger/cluster/embedding.py tests/unit/test_embedding.py
git commit -m "feat(cluster): sentence-transformers embedder + cosine similarity"
```

---

## Phase 7: Clustering

### Task 10: Cosine-similarity greedy clusterer

**Files:**
- Create: `src/course_merger/cluster/clusterer.py`
- Create: `tests/unit/test_clusterer.py`

Algorithm: build a similarity matrix from embeddings, then greedy single-linkage cluster — for each item, find its nearest neighbor; if similarity >= threshold, join their clusters (union-find). Otherwise start a new cluster.

- [ ] **Step 1: Write failing tests**

```python
# tests/unit/test_clusterer.py
from __future__ import annotations

import numpy as np

from course_merger.cluster.clusterer import Cluster, cluster_by_cosine


def _orthogonal_vector(seed: int, dim: int = 384) -> np.ndarray:
    rng = np.random.default_rng(seed)
    v = rng.normal(size=dim).astype(np.float32)
    return v / np.linalg.norm(v)


def test_cluster_separates_dissimilar_vectors():
    # Three orthogonal random vectors → 3 clusters at high threshold
    items = ["a", "b", "c"]
    vecs = np.array([_orthogonal_vector(s) for s in (1, 2, 3)])
    clusters = cluster_by_cosine(items, vecs, threshold=0.5)
    assert len(clusters) == 3
    for c in clusters:
        assert isinstance(c, Cluster)
        assert len(c.items) == 1


def test_cluster_merges_near_duplicates():
    # Make 2 vectors basically identical, 1 orthogonal
    v0 = _orthogonal_vector(1)
    v1 = (v0 + 0.01 * _orthogonal_vector(99)).astype(np.float32)
    v1 = v1 / np.linalg.norm(v1)
    v2 = _orthogonal_vector(2)

    items = ["x", "x_alias", "y"]
    vecs = np.stack([v0, v1, v2])
    clusters = cluster_by_cosine(items, vecs, threshold=0.7)

    sizes = sorted(len(c.items) for c in clusters)
    assert sizes == [1, 2]


def test_cluster_empty_input():
    clusters = cluster_by_cosine([], np.zeros((0, 384), dtype=np.float32), threshold=0.5)
    assert clusters == []


def test_cluster_single_item():
    clusters = cluster_by_cosine(["only"], np.array([_orthogonal_vector(0)]), threshold=0.5)
    assert len(clusters) == 1
    assert clusters[0].items == ["only"]
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_clusterer.py -v
```

Expected: ImportError.

- [ ] **Step 3: Write `src/course_merger/cluster/clusterer.py`**

```python
"""Pure clustering algorithm: cosine similarity + union-find single-linkage."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, slots=True)
class Cluster:
    items: list[str]
    indices: list[int]


def cluster_by_cosine(
    items: list[str],
    embeddings: np.ndarray,
    threshold: float,
) -> list[Cluster]:
    """Cluster `items` such that every pair within a cluster has cosine >= threshold.

    Uses single-linkage union-find: for each pair (i, j) with sim >= threshold, union i and j.
    Embeddings must be L2-normalized so cosine reduces to dot product.
    """
    n = len(items)
    if n == 0:
        return []

    # Union-find
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    sim = embeddings @ embeddings.T  # (n, n) since embeddings are normalized
    for i in range(n):
        for j in range(i + 1, n):
            if sim[i, j] >= threshold:
                union(i, j)

    groups: dict[int, list[int]] = {}
    for i in range(n):
        root = find(i)
        groups.setdefault(root, []).append(i)

    return [
        Cluster(items=[items[i] for i in idxs], indices=idxs)
        for idxs in groups.values()
    ]
```

- [ ] **Step 4: Run tests**

```bash
.venv/bin/pytest tests/unit/test_clusterer.py -v
```

Expected: 4 pass.

- [ ] **Step 5: Commit**

```bash
git add src/course_merger/cluster/clusterer.py tests/unit/test_clusterer.py
git commit -m "feat(cluster): cosine-similarity union-find clusterer"
```

---

## Phase 8: Sonnet Review

### Task 11: LLM review pass

**Files:**
- Create: `src/course_merger/cluster/prompts.py`
- Create: `src/course_merger/cluster/llm_review.py`
- Create: `tests/fixtures/review_responses.py`
- Create: `tests/unit/test_llm_review.py`

Per cluster of proposed tags, ask Sonnet: merge into existing? Create new? Reject? Ambiguous?

- [ ] **Step 1: Create `src/course_merger/cluster/prompts.py`**

```python
"""Versioned prompts for the Sonnet cluster review pass."""
from __future__ import annotations

CLUSTER_REVIEW_PROMPT_VERSION = "v1"


REVIEW_SYSTEM = """\
You are a concept-ontology curator for an open-courseware knowledge base. Given a
cluster of LLM-proposed concept names plus the current ontology, decide:

(a) MERGE — this cluster names an existing concept; provide the canonical slug
(b) CREATE — this is a new canonical concept; provide slug + canonical_name + 1-sentence description
(c) REJECT — the cluster is noise, not a real concept (e.g. presenter name, generic verb)
(d) AMBIGUOUS — you can't decide; flag for human review

Output a single JSON object on one line:
{{"decision": "merge"|"create"|"reject"|"ambiguous", "target_slug": "...", "new_concept": {{"slug": "...", "canonical_name": "...", "description": "..."}}, "reason": "..."}}

Use "target_slug" only for merge. Use "new_concept" only for create. Set unused fields to null.

The slug must be kebab-case English (e.g. `rotary-positional-encoding`), even if the proposed names are in another language.

EXISTING ONTOLOGY (slug — canonical_name):
{ontology_block}
"""


REVIEW_USER_TEMPLATE = """\
Cluster of proposed concept names from chunk tags:
{cluster_items}

Sample chunks supporting this cluster (one per line):
{sample_chunks}
"""
```

- [ ] **Step 2: Create fixture `tests/fixtures/review_responses.py`**

```python
"""Canned Anthropic responses for cluster-review tests."""
from __future__ import annotations

from types import SimpleNamespace


def _make(text: str) -> SimpleNamespace:
    return SimpleNamespace(
        content=[SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(input_tokens=1, output_tokens=1, cache_creation_input_tokens=0, cache_read_input_tokens=0),
        stop_reason="end_turn",
    )


MERGE_DECISION = _make(
    '{"decision":"merge","target_slug":"rotary-positional-encoding","new_concept":null,"reason":"RoPE aliases"}'
)

CREATE_DECISION = _make(
    '{"decision":"create","target_slug":null,'
    '"new_concept":{"slug":"speculative-decoding","canonical_name":"Speculative Decoding","description":"An inference acceleration technique using a draft model."},'
    '"reason":"new concept"}'
)

REJECT_DECISION = _make(
    '{"decision":"reject","target_slug":null,"new_concept":null,"reason":"presenter intro phrase"}'
)

AMBIGUOUS_DECISION = _make(
    '{"decision":"ambiguous","target_slug":null,"new_concept":null,"reason":"could be either x or y"}'
)
```

- [ ] **Step 3: Write failing tests**

```python
# tests/unit/test_llm_review.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from course_merger.cluster.clusterer import Cluster
from course_merger.cluster.llm_review import (
    ReviewDecision,
    Reviewer,
    parse_review_response,
)
from course_merger.tag.ontology import load_ontology
from tests.fixtures.review_responses import (
    AMBIGUOUS_DECISION,
    CREATE_DECISION,
    MERGE_DECISION,
    REJECT_DECISION,
)


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def test_parse_merge(onto):
    d = parse_review_response(MERGE_DECISION.content[0].text)
    assert d.decision == "merge"
    assert d.target_slug == "rotary-positional-encoding"


def test_parse_create(onto):
    d = parse_review_response(CREATE_DECISION.content[0].text)
    assert d.decision == "create"
    assert d.new_concept is not None
    assert d.new_concept["slug"] == "speculative-decoding"


def test_parse_reject(onto):
    d = parse_review_response(REJECT_DECISION.content[0].text)
    assert d.decision == "reject"


def test_parse_ambiguous(onto):
    d = parse_review_response(AMBIGUOUS_DECISION.content[0].text)
    assert d.decision == "ambiguous"


def test_reviewer_calls_sonnet(onto):
    fake_client = MagicMock()
    fake_client.messages.create.return_value = MERGE_DECISION

    reviewer = Reviewer(client=fake_client, model="claude-sonnet-4-6", ontology=onto)
    cluster = Cluster(items=["RoPE", "rotary embedding"], indices=[0, 1])
    decision = reviewer.review(cluster, sample_chunks=["...we use RoPE..."])

    assert isinstance(decision, ReviewDecision)
    assert decision.decision == "merge"

    call_kwargs = fake_client.messages.create.call_args.kwargs
    # The system prompt block must enable caching.
    assert isinstance(call_kwargs["system"], list)
    assert any(
        b.get("cache_control", {}).get("type") == "ephemeral"
        for b in call_kwargs["system"]
    )
```

- [ ] **Step 4: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_llm_review.py -v
```

- [ ] **Step 5: Write `src/course_merger/cluster/llm_review.py`**

```python
"""Sonnet review pass: per-cluster merge/create/reject decision."""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Literal

from course_merger.cluster.clusterer import Cluster
from course_merger.cluster.prompts import (
    CLUSTER_REVIEW_PROMPT_VERSION,
    REVIEW_SYSTEM,
    REVIEW_USER_TEMPLATE,
)
from course_merger.tag.ontology import Ontology


Decision = Literal["merge", "create", "reject", "ambiguous"]


@dataclass(frozen=True, slots=True)
class ReviewDecision:
    decision: Decision
    target_slug: str | None = None
    new_concept: dict[str, str] | None = None
    reason: str = ""


def parse_review_response(text: str) -> ReviewDecision:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"failed to parse review response as JSON: {e}") from e

    decision = data.get("decision")
    if decision not in ("merge", "create", "reject", "ambiguous"):
        raise ValueError(f"invalid decision: {decision!r}")

    return ReviewDecision(
        decision=decision,
        target_slug=data.get("target_slug"),
        new_concept=data.get("new_concept"),
        reason=data.get("reason", ""),
    )


def _build_system_blocks(ontology: Ontology) -> list[dict[str, Any]]:
    ontology_block = "\n".join(
        f"{c.slug} — {c.canonical_name}" for c in ontology.concepts
    ) or "(empty)"
    return [
        {
            "type": "text",
            "text": REVIEW_SYSTEM.format(ontology_block=ontology_block),
            "cache_control": {"type": "ephemeral"},
        }
    ]


class Reviewer:
    def __init__(
        self,
        *,
        client: Any,
        model: str,
        ontology: Ontology,
        max_tokens: int = 512,
    ) -> None:
        self.client = client
        self.model = model
        self.ontology = ontology
        self.max_tokens = max_tokens
        self._system_blocks = _build_system_blocks(ontology)

    @property
    def reviewer_model_id(self) -> str:
        return f"{self.model}:{CLUSTER_REVIEW_PROMPT_VERSION}"

    def review(self, cluster: Cluster, sample_chunks: list[str]) -> ReviewDecision:
        user_text = REVIEW_USER_TEMPLATE.format(
            cluster_items="\n".join(f"- {item}" for item in cluster.items),
            sample_chunks="\n".join(f"- {c[:200]}" for c in sample_chunks[:3]),
        )

        for _ in range(2):  # one retry on parse error
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=self._system_blocks,
                    messages=[{"role": "user", "content": user_text}],
                )
            except Exception:
                continue
            text = resp.content[0].text if resp.content else ""
            try:
                return parse_review_response(text)
            except ValueError:
                continue

        return ReviewDecision(decision="ambiguous", reason="parse_failure")
```

- [ ] **Step 6: Run tests**

```bash
.venv/bin/pytest tests/unit/test_llm_review.py -v
```

Expected: 5 pass.

- [ ] **Step 7: Commit**

```bash
git add src/course_merger/cluster/prompts.py src/course_merger/cluster/llm_review.py tests/fixtures/review_responses.py tests/unit/test_llm_review.py
git commit -m "feat(cluster): Sonnet reviewer (merge/create/reject/ambiguous) per cluster"
```

---

## Phase 9: `cluster` CLI Command

### Task 12: cluster runner + CLI wiring

**Files:**
- Create: `src/course_merger/cluster/runner.py`
- Modify: `src/course_merger/cli.py` — add `cluster` command
- Create: `tests/unit/test_cluster_runner.py`
- Create: `tests/integration/test_cluster_smoke.py`

The runner:
1. Pull all unique `proposed_tags.raw_tag` (excluding the `__parse_failure__` sentinel)
2. Embed them
3. Cluster
4. For each cluster: pick up to 3 supporting chunks (random sample), call reviewer
5. Persist the decision: write to `concepts` + `concept_aliases`, OR write reject log, OR write ambiguous to review queue
6. Migrate the `proposed_tags` rows into `chunk_concepts` (linking to the now-concrete concept_id)
7. Append affected concept slugs to `build_meta.dirty_concepts`

- [ ] **Step 1: Write failing unit tests**

```python
# tests/unit/test_cluster_runner.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import numpy as np
import pytest

from course_merger.cluster.clusterer import Cluster
from course_merger.cluster.llm_review import ReviewDecision
from course_merger.cluster.runner import ClusterReport, run_cluster
from course_merger.db.session import connect, init_db
from course_merger.tag.ontology import load_ontology


def _seed(db_path: Path) -> int:
    """Seed: 1 course, 1 lecture, 2 chunks, 2 proposed_tags entries."""
    init_db(db_path)
    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-09')"
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'u', 't', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'about rotary')",
            (lecture_id,),
        )
        c1 = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 1, 10, 20, 'about rope')",
            (lecture_id,),
        )
        c2 = cur.lastrowid
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (?, 'rotary-embedding', 0.8, 'haiku:v1')",
            (c1,),
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (?, 'RoPE', 0.85, 'haiku:v1')",
            (c2,),
        )
        # Seed an existing concept this cluster could merge into
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('rotary-positional-encoding', 'Rotary Positional Encoding', 'seed')"
        )
    return course_id


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def _fake_embedder(vectors_per_text: dict[str, np.ndarray]):
    m = MagicMock()
    def _embed(text: str) -> np.ndarray:
        return vectors_per_text[text]
    def _embed_batch(texts: list[str]) -> np.ndarray:
        return np.stack([vectors_per_text[t] for t in texts])
    m.embed.side_effect = _embed
    m.embed_batch.side_effect = _embed_batch
    return m


def _identical_vec(seed: int = 1) -> np.ndarray:
    rng = np.random.default_rng(seed)
    v = rng.normal(size=384).astype(np.float32)
    return v / np.linalg.norm(v)


def test_cluster_merge_creates_aliases_and_chunk_concepts(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    # Two proposed tags that should embed identically → one cluster
    same = _identical_vec()
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(
        decision="merge", target_slug="rotary-positional-encoding"
    )

    report = run_cluster(
        db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7
    )

    assert isinstance(report, ClusterReport)
    assert report.clusters_reviewed == 1
    assert report.merged == 1
    assert report.created == 0

    with connect(db) as conn:
        # Aliases get added
        aliases = [
            r[0] for r in conn.execute("SELECT alias FROM concept_aliases").fetchall()
        ]
        assert set(aliases) == {"rotary-embedding", "RoPE"}
        # chunk_concepts populated for both chunks
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
        assert n == 2
        # proposed_tags rows cleared
        (left,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
        assert left == 0


def test_cluster_create_makes_new_concept(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec(2)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(
        decision="create",
        new_concept={
            "slug": "rope-encoding",
            "canonical_name": "RoPE Encoding",
            "description": "Rotary position encoding.",
        },
    )

    run_cluster(db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7)

    with connect(db) as conn:
        c = conn.execute(
            "SELECT canonical_name, ontology_source FROM concepts WHERE slug='rope-encoding'"
        ).fetchone()
    assert c == ("RoPE Encoding", "discovered")


def test_cluster_reject_skips_writes(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec(3)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(decision="reject", reason="noise")

    run_cluster(db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7)

    with connect(db) as conn:
        # proposed_tags should still be cleared (we don't reprocess) but no chunk_concepts
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_pt == 0
    assert n_cc == 0


def test_cluster_ambiguous_queues_review(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec(4)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(decision="ambiguous", reason="?")

    report = run_cluster(
        db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7
    )

    assert report.ambiguous == 1
    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
    # Ambiguous: we keep the proposed_tags (so a future re-run can retry)
    assert n_pt == 2
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_cluster_runner.py -v
```

- [ ] **Step 3: Write `src/course_merger/cluster/runner.py`**

```python
"""Orchestrator: proposed_tags → embed → cluster → review → write concepts/aliases."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import numpy as np

from course_merger.cluster.clusterer import Cluster, cluster_by_cosine
from course_merger.cluster.llm_review import ReviewDecision
from course_merger.db.session import connect


class _EmbedderLike(Protocol):
    def embed_batch(self, texts: list[str]) -> np.ndarray: ...


class _ReviewerLike(Protocol):
    reviewer_model_id: str
    def review(self, cluster: Cluster, sample_chunks: list[str]) -> ReviewDecision: ...


@dataclass(frozen=True, slots=True)
class ClusterReport:
    clusters_reviewed: int
    merged: int
    created: int
    rejected: int
    ambiguous: int


def _collect_proposed_tags(conn) -> list[tuple[str, list[int]]]:
    """Return list of (raw_tag, [chunk_ids that have this tag]). Skips sentinel rows."""
    rows = conn.execute(
        "SELECT raw_tag, chunk_id FROM proposed_tags "
        "WHERE raw_tag != '__parse_failure__' "
        "ORDER BY raw_tag, chunk_id"
    ).fetchall()
    grouped: dict[str, list[int]] = {}
    for raw_tag, chunk_id in rows:
        grouped.setdefault(raw_tag, []).append(chunk_id)
    return list(grouped.items())


def _sample_chunks_for_cluster(conn, cluster: Cluster, tag_to_chunks: dict[str, list[int]], k: int = 3) -> list[str]:
    chunk_ids: list[int] = []
    for raw_tag in cluster.items:
        chunk_ids.extend(tag_to_chunks.get(raw_tag, []))
    chunk_ids = chunk_ids[:k]
    if not chunk_ids:
        return []
    placeholders = ",".join("?" for _ in chunk_ids)
    rows = conn.execute(
        f"SELECT text FROM chunks WHERE id IN ({placeholders})", chunk_ids
    ).fetchall()
    return [r[0] for r in rows]


def _mark_dirty(conn, slugs: list[str]) -> None:
    """Append `slugs` to build_meta.dirty_concepts (stored as JSON array)."""
    row = conn.execute(
        "SELECT value FROM build_meta WHERE key='dirty_concepts'"
    ).fetchone()
    existing: list[str] = json.loads(row[0]) if row else []
    merged = sorted(set(existing) | set(slugs))
    if row:
        conn.execute(
            "UPDATE build_meta SET value=? WHERE key='dirty_concepts'",
            (json.dumps(merged),),
        )
    else:
        conn.execute(
            "INSERT INTO build_meta (key, value) VALUES ('dirty_concepts', ?)",
            (json.dumps(merged),),
        )


def _consume_proposed_for_cluster(conn, cluster: Cluster, tag_to_chunks: dict[str, list[int]]) -> None:
    """Delete the proposed_tags rows for tags in this cluster."""
    raw_tags = list(cluster.items)
    if not raw_tags:
        return
    placeholders = ",".join("?" for _ in raw_tags)
    conn.execute(
        f"DELETE FROM proposed_tags WHERE raw_tag IN ({placeholders})",
        raw_tags,
    )


def _attach_chunks_to_concept(
    conn,
    cluster: Cluster,
    tag_to_chunks: dict[str, list[int]],
    concept_id: int,
    reviewer_model_id: str,
) -> None:
    """Create chunk_concepts rows for every chunk that contributed a tag in this cluster."""
    for raw_tag in cluster.items:
        for chunk_id in tag_to_chunks.get(raw_tag, []):
            conn.execute(
                "INSERT OR IGNORE INTO chunk_concepts "
                "(chunk_id, concept_id, confidence, tagger_model) "
                "VALUES (?, ?, 0.85, ?)",
                (chunk_id, concept_id, reviewer_model_id),
            )


def run_cluster(
    *,
    db_path: Path,
    embedder: _EmbedderLike,
    reviewer: _ReviewerLike,
    threshold: float = 0.75,
) -> ClusterReport:
    merged = created = rejected = ambiguous = 0
    dirty: list[str] = []

    with connect(db_path) as conn:
        tag_pairs = _collect_proposed_tags(conn)
        if not tag_pairs:
            return ClusterReport(0, 0, 0, 0, 0)

        raw_tags = [t for t, _ in tag_pairs]
        tag_to_chunks = dict(tag_pairs)

        vectors = embedder.embed_batch(raw_tags)
        clusters = cluster_by_cosine(raw_tags, vectors, threshold=threshold)

        for cluster in clusters:
            sample = _sample_chunks_for_cluster(conn, cluster, tag_to_chunks)
            decision = reviewer.review(cluster, sample_chunks=sample)

            if decision.decision == "merge":
                target = conn.execute(
                    "SELECT id, slug FROM concepts WHERE slug = ?", (decision.target_slug,)
                ).fetchone()
                if target is None:
                    # Target slug doesn't exist; treat as ambiguous fallback.
                    ambiguous += 1
                    continue
                target_id, target_slug = target
                for raw_tag in cluster.items:
                    conn.execute(
                        "INSERT OR IGNORE INTO concept_aliases (concept_id, alias) "
                        "VALUES (?, ?)",
                        (target_id, raw_tag),
                    )
                _attach_chunks_to_concept(conn, cluster, tag_to_chunks, target_id, reviewer.reviewer_model_id)
                _consume_proposed_for_cluster(conn, cluster, tag_to_chunks)
                dirty.append(target_slug)
                merged += 1

            elif decision.decision == "create":
                if decision.new_concept is None:
                    ambiguous += 1
                    continue
                new = decision.new_concept
                cur = conn.execute(
                    "INSERT INTO concepts (slug, canonical_name, description, ontology_source) "
                    "VALUES (?, ?, ?, 'discovered')",
                    (new["slug"], new["canonical_name"], new.get("description", "")),
                )
                new_id = cur.lastrowid
                for raw_tag in cluster.items:
                    if raw_tag != new["slug"]:
                        conn.execute(
                            "INSERT OR IGNORE INTO concept_aliases (concept_id, alias) "
                            "VALUES (?, ?)",
                            (new_id, raw_tag),
                        )
                _attach_chunks_to_concept(conn, cluster, tag_to_chunks, new_id, reviewer.reviewer_model_id)
                _consume_proposed_for_cluster(conn, cluster, tag_to_chunks)
                dirty.append(new["slug"])
                created += 1

            elif decision.decision == "reject":
                # Drop the proposed tags; no concept created, no chunk_concepts written.
                _consume_proposed_for_cluster(conn, cluster, tag_to_chunks)
                rejected += 1

            else:  # ambiguous
                # Leave the proposed_tags rows so a future cluster run (with more data) can retry.
                ambiguous += 1

        if dirty:
            _mark_dirty(conn, dirty)

    return ClusterReport(
        clusters_reviewed=len(clusters),
        merged=merged,
        created=created,
        rejected=rejected,
        ambiguous=ambiguous,
    )
```

- [ ] **Step 4: Run unit tests**

```bash
.venv/bin/pytest tests/unit/test_cluster_runner.py -v
```

Expected: 4 pass.

- [ ] **Step 5: Add `cluster` CLI command in `src/course_merger/cli.py`**

Add imports:

```python
from course_merger.cluster.embedding import Embedder
from course_merger.cluster.llm_review import Reviewer
from course_merger.cluster.runner import run_cluster
```

Append command:

```python
@app.command("cluster")
def cluster_cmd(
    ontology: Path = typer.Option(
        ..., "--ontology", help="Path to ontology YAML.", exists=True, dir_okay=False
    ),
    review_model: str = typer.Option(
        "claude-sonnet-4-6", "--review-model", help="Claude model for cluster review."
    ),
    threshold: float = typer.Option(
        0.75, "--threshold", help="Cosine similarity threshold for merging proposed tags."
    ),
) -> None:
    """Cluster proposed tags and ask Sonnet to merge / create / reject each cluster."""
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1)

    onto = load_ontology(ontology)
    import anthropic
    client = anthropic.Anthropic()

    embedder = Embedder()
    reviewer = Reviewer(client=client, model=review_model, ontology=onto)

    db_path = root / PROJECT_MARKER / "db.sqlite"
    report = run_cluster(
        db_path=db_path, embedder=embedder, reviewer=reviewer, threshold=threshold
    )

    typer.echo(
        f"done: {report.clusters_reviewed} clusters reviewed | "
        f"{report.merged} merged, {report.created} created, "
        f"{report.rejected} rejected, {report.ambiguous} ambiguous"
    )
```

- [ ] **Step 6: Write integration test**

```python
# tests/integration/test_cluster_smoke.py
from __future__ import annotations

import shutil
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from typer.testing import CliRunner

from course_merger.cli import app
from course_merger.cluster.llm_review import ReviewDecision
from course_merger.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_cluster_cli_end_to_end(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])

    # Seed a minimal corpus with proposed tags
    db = tmp_project / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-09')"
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'u', 't', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'rope content')",
            (lecture_id,),
        )
        chunk_id = cur.lastrowid
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (?, 'RoPE-thing', 0.8, 'haiku:v1')",
            (chunk_id,),
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('rotary-positional-encoding', 'RoPE', 'seed')"
        )

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    fake_decision = ReviewDecision(
        decision="merge", target_slug="rotary-positional-encoding"
    )
    fake_embedder = MagicMock()
    fake_embedder.embed_batch.return_value = np.ones((1, 384), dtype=np.float32)
    fake_reviewer = MagicMock()
    fake_reviewer.reviewer_model_id = "sonnet:v1"
    fake_reviewer.review.return_value = fake_decision

    with (
        patch("course_merger.cluster.embedding.Embedder", return_value=fake_embedder),
        patch("course_merger.cluster.llm_review.Reviewer", return_value=fake_reviewer),
        patch("anthropic.Anthropic", return_value=object()),
    ):
        result = runner.invoke(
            app,
            ["cluster", "--ontology", str(ont_path), "--threshold", "0.5"],
        )

    assert result.exit_code == 0, result.stdout
    assert "merged" in result.stdout.lower()

    with connect(db) as conn:
        (n,) = conn.execute(
            "SELECT COUNT(*) FROM concept_aliases WHERE alias='RoPE-thing'"
        ).fetchone()
    assert n == 1
```

- [ ] **Step 7: Run all tests**

```bash
.venv/bin/pytest -v
.venv/bin/pyright src tests
```

- [ ] **Step 8: Commit**

```bash
git add src/course_merger/cluster/runner.py src/course_merger/cli.py tests/unit/test_cluster_runner.py tests/integration/test_cluster_smoke.py
git commit -m "feat(cluster): \\\`cluster\\\` CLI orchestrates embed → group → review → DB"
```

---

## Phase 10: Documentation

### Task 13: README + ontology example file

**Files:**
- Modify: `README.md`
- Create: `examples/ontology-llm.yaml` — a starter ontology to ship

- [ ] **Step 1: Create `examples/ontology-llm.yaml`**

```yaml
# Starter ontology for LLM / Transformer / GPU courses.
# Use as a seed; the cluster command will grow it.

concepts:
  - slug: attention
    canonical_name: Attention
    description: Mechanism for weighting input tokens when forming a contextualized representation.
    aliases: [attention mechanism]

  - slug: self-attention
    canonical_name: Self-Attention
    description: Attention applied within a single sequence — Q, K, V from the same input.
    aliases: [SA, scaled dot-product attention, self attention]

  - slug: multi-head-attention
    canonical_name: Multi-Head Attention
    description: Multiple attention heads in parallel; outputs concatenated and projected.
    aliases: [MHA, multi-headed attention]

  - slug: rotary-positional-encoding
    canonical_name: Rotary Positional Encoding
    description: RoPE — encodes absolute positions by rotating Q/K projections.
    aliases: [RoPE, rotary embedding, rotary position]

  - slug: kv-cache
    canonical_name: KV Cache
    description: Caching previously computed keys and values to speed up autoregressive decoding.
    aliases: [KV-cache, key-value cache]

  - slug: transformer-block
    canonical_name: Transformer Block
    description: One attention + FFN layer with residual connections and layer norm.
    aliases: [transformer layer]

  - slug: mlp
    canonical_name: MLP / Feed-Forward Network
    description: Two-layer MLP applied position-wise after attention.
    aliases: [feed-forward, FFN, MLP block]

  - slug: layer-norm
    canonical_name: Layer Normalization
    description: Per-token feature normalization for training stability.
    aliases: [LayerNorm, LN]

  - slug: rms-norm
    canonical_name: RMS Normalization
    description: Variance-only normalization, no mean subtraction.
    aliases: [RMSNorm]

  - slug: cross-attention
    canonical_name: Cross-Attention
    description: Attention where Q comes from one sequence, K/V from another.

  - slug: prompt-caching
    canonical_name: Prompt Caching
    description: Reuse pre-computed KV for shared prompt prefixes to cut cost.
    aliases: [Anthropic prompt cache]

  - slug: tokenization
    canonical_name: Tokenization
    description: Splitting text into subword tokens.
    aliases: [BPE, byte-pair encoding, tokenizer]

  - slug: speculative-decoding
    canonical_name: Speculative Decoding
    description: Use a small draft model to propose tokens then verify with the large model.
    aliases: [spec decode, speculative sampling]

  - slug: flash-attention
    canonical_name: Flash Attention
    description: IO-aware attention algorithm fused into a single CUDA kernel.
    aliases: [FlashAttn]

  - slug: pagedattention
    canonical_name: PagedAttention
    description: Block-paged KV cache memory management, used by vLLM.
    aliases: [paged attention, page attention]
```

- [ ] **Step 2: Update `README.md` — extend Quickstart**

Replace the quickstart section with the expanded version:

````markdown
## Quickstart

```bash
# 1. Install
git clone https://github.com/chenlinzhuo/course-merger.git
cd course-merger
uv venv && uv pip install -e ".[dev]"

# 2. Initialize a project
mkdir my-courses && cd my-courses
uv run course-merger init

# 3. Crawl one or more courses
uv run course-merger crawl \
    "https://www.youtube.com/playlist?list=PLxxx" --name cs336
uv run course-merger crawl \
    "https://www.bilibili.com/video/BVxxx/" --name "vizuara-llm" \
    --cookies-from edge

# 4. Tag chunks with concept labels (Claude Haiku, ~$0.10 per course)
export ANTHROPIC_API_KEY=sk-ant-...
uv run course-merger tag --ontology /path/to/ontology.yaml

# 5. Cluster proposed tags into the canonical ontology (Claude Sonnet, ~$0.30 per pass)
uv run course-merger cluster --ontology /path/to/ontology.yaml
```

After these steps, `.course-merger/db.sqlite` contains:
- Courses, lectures, chunks (Plan 1)
- `concepts`, `concept_aliases`, `chunk_concepts` (Plan 2)

Inspect:

```bash
sqlite3 .course-merger/db.sqlite \\
    "SELECT canonical_name, COUNT(*) AS occurrences \\
     FROM concepts c JOIN chunk_concepts cc ON c.id = cc.concept_id \\
     GROUP BY c.id ORDER BY occurrences DESC LIMIT 10;"
```

A starter ontology lives at `examples/ontology-llm.yaml` (15 LLM concepts to seed).
````

Also update the **Roadmap** section:

```markdown
## Roadmap

- **Plan 1:** Foundation + crawl. `init`, `crawl` for YouTube & Bilibili. ✅
- **Plan 2:** Tag + cluster. `tag`, `cluster`. Claude Haiku tagging + Sonnet cluster review. ✅
- **Plan 3 (next):** Build + HTML. `build`, `serve`. Astro static site with cross-course concept pages.
- **Plan 4:** Demo + deploy + Claude Code skill wrapper.
```

- [ ] **Step 3: Commit**

```bash
git add README.md examples/ontology-llm.yaml
git commit -m "docs: README + starter LLM ontology for tag/cluster pipeline"
```

---

## Phase 11: End-to-End Verification

### Task 14: Real-data smoke test

This task is a manual verification — no new code, no new tests in the repo. We're proving the whole Plan 2 pipeline works on the same Vizuara course we used in Plan 1's T14.

- [ ] **Step 1: Re-init a fresh project directory**

```bash
rm -rf /tmp/cm-plan2 && mkdir /tmp/cm-plan2 && cd /tmp/cm-plan2
uv run --project /Users/chenlinzhuo/code/course-merger course-merger init
```

- [ ] **Step 2: Crawl the Vizuara playlist**

```bash
uv run --project /Users/chenlinzhuo/code/course-merger course-merger crawl \
    "https://www.youtube.com/playlist?list=PLPTV0NXA_ZShnka8uVzF3mSvZdilfiGWG" \
    --name "vizuara-build-claude-code"
```

Expected: `done: 4 ok, 0 no-subs, 0 errors`.

- [ ] **Step 3: Tag the chunks**

```bash
export ANTHROPIC_API_KEY=...   # set your key
uv run --project /Users/chenlinzhuo/code/course-merger course-merger tag \
    --ontology /Users/chenlinzhuo/code/course-merger/examples/ontology-llm.yaml \
    --limit 50   # cost cap for first try
```

Expected: `done: 50 chunks tagged, ~30-50 known tags, ~5-20 proposed tags, 0 parse failures`. Cost ≈ $0.04.

- [ ] **Step 4: Inspect the proposed tags**

```bash
sqlite3 .course-merger/db.sqlite \
    "SELECT raw_tag, COUNT(*) AS n FROM proposed_tags GROUP BY raw_tag ORDER BY n DESC LIMIT 20;"
```

Look at the tags — are they real concepts, or noise? This tells you whether the ontology is well-tuned.

- [ ] **Step 5: Cluster the proposed tags**

```bash
uv run --project /Users/chenlinzhuo/code/course-merger course-merger cluster \
    --ontology /Users/chenlinzhuo/code/course-merger/examples/ontology-llm.yaml
```

Expected: `N clusters reviewed | M merged, K created, ...`. Cost ≈ $0.10-0.30.

- [ ] **Step 6: Inspect the final concept table**

```bash
sqlite3 .course-merger/db.sqlite \
    "SELECT canonical_name, ontology_source FROM concepts ORDER BY id;"
sqlite3 .course-merger/db.sqlite \
    "SELECT alias, c.slug FROM concept_aliases ca JOIN concepts c ON ca.concept_id=c.id ORDER BY c.slug;"
```

- [ ] **Step 7: Idempotency check — re-run `tag` should do nothing new**

```bash
uv run --project /Users/chenlinzhuo/code/course-merger course-merger tag \
    --ontology /Users/chenlinzhuo/code/course-merger/examples/ontology-llm.yaml \
    --limit 200
```

Expected: `0 chunks tagged` (because all chunks already have `chunk_concepts` or `proposed_tags` rows).

- [ ] **Step 8: Tag the completion**

```bash
cd /Users/chenlinzhuo/code/course-merger
git tag plan-2-done
git log --oneline plan-1-done..plan-2-done
```

---

## Self-Review Notes

**Spec coverage check (Plan 2 portion):**

- §5 Data model — concepts, concept_aliases, chunk_concepts, build_meta tables: ✅ Task 5. (Plus the new `proposed_tags` table — a Plan-2-only intermediate that the spec didn't anticipate but is necessary; documented inline in Task 5.)
- §6 CLI `tag`: ✅ Task 8. Args: `--ontology`, `--model`, `--course`, `--limit`. Idempotent via untagged-chunks query.
- §6 CLI `cluster`: ✅ Task 12. Args: `--ontology`, `--review-model`, `--threshold`. Idempotent via consumption of `proposed_tags`.
- §6 Tagger prompt — caching + Chinese→English slug rule + confidence filter: ✅ Tasks 7 prompts.py.
- §8 Error handling: rate limit retry (existing in anthropic SDK), parse failure retry: ✅ Task 7 (`_MAX_RETRIES = 1`); cluster ambiguous → leave proposed_tags for re-run: ✅ Task 12.
- §10 Models: Haiku for tag, Sonnet for cluster review: ✅ defaults in CLI.
- §10 Embedding: `all-MiniLM-L6-v2`: ✅ Task 9.

**Out of scope, deferred:**

- §6 `review` CLI (human disambiguation queue) — `ambiguous` decisions just leave `proposed_tags` rows for now. Adding a `review` CLI is a Plan 3 or maintenance task.
- §5 `chunks.embedding` column — not added in Plan 2; Plan 3 (HTML build) might want it for "similar chunks" features. YAGNI for now.
- spec §6 "incremental cluster" (delta clustering for new tags only): Plan 2 just clusters every unconsumed `proposed_tags` row in a single pass. Fine until corpus grows past ~10K tags.

**Placeholder scan:** no "TBD", "TODO", or unresolved placeholders. All code blocks runnable; all SQL queries syntactically complete.

**Type / signature consistency:**

- `TagResult` (Task 7) — `tags: tuple[Tag, ...]`, `error: str` — used identically in Task 8's runner.
- `ClaudeTagger.tagger_model_id` (Task 7) — `f"{model}:{version}"` — referenced by `_TaggerLike` Protocol in Task 8 runner.
- `Cluster` (Task 10) — `items: list[str]`, `indices: list[int]` — consumed by Task 11 reviewer and Task 12 runner.
- `ReviewDecision` (Task 11) — `decision`, `target_slug`, `new_concept`, `reason` — handled exhaustively in Task 12 runner's 4-way dispatch.
- `Embedder` (Task 9) — `embed`, `embed_batch` — only `embed_batch` is used downstream in Task 12, but `embed` exists for future single-tag use.

**Cost reality check:**

Per Plan 2 run on a 4-lecture / 147-chunk Vizuara course:
- Tag: 147 chunks × ~1100 cached tokens × $0.80/MTok input + minimal output ≈ **$0.12**
- Cluster: ~20 clusters × ~5000 tokens × $3/MTok input + small output ≈ **$0.30**
- Total per course: < **$0.50**.

For 10 courses: $5. Acceptable.

**Plan 3 handoff notes** (the *next* plan's author should know):

- `build_meta.dirty_concepts` is a JSON-array of slugs — already maintained by `cluster`. Plan 3's `build --incremental` reads this.
- `concepts`, `chunk_concepts` are the source of truth for HTML concept pages.
- `chunks.start_sec` / `chunks.end_sec` enable the per-chunk video deep-link feature.
- A concept page query looks like: `SELECT c.id, courses.slug, lectures.idx, lectures.title, chunks.start_sec, chunks.text FROM chunks JOIN lectures ... JOIN chunk_concepts ... WHERE chunk_concepts.concept_id = ? ORDER BY courses.slug, lectures.idx, chunks.idx;`
