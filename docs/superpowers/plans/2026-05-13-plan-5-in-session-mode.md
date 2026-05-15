# Plan 5 — In-Session Mode for Max Users Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let Claude Max subscribers run the full `video-to-notebook` pipeline inside a Claude Code conversation without paying for separate Anthropic API access. The `tag` and `cluster` commands each grow `--print-prompts` (emits a JSON envelope of decisions to make) and `--apply-results <file>` (reads decisions JSON, writes to DB). Claude in conversation produces the decisions using its own reasoning, billed via the user's Max subscription.

**Architecture:** Each command's API-backed path stays untouched. A new `prompt_io.py` module per package (`tag/`, `cluster/`) exposes pure functions that (a) collect work items into a JSON envelope and (b) apply a results JSON to the DB. The CLI grows new flags that wire into these new functions, mutually exclusive with the existing API-call mode. No new dependencies.

**Tech Stack:** Same as v1 (Python 3.12 + Typer + SQLite). Only adds JSON serialization patterns over existing tag/cluster logic.

**Repo:** `/Users/chenlinzhuo/code/video-to-notebook/` (at tag `v1.0.0`).

---

## File Structure

```
video-to-notebook/
├── src/video_to_notebook/
│   ├── cli.py                              # MODIFY: add --print-prompts / --apply-results to tag + cluster
│   ├── tag/
│   │   ├── prompt_io.py                    # NEW: collect_tag_prompts + apply_tag_results
│   │   ├── runner.py                       # unchanged
│   │   └── ontology.py                     # unchanged
│   └── cluster/
│       ├── prompt_io.py                    # NEW: collect_cluster_prompts + apply_cluster_results
│       └── runner.py                       # MODIFY (small): expose 3 helpers as public
├── skills/video-to-notebook/SKILL.md           # MODIFY: in-session workflow section
├── README.md                               # MODIFY: in-session mode + trade-off table
└── tests/
    ├── unit/
    │   ├── test_tag_prompt_io.py           # NEW
    │   └── test_cluster_prompt_io.py       # NEW
    └── integration/
        ├── test_tag_smoke.py               # MODIFY: add print/apply tests
        └── test_cluster_smoke.py           # MODIFY: add print test
```

JSON Schema contracts (lock these in early — every task references them):

### Tag prompts envelope (output of `tag --print-prompts`)

```json
{
  "schema_version": "1",
  "kind": "tag_prompts",
  "ontology_slugs": ["self-attention", "attention", "kv-cache"],
  "instructions": "For each chunk, return 1-3 concept tags...",
  "chunks": [
    {"chunk_id": 1, "text": "self attention computes pairwise..."},
    {"chunk_id": 2, "text": "the rotary embedding rotates..."}
  ]
}
```

### Tag results envelope (input of `tag --apply-results`)

```json
{
  "schema_version": "1",
  "kind": "tag_results",
  "tagger_model_id": "claude-code-max:v1",
  "results": [
    {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.95}]},
    {"chunk_id": 2, "tags": [{"slug": "proposed:rotary-embedding", "confidence": 0.72}]}
  ]
}
```

### Cluster prompts envelope

```json
{
  "schema_version": "1",
  "kind": "cluster_prompts",
  "ontology": [
    {"slug": "self-attention", "canonical_name": "Self-Attention"}
  ],
  "instructions": "For each cluster, decide one of: merge / create / reject / ambiguous.",
  "clusters": [
    {"cluster_id": 0, "items": ["RoPE", "rotary embedding"], "sample_chunks": ["...we use RoPE..."]}
  ],
  "_tag_to_chunks": {"RoPE": [2], "rotary embedding": [1]}
}
```

### Cluster results envelope

```json
{
  "schema_version": "1",
  "kind": "cluster_results",
  "reviewer_model_id": "claude-code-max:v1",
  "decisions": [
    {"cluster_id": 0, "decision": "merge", "target_slug": "rotary-positional-encoding"}
  ]
}
```

The apply step needs BOTH envelopes; the CLI bundles them as `{"_prompts_envelope": {...}, "decisions_envelope": {...}}` in a single file.

---

## Task 1: Tag in-session mode

**Files:**
- Create: `src/video_to_notebook/tag/prompt_io.py`
- Modify: `src/video_to_notebook/cli.py` (add flags to `tag` command)
- Create: `tests/unit/test_tag_prompt_io.py`
- Modify: `tests/integration/test_tag_smoke.py` (add 3 tests)

### Step 1: Failing unit tests `tests/unit/test_tag_prompt_io.py`

- [ ] Write the test file with 8 tests covering: collect-only-untagged, limit + course filter, full chunk text preserved, apply known-slug writes chunk_concepts, apply proposed-slug writes proposed_tags, apply filters low-confidence, apply rejects wrong schema_version, apply rejects wrong kind. Full content:

