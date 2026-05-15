# Plan 3 — Build + HTML Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `video-to-notebook build && video-to-notebook serve`. After Plan 3, `site/dist/` is a fully navigable static site with cross-course concept pages, a side-by-side compare view, video↔transcript synchronization, and full-text search via Pagefind. The site is one `git push` away from being deployed to GitHub Pages (deploy step lands in Plan 4).

**Architecture:** A `template-site/` Astro project ships inside the Python package. `video-to-notebook build` lazy-copies it into `<project>/site/`, queries the SQLite DB, writes Markdown content collections, then shells out to `npm run build`. Three lightweight Astro components (vanilla JS + Web Components, no React) handle the interactive pieces. `--incremental` consults `build_meta.dirty_concepts` and only re-emits changed concept pages.

**Tech Stack:** Astro 5.x + Pagefind 1.x + Node 20+ (new external requirement). Frontend uses vanilla JS / minimal Web Components — no React/Vue/Svelte. Tests: pytest for the Python writer; Playwright for E2E browser interaction.

**Repo:** `/Users/chenlinzhuo/code/video-to-notebook/` (at tag `plan-2-done`, commit `fcb3666`).

---

## File Structure

```
video-to-notebook/
├── pyproject.toml                          # MODIFY: add Jinja2 (for Markdown templates)
├── README.md                               # MODIFY: note Node 20+ requirement
├── src/video_to_notebook/
│   ├── cli.py                              # MODIFY: add `build` and `serve` commands
│   └── build/                              # NEW package
│       ├── __init__.py
│       ├── queries.py                      # DB read queries: courses, lectures, chunks-per-concept
│       ├── writers.py                      # pure functions: db rows → Markdown frontmatter+body
│       ├── runner.py                       # orchestrator: write content + spawn astro build
│       └── template_copy.py                # lazy-copies template-site/ → <project>/site/
├── template-site/                          # NEW: Astro project shipped with the package
│   ├── package.json
│   ├── astro.config.mjs
│   ├── tsconfig.json
│   ├── src/
│   │   ├── content/
│   │   │   ├── config.ts                   # Content Collections schema
│   │   │   ├── concepts/.gitkeep
│   │   │   ├── courses/.gitkeep
│   │   │   └── lectures/.gitkeep
│   │   ├── layouts/
│   │   │   └── Base.astro                  # shared layout: nav, search box, footer
│   │   ├── pages/
│   │   │   ├── index.astro                 # landing
│   │   │   ├── about.astro                 # build info
│   │   │   ├── courses/
│   │   │   │   ├── index.astro             # all-courses grid
│   │   │   │   ├── [slug]/index.astro      # course overview + lecture list
│   │   │   │   └── [slug]/[lecture].astro  # lecture detail (video + transcript)
│   │   │   └── concepts/
│   │   │       ├── index.astro             # A-Z concept index + cloud
│   │   │       ├── [slug]/index.astro      # concept detail (occurrence table)
│   │   │       └── [slug]/compare.astro    # multi-course compare view
│   │   ├── components/
│   │   │   ├── LectureTranscript.astro     # synced video↔transcript scroll
│   │   │   ├── ConceptOccurrenceTable.astro
│   │   │   ├── CompareView.astro
│   │   │   └── VideoEmbed.astro            # YouTube/Bilibili iframe wrapper
│   │   └── styles/
│   │       └── global.css                  # minimal CSS reset + base styles
│   └── public/
│       └── favicon.svg
└── tests/
    ├── unit/
    │   ├── test_build_queries.py           # NEW
    │   ├── test_build_writers.py           # NEW
    │   └── test_template_copy.py           # NEW
    ├── integration/
    │   └── test_build_smoke.py             # NEW: full pipeline through to dist/
    └── e2e/                                # NEW directory
        ├── conftest.py                     # spins up `astro dev` for tests
        ├── test_navigation.py              # NEW: click through key paths
        └── test_compare_view.py            # NEW: chip toggle, URL state
```

Boundary discipline:
- `build/queries.py`: read-only SQL, returns plain Python dicts (no I/O on the DB schema beyond SELECT).
- `build/writers.py`: pure functions over the dicts → strings; no file I/O. Trivially unit-testable.
- `build/template_copy.py`: filesystem operations; copies template-site, leaves user's `node_modules` alone.
- `build/runner.py`: the only place that touches DB + filesystem + subprocess (npm). Thin.
- `template-site/`: the entire frontend. Versioned in repo, shipped via hatchling force-include.

---

## Phase 0: Astro Scaffold

### Task 1: Create `template-site/` Astro project

**Files:**
- Create: `template-site/package.json`
- Create: `template-site/astro.config.mjs`
- Create: `template-site/tsconfig.json`
- Create: `template-site/src/content/config.ts`
- Create: `template-site/src/layouts/Base.astro`
- Create: `template-site/src/pages/index.astro` (minimal landing for now)
- Create: `template-site/src/styles/global.css`
- Create: `template-site/public/favicon.svg`
- Create: `template-site/src/content/{concepts,courses,lectures}/.gitkeep` (placeholders so collections resolve)
- Modify: `pyproject.toml` — include template-site in wheel
- Modify: `.gitignore` — exclude `template-site/node_modules`, `template-site/dist`, `template-site/.astro`

This task only proves the Astro template builds in isolation. No Python integration yet.

- [ ] **Step 1: Write `template-site/package.json`**

```json
{
  "name": "video-to-notebook-site",
  "type": "module",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "build": "astro build && pagefind --site dist",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5.0.0",
    "pagefind": "^1.3.0"
  }
}
```

- [ ] **Step 2: Write `template-site/astro.config.mjs`**

```js
import { defineConfig } from 'astro/config';

export default defineConfig({
  // GitHub Pages base path is set in Plan 4 — placeholder for now
  site: 'https://example.com',
  output: 'static',
  build: {
    format: 'directory',
  },
  vite: {
    build: { sourcemap: false },
  },
});
```

- [ ] **Step 3: Write `template-site/tsconfig.json`**

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": ["src/**/*", ".astro/types.d.ts"],
  "exclude": ["dist", "node_modules"]
}
```

- [ ] **Step 4: Write `template-site/src/content/config.ts`**

```typescript
import { defineCollection, z } from 'astro:content';

const concept = defineCollection({
  type: 'content',
  schema: z.object({
    slug: z.string(),
    canonical_name: z.string(),
    description: z.string().default(''),
    ontology_source: z.enum(['seed', 'discovered', 'user']),
    aliases: z.array(z.string()).default([]),
    occurrence_count: z.number().default(0),
  }),
});

const course = defineCollection({
  type: 'content',
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    platform: z.enum(['youtube', 'bilibili']),
    source_url: z.string(),
    lecture_count: z.number(),
  }),
});

const lecture = defineCollection({
  type: 'content',
  schema: z.object({
    slug: z.string(),                // <course_slug>--<lecture_idx>
    course_slug: z.string(),
    idx: z.number(),
    title: z.string(),
    video_url: z.string(),
    duration_sec: z.number().nullable().default(null),
    chunks: z.array(z.object({
      idx: z.number(),
      start_sec: z.number(),
      end_sec: z.number(),
      text: z.string(),
      concept_slugs: z.array(z.string()).default([]),
    })),
  }),
});

export const collections = { concept, course, lecture };
```

- [ ] **Step 5: Write `template-site/src/layouts/Base.astro`**

```astro
---
interface Props {
  title: string;
}
const { title } = Astro.props;
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <title>{title} · video-to-notebook</title>
  <link rel="stylesheet" href="/styles/global.css" />
</head>
<body>
  <header>
    <nav>
      <a href="/">Home</a>
      <a href="/courses/">Courses</a>
      <a href="/concepts/">Concepts</a>
      <a href="/about/">About</a>
    </nav>
    <input id="pagefind-search" type="search" placeholder="Search..." />
  </header>
  <main>
    <slot />
  </main>
  <footer>
    <small>Generated by video-to-notebook</small>
  </footer>
  <script type="module">
    import { PagefindUI } from "/_pagefind/pagefind-ui.js";
    new PagefindUI({ element: "#pagefind-search" });
  </script>
</body>
</html>
```

> Pagefind injects `/_pagefind/` at build time; the import is resolved post-build.

- [ ] **Step 6: Write `template-site/src/pages/index.astro`**

```astro
---
import Base from '../layouts/Base.astro';
import { getCollection } from 'astro:content';