```python
from __future__ import annotations

import json
from pathlib import Path

import pytest

from video_to_notebook.db.session import connect, init_db
from video_to_notebook.tag.ontology import load_ontology
from video_to_notebook.tag.prompt_io import (
    apply_tag_results,
    collect_tag_prompts,
)
from video_to_notebook.tag.runner import TagReport


def _seed(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'https://x', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'self attention is great')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 1, 1, 60, 120, 'rotary embedding is RoPE')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'self-attention', 'Self-Attention', 'seed')"
        )


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def test_collect_returns_only_untagged(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'previous:v1')"
        )

    envelope = collect_tag_prompts(db_path=db, ontology=onto)

    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "tag_prompts"
    assert "self-attention" in envelope["ontology_slugs"]
    chunk_ids = [c["chunk_id"] for c in envelope["chunks"]]
    assert chunk_ids == [2]


def test_collect_respects_limit_and_course(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_tag_prompts(db_path=db, ontology=onto, limit=1)
    assert len(envelope["chunks"]) == 1

    envelope_all = collect_tag_prompts(db_path=db, ontology=onto, course_slug="c1")
    assert len(envelope_all["chunks"]) == 2

    envelope_none = collect_tag_prompts(db_path=db, ontology=onto, course_slug="nonexistent")
    assert envelope_none["chunks"] == []


def test_collect_includes_full_chunk_text(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    envelope = collect_tag_prompts(db_path=db, ontology=onto)
    texts = [c["text"] for c in envelope["chunks"]]
    assert any("self attention" in t for t in texts)


def test_apply_writes_chunk_concepts_for_known_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [
            {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.95}]},
            {"chunk_id": 2, "tags": []},
        ],
    }
    report = apply_tag_results(db_path=db, ontology=onto, results=results)

    assert isinstance(report, TagReport)
    assert report.chunks_tagged == 2
    assert report.tags_known_written == 1
    with connect(db) as conn:
        rows = conn.execute(
            "SELECT tagger_model FROM chunk_concepts WHERE chunk_id = 1"
        ).fetchall()
    assert rows == [("claude-code-max:v1",)]


def test_apply_writes_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [
            {"chunk_id": 2, "tags": [{"slug": "proposed:rotary-embedding", "confidence": 0.7}]},
        ],
    }
    apply_tag_results(db_path=db, ontology=onto, results=results)
    with connect(db) as conn:
        rows = conn.execute("SELECT raw_tag, tagger_model FROM proposed_tags").fetchall()
    assert rows == [("rotary-embedding", "claude-code-max:v1")]


def test_apply_filters_low_confidence(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [
            {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.3}]},
        ],
    }
    report = apply_tag_results(db_path=db, ontology=onto, results=results)
    assert report.tags_known_written == 0
    with connect(db) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 0


def test_apply_rejects_wrong_schema_version(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "999",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [],
    }
    with pytest.raises(ValueError, match="schema_version"):
        apply_tag_results(db_path=db, ontology=onto, results=results)


def test_apply_rejects_wrong_kind(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    results = {
        "schema_version": "1",
        "kind": "cluster_results",
        "tagger_model_id": "x",
        "results": [],
    }
    with pytest.raises(ValueError, match="kind"):
        apply_tag_results(db_path=db, ontology=onto, results=results)
```

### Step 2: Confirm fails

```bash
cd /Users/chenlinzhuo/code/video-to-notebook && .venv/bin/pytest tests/unit/test_tag_prompt_io.py -v
```

Expected: ImportError on `video_to_notebook.tag.prompt_io`.

### Step 3: Write `src/video_to_notebook/tag/prompt_io.py`

```python
"""In-session tag mode: collect prompts as JSON, apply decisions back to DB.

Lets Claude Max subscribers run tag inside a Claude Code conversation without
a separate Anthropic API key. The conversation flow:
  1. `video-to-notebook tag --print-prompts ...` emits envelope to stdout
  2. Claude (conversation agent) produces decisions JSON
  3. `video-to-notebook tag --apply-results decisions.json` writes to DB
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from video_to_notebook.db.session import connect
from video_to_notebook.tag.ontology import Ontology
from video_to_notebook.tag.runner import TagReport, _untagged_chunks_query


SCHEMA_VERSION = "1"
DEFAULT_TAGGER_MODEL_ID = "claude-code-max:v1"

_MIN_CONFIDENCE = 0.5
_PROPOSED_PREFIX = "proposed:"

_TAGGER_INSTRUCTIONS = (
    "For each chunk, return 1-3 concept tags. Each tag's `slug` is either "
    "(a) one of the ontology_slugs in the envelope, or "
    "(b) prefixed `proposed:` to coin a new concept (use sparingly, "
    "<=1 per chunk). Each tag needs a `confidence` in [0.0, 1.0]; "
    "values below 0.5 are dropped. Slugs must be kebab-case English even "
    "if the chunk is Chinese or mixed-language."
)


def collect_tag_prompts(
    *,
    db_path: Path,
    ontology: Ontology,
    course_slug: str | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    sql, params = _untagged_chunks_query(course_slug)
    with connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
    if limit is not None:
        rows = rows[:limit]
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "tag_prompts",
        "ontology_slugs": [c.slug for c in ontology.concepts],
        "instructions": _TAGGER_INSTRUCTIONS,
        "chunks": [{"chunk_id": r[0], "text": r[1]} for r in rows],
    }


def apply_tag_results(
    *,
    db_path: Path,
    ontology: Ontology,
    results: dict[str, Any],
) -> TagReport:
    if results.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"tag results schema_version {results.get('schema_version')!r} "
            f"is not supported (expected {SCHEMA_VERSION!r})"
        )
    if results.get("kind") != "tag_results":
        raise ValueError(
            f"tag results kind {results.get('kind')!r} is not 'tag_results'"
        )

    tagger_model_id = results.get("tagger_model_id", DEFAULT_TAGGER_MODEL_ID)
    raw_results = results.get("results", []) or []

    chunks_tagged = 0
    tags_known_written = 0
    tags_proposed_written = 0

    with connect(db_path) as conn:
        for entry in raw_results:
            chunk_id = entry.get("chunk_id")
            if chunk_id is None:
                continue
            chunks_tagged += 1

            for tag in entry.get("tags") or []:
                slug = tag.get("slug", "")
                confidence = float(tag.get("confidence", 0.0))
                if confidence < _MIN_CONFIDENCE:
                    continue
                is_proposed = slug.startswith(_PROPOSED_PREFIX)
                clean_slug = slug[len(_PROPOSED_PREFIX):] if is_proposed else slug
                if not clean_slug:
                    continue

                if is_proposed:
                    conn.execute(
                        "INSERT OR IGNORE INTO proposed_tags "
                        "(chunk_id, raw_tag, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, clean_slug, confidence, tagger_model_id),
                    )
                    tags_proposed_written += 1
                else:
                    concept = conn.execute(
                        "SELECT id FROM concepts WHERE slug = ?", (clean_slug,)
                    ).fetchone()
                    if concept is None:
                        conn.execute(
                            "INSERT OR IGNORE INTO proposed_tags "
                            "(chunk_id, raw_tag, confidence, tagger_model) "
                            "VALUES (?, ?, ?, ?)",
                            (chunk_id, clean_slug, confidence, tagger_model_id),
                        )
                        tags_proposed_written += 1
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO chunk_concepts "
                        "(chunk_id, concept_id, confidence, tagger_model) "
                        "VALUES (?, ?, ?, ?)",
                        (chunk_id, concept[0], confidence, tagger_model_id),
                    )
                    tags_known_written += 1

    return TagReport(
        chunks_tagged=chunks_tagged,
        tags_known_written=tags_known_written,
        tags_proposed_written=tags_proposed_written,
        parse_failures=0,
    )
```

### Step 4: Run tests, expect PASS

```bash
.venv/bin/pytest tests/unit/test_tag_prompt_io.py -v
```

### Step 5: Modify `src/video_to_notebook/cli.py`

Add imports near the existing tag imports:

```python
import json
import sys
from video_to_notebook.tag.prompt_io import apply_tag_results, collect_tag_prompts
```

Replace the `tag_cmd` function body:

```python
@app.command("tag")
def tag_cmd(
    ontology: Path = typer.Option(
        ..., "--ontology", help="Path to ontology YAML.", exists=True, dir_okay=False
    ),
    model: str = typer.Option(
        "claude-haiku-4-5", "--model", help="Claude model id (API mode only)."
    ),
    course: str | None = typer.Option(
        None, "--course", help="Only tag chunks of this course slug."
    ),
    limit: int | None = typer.Option(
        None, "--limit", help="Max chunks to process this run."
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="Emit untagged chunks as JSON envelope to stdout (in-session mode).",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Read tag results JSON from this path and write to DB (in-session mode).",
    ),
) -> None:
    """Assign concept tags to chunks. Default mode calls Claude Haiku.

    --print-prompts / --apply-results provide an API-free path for Claude
    Max subscribers running inside a Claude Code conversation.
    """
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1)

    if print_prompts and apply_results is not None:
        typer.echo("error: --print-prompts and --apply-results are mutually exclusive")
        raise typer.Exit(code=1)

    onto = load_ontology(ontology)
    db_path = root / PROJECT_MARKER / "db.sqlite"

    if print_prompts:
        envelope = collect_tag_prompts(
            db_path=db_path, ontology=onto, course_slug=course, limit=limit,
        )
        sys.stdout.write(json.dumps(envelope, ensure_ascii=False, indent=2))
        sys.stdout.write("\n")
        return

    if apply_results is not None:
        with apply_results.open("r", encoding="utf-8") as fh:
            results = json.load(fh)
        report = apply_tag_results(db_path=db_path, ontology=onto, results=results)
        typer.echo(
            f"done (in-session): {report.chunks_tagged} chunks tagged, "
            f"{report.tags_known_written} known tags, "
            f"{report.tags_proposed_written} proposed tags"
        )
        return

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
```

### Step 6: Append integration tests to `tests/integration/test_tag_smoke.py`

```python
@pytest.mark.integration
def test_tag_print_prompts_emits_envelope(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'hello world')"
        )

    import shutil
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path), "--print-prompts"])
    assert result.exit_code == 0, result.stdout

    import json as _json
    envelope = _json.loads(result.stdout)
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "tag_prompts"
    assert len(envelope["chunks"]) == 1
    assert envelope["chunks"][0]["text"] == "hello world"


@pytest.mark.integration
def test_tag_apply_results_writes_db(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        course_id = cur.lastrowid
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'u', 't', 'ok')",
            (course_id,),
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'self attention.')"
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )

    import shutil, json as _json
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    results_path = tmp_project / "results.json"
    results_path.write_text(_json.dumps({
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [{"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.9}]}],
    }))

    result = runner.invoke(
        app,
        ["tag", "--ontology", str(ont_path), "--apply-results", str(results_path)],
    )
    assert result.exit_code == 0, result.stdout
    assert "1 known tags" in result.stdout

    with connect(db) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 1


@pytest.mark.integration
def test_tag_print_and_apply_mutually_exclusive(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    import shutil
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)
    results_path = tmp_project / "fake.json"
    results_path.write_text("{}")

    result = runner.invoke(
        app,
        ["tag", "--ontology", str(ont_path),
         "--print-prompts", "--apply-results", str(results_path)],
    )
    assert result.exit_code != 0
    assert "mutually exclusive" in result.stdout.lower()
```