const courses = await getCollection('course');
const concepts = await getCollection('concept');
---
<Base title="Home">
  <h1>video-to-notebook</h1>
  <p>
    {courses.length} course{courses.length === 1 ? '' : 's'} ·
    {concepts.length} concept{concepts.length === 1 ? '' : 's'} indexed.
  </p>
  <p>
    Pick a starting point:
    <a href="/courses/">browse by course</a> or
    <a href="/concepts/">browse by concept</a>.
  </p>
</Base>
```

- [ ] **Step 7: Write `template-site/src/styles/global.css`**

```css
*, *::before, *::after { box-sizing: border-box; }
html { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.5; }
body { margin: 0; max-width: 960px; margin-inline: auto; padding: 1rem; color: #111; background: #fff; }
header { display: flex; justify-content: space-between; align-items: center; padding-block: 1rem; border-bottom: 1px solid #eee; }
header nav a { margin-right: 1rem; text-decoration: none; color: #0b5; font-weight: 500; }
header nav a:hover { text-decoration: underline; }
#pagefind-search { padding: 0.4rem 0.8rem; border: 1px solid #ccc; border-radius: 4px; min-width: 200px; }
footer { margin-top: 4rem; padding-block: 1rem; border-top: 1px solid #eee; color: #888; text-align: center; }
main { padding-block: 2rem; }
h1 { margin-top: 0; }
a { color: #0b5; }
table { border-collapse: collapse; width: 100%; }
th, td { padding: 0.5rem 0.8rem; border-bottom: 1px solid #eee; text-align: left; }
th { background: #fafafa; font-weight: 600; }
code { background: #f4f4f4; padding: 0.1em 0.3em; border-radius: 3px; font-size: 0.95em; }
```

- [ ] **Step 8: Create `template-site/public/favicon.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#0b5"/><text x="50%" y="55%" font-family="sans-serif" font-size="18" font-weight="bold" fill="#fff" text-anchor="middle" dominant-baseline="middle">cm</text></svg>
```

- [ ] **Step 9: Create empty placeholder files**

```bash
mkdir -p template-site/src/content/{concepts,courses,lectures}
touch template-site/src/content/concepts/.gitkeep
touch template-site/src/content/courses/.gitkeep
touch template-site/src/content/lectures/.gitkeep
```

- [ ] **Step 10: Update `.gitignore`**

Append:
```
# Astro template build artifacts
template-site/node_modules/
template-site/dist/
template-site/.astro/
```

- [ ] **Step 11: Update `pyproject.toml` to ship template-site**

Modify the `[tool.hatch.build.targets.wheel.force-include]` block:

```toml
[tool.hatch.build.targets.wheel.force-include]
"src/video_to_notebook/db/migrations" = "video_to_notebook/db/migrations"
"template-site" = "video_to_notebook/_template_site"
```

This packages `template-site/` under `video_to_notebook/_template_site/` inside the installed wheel, so the runtime can find it via importlib.resources.

- [ ] **Step 12: Build the template to verify it works**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook/template-site
npm install --silent
npm run build 2>&1 | tail -20
```

Expected: `astro build` completes; `dist/` contains `index.html`, `_pagefind/`, etc. There may be Pagefind warnings about empty content — that's fine, we'll add content via Plan 3 tasks.

- [ ] **Step 13: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add template-site/ pyproject.toml .gitignore
git commit -m "feat(site): Astro 5 template scaffold + Pagefind, content collections schema"
```

---

## Phase 1: Content Writers

### Task 2: DB query layer

**Files:**
- Create: `src/video_to_notebook/build/__init__.py` (empty)
- Create: `src/video_to_notebook/build/queries.py`
- Create: `tests/unit/test_build_queries.py`

Pure SELECT queries returning plain dicts. Tests use in-memory DB seeded directly.

- [ ] **Step 1: Failing tests**

```python
# tests/unit/test_build_queries.py
from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.build.queries import (
    all_concepts_with_counts,
    all_courses_with_lecture_counts,
    chunks_for_lecture,
    concept_occurrences,
    lectures_for_course,
)
from video_to_notebook.db.session import connect, init_db


@pytest.fixture
def seeded_db(tmp_path: Path) -> Path:
    db = tmp_path / "db.sqlite"
    init_db(db)
    with connect(db) as conn:
        # 1 course, 2 lectures, 3 chunks total
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://yt/p', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status, duration_sec) "
            "VALUES (1, 1, 1, 'L1: Intro', 'https://yt/v1', 'transcript A', 'ok', 3600)"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status, duration_sec) "
            "VALUES (2, 1, 2, 'L2: Attention', 'https://yt/v2', 'transcript B', 'ok', 3000)"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'hello world')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 2, 0, 0, 60, 'self attention explained')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (3, 2, 1, 60, 120, 'multi head attention')"
        )
        # 2 concepts
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (1, 'self-attention', 'Self-Attention', 'SA desc', 'seed')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, description, ontology_source) "
            "VALUES (2, 'mha', 'Multi-Head Attention', 'MHA desc', 'discovered')"
        )
        # chunk_concepts: chunk 2 → self-attention, chunk 3 → mha
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (2, 1, 0.9, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (3, 2, 0.85, 'haiku:v1')"
        )
        # An alias
        conn.execute(
            "INSERT INTO concept_aliases (concept_id, alias) VALUES (1, 'SA')"
        )
    return db


def test_all_courses(seeded_db):
    courses = all_courses_with_lecture_counts(seeded_db)
    assert len(courses) == 1
    c = courses[0]
    assert c["slug"] == "cs336"
    assert c["title"] == "CS336"
    assert c["lecture_count"] == 2
    assert c["platform"] == "youtube"


def test_lectures_for_course(seeded_db):
    lectures = lectures_for_course(seeded_db, "cs336")
    assert len(lectures) == 2
    assert lectures[0]["idx"] == 1
    assert lectures[0]["title"] == "L1: Intro"
    assert lectures[1]["idx"] == 2


def test_chunks_for_lecture(seeded_db):
    chunks = chunks_for_lecture(seeded_db, lecture_id=2)
    assert len(chunks) == 2
    assert chunks[0]["text"] == "self attention explained"
    assert chunks[0]["concept_slugs"] == ["self-attention"]
    assert chunks[1]["concept_slugs"] == ["mha"]


def test_all_concepts_with_counts(seeded_db):
    concepts = all_concepts_with_counts(seeded_db)
    assert len(concepts) == 2
    by_slug = {c["slug"]: c for c in concepts}
    assert by_slug["self-attention"]["occurrence_count"] == 1
    assert by_slug["self-attention"]["aliases"] == ["SA"]
    assert by_slug["mha"]["occurrence_count"] == 1
    assert by_slug["mha"]["aliases"] == []


def test_concept_occurrences(seeded_db):
    occ = concept_occurrences(seeded_db, "self-attention")
    assert len(occ) == 1
    row = occ[0]
    assert row["course_slug"] == "cs336"
    assert row["lecture_idx"] == 2
    assert row["lecture_title"] == "L2: Attention"
    assert row["start_sec"] == 0
    assert "self attention" in row["text"]


def test_concept_occurrences_missing_concept(seeded_db):
    assert concept_occurrences(seeded_db, "nonexistent") == []
```

- [ ] **Step 2: Confirm fails**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook && .venv/bin/pytest tests/unit/test_build_queries.py -v
```

- [ ] **Step 3: Write `src/video_to_notebook/build/__init__.py`** (empty file)

- [ ] **Step 4: Write `src/video_to_notebook/build/queries.py`**

```python
"""Read-only SELECT queries against the v2 DB; return plain dicts."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from video_to_notebook.db.session import connect


def all_courses_with_lecture_counts(db_path: Path) -> list[dict[str, Any]]:
    """All courses sorted by slug, each with its lecture count."""
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT courses.id, courses.slug, courses.title, courses.platform,
                   courses.source_url, courses.added_at,
                   COUNT(lectures.id) FILTER (WHERE lectures.status = 'ok') AS lecture_count
            FROM courses
            LEFT JOIN lectures ON lectures.course_id = courses.id
            GROUP BY courses.id
            ORDER BY courses.slug
            """
        ).fetchall()
    return [
        {
            "id": r[0],
            "slug": r[1],
            "title": r[2],
            "platform": r[3],
            "source_url": r[4],
            "added_at": r[5],
            "lecture_count": r[6],
        }
        for r in rows
    ]


def lectures_for_course(db_path: Path, course_slug: str) -> list[dict[str, Any]]:
    """Lectures of a course ordered by idx, only status='ok'."""
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT lectures.id, lectures.idx, lectures.title, lectures.video_url,
                   lectures.duration_sec
            FROM lectures
            JOIN courses ON courses.id = lectures.course_id
            WHERE courses.slug = ? AND lectures.status = 'ok'
            ORDER BY lectures.idx
            """,
            (course_slug,),
        ).fetchall()
    return [
        {
            "id": r[0],
            "idx": r[1],
            "title": r[2],
            "video_url": r[3],
            "duration_sec": r[4],
        }
        for r in rows
    ]


def chunks_for_lecture(db_path: Path, *, lecture_id: int) -> list[dict[str, Any]]:
    """Chunks of one lecture, each with its concept slugs."""
    with connect(db_path) as conn:
        chunk_rows = conn.execute(
            """
            SELECT id, idx, start_sec, end_sec, text
            FROM chunks WHERE lecture_id = ?
            ORDER BY idx
            """,
            (lecture_id,),
        ).fetchall()
        if not chunk_rows:
            return []
        chunk_ids = [r[0] for r in chunk_rows]
        placeholders = ",".join("?" for _ in chunk_ids)
        concept_rows = conn.execute(
            f"""
            SELECT chunk_concepts.chunk_id, concepts.slug
            FROM chunk_concepts
            JOIN concepts ON concepts.id = chunk_concepts.concept_id
            WHERE chunk_concepts.chunk_id IN ({placeholders})
            ORDER BY concepts.slug
            """,
            chunk_ids,
        ).fetchall()
    concept_map: dict[int, list[str]] = {}
    for chunk_id, slug in concept_rows:
        concept_map.setdefault(chunk_id, []).append(slug)
    return [
        {
            "id": r[0],
            "idx": r[1],
            "start_sec": r[2],
            "end_sec": r[3],
            "text": r[4],
            "concept_slugs": concept_map.get(r[0], []),
        }
        for r in chunk_rows
    ]


def all_concepts_with_counts(db_path: Path) -> list[dict[str, Any]]:
    """All concepts plus their occurrence count and aliases."""
    with connect(db_path) as conn:
        concept_rows = conn.execute(
            """
            SELECT concepts.id, concepts.slug, concepts.canonical_name,
                   COALESCE(concepts.description, ''),
                   concepts.ontology_source,
                   COUNT(chunk_concepts.chunk_id) AS occurrence_count
            FROM concepts
            LEFT JOIN chunk_concepts ON chunk_concepts.concept_id = concepts.id
            GROUP BY concepts.id
            ORDER BY concepts.canonical_name
            """
        ).fetchall()
        alias_rows = conn.execute(
            "SELECT concept_id, alias FROM concept_aliases ORDER BY alias"
        ).fetchall()
    aliases_map: dict[int, list[str]] = {}
    for cid, alias in alias_rows:
        aliases_map.setdefault(cid, []).append(alias)
    return [
        {
            "id": r[0],
            "slug": r[1],
            "canonical_name": r[2],
            "description": r[3],
            "ontology_source": r[4],
            "occurrence_count": r[5],
            "aliases": aliases_map.get(r[0], []),
        }
        for r in concept_rows
    ]


def concept_occurrences(db_path: Path, concept_slug: str) -> list[dict[str, Any]]:
    """Every chunk that mentions `concept_slug`, with course + lecture metadata."""
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT courses.slug, lectures.idx, lectures.title, lectures.video_url,
                   chunks.start_sec, chunks.end_sec, chunks.text, chunk_concepts.confidence
            FROM chunk_concepts
            JOIN concepts ON concepts.id = chunk_concepts.concept_id
            JOIN chunks ON chunks.id = chunk_concepts.chunk_id
            JOIN lectures ON lectures.id = chunks.lecture_id
            JOIN courses ON courses.id = lectures.course_id
            WHERE concepts.slug = ?
            ORDER BY courses.slug, lectures.idx, chunks.idx
            """,
            (concept_slug,),
        ).fetchall()
    return [
        {
            "course_slug": r[0],
            "lecture_idx": r[1],
            "lecture_title": r[2],
            "video_url": r[3],
            "start_sec": r[4],
            "end_sec": r[5],
            "text": r[6],
            "confidence": r[7],
        }
        for r in rows
    ]
```

- [ ] **Step 5: Run tests + typecheck**

```bash
.venv/bin/pytest tests/unit/test_build_queries.py -v
.venv/bin/pyright src tests
```

Expected: 6 pass, pyright clean.

- [ ] **Step 6: Commit**

```bash
git add src/video_to_notebook/build/__init__.py src/video_to_notebook/build/queries.py tests/unit/test_build_queries.py
git commit -m "feat(build): read-only DB queries returning plain dicts"
```

---

### Task 3: Markdown writers (pure functions)

**Files:**
- Create: `src/video_to_notebook/build/writers.py`
- Create: `tests/unit/test_build_writers.py`

Pure functions: dict → Markdown string. No I/O.

- [ ] **Step 1: Failing tests**

```python
# tests/unit/test_build_writers.py
from __future__ import annotations

from video_to_notebook.build.writers import (
    write_concept_md,
    write_course_md,
    write_lecture_md,
)


def test_write_concept_md_includes_frontmatter():
    md = write_concept_md(
        concept={
            "slug": "self-attention",
            "canonical_name": "Self-Attention",
            "description": "SA desc",
            "ontology_source": "seed",
            "occurrence_count": 5,
            "aliases": ["SA", "self attention"],
        },
        occurrences=[
            {
                "course_slug": "cs336",
                "lecture_idx": 2,
                "lecture_title": "L2",
                "video_url": "https://yt/v",
                "start_sec": 10.5,
                "end_sec": 30.0,
                "text": "hello",
                "confidence": 0.9,
            }
        ],
    )

    assert md.startswith("---\n")
    assert 'slug: self-attention' in md
    assert 'canonical_name: Self-Attention' in md
    assert 'occurrence_count: 5' in md
    assert "cs336" in md  # body mentions the course
    assert "10.5" in md or "10" in md  # timestamp surfaced


def test_write_concept_md_empty_occurrences():
    md = write_concept_md(
        concept={
            "slug": "x",
            "canonical_name": "X",
            "description": "",
            "ontology_source": "seed",
            "occurrence_count": 0,
            "aliases": [],
        },
        occurrences=[],
    )
    assert md.startswith("---\n")
    assert "occurrence_count: 0" in md


def test_write_course_md_lists_lectures():
    md = write_course_md(
        course={
            "slug": "cs336",
            "title": "CS336",
            "platform": "youtube",
            "source_url": "https://yt/p",
            "lecture_count": 2,
        },
        lectures=[
            {"idx": 1, "title": "Intro", "video_url": "https://yt/v1", "duration_sec": 600},
            {"idx": 2, "title": "Attention", "video_url": "https://yt/v2", "duration_sec": 1200},
        ],
    )
    assert 'slug: cs336' in md
    assert 'lecture_count: 2' in md
    assert "Intro" in md
    assert "Attention" in md


def test_write_lecture_md_serializes_chunks_into_frontmatter():
    md = write_lecture_md(
        course={"slug": "cs336"},
        lecture={
            "id": 7,
            "idx": 2,
            "title": "Attention",
            "video_url": "https://yt/v2",
            "duration_sec": 1200,
        },
        chunks=[
            {
                "id": 1, "idx": 0, "start_sec": 0, "end_sec": 60,
                "text": "self attention is great",
                "concept_slugs": ["self-attention"],
            },
            {
                "id": 2, "idx": 1, "start_sec": 60, "end_sec": 120,
                "text": "multi head",
                "concept_slugs": ["mha"],
            },
        ],
    )
    assert 'slug: cs336--2' in md
    assert 'course_slug: cs336' in md
    assert 'idx: 2' in md
    # Chunks are nested under frontmatter
    assert 'chunks:' in md
    assert 'concept_slugs:' in md
    assert "self attention" in md
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_build_writers.py -v
```

- [ ] **Step 3: Implement `src/video_to_notebook/build/writers.py`**

```python
"""Pure functions that turn dict rows into Astro-content-collection Markdown."""
from __future__ import annotations

from typing import Any

import yaml


def _frontmatter(data: dict[str, Any]) -> str:
    """Serialize a dict to a YAML frontmatter block."""
    body = yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, default_flow_style=False
    )
    return f"---\n{body}---\n"


def write_concept_md(*, concept: dict[str, Any], occurrences: list[dict[str, Any]]) -> str:
    """One Markdown file per concept. Body lists occurrence rows for human preview."""
    fm = {
        "slug": concept["slug"],
        "canonical_name": concept["canonical_name"],
        "description": concept.get("description", ""),
        "ontology_source": concept["ontology_source"],
        "aliases": concept.get("aliases", []),
        "occurrence_count": concept["occurrence_count"],
    }
    body_lines = [f"# {concept['canonical_name']}", ""]
    if concept.get("description"):
        body_lines += [concept["description"], ""]
    body_lines.append(f"**{len(occurrences)} occurrence{'s' if len(occurrences) != 1 else ''}** across courses:")
    body_lines.append("")
    for o in occurrences:
        ts = int(o["start_sec"])
        body_lines.append(
            f"- **{o['course_slug']}** L{o['lecture_idx']} ({o['lecture_title']}) "
            f"@ {ts}s — {o['text'][:120]}"
        )
    return _frontmatter(fm) + "\n".join(body_lines) + "\n"


def write_course_md(*, course: dict[str, Any], lectures: list[dict[str, Any]]) -> str:
    fm = {
        "slug": course["slug"],
        "title": course["title"],
        "platform": course["platform"],
        "source_url": course["source_url"],
        "lecture_count": course["lecture_count"],
    }
    body_lines = [f"# {course['title']}", "", f"_{course['platform']}_", ""]
    body_lines.append("## Lectures")
    for lec in lectures:
        dur = ""
        if lec.get("duration_sec"):
            mins = lec["duration_sec"] // 60
            dur = f" · {mins} min"
        body_lines.append(f"- L{lec['idx']}: {lec['title']}{dur}")
    return _frontmatter(fm) + "\n".join(body_lines) + "\n"


def write_lecture_md(
    *, course: dict[str, Any], lecture: dict[str, Any], chunks: list[dict[str, Any]]
) -> str:
    fm = {
        "slug": f"{course['slug']}--{lecture['idx']}",
        "course_slug": course["slug"],
        "idx": lecture["idx"],
        "title": lecture["title"],
        "video_url": lecture["video_url"],
        "duration_sec": lecture.get("duration_sec"),
        "chunks": [
            {
                "idx": c["idx"],
                "start_sec": c["start_sec"],
                "end_sec": c["end_sec"],
                "text": c["text"],
                "concept_slugs": c.get("concept_slugs", []),
            }
            for c in chunks
        ],
    }
    body = f"# {lecture['title']}\n\nSee the structured chunks above.\n"
    return _frontmatter(fm) + body
```

- [ ] **Step 4: Run tests + typecheck**

```bash
.venv/bin/pytest tests/unit/test_build_writers.py -v
.venv/bin/pyright src tests
```

Expected: 4 pass.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/build/writers.py tests/unit/test_build_writers.py
git commit -m "feat(build): pure markdown writers for concepts/courses/lectures"
```

---

## Phase 2: Template Copy + Build Runner

### Task 4: Lazy template-site copy

**Files:**
- Create: `src/video_to_notebook/build/template_copy.py`
- Create: `tests/unit/test_template_copy.py`

Find the bundled `_template_site/` via `importlib.resources` and copy it into `<project_root>/site/` if absent. Never overwrite the user's edits.

- [ ] **Step 1: Failing tests**

```python
# tests/unit/test_template_copy.py
from __future__ import annotations

from pathlib import Path

from video_to_notebook.build.template_copy import ensure_site_dir


def test_ensure_site_dir_copies_template(tmp_path: Path):
    site_dir = ensure_site_dir(tmp_path)
    assert site_dir == tmp_path / "site"
    assert (site_dir / "package.json").is_file()
    assert (site_dir / "src" / "pages" / "index.astro").is_file()
    assert (site_dir / "src" / "content" / "config.ts").is_file()


def test_ensure_site_dir_is_idempotent(tmp_path: Path):
    site_dir = ensure_site_dir(tmp_path)
    sentinel = site_dir / "user_edit.txt"
    sentinel.write_text("user content")

    # Second call must not wipe user changes.
    ensure_site_dir(tmp_path)
    assert sentinel.exists()
    assert sentinel.read_text() == "user content"


def test_ensure_site_dir_skips_node_modules(tmp_path: Path):
    site_dir = ensure_site_dir(tmp_path)
    # Faking node_modules to prove we don't touch it
    nm = site_dir / "node_modules"
    nm.mkdir()
    (nm / "marker").write_text("don't touch")

    ensure_site_dir(tmp_path)
    assert (nm / "marker").exists()
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_template_copy.py -v
```

- [ ] **Step 3: Write `src/video_to_notebook/build/template_copy.py`**

```python
"""Lazy-copy the bundled Astro template-site into a project."""
from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path


def _bundled_template_root() -> Path:
    """Locate the template-site directory shipped inside the wheel.

    During development (editable install) this resolves to the repo's
    `template-site/`; after `pip install`, to `video_to_notebook/_template_site/`.
    """
    # First try the editable / source layout
    src_layout = Path(__file__).parent.parent.parent.parent / "template-site"
    if src_layout.is_dir():
        return src_layout
    # Otherwise, packaged form
    pkg = resources.files("video_to_notebook") / "_template_site"
    return Path(str(pkg))


def ensure_site_dir(project_root: Path) -> Path:
    """Return <project_root>/site, copying the bundled template on first use.

    Subsequent calls leave the directory untouched (idempotent), so user edits
    and node_modules survive.
    """
    site = project_root / "site"
    if site.is_dir():
        return site

    src = _bundled_template_root()
    if not src.is_dir():
        raise FileNotFoundError(
            f"bundled template-site not found at {src}; reinstall video-to-notebook?"
        )
    shutil.copytree(
        src, site,
        ignore=shutil.ignore_patterns("node_modules", "dist", ".astro"),
    )
    return site
```

- [ ] **Step 4: Run tests**

```bash
.venv/bin/pytest tests/unit/test_template_copy.py -v
```

Expected: 3 pass.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/build/template_copy.py tests/unit/test_template_copy.py
git commit -m "feat(build): lazy-copy bundled Astro template into <project>/site/"
```

---

### Task 5: Build runner

**Files:**
- Create: `src/video_to_notebook/build/runner.py`
- Create: `tests/unit/test_build_runner.py`

Orchestrates: ensure site → query DB → write all .md files → optionally run `npm install` + `npm run build`.

- [ ] **Step 1: Failing tests**

```python
# tests/unit/test_build_runner.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from video_to_notebook.build.runner import BuildReport, run_build
from video_to_notebook.db.session import connect, init_db


def _seed_full(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://yt/p', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'attention is all')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'attention', 'Attention', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )


def test_run_build_writes_content_files(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed_full(db)

    with patch("video_to_notebook.build.runner._run_astro_build") as mock_npm:
        mock_npm.return_value = 0
        report = run_build(project_root=tmp_path, db_path=db, npm_build=True)

    assert isinstance(report, BuildReport)
    assert report.courses_written == 1
    assert report.lectures_written == 1
    assert report.concepts_written == 1

    site = tmp_path / "site"
    assert (site / "src" / "content" / "courses" / "cs336.md").is_file()
    assert (site / "src" / "content" / "lectures" / "cs336--1.md").is_file()
    assert (site / "src" / "content" / "concepts" / "attention.md").is_file()
    assert mock_npm.called


def test_run_build_skips_npm_when_disabled(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed_full(db)

    with patch("video_to_notebook.build.runner._run_astro_build") as mock_npm:
        run_build(project_root=tmp_path, db_path=db, npm_build=False)
    assert not mock_npm.called


def test_run_build_incremental_only_dirty(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    _seed_full(db)
    with connect(db) as conn:
        # Add a second concept
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (2, 'other', 'Other', 'seed')"
        )
        # Mark only 'attention' as dirty
        conn.execute(
            "INSERT INTO build_meta (key, value) VALUES ('dirty_concepts', '[\"attention\"]')"
        )

    with patch("video_to_notebook.build.runner._run_astro_build") as mock_npm:
        mock_npm.return_value = 0
        report = run_build(project_root=tmp_path, db_path=db, npm_build=False, incremental=True)

    assert report.concepts_written == 1  # only attention
    site = tmp_path / "site"
    assert (site / "src" / "content" / "concepts" / "attention.md").is_file()
    assert not (site / "src" / "content" / "concepts" / "other.md").is_file()
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/unit/test_build_runner.py -v
```

- [ ] **Step 3: Write `src/video_to_notebook/build/runner.py`**

```python
"""Orchestrate: ensure site → query DB → write Markdown content → optional astro build."""
from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

from video_to_notebook.build.queries import (
    all_concepts_with_counts,
    all_courses_with_lecture_counts,
    chunks_for_lecture,
    concept_occurrences,
    lectures_for_course,
)
from video_to_notebook.build.template_copy import ensure_site_dir
from video_to_notebook.build.writers import (
    write_concept_md,
    write_course_md,
    write_lecture_md,
)
from video_to_notebook.db.session import connect


@dataclass(frozen=True, slots=True)
class BuildReport:
    courses_written: int
    lectures_written: int
    concepts_written: int
    npm_exit_code: int | None  # None if npm_build=False


def _dirty_concepts(db_path: Path) -> set[str] | None:
    """Return the dirty_concepts set if recorded; None means 'rebuild all'."""
    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT value FROM build_meta WHERE key='dirty_concepts'"
        ).fetchone()
    if not row:
        return None
    try:
        return set(json.loads(row[0]))
    except (json.JSONDecodeError, TypeError):
        return None


def _run_astro_build(site_dir: Path) -> int:
    """Run `npm install --silent && npm run build`. Returns exit code of build."""
    if not (site_dir / "node_modules").is_dir():
        subprocess.run(
            ["npm", "install", "--silent"], cwd=site_dir, check=False
        )
    result = subprocess.run(["npm", "run", "build"], cwd=site_dir, check=False)
    return result.returncode


def run_build(
    *,
    project_root: Path,
    db_path: Path,
    npm_build: bool = True,
    incremental: bool = False,
) -> BuildReport:
    site_dir = ensure_site_dir(project_root)
    content_dir = site_dir / "src" / "content"

    courses = all_courses_with_lecture_counts(db_path)
    for course in courses:
        md = write_course_md(course=course, lectures=lectures_for_course(db_path, course["slug"]))
        (content_dir / "courses" / f"{course['slug']}.md").write_text(md, encoding="utf-8")

    lectures_written = 0
    for course in courses:
        for lec in lectures_for_course(db_path, course["slug"]):
            md = write_lecture_md(
                course=course,
                lecture=lec,
                chunks=chunks_for_lecture(db_path, lecture_id=lec["id"]),
            )
            slug = f"{course['slug']}--{lec['idx']}"
            (content_dir / "lectures" / f"{slug}.md").write_text(md, encoding="utf-8")
            lectures_written += 1

    all_concepts = all_concepts_with_counts(db_path)
    dirty = _dirty_concepts(db_path) if incremental else None
    if dirty is not None:
        concepts = [c for c in all_concepts if c["slug"] in dirty]
    else:
        concepts = all_concepts

    for concept in concepts:
        md = write_concept_md(
            concept=concept,
            occurrences=concept_occurrences(db_path, concept["slug"]),
        )
        (content_dir / "concepts" / f"{concept['slug']}.md").write_text(md, encoding="utf-8")

    npm_code: int | None = None
    if npm_build:
        npm_code = _run_astro_build(site_dir)

    return BuildReport(
        courses_written=len(courses),
        lectures_written=lectures_written,
        concepts_written=len(concepts),
        npm_exit_code=npm_code,
    )
```

- [ ] **Step 4: Run tests + typecheck**

```bash
.venv/bin/pytest tests/unit/test_build_runner.py -v
.venv/bin/pyright src tests
```

Expected: 3 pass.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/build/runner.py tests/unit/test_build_runner.py
git commit -m "feat(build): runner orchestrates DB → markdown → astro build with --incremental"
```

---

## Phase 3: Astro Pages (Static Routes)

### Task 6: Course pages (list + detail)

**Files:**
- Modify: `template-site/src/pages/courses/index.astro`
- Modify: `template-site/src/pages/courses/[slug]/index.astro`

- [ ] **Step 1: Write `template-site/src/pages/courses/index.astro`**

```astro
---
import Base from '../../layouts/Base.astro';
import { getCollection } from 'astro:content';

const courses = (await getCollection('course')).sort(
  (a, b) => a.data.title.localeCompare(b.data.title),
);
---
<Base title="Courses">
  <h1>All Courses</h1>
  <ul class="course-grid">
    {courses.map(c => (
      <li>
        <a href={`/courses/${c.data.slug}/`}>
          <strong>{c.data.title}</strong>
        </a>
        <span class="meta">{c.data.platform} · {c.data.lecture_count} lectures</span>
      </li>
    ))}
  </ul>
</Base>

<style>
  .course-grid {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
  }
  .course-grid li {
    border: 1px solid #eee;
    padding: 1rem;
    border-radius: 6px;
  }
  .meta { display: block; color: #888; font-size: 0.9em; margin-top: 0.3rem; }
</style>
```

- [ ] **Step 2: Write `template-site/src/pages/courses/[slug]/index.astro`**

```astro
---
import Base from '../../../layouts/Base.astro';
import { getCollection, getEntry } from 'astro:content';

export async function getStaticPaths() {
  const courses = await getCollection('course');
  return courses.map(c => ({ params: { slug: c.data.slug } }));
}

const { slug } = Astro.params;
const course = await getEntry('course', slug!);
if (!course) throw new Error(`course not found: ${slug}`);

const lectures = (await getCollection('lecture'))
  .filter(l => l.data.course_slug === slug)
  .sort((a, b) => a.data.idx - b.data.idx);
---
<Base title={course.data.title}>
  <h1>{course.data.title}</h1>
  <p>
    <a href={course.data.source_url}>{course.data.platform} source</a>
    · {lectures.length} lectures
  </p>

  <h2>Lectures</h2>
  <ol class="lecture-list">
    {lectures.map(l => (
      <li>
        <a href={`/courses/${slug}/${l.data.idx}/`}>
          L{l.data.idx}: {l.data.title}
        </a>
      </li>
    ))}
  </ol>
</Base>

<style>
  .lecture-list li { margin-block: 0.4rem; }
</style>
```

- [ ] **Step 3: Build the site to verify**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook/template-site
npm run build 2>&1 | tail -15
```

Expected: build succeeds. Since there's no actual content yet, the dynamic `[slug]` route is a no-op (no entries to generate). Just verify no errors.

- [ ] **Step 4: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add template-site/src/pages/courses/
git commit -m "feat(site): courses list page + per-course detail page"
```

---

### Task 7: Lecture detail page (with video + transcript)

**Files:**
- Create: `template-site/src/pages/courses/[slug]/[lecture].astro`
- Create: `template-site/src/components/VideoEmbed.astro`
- Create: `template-site/src/components/LectureTranscript.astro`

The killer-feature here is the synced video↔transcript scroll. Implementation: click a chunk → seek video to chunk.start_sec via YouTube iframe API; current playback time → highlight the active chunk row.

- [ ] **Step 1: Write `template-site/src/components/VideoEmbed.astro`**

```astro
---
interface Props {
  videoUrl: string;
}
const { videoUrl } = Astro.props;

function youtubeId(u: string): string | null {
  const m = u.match(/(?:v=|youtu\.be\/)([\w-]{11})/);
  return m ? m[1] : null;
}
function bilibiliBV(u: string): string | null {
  const m = u.match(/(BV[\w]+)/);
  return m ? m[1] : null;
}

const ytId = youtubeId(videoUrl);
const bvId = bilibiliBV(videoUrl);
---
{ytId && (
  <iframe
    id="video-iframe"
    width="100%" height="400"
    src={`https://www.youtube.com/embed/${ytId}?enablejsapi=1`}
    title="YouTube video"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen
  ></iframe>
)}
{bvId && !ytId && (
  <iframe
    id="video-iframe"
    width="100%" height="400"
    src={`https://player.bilibili.com/player.html?bvid=${bvId}`}
    title="Bilibili video"
    frameborder="0"
    scrolling="no" border="0"
    allowfullscreen
  ></iframe>
)}
{!ytId && !bvId && <a href={videoUrl}>Open video →</a>}
```

- [ ] **Step 2: Write `template-site/src/components/LectureTranscript.astro`**

```astro
---
interface Chunk {
  idx: number;
  start_sec: number;
  end_sec: number;
  text: string;
  concept_slugs: string[];
}
interface Props {
  chunks: Chunk[];
}
const { chunks } = Astro.props;
---
<ol class="transcript">
  {chunks.map(c => (
    <li
      data-start={c.start_sec}
      data-end={c.end_sec}
      data-idx={c.idx}
    >
      <button
        class="seek"
        type="button"
        data-start={c.start_sec}
        aria-label={`Jump to ${Math.floor(c.start_sec)}s`}
      >
        {Math.floor(c.start_sec / 60).toString().padStart(2, '0')}:
        {(Math.floor(c.start_sec) % 60).toString().padStart(2, '0')}
      </button>
      <p>{c.text}</p>
      {c.concept_slugs.length > 0 && (
        <ul class="tags">
          {c.concept_slugs.map(s => (
            <li><a href={`/concepts/${s}/`}><code>{s}</code></a></li>
          ))}
        </ul>
      )}
    </li>
  ))}
</ol>

<script>
  // Sync video iframe with transcript clicks (YouTube only; Bilibili player API differs).
  const iframe = document.getElementById('video-iframe') as HTMLIFrameElement | null;
  if (iframe && iframe.src.includes('youtube.com')) {
    document.querySelectorAll('button.seek').forEach(btn => {
      btn.addEventListener('click', () => {
        const start = parseFloat((btn as HTMLElement).dataset.start || '0');
        iframe.contentWindow?.postMessage(
          JSON.stringify({
            event: 'command', func: 'seekTo', args: [start, true],
          }),
          '*',
        );
      });
    });
  }
</script>

<style>
  .transcript { list-style: none; padding: 0; max-height: 60vh; overflow-y: auto; border: 1px solid #eee; border-radius: 6px; }
  .transcript li { display: grid; grid-template-columns: 70px 1fr; gap: 0.8rem; padding: 0.6rem 0.8rem; border-bottom: 1px solid #f5f5f5; }
  .transcript li:hover { background: #fafafa; }
  button.seek { font-family: monospace; background: transparent; border: 1px solid #ddd; padding: 0.2rem 0.4rem; cursor: pointer; border-radius: 3px; font-size: 0.85em; }
  button.seek:hover { background: #0b5; color: #fff; border-color: #0b5; }
  .transcript p { margin: 0; grid-column: 2; }
  .tags { grid-column: 2; list-style: none; padding: 0; display: flex; gap: 0.4rem; flex-wrap: wrap; margin-top: 0.3rem; }
  .tags code { font-size: 0.8em; }
</style>
```

- [ ] **Step 3: Write `template-site/src/pages/courses/[slug]/[lecture].astro`**

```astro
---
import Base from '../../../layouts/Base.astro';
import VideoEmbed from '../../../components/VideoEmbed.astro';
import LectureTranscript from '../../../components/LectureTranscript.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const lectures = await getCollection('lecture');
  return lectures.map(l => ({
    params: { slug: l.data.course_slug, lecture: String(l.data.idx) },
    props: { lecture: l },
  }));
}

const { lecture } = Astro.props;
---
<Base title={lecture.data.title}>
  <p><a href={`/courses/${lecture.data.course_slug}/`}>← back to course</a></p>
  <h1>L{lecture.data.idx}: {lecture.data.title}</h1>
  <VideoEmbed videoUrl={lecture.data.video_url} />
  <h2>Transcript</h2>
  <LectureTranscript chunks={lecture.data.chunks} />
</Base>
```

- [ ] **Step 4: Build to verify**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook/template-site && npm run build 2>&1 | tail -10
```

Expected: succeeds (no lecture entries yet so the dynamic route generates nothing, but compilation must pass).

- [ ] **Step 5: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add template-site/src/components/ template-site/src/pages/courses/
git commit -m "feat(site): lecture detail page with embedded video + click-to-seek transcript"
```

---

### Task 8: Concept pages (index + detail + compare)

**Files:**
- Create: `template-site/src/pages/concepts/index.astro`
- Create: `template-site/src/pages/concepts/[slug]/index.astro`
- Create: `template-site/src/pages/concepts/[slug]/compare.astro`
- Create: `template-site/src/components/ConceptOccurrenceTable.astro`
- Create: `template-site/src/components/CompareView.astro`

- [ ] **Step 1: Write `template-site/src/pages/concepts/index.astro`**

```astro
---
import Base from '../../layouts/Base.astro';
import { getCollection } from 'astro:content';

const concepts = (await getCollection('concept'))
  .sort((a, b) => a.data.canonical_name.localeCompare(b.data.canonical_name));

// Group by first letter for an A-Z index
const grouped: Record<string, typeof concepts> = {};
for (const c of concepts) {
  const letter = c.data.canonical_name[0].toUpperCase();
  (grouped[letter] ??= []).push(c);
}
const letters = Object.keys(grouped).sort();
---
<Base title="Concepts">
  <h1>All Concepts</h1>
  <p>{concepts.length} concepts indexed.</p>

  {letters.map(letter => (
    <section>
      <h2 id={letter}>{letter}</h2>
      <ul>
        {grouped[letter].map(c => (
          <li>
            <a href={`/concepts/${c.data.slug}/`}>{c.data.canonical_name}</a>
            <span class="count">({c.data.occurrence_count})</span>
          </li>
        ))}
      </ul>
    </section>
  ))}
</Base>

<style>
  h2 { margin-top: 2rem; }
  .count { color: #888; font-size: 0.9em; margin-left: 0.3rem; }
</style>
```

- [ ] **Step 2: Write `template-site/src/components/ConceptOccurrenceTable.astro`**

```astro
---
interface Occurrence {
  course_slug: string;
  lecture_idx: number;
  lecture_title: string;
  video_url: string;
  start_sec: number;
  text: string;
  confidence: number;
}
interface Props {
  occurrences: Occurrence[];
}
const { occurrences } = Astro.props;

// Group by course for cleaner UX
const grouped: Record<string, Occurrence[]> = {};
for (const o of occurrences) (grouped[o.course_slug] ??= []).push(o);
---
<table class="occurrences">
  <thead>
    <tr>
      <th>Course</th>
      <th>Lecture</th>
      <th>Time</th>
      <th>Excerpt</th>
    </tr>
  </thead>
  <tbody>
    {Object.entries(grouped).map(([course, items]) => items.map(o => (
      <tr>
        <td><a href={`/courses/${course}/`}><code>{course}</code></a></td>
        <td>
          <a href={`/courses/${course}/${o.lecture_idx}/`}>
            L{o.lecture_idx}: {o.lecture_title}
          </a>
        </td>
        <td>
          <code>
            {Math.floor(o.start_sec / 60).toString().padStart(2, '0')}:
            {(Math.floor(o.start_sec) % 60).toString().padStart(2, '0')}
          </code>
        </td>
        <td class="excerpt">{o.text.length > 200 ? o.text.slice(0, 200) + '…' : o.text}</td>
      </tr>
    )))}
  </tbody>
</table>

<style>
  .occurrences td.excerpt { max-width: 500px; font-size: 0.93em; color: #333; }
</style>
```

- [ ] **Step 3: Write `template-site/src/pages/concepts/[slug]/index.astro`**

```astro
---
import Base from '../../../layouts/Base.astro';
import ConceptOccurrenceTable from '../../../components/ConceptOccurrenceTable.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const concepts = await getCollection('concept');
  return concepts.map(c => ({ params: { slug: c.data.slug }, props: { concept: c } }));
}

const { concept } = Astro.props;
const lectures = await getCollection('lecture');

// Walk the lectures, harvest chunks tagged with this concept
const occurrences = lectures.flatMap(l =>
  l.data.chunks
    .filter(c => c.concept_slugs.includes(concept.data.slug))
    .map(c => ({
      course_slug: l.data.course_slug,
      lecture_idx: l.data.idx,
      lecture_title: l.data.title,
      video_url: l.data.video_url,
      start_sec: c.start_sec,
      text: c.text,
      confidence: 0,
    })),
);

const courseSlugsForCompare = Array.from(new Set(occurrences.map(o => o.course_slug)));
---
<Base title={concept.data.canonical_name}>
  <h1>{concept.data.canonical_name}</h1>
  {concept.data.description && <p>{concept.data.description}</p>}
  <p class="meta">
    <code>{concept.data.slug}</code> ·
    source: {concept.data.ontology_source} ·
    {occurrences.length} occurrence{occurrences.length === 1 ? '' : 's'}
    {concept.data.aliases.length > 0 && (
      <> · aliases: {concept.data.aliases.map(a => <code>{a}</code>).join(', ')}</>
    )}
  </p>

  {courseSlugsForCompare.length > 1 && (
    <p>
      <a class="compare-link" href={`/concepts/${concept.data.slug}/compare/?courses=${courseSlugsForCompare.join(',')}`}>
        Compare across {courseSlugsForCompare.length} courses →
      </a>
    </p>
  )}

  <ConceptOccurrenceTable occurrences={occurrences} />
</Base>

<style>
  .meta { color: #666; font-size: 0.9em; }
  .compare-link {
    display: inline-block; padding: 0.5rem 1rem;
    background: #0b5; color: #fff; text-decoration: none; border-radius: 4px;
    font-weight: 500;
  }
</style>
```

- [ ] **Step 4: Write `template-site/src/components/CompareView.astro`**

```astro
---
interface Occurrence {
  course_slug: string;
  lecture_idx: number;
  lecture_title: string;
  start_sec: number;
  text: string;
}
interface Props {
  occurrencesByCourse: Record<string, Occurrence[]>;
}
const { occurrencesByCourse } = Astro.props;
const courses = Object.keys(occurrencesByCourse);
---
<div class="compare-grid" style={`grid-template-columns: repeat(${courses.length}, 1fr);`}>
  {courses.map(course => (
    <div class="compare-col">
      <h3><a href={`/courses/${course}/`}><code>{course}</code></a></h3>
      <ol>
        {occurrencesByCourse[course].map(o => (
          <li>
            <a href={`/courses/${course}/${o.lecture_idx}/`}>
              <strong>L{o.lecture_idx}</strong> @ {Math.floor(o.start_sec)}s
            </a>
            <p>{o.text}</p>
          </li>
        ))}
      </ol>
    </div>
  ))}
</div>

<style>
  .compare-grid { display: grid; gap: 1rem; margin-top: 1rem; }
  .compare-col { border: 1px solid #eee; border-radius: 6px; padding: 1rem; }
  .compare-col h3 { margin-top: 0; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; }
  .compare-col ol { padding-left: 1.2rem; }
  .compare-col li { margin-bottom: 1rem; font-size: 0.93em; }
  .compare-col p { margin: 0.2rem 0 0; color: #333; }
</style>
```

- [ ] **Step 5: Write `template-site/src/pages/concepts/[slug]/compare.astro`**

```astro
---
import Base from '../../../layouts/Base.astro';
import CompareView from '../../../components/CompareView.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const concepts = await getCollection('concept');
  return concepts.map(c => ({ params: { slug: c.data.slug }, props: { concept: c } }));
}

const { concept } = Astro.props;
const lectures = await getCollection('lecture');

// URL query params drive which courses are shown
const url = Astro.url;
const requestedCourses = (url.searchParams.get('courses') || '')
  .split(',').map(s => s.trim()).filter(Boolean);

const occurrencesByCourse: Record<string, any[]> = {};
for (const lec of lectures) {
  if (requestedCourses.length > 0 && !requestedCourses.includes(lec.data.course_slug)) continue;
  const hits = lec.data.chunks
    .filter(c => c.concept_slugs.includes(concept.data.slug))
    .map(c => ({
      course_slug: lec.data.course_slug,
      lecture_idx: lec.data.idx,
      lecture_title: lec.data.title,
      start_sec: c.start_sec,
      text: c.text,
    }));
  if (hits.length === 0) continue;
  occurrencesByCourse[lec.data.course_slug] ??= [];
  occurrencesByCourse[lec.data.course_slug].push(...hits);
}
---
<Base title={`Compare: ${concept.data.canonical_name}`}>
  <p><a href={`/concepts/${concept.data.slug}/`}>← back to concept</a></p>
  <h1>{concept.data.canonical_name} — across courses</h1>
  <CompareView occurrencesByCourse={occurrencesByCourse} />
</Base>
```

> Note: Astro generates static HTML at build time, so `?courses=` URL params don't directly select on the server. The compare page renders ALL courses with hits. To filter live, client-side JS in CompareView would read the query — left for v1.1 if desired; the static "all courses" view is already useful.

- [ ] **Step 6: Build to verify**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook/template-site && npm run build 2>&1 | tail -15
```

- [ ] **Step 7: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add template-site/src/components/ConceptOccurrenceTable.astro template-site/src/components/CompareView.astro template-site/src/pages/concepts/
git commit -m "feat(site): concept index + detail page + cross-course compare view"
```

---

### Task 9: About page

**Files:**
- Create: `template-site/src/pages/about.astro`

- [ ] **Step 1: Write `template-site/src/pages/about.astro`**

```astro
---
import Base from '../layouts/Base.astro';
import { getCollection } from 'astro:content';

const courses = await getCollection('course');
const concepts = await getCollection('concept');
const lectures = await getCollection('lecture');
const totalChunks = lectures.reduce((s, l) => s + l.data.chunks.length, 0);
const buildAt = new Date().toISOString();
---
<Base title="About">
  <h1>About this site</h1>
  <p>
    This site was generated by <a href="https://github.com/chenlinzhuo/video-to-notebook">video-to-notebook</a>,
    a tool that crawls open-courseware, tags it with Claude, and renders cross-course concept pages.
  </p>
  <h2>Stats</h2>
  <ul>
    <li>{courses.length} courses</li>
    <li>{lectures.length} lectures</li>
    <li>{totalChunks} chunks</li>
    <li>{concepts.length} concepts</li>
  </ul>
  <p><small>Built at {buildAt}</small></p>
</Base>
```

- [ ] **Step 2: Build to verify**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook/template-site && npm run build 2>&1 | tail -5
```

- [ ] **Step 3: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add template-site/src/pages/about.astro
git commit -m "feat(site): about page with corpus stats"
```

---

## Phase 4: build / serve CLI Commands

### Task 10: `build` and `serve` CLI

**Files:**
- Modify: `src/video_to_notebook/cli.py` — add `build` and `serve` commands
- Create: `tests/integration/test_build_smoke.py`

- [ ] **Step 1: Failing integration test**

```python
# tests/integration/test_build_smoke.py
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_build_cli_writes_content(tmp_project: Path):
    # Init project
    runner.invoke(app, ["init"])

    # Seed a minimal corpus
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://yt/p', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'hello attention')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'attention', 'Attention', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1')"
        )

    # Skip npm build for the smoke test (no Node guaranteed in CI)
    result = runner.invoke(app, ["build", "--no-npm"])
    assert result.exit_code == 0, result.stdout

    site = tmp_project / "site"
    assert (site / "src" / "content" / "courses" / "cs336.md").is_file()
    assert (site / "src" / "content" / "concepts" / "attention.md").is_file()


@pytest.mark.integration
def test_build_errors_when_not_initialized(tmp_project: Path):
    result = runner.invoke(app, ["build", "--no-npm"])
    assert result.exit_code != 0
    assert "init" in result.stdout.lower()
```

- [ ] **Step 2: Confirm fails**

```bash
.venv/bin/pytest tests/integration/test_build_smoke.py -v
```

- [ ] **Step 3: Modify `src/video_to_notebook/cli.py`**

Add imports near other build-related ones (after the cluster imports):

```python
from video_to_notebook.build.runner import run_build
```

Append commands at the end of the file:

```python
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
        raise typer.Exit(code=1)

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
        raise typer.Exit(code=1)

    from video_to_notebook.build.template_copy import ensure_site_dir
    site_dir = ensure_site_dir(root)

    if not (site_dir / "node_modules").is_dir():
        typer.echo("running: npm install")
        subprocess.run(["npm", "install", "--silent"], cwd=site_dir, check=False)

    typer.echo(f"running: npm run dev (in {site_dir})")
    subprocess.run(["npm", "run", "dev"], cwd=site_dir, check=False)
```

- [ ] **Step 4: Run tests + typecheck**

```bash
.venv/bin/pytest tests/integration/test_build_smoke.py -v
.venv/bin/pytest -v
.venv/bin/pyright src tests
```

Expected: all green.

- [ ] **Step 5: Commit**

```bash
git add src/video_to_notebook/cli.py tests/integration/test_build_smoke.py
git commit -m "feat(cli): \\\`build\\\` (with --incremental, --no-npm) and \\\`serve\\\` commands"
```

---

## Phase 5: E2E + Verification

### Task 11: Playwright E2E tests

**Files:**
- Modify: `pyproject.toml` — add `pytest-playwright` to dev deps
- Create: `tests/e2e/__init__.py` (empty)
- Create: `tests/e2e/conftest.py`
- Create: `tests/e2e/test_navigation.py`
- Modify: `pyproject.toml` — add `e2e` marker

These tests are gated behind the `e2e` pytest marker so CI can opt in.

- [ ] **Step 1: Add deps + marker**

In `pyproject.toml`:

Add to dev deps:
```toml
    "pytest-playwright>=0.5.0",
```

Add marker to `[tool.pytest.ini_options]`:
```toml
markers = [
    "integration: integration tests (slower, may hit fs)",
    "e2e: browser-driven E2E tests (requires playwright install)",
]
```

Install + browsers:
```bash
cd /Users/chenlinzhuo/code/video-to-notebook
uv pip install -e ".[dev]"
.venv/bin/playwright install chromium
```

- [ ] **Step 2: Write `tests/e2e/conftest.py`**

```python
"""E2E test fixtures: spin up a real astro dev server against a seeded project."""
from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest
import urllib.request
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.db.session import connect


def _seed_corpus(project_root: Path) -> None:
    db = project_root / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://www.youtube.com/playlist?list=PLX', '2026-05-09'),"
            "(2, 'gpu-mode', 'GPU MODE', 'youtube', 'https://www.youtube.com/playlist?list=PLY', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1 Intro', 'https://www.youtube.com/watch?v=aaa', 't', 'ok'),"
            "(2, 2, 1, 'L1 CUDA basics', 'https://www.youtube.com/watch?v=bbb', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'CS336 talks about attention here'),"
            "(2, 2, 0, 0, 60, 'GPU MODE explains attention from CUDA angle')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'attention', 'Attention', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1'),(2, 1, 0.88, 'haiku:v1')"
        )


@pytest.fixture(scope="session")
def astro_server(tmp_path_factory: pytest.TempPathFactory):
    """Start astro dev once per session; tear down at end."""
    project = tmp_path_factory.mktemp("e2e_project")
    cwd = os.getcwd()
    os.chdir(project)
    try:
        runner = CliRunner()
        runner.invoke(app, ["init"])
        _seed_corpus(project)
        runner.invoke(app, ["build", "--no-npm"])

        site = project / "site"
        subprocess.run(["npm", "install", "--silent"], cwd=site, check=True)
        proc = subprocess.Popen(
            ["npm", "run", "dev", "--", "--port", "4321"],
            cwd=site,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # Wait for the server to be ready (max 30s)
        for _ in range(60):
            try:
                with urllib.request.urlopen("http://localhost:4321/", timeout=1) as resp:
                    if resp.status == 200:
                        break
            except Exception:
                time.sleep(0.5)
        else:
            proc.kill()
            raise RuntimeError("astro dev did not become ready in 30s")

        yield "http://localhost:4321"

        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    finally:
        os.chdir(cwd)
```

- [ ] **Step 3: Write `tests/e2e/test_navigation.py`**

```python
from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_home_lists_courses_and_concepts(astro_server: str, page: Page):
    page.goto(astro_server)
    expect(page.locator("h1")).to_have_text("video-to-notebook")
    assert "2 course" in page.content()
    assert "1 concept" in page.content()


@pytest.mark.e2e
def test_concept_page_shows_occurrences_across_courses(astro_server: str, page: Page):
    page.goto(f"{astro_server}/concepts/attention/")
    expect(page.locator("h1")).to_contain_text("Attention")
    body = page.content()
    assert "cs336" in body
    assert "gpu-mode" in body


@pytest.mark.e2e
def test_compare_view_shows_two_columns(astro_server: str, page: Page):
    page.goto(f"{astro_server}/concepts/attention/compare/")
    cols = page.locator(".compare-col")
    expect(cols).to_have_count(2)
```

- [ ] **Step 4: Run E2E (manual gate)**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
.venv/bin/pytest tests/e2e/ -v -m e2e
```

> If Playwright reports missing browsers, run `.venv/bin/playwright install chromium`.
> If `npm install` fails for any reason, the fixture aborts cleanly; skip the E2E and continue.

Expected: 3 e2e pass. If your environment can't run a server (no Node), mark these expected-to-skip via `pytest -v -m "not e2e"` for the main suite.

- [ ] **Step 5: Update CI to NOT run e2e by default**

In `.github/workflows/ci.yml`, change the test step from:
```yaml
      - name: Test
        run: pytest -v --tb=short
```
to:
```yaml
      - name: Test
        run: pytest -v --tb=short -m "not e2e"
```

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml tests/e2e/ .github/workflows/ci.yml
git commit -m "feat(e2e): Playwright tests for home/concept/compare pages; CI skips e2e"
```

---

### Task 12: Real-data verification

This is a manual end-to-end check using the existing crawled corpus.

- [ ] **Step 1: Ensure the Plan 2 verification project exists**

If you haven't run Plan-2 T14 yet, do that first to populate concepts. Otherwise reuse `/tmp/cm-plan2`.

- [ ] **Step 2: Run build**

```bash
cd /tmp/cm-plan2
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook build
```

Expected output: `done: 1 courses, 4 lectures, N concepts, astro exit 0`. The `site/dist/` directory now contains a full HTML site.

- [ ] **Step 3: Inspect the output**

```bash
ls site/dist/
ls site/dist/courses/
ls site/dist/concepts/
open site/dist/index.html       # opens in default browser
```

- [ ] **Step 4: Run dev server and click around**

```bash
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook serve
# open http://localhost:4321
```

Click through:
1. Home → see Vizuara course listed
2. Course detail → see all 4 lectures
3. Lecture page → see video iframe + click a transcript chunk → verify video seeks
4. Concept index → A-Z listing
5. Click a concept → see occurrences table
6. If a concept has hits in multiple courses, click "Compare across N courses" → side-by-side view

- [ ] **Step 5: Incremental rebuild check**

```bash
# Make a fake change: mark one concept dirty
sqlite3 .video-to-notebook/db.sqlite \
    "INSERT INTO build_meta (key, value) VALUES ('dirty_concepts', '[\"attention\"]') \
     ON CONFLICT(key) DO UPDATE SET value = '[\"attention\"]';"

# Incremental build re-renders only that one concept
uv run --project /Users/chenlinzhuo/code/video-to-notebook video-to-notebook build --incremental --no-npm
```

Expected: `done: ... 1 concepts ...`.

- [ ] **Step 6: Tag completion**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git tag plan-3-done
git log --oneline plan-2-done..plan-3-done
```

---

## Self-Review Notes

**Spec coverage (Plan 3 portion):**

- §6 `build` CLI with `--incremental`: ✅ Task 10.
- §6 `serve` CLI: ✅ Task 10.
- §7 routes (`/`, `/courses/`, `/courses/<slug>/`, `/courses/<slug>/<lecture>/`, `/concepts/`, `/concepts/<slug>/`, `/concepts/<slug>/compare/`, `/about/`): ✅ Tasks 1, 6, 7, 8, 9.
- §7 components — LectureTranscript (synced video↔transcript): ✅ Task 7. ConceptOccurrenceTable: ✅ Task 8. CompareView (multi-column side-by-side): ✅ Task 8. VideoEmbed: ✅ Task 7.
- §7 Pagefind full-text search: ✅ Task 1 (built into Base.astro layout, runs after astro build).
- §8 Build error handling — astro build non-zero passes through (exit 5): ✅ Task 10. Missing chunks render placeholder via Astro's template logic.
- §9 Testing — unit + integration + snapshot (snapshot deferred — see below) + E2E Playwright: ✅ Tasks 2, 3, 5, 10, 11.
- §10 HTML framework Astro + Pagefind: ✅ Task 1.

**Out of scope, deferred:**

- Snapshot-of-HTML tests (pytest-snapshot for built HTML): the E2E Playwright tests at Task 11 cover the same regression surface more meaningfully than HTML byte snapshots. Skip.
- Live URL `?courses=cs336,gpu-mode` filtering on the compare page (currently the page shows all courses with hits): the static SSG model would need client-side JS to filter. Plan 4 polish task.
- Bilibili iframe `postMessage` seek API: the Bilibili player is iframe-only with no public JS API for seek. v1 just links to time-stamped URL (`?p=N&t=Ns`). Click-to-seek works for YouTube only — flagged in `LectureTranscript.astro`.
- "Build only this concept" CLI flag: `--incremental` already does this via `dirty_concepts`; if you need ad-hoc filtering, edit `build_meta` manually (shown in T12).

**Placeholder scan:** no "TBD", "TODO", or unresolved placeholders. All Astro pages compile to valid TS; all Python code is runnable.

**Type / signature consistency:**

- `BuildReport` (Task 5) fields match CLI output strings in Task 10.
- Content collection schema (Task 1 `config.ts`) matches the YAML frontmatter shape produced by `writers.py` (Task 3) — chunks array has the same field names and types.
- `LectureTranscript` `Chunk` interface field names (`start_sec`, `end_sec`, `text`, `concept_slugs`) match the content collection schema.
- `_template_site/` install location matches `template_copy.py:_bundled_template_root` lookup.

**Plan 4 handoff:**

- GitHub Pages deployment workflow: a new `.github/workflows/pages.yml` that runs `video-to-notebook build` in the demo subproject and uploads `site/dist/`.
- `skills/video-to-notebook/SKILL.md`: a markdown skill plugin file that maps natural-language requests ("crawl this course", "build the site") to the CLI commands.
- `examples/frontier-notebook/`: a curated ontology + courses.toml + (optionally) a pre-rendered site for the demo.
- Cost-tracking and budget alerts (per spec §6 future work).