### Step 7: Run all tests + typecheck

```bash
.venv/bin/pytest -v -m "not e2e"
.venv/bin/pyright src tests
```

Expected: existing 103 + 8 unit + 3 integration = 114 pass. Pyright clean.

### Step 8: Commit

```bash
git add src/video_to_notebook/tag/prompt_io.py src/video_to_notebook/cli.py tests/unit/test_tag_prompt_io.py tests/integration/test_tag_smoke.py
git commit -m "feat(tag): \\\`--print-prompts\\\` / \\\`--apply-results\\\` for in-session mode (Max path)"
```

---

## Task 2: Cluster in-session mode

**Files:**
- Modify: `src/video_to_notebook/cluster/runner.py` (rename 3 private helpers → public)
- Create: `src/video_to_notebook/cluster/prompt_io.py`
- Modify: `src/video_to_notebook/cli.py` (add flags to `cluster` command)
- Create: `tests/unit/test_cluster_prompt_io.py`
- Modify: `tests/integration/test_cluster_smoke.py`

### Step 1: Make 3 runner helpers public

In `src/video_to_notebook/cluster/runner.py`, rename these functions in their definition AND in their call sites within the same file:

| Old name | New name |
|----------|----------|
| `_mark_dirty` | `mark_dirty` |
| `_consume_proposed_for_cluster` | `consume_proposed_for_cluster` |
| `_attach_chunks_to_concept` | `attach_chunks_to_concept` |

Bodies stay identical. There are 4 call sites in `run_cluster()` to update.

### Step 2: Run cluster tests to verify nothing broke

```bash
.venv/bin/pytest tests/unit/test_cluster_runner.py tests/integration/test_cluster_smoke.py -v
```

Expected: still 5 pass.

### Step 3: Write failing unit tests `tests/unit/test_cluster_prompt_io.py`

```python
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import numpy as np
import pytest

from video_to_notebook.cluster.prompt_io import (
    apply_cluster_results,
    collect_cluster_prompts,
)
from video_to_notebook.cluster.runner import ClusterReport
from video_to_notebook.db.session import connect, init_db
from video_to_notebook.tag.ontology import load_ontology


def _seed(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'rotary content')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 1, 1, 60, 120, 'rope content')"
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (1, 'rotary-embedding', 0.8, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (2, 'RoPE', 0.85, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'rotary-positional-encoding', 'Rotary Positional Encoding', 'seed')"
        )


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def _same_vec(seed: int = 1) -> np.ndarray:
    rng = np.random.default_rng(seed)
    v = rng.normal(size=384).astype(np.float32)
    return v / np.linalg.norm(v)


def _fake_embedder(vecs: dict[str, np.ndarray]):
    m = MagicMock()
    m.embed_batch.side_effect = lambda texts: np.stack([vecs[t] for t in texts])
    return m


def test_collect_emits_clusters_and_samples(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec()
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "cluster_prompts"
    assert any(c["slug"] == "rotary-positional-encoding" for c in envelope["ontology"])
    assert len(envelope["clusters"]) == 1
    cluster = envelope["clusters"][0]
    assert cluster["cluster_id"] == 0
    assert set(cluster["items"]) == {"rotary-embedding", "RoPE"}
    assert "_tag_to_chunks" in envelope


def test_collect_empty_when_no_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    init_db(db)
    embedder = MagicMock()
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    assert envelope["clusters"] == []
    embedder.embed_batch.assert_not_called()


def test_apply_merge_writes_aliases_and_chunk_concepts(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec()
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "merge",
            "target_slug": "rotary-positional-encoding",
        }],
    }
    report = apply_cluster_results(
        db_path=db, ontology=onto, prompts=envelope, decisions=decisions,
    )
    assert isinstance(report, ClusterReport)
    assert report.merged == 1
    with connect(db) as conn:
        aliases = [r[0] for r in conn.execute("SELECT alias FROM concept_aliases").fetchall()]
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
    assert set(aliases) == {"rotary-embedding", "RoPE"}
    assert n_cc == 2
    assert n_pt == 0


def test_apply_create_makes_new_concept(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec(2)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "create",
            "new_concept": {
                "slug": "rope-encoding",
                "canonical_name": "RoPE Encoding",
                "description": "Rotary position encoding.",
            },
        }],
    }
    apply_cluster_results(db_path=db, ontology=onto, prompts=envelope, decisions=decisions)
    with connect(db) as conn:
        c = conn.execute(
            "SELECT canonical_name, ontology_source FROM concepts WHERE slug='rope-encoding'"
        ).fetchone()
    assert c == ("RoPE Encoding", "discovered")


def test_apply_reject_drops_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec(3)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "reject",
            "reason": "noise",
        }],
    }
    apply_cluster_results(db_path=db, ontology=onto, prompts=envelope, decisions=decisions)
    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_pt == 0
    assert n_cc == 0


def test_apply_ambiguous_keeps_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec(4)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "ambiguous",
            "reason": "?",
        }],
    }
    report = apply_cluster_results(
        db_path=db, ontology=onto, prompts=envelope, decisions=decisions,
    )
    assert report.ambiguous == 1
    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
    assert n_pt == 2


def test_apply_rejects_wrong_schema_version(tmp_path: Path, onto):
    decisions = {
        "schema_version": "999",
        "kind": "cluster_results",
        "reviewer_model_id": "x",
        "decisions": [],
    }
    with pytest.raises(ValueError, match="schema_version"):
        apply_cluster_results(
            db_path=tmp_path / "db.sqlite", ontology=onto,
            prompts={"schema_version": "1", "kind": "cluster_prompts", "clusters": [], "_tag_to_chunks": {}},
            decisions=decisions,
        )


def test_apply_rejects_wrong_kind(tmp_path: Path, onto):
    decisions = {
        "schema_version": "1",
        "kind": "tag_results",
        "reviewer_model_id": "x",
        "decisions": [],
    }
    with pytest.raises(ValueError, match="kind"):
        apply_cluster_results(
            db_path=tmp_path / "db.sqlite", ontology=onto,
            prompts={"schema_version": "1", "kind": "cluster_prompts", "clusters": [], "_tag_to_chunks": {}},
            decisions=decisions,
        )
```

### Step 4: Write `src/video_to_notebook/cluster/prompt_io.py`

```python
"""In-session cluster mode: collect cluster prompts as JSON, apply decisions to DB.

See `video_to_notebook.tag.prompt_io` for the rationale (Claude Max subscribers).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol

import numpy as np

from video_to_notebook.cluster.clusterer import Cluster, cluster_by_cosine
from video_to_notebook.cluster.runner import (
    ClusterReport,
    _collect_proposed_tags,
    _sample_chunks_for_cluster,
    attach_chunks_to_concept,
    consume_proposed_for_cluster,
    mark_dirty,
)
from video_to_notebook.db.session import connect
from video_to_notebook.tag.ontology import Ontology


SCHEMA_VERSION = "1"
DEFAULT_REVIEWER_MODEL_ID = "claude-code-max:v1"

_CLUSTER_INSTRUCTIONS = (
    "For each cluster, decide one of: "
    "(a) merge — provide `target_slug` from the existing ontology; "
    "(b) create — provide `new_concept: {slug, canonical_name, description}`; "
    "(c) reject — cluster is noise; "
    "(d) ambiguous — flag for human review. "
    "Slugs are kebab-case English even if cluster items are in another language."
)


class _EmbedderLike(Protocol):
    def embed_batch(self, texts: list[str]) -> np.ndarray: ...


def collect_cluster_prompts(
    *,
    db_path: Path,
    ontology: Ontology,
    embedder: _EmbedderLike,
    threshold: float = 0.75,
) -> dict[str, Any]:
    """Embed proposed tags, run cosine clustering, emit envelope."""
    with connect(db_path) as conn:
        tag_pairs = _collect_proposed_tags(conn)

    if not tag_pairs:
        return {
            "schema_version": SCHEMA_VERSION,
            "kind": "cluster_prompts",
            "ontology": [
                {"slug": c.slug, "canonical_name": c.canonical_name}
                for c in ontology.concepts
            ],
            "instructions": _CLUSTER_INSTRUCTIONS,
            "clusters": [],
            "_tag_to_chunks": {},
        }

    raw_tags = [t for t, _ in tag_pairs]
    tag_to_chunks: dict[str, list[int]] = dict(tag_pairs)
    vectors = embedder.embed_batch(raw_tags)
    clusters = cluster_by_cosine(raw_tags, vectors, threshold=threshold)

    envelope_clusters: list[dict[str, Any]] = []
    with connect(db_path) as conn:
        for idx, cluster in enumerate(clusters):
            sample = _sample_chunks_for_cluster(conn, cluster, tag_to_chunks)
            envelope_clusters.append({
                "cluster_id": idx,
                "items": list(cluster.items),
                "sample_chunks": sample,
            })

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "cluster_prompts",
        "ontology": [
            {"slug": c.slug, "canonical_name": c.canonical_name}
            for c in ontology.concepts
        ],
        "instructions": _CLUSTER_INSTRUCTIONS,
        "clusters": envelope_clusters,
        "_tag_to_chunks": tag_to_chunks,
    }


def apply_cluster_results(
    *,
    db_path: Path,
    ontology: Ontology,
    prompts: dict[str, Any],
    decisions: dict[str, Any],
) -> ClusterReport:
    if decisions.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"cluster decisions schema_version {decisions.get('schema_version')!r} "
            f"is not supported (expected {SCHEMA_VERSION!r})"
        )
    if decisions.get("kind") != "cluster_results":
        raise ValueError(
            f"cluster decisions kind {decisions.get('kind')!r} is not 'cluster_results'"
        )

    reviewer_model_id = decisions.get("reviewer_model_id", DEFAULT_REVIEWER_MODEL_ID)
    tag_to_chunks: dict[str, list[int]] = prompts.get("_tag_to_chunks", {})
    clusters_by_id = {c["cluster_id"]: c for c in prompts.get("clusters", [])}

    merged = created = rejected = ambiguous = 0
    dirty: list[str] = []

    with connect(db_path) as conn:
        for entry in decisions.get("decisions", []):
            cluster_id = entry.get("cluster_id")
            envelope_cluster = clusters_by_id.get(cluster_id)
            if envelope_cluster is None:
                ambiguous += 1
                continue
            cluster = Cluster(
                items=list(envelope_cluster["items"]),
                indices=list(range(len(envelope_cluster["items"]))),
            )
            kind = entry.get("decision")

            if kind == "merge":
                target = conn.execute(
                    "SELECT id, slug FROM concepts WHERE slug = ?",
                    (entry.get("target_slug"),),
                ).fetchone()
                if target is None:
                    ambiguous += 1
                    continue
                target_id, slug_in_db = target
                for raw_tag in cluster.items:
                    conn.execute(
                        "INSERT OR IGNORE INTO concept_aliases (concept_id, alias) "
                        "VALUES (?, ?)",
                        (target_id, raw_tag),
                    )
                attach_chunks_to_concept(conn, cluster, tag_to_chunks, target_id, reviewer_model_id)
                consume_proposed_for_cluster(conn, cluster)
                dirty.append(slug_in_db)
                merged += 1

            elif kind == "create":
                new = entry.get("new_concept")
                if not new or not new.get("slug") or not new.get("canonical_name"):
                    ambiguous += 1
                    continue
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
                attach_chunks_to_concept(conn, cluster, tag_to_chunks, new_id, reviewer_model_id)
                consume_proposed_for_cluster(conn, cluster)
                dirty.append(new["slug"])
                created += 1

            elif kind == "reject":
                consume_proposed_for_cluster(conn, cluster)
                rejected += 1

            else:
                ambiguous += 1

        if dirty:
            mark_dirty(conn, dirty)

    return ClusterReport(
        clusters_reviewed=len(decisions.get("decisions", [])),
        merged=merged,
        created=created,
        rejected=rejected,
        ambiguous=ambiguous,
    )
```

### Step 5: Run tests, expect PASS

```bash
.venv/bin/pytest tests/unit/test_cluster_prompt_io.py -v
```

### Step 6: Modify `src/video_to_notebook/cli.py` — `cluster_cmd`

Add imports:

```python
from video_to_notebook.cluster.prompt_io import (
    apply_cluster_results,
    collect_cluster_prompts,
)
```

Replace `cluster_cmd`:

```python
@app.command("cluster")
def cluster_cmd(
    ontology: Path = typer.Option(
        ..., "--ontology", help="Path to ontology YAML.", exists=True, dir_okay=False
    ),
    review_model: str = typer.Option(
        "claude-sonnet-4-6", "--review-model", help="Claude model for review (API mode)."
    ),
    threshold: float = typer.Option(
        0.75, "--threshold", help="Cosine similarity threshold for merging proposed tags."
    ),
    print_prompts: bool = typer.Option(
        False, "--print-prompts",
        help="Emit cluster decisions to stdout (in-session mode).",
    ),
    apply_results: Path | None = typer.Option(
        None, "--apply-results",
        help="Apply a cluster decisions JSON bundle to DB. The file must contain "
        "both `_prompts_envelope` and `decisions_envelope` (or top-level decisions).",
    ),
) -> None:
    """Cluster proposed tags. Default mode calls Claude Sonnet.

    --print-prompts / --apply-results provide an API-free path.
    """
    try:
        root = find_project_root(Path.cwd())
    except ProjectNotInitializedError as e:
        typer.echo(f"error: {e}")
        raise typer.Exit(code=1)

    if print_prompts and apply_results is not None:
        typer.echo("error: --print-prompts and --apply-results are mutually exclusive")
        raise typer.Exit(code=1)

    onto = load_ontology(ontology)
    db_path = root / PROJECT_MARKER / "db.sqlite"
    embedder = Embedder()

    if print_prompts:
        envelope = collect_cluster_prompts(
            db_path=db_path, ontology=onto, embedder=embedder, threshold=threshold,
        )
        sys.stdout.write(json.dumps(envelope, ensure_ascii=False, indent=2))
        sys.stdout.write("\n")
        return

    if apply_results is not None:
        with apply_results.open("r", encoding="utf-8") as fh:
            payload = json.load(fh)
        prompts = payload.get("_prompts_envelope") or payload.get("prompts")
        decisions = payload.get("decisions_envelope") or payload.get("decisions") or payload
        if prompts is None or "clusters" not in prompts:
            typer.echo(
                "error: --apply-results JSON must include the original prompts envelope "
                "(under `_prompts_envelope`) and the decisions (under `decisions_envelope`)."
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
```

### Step 7: Append integration test to `tests/integration/test_cluster_smoke.py`

```python
@pytest.mark.integration
def test_cluster_print_prompts_emits_envelope(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'rope text')"
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (1, 'RoPE-thing', 0.8, 'haiku:v1')"
        )

    import shutil
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    with patch(
        "video_to_notebook.cluster.embedding.Embedder.embed_batch",
        return_value=np.ones((1, 384), dtype=np.float32),
    ):
        result = runner.invoke(
            app,
            ["cluster", "--ontology", str(ont_path),
             "--threshold", "0.5", "--print-prompts"],
        )

    assert result.exit_code == 0, result.stdout
    import json as _json
    envelope = _json.loads(result.stdout)
    assert envelope["kind"] == "cluster_prompts"
    assert len(envelope["clusters"]) == 1
    assert envelope["clusters"][0]["items"] == ["RoPE-thing"]
```

Ensure `import numpy as np` and `from unittest.mock import patch` are present at the top of the file.

### Step 8: Run full suite + typecheck

```bash
.venv/bin/pytest -v -m "not e2e"
.venv/bin/pyright src tests
```

Expected: 114 + 8 + 1 = 123 pass. Pyright clean.

### Step 9: Commit

```bash
git add src/video_to_notebook/cluster/ src/video_to_notebook/cli.py tests/unit/test_cluster_prompt_io.py tests/integration/test_cluster_smoke.py
git commit -m "feat(cluster): \\\`--print-prompts\\\` / \\\`--apply-results\\\` for in-session mode"
```

---

## Task 3: SKILL.md in-session workflow + heuristic

**Files:**
- Modify: `skills/video-to-notebook/SKILL.md`

### Step 1: Read the current SKILL.md and append a new section after "## The 5-step pipeline" (and before "## Quick recipes")

Insert the following:

```markdown
## In-session mode (Claude Max users — no API key)

If the user has Claude Max (or any Claude Code subscription), they should NOT need a separate Anthropic API key. The tag and cluster commands each support a two-step pattern: emit work to JSON, decide in the conversation, apply back.

### When to recommend this mode

After Step 2 (crawl), check chunk count:

```bash
sqlite3 .video-to-notebook/db.sqlite "SELECT COUNT(*) FROM chunks"
```

| Chunk count | Mode |
|-------------|------|
| **< 200** | **In-session** (no API key, free via subscription) |
| 200–1000 | Either; in-session is slower but free |
| > 1000 | **API mode** — too slow to batch through conversation |

If user explicitly says "I have Max" or "no API key", default to in-session regardless of size.

### In-session tag loop

```bash
video-to-notebook tag --ontology <ont.yaml> --print-prompts --limit 20 > /tmp/cm-prompts.json
```

Read `/tmp/cm-prompts.json`:

```json
{
  "schema_version": "1",
  "kind": "tag_prompts",
  "ontology_slugs": ["self-attention", ...],
  "chunks": [{"chunk_id": 1, "text": "..."}, ...]
}
```

For each chunk, decide tags (in your own reasoning) and write to `/tmp/cm-results.json`:

```json
{
  "schema_version": "1",
  "kind": "tag_results",
  "tagger_model_id": "claude-code-max:v1",
  "results": [
    {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.9}]}
  ]
}
```

Apply:

```bash
video-to-notebook tag --ontology <ont.yaml> --apply-results /tmp/cm-results.json
```

Repeat until `--print-prompts` returns empty `chunks` array.

### In-session cluster

```bash
video-to-notebook cluster --ontology <ont.yaml> --print-prompts > /tmp/cm-cluster-prompts.json
```

Read the envelope. For each cluster, decide merge / create / reject / ambiguous.

Construct apply bundle (single file with BOTH envelopes):

```json
{
  "_prompts_envelope": { ... full /tmp/cm-cluster-prompts.json content ... },
  "decisions_envelope": {
    "schema_version": "1",
    "kind": "cluster_results",
    "reviewer_model_id": "claude-code-max:v1",
    "decisions": [
      {"cluster_id": 0, "decision": "merge", "target_slug": "rotary-positional-encoding"}
    ]
  }
}
```

Apply:

```bash
video-to-notebook cluster --ontology <ont.yaml> --apply-results /tmp/cm-cluster-apply.json
```
```

### Step 2: Commit

```bash
git add skills/video-to-notebook/SKILL.md
git commit -m "feat(skill): in-session workflow for Claude Max users (no API key path)"
```

---

## Task 4: README + roadmap update

**Files:**
- Modify: `README.md`

### Step 1: After "Use it as a Claude Code skill" section, insert

```markdown
## In-session mode (Claude Max users)

If you have a Claude Max subscription, you can skip the Anthropic API key. `video-to-notebook tag` and `video-to-notebook cluster` each accept two new flags:

- `--print-prompts` emits a JSON envelope of work to stdout.
- `--apply-results <file>` reads a decisions JSON and writes results to the DB.

Inside Claude Code, the conversation goes:

```
You: "Crawl this playlist and tag using examples/ontology-llm.yaml. I have Max."

Claude (in conversation):
  - Bash: video-to-notebook init && video-to-notebook crawl <url>
  - Bash: video-to-notebook tag --ontology ... --print-prompts --limit 20 > p.json
  - (reads p.json, decides tags via its own reasoning)
  - writes r.json with decisions
  - Bash: video-to-notebook tag --ontology ... --apply-results r.json
  - (repeats batch by batch)
  - same loop for cluster
  - Bash: video-to-notebook build
```

The skill at `skills/video-to-notebook/SKILL.md` automates this. Install via `bash skills/video-to-notebook/scripts/install-locally.sh`.

Trade-offs:

| | API mode | In-session mode |
|---|----------|----------------|
| API key required | Yes | No |
| Cost for demo corpus | ~$2-4 | $0 extra (covered by Max) |
| Speed for 1000 chunks | ~5-10 min | ~1-2 hours |
| Speed for 100 chunks | ~30 sec | ~5-10 min |
| Best for | Large corpora | Small experiments |
```

### Step 2: Find "Roadmap (deferred to v2)" section in README. Move the API-key-free option OUT of v2 if present, OR add a "Shipped in v1.1" note above the roadmap

Add this paragraph before "## Roadmap (deferred to v2)":

```markdown
**Shipped in v1.1** (2026-05-13): in-session mode for Claude Max users via `--print-prompts` / `--apply-results` flags on `tag` and `cluster`.
```

### Step 3: Commit

```bash
git add README.md
git commit -m "docs: README in-session mode section + v1.1 shipped note"
```

---

## Task 5: Live end-to-end verification (controller-executed)

This task is executed by the controller (Claude in this conversation), not a fresh subagent. It proves the in-session loop works on a real small corpus.

### Step 1: Reset throwaway project

```bash
rm -rf /tmp/cm-in-session && mkdir /tmp/cm-in-session && cd /tmp/cm-in-session
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook init
```

### Step 2: Crawl a small course

```bash
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook crawl \
    "https://www.youtube.com/playlist?list=PLPTV0NXA_ZShnka8uVzF3mSvZdilfiGWG" \
    --name "vizuara-build-claude-code"
```

Expected: 3 lectures ok, 1 error (members-only), ~100-150 chunks.

### Step 3: Emit tag prompts for first 20 chunks

```bash
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook tag \
    --ontology /Users/chenlinzhuo/code/video-to-notebook/examples/ontology-llm.yaml \
    --print-prompts --limit 20 > /tmp/cm-prompts-1.json

.venv/bin/python3 -c "
import json
e = json.load(open('/tmp/cm-prompts-1.json'))
print('chunks:', len(e['chunks']), 'ontology:', len(e['ontology_slugs']))
"
```

Expected: 20 chunks, 15 ontology slugs.

### Step 4: Decide tags (controller reads + reasons + writes JSON)

The controller reads `/tmp/cm-prompts-1.json`, decides tags for each chunk by reasoning over chunk text + ontology slugs, writes `/tmp/cm-results-1.json` in `tag_results` schema:

```json
{
  "schema_version": "1",
  "kind": "tag_results",
  "tagger_model_id": "claude-code-max:v1",
  "results": [{"chunk_id": N, "tags": [...]}, ...]
}
```

### Step 5: Apply tag results

```bash
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook tag \
    --ontology /Users/chenlinzhuo/code/video-to-notebook/examples/ontology-llm.yaml \
    --apply-results /tmp/cm-results-1.json
```

Expected: `done (in-session): 20 chunks tagged, N known tags, M proposed tags`.

### Step 6: Verify DB state

```bash
sqlite3 .video-to-notebook/db.sqlite \
    "SELECT tagger_model, COUNT(*) FROM chunk_concepts GROUP BY tagger_model;"
sqlite3 .video-to-notebook/db.sqlite \
    "SELECT COUNT(*) FROM proposed_tags;"
```

Expected: rows with `tagger_model = "claude-code-max:v1"`.

### Step 7: Repeat tag for the rest

Loop steps 3-5 with `--limit 20` until print-prompts returns empty `chunks`.

### Step 8: Emit cluster prompts

```bash
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook cluster \
    --ontology /Users/chenlinzhuo/code/video-to-notebook/examples/ontology-llm.yaml \
    --print-prompts > /tmp/cm-cluster-prompts.json
```

### Step 9: Decide clusters + bundle + apply

Controller reads cluster envelope, decides per cluster, writes `/tmp/cm-cluster-apply.json` with bundle:

```json
{
  "_prompts_envelope": { ... },
  "decisions_envelope": { "schema_version": "1", "kind": "cluster_results", "decisions": [...] }
}
```

```bash
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook cluster \
    --ontology /Users/chenlinzhuo/code/video-to-notebook/examples/ontology-llm.yaml \
    --apply-results /tmp/cm-cluster-apply.json
```

### Step 10: Build + inspect

```bash
/Users/chenlinzhuo/code/video-to-notebook/.venv/bin/video-to-notebook build
ls site/dist/concepts/
```

Open `site/dist/index.html` and verify concept pages show chunks tagged via in-session.

### Step 11: Tag milestone

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git tag plan-5-done
git tag -a v1.1.0 -m "v1.1.0 — in-session mode for Claude Max subscribers"
git log --oneline v1.0.0..v1.1.0
```

---

## Self-Review Notes

**Spec coverage:**

- `tag --print-prompts` / `tag --apply-results`: ✅ Task 1.
- `cluster --print-prompts` / `cluster --apply-results`: ✅ Task 2.
- Schema versioning + kind validation: ✅ Tasks 1 + 2.
- `tagger_model_id` / `reviewer_model_id` defaults to `"claude-code-max:v1"`: ✅.
- SKILL.md heuristic by chunk count: ✅ Task 3.
- README explains for non-Claude-Code readers: ✅ Task 4.
- End-to-end verification live: ✅ Task 5.

**Out of scope, deferred:**

- Auto-mode selection in the CLI itself (`tag --auto-mode`): kept in SKILL.md heuristic, not in the CLI.
- Streaming print-prompts (continuous stdout): YAGNI — batched `--limit N` suffices.

**Placeholder scan:** none. All code blocks runnable; all JSON schemas explicit.

**Type / signature consistency:**

- `collect_tag_prompts` / `apply_tag_results` return types match existing `TagReport`.
- `collect_cluster_prompts` / `apply_cluster_results` return types match existing `ClusterReport`.
- Renamed cluster helpers (`mark_dirty`, `consume_proposed_for_cluster`, `attach_chunks_to_concept`) used identically in `runner.py` and `prompt_io.py`.
- JSON fields consistent at produce/consume: `schema_version`, `kind`, `chunk_id`, `cluster_id`, `tags[].slug`, `tags[].confidence`, `decision`, `target_slug`, `new_concept`.

**No backlog from Plan 4** to address.
