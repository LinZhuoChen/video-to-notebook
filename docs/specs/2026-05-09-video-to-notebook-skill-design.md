# video-to-notebook — Design Spec

**Date:** 2026-05-09
**Author:** chenlinzhuo
**Status:** Draft (post-brainstorming)
**Related:** [video-course-notes skill](~/.claude/skills/video-course-notes/) (extracts subtitle pipeline this project will reuse)

---

## 1. Goals & Non-Goals

### Goals

- **A reusable Claude Code skill + Python CLI** that ingests open-courseware (YouTube / Bilibili), tags chunks with concept labels via Claude, clusters labels into a unified ontology across courses, and emits an interactive static HTML site for self-study.
- Cross-course **concept-anchored navigation**: one concept page lists every lecture excerpt that touches it, with a side-by-side "compare across courses" view.
- **Incremental architecture**: adding the 11th course only re-tags the new course; concept clustering is a delta operation; HTML build re-renders only dirty pages.
- **OSS distribution + a flagship demo site.** The repo ships as a generic tool; the author's *Frontier Notebook* (World Models × Agents) corpus serves as the showcase deployed to GitHub Pages.

### Non-Goals

- Not a full LMS (no user accounts, progress tracking, quizzes, payments).
- Not a hosted SaaS (no server, no DB beyond a local SQLite file).
- **v1 does not auto-transcribe.** If a video has no subtitles (manual / auto-generated / AI), the lecture is skipped with a clear report. Whisper-based fallback (mlx-whisper / Groq) is explicitly deferred to v2 — see §11.
- v1 platforms: YouTube + Bilibili only. Coursera/edX/MIT-OCW deferred to plugin contracts.
- Does not rewrite lectures into a synthesized "AI textbook" (versioned in a future v2 if there's appetite, has higher copyright risk).

---

## 2. Target User & Demo Site

| Audience | Story |
|----------|-------|
| **Primary**: a self-learner or researcher who already follows ≥3 open courses on overlapping topics (e.g. "I've watched CS336 + GPU-MODE + Vizuara LLM Context Engineering — show me where they all explain attention so I can triangulate") |
| **Secondary**: course note-takers who want their notes auto-organized into a public site |
| **Showcase**: author's `frontier-notebook` demo, ingesting 5–8 World-Models / Agents courses from his Obsidian vault and publishing to `frontiernotebook.dev` |

---

## 3. Architecture

### 3.1 Pipeline shape

Five **independent, idempotent, resumable** subcommands sharing one local SQLite:

```
                 ┌──────────────────────────────────────┐
                 │           SQLite (.video-to-notebook/db) │
                 │  courses · lectures · chunks         │
                 │  concepts · chunk_concepts · aliases │
                 └──────────────────────────────────────┘
                          ↑           ↑          ↑
   ┌──────────┐   crawl   │           │ tag      │ cluster   ┌──────────┐
   │ yt-dlp   │──────────▶│           │ (Haiku)  │ (Sonnet)  │  build   │
   │ subtitles│           │           │          │           │ (Astro)  │
   └──────────┘           │           │          │           └────┬─────┘
                                                              dist/  → GitHub Pages
```

Each command can be re-run safely; partial failure leaves DB in a consistent state and the next run picks up at the cursor.

### 3.2 Why DB-incremental over single-pipeline

- Demo site grows from 3 → 30 courses; LLM tagging cost would compound linearly without caching.
- Re-tuning ontology should re-render only affected concept pages, not redo all transcripts.
- A schema forces explicit data contracts between stages (no implicit JSON files between scripts).

### 3.3 Why concept-anchored merging (not full synthesis)

- The cross-course UX killer feature is *seeing the same concept explained four ways*, not reading a fifth synthetic version.
- Avoids copyright/attribution problems: every excerpt links back to the source video at the precise timestamp.
- Reuses what the author already does manually in his Obsidian vault (256 concept pages with `Sources:` sections).

---

## 4. Repository Layout

```
video-to-notebook/
├── pyproject.toml                 # uv-managed Python package, dependencies pinned
├── README.md                      # quickstart + GIF
├── LICENSE                        # MIT
├── .github/workflows/
│   ├── ci.yml                     # lint + typecheck + test matrix
│   └── pages.yml                  # build & deploy demo site on push to main
├── src/video_to_notebook/
│   ├── __init__.py
│   ├── cli.py                     # Typer app: init/crawl/tag/cluster/build/serve/review
│   ├── crawl/
│   │   ├── base.py                # Crawler ABC + chunker
│   │   ├── youtube.py
│   │   └── bilibili.py
│   ├── tag/
│   │   ├── claude_tagger.py       # Anthropic SDK calls, retry, parse
│   │   ├── prompts.py             # System prompts as constants (versioned)
│   │   └── ontology.py            # Seed loading, slug normalization
│   ├── cluster/
│   │   ├── embedding.py           # MiniLM via sentence-transformers
│   │   ├── llm_review.py          # Sonnet pass to merge/split clusters
│   │   └── aliases.py             # alias normalization + persistence
│   ├── build/
│   │   ├── astro_writer.py        # writes content/* MD files
│   │   └── templates.py           # frontmatter helpers
│   └── db/
│       ├── schema.sql             # canonical schema (single source of truth)
│       ├── migrations/            # 0001_initial.sql, ...
│       └── session.py             # connection pool, transaction helpers
├── template-site/                 # init copies this into <project>/site/
│   ├── astro.config.mjs
│   ├── package.json
│   ├── src/
│   │   ├── content/
│   │   │   ├── config.ts          # Astro Content Collections schema
│   │   │   ├── courses/           # populated by build
│   │   │   └── concepts/          # populated by build
│   │   ├── pages/
│   │   │   ├── index.astro
│   │   │   ├── courses/[slug]/index.astro
│   │   │   ├── courses/[slug]/[lecture].astro
│   │   │   ├── concepts/index.astro
│   │   │   ├── concepts/[slug]/index.astro
│   │   │   └── concepts/[slug]/compare.astro
│   │   └── components/
│   │       ├── LectureTranscript.astro    # synced video↔transcript scroll
│   │       ├── ConceptOccurrenceTable.astro
│   │       ├── CompareView.astro          # multi-course side-by-side
│   │       └── VideoEmbed.astro
│   └── public/
├── skills/video-to-notebook/
│   ├── SKILL.md                   # Claude Code skill plugin
│   └── scripts/                   # thin shell wrappers around CLI
├── examples/frontier-notebook/    # author's demo deployment config
│   ├── ontology/concepts.yaml     # exported from Obsidian vault
│   ├── courses.toml               # course URLs to crawl
│   └── README.md
├── tests/
│   ├── conftest.py
│   ├── fixtures/mini_course/      # 3 lectures × 5 chunks, recorded transcripts
│   ├── unit/
│   │   ├── test_chunker.py
│   │   ├── test_aliases.py
│   │   └── test_tagger_contract.py
│   ├── integration/
│   │   └── test_pipeline.py       # full crawl→build with vcrpy cassettes
│   ├── snapshot/
│   │   └── test_html_output.py
│   └── e2e/
│       └── test_ui.py             # playwright
└── docs/
    ├── architecture.md
    ├── ontology-format.md
    └── plugin-api.md              # for future Coursera/edX adapters
```

**Two distribution channels:**

- `pip install video-to-notebook` — for CLI users.
- Claude Code skill marketplace — natural-language entry point that calls the CLI under the hood.

---

## 5. Data Model (SQLite)

```sql
CREATE TABLE courses (
  id            INTEGER PRIMARY KEY,
  slug          TEXT UNIQUE NOT NULL,        -- "cs336", "gpu-mode"
  title         TEXT NOT NULL,
  platform      TEXT NOT NULL,               -- youtube | bilibili
  source_url    TEXT NOT NULL,
  added_at      TEXT NOT NULL                -- ISO8601 UTC
);

CREATE TABLE lectures (
  id            INTEGER PRIMARY KEY,
  course_id     INTEGER NOT NULL REFERENCES courses,
  idx           INTEGER NOT NULL,            -- 1-indexed
  title         TEXT NOT NULL,
  video_url     TEXT NOT NULL,               -- per-video URL (not playlist)
  duration_sec  INTEGER,
  transcript    TEXT,                        -- NULL = crawl failed
  status        TEXT NOT NULL,               -- ok | paywalled | no_subs | error
  UNIQUE (course_id, idx)
);

CREATE TABLE chunks (
  id            INTEGER PRIMARY KEY,
  lecture_id    INTEGER NOT NULL REFERENCES lectures,
  idx           INTEGER NOT NULL,
  start_sec     REAL NOT NULL,               -- for video timestamp link
  end_sec       REAL NOT NULL,
  text          TEXT NOT NULL,               -- ~300-800 token target
  embedding     BLOB                         -- np.float32[384] from MiniLM
);

CREATE TABLE concepts (
  id              INTEGER PRIMARY KEY,
  slug            TEXT UNIQUE NOT NULL,      -- "self-attention"
  canonical_name  TEXT NOT NULL,             -- "Self-Attention"
  description     TEXT,                      -- 1–2 sentence definition
  ontology_source TEXT NOT NULL              -- seed | discovered | user
);

CREATE TABLE concept_aliases (
  concept_id    INTEGER NOT NULL REFERENCES concepts,
  alias         TEXT NOT NULL,
  UNIQUE (alias)
);

CREATE TABLE chunk_concepts (
  chunk_id      INTEGER NOT NULL REFERENCES chunks,
  concept_id    INTEGER NOT NULL REFERENCES concepts,
  confidence    REAL NOT NULL,                -- 0.0–1.0 from LLM
  tagger_model  TEXT NOT NULL,                -- "claude-haiku-4-5"
  PRIMARY KEY (chunk_id, concept_id)
);

CREATE TABLE build_meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL                         -- last_cluster_hash, last_build_at, dirty_concepts
);

CREATE INDEX idx_chunk_lecture ON chunks(lecture_id);
CREATE INDEX idx_chunk_concept_concept ON chunk_concepts(concept_id);
```

**Design notes:**
- Embeddings stored as raw `BLOB` (np.float32[384]) — sqlite-vec is overkill at < 50k chunks; in-memory cosine is fast enough.
- `concept_aliases` is the cluster stage's main output; queries hit it during build to map raw tags back to canonical concepts.
- `build_meta.dirty_concepts` is a JSON array, populated by `tag` and `cluster` runs, consumed by `build --incremental`.

---

## 6. CLI Commands

| Command | Args | Behavior | Idempotency |
|---------|------|----------|------|
| `init [--ontology PATH] [--force]` | optional seed concepts YAML | scaffold `.video-to-notebook/{db.sqlite, config.toml, site/}`; if ontology, insert concepts with `ontology_source='seed'` | errors if already initialized unless `--force` |
| `crawl <url> [--name SLUG] [--lang L] [--cookies-from BROWSER] [--force]` | YouTube/Bilibili URL (single or playlist) | yt-dlp → chunker → DB. Chunker prefers explicit chapter markers; falls back to ~30s sliding windows. **Bilibili specifics**: requires `--cookies-from edge\|chrome\|firefox` (login state); playlist iteration uses `?p=N` not video IDs; subtitle language tries `ai-zh` → `ai-en` → abort with `status='no_subs'`. **YouTube specifics**: playlist iteration uses per-video IDs from `--flat-playlist` (avoids the v0 bug where `--no-playlist` resolved every iteration to the same video); subtitle language tries `--write-subs` → `--write-auto-subs en`. | duplicate `(course_slug, lecture.idx)` skipped unless `--force` |
| `tag [--course SLUG] [--model M] [--limit N]` | chunks without tags | for each untagged chunk, call Claude with current ontology (top-200 by usage); parse JSON; insert `chunk_concepts` and stash `proposed:` tags for cluster pass | only processes chunks lacking entries; resumable mid-run |
| `cluster [--threshold T] [--dry-run]` | proposed tags + existing concepts | (a) embed proposed tags; (b) cluster within distance `T`; (c) Sonnet decides per cluster: merge / new concept / reject; (d) write `concepts` + `concept_aliases`, mark dirty concepts | input-hash cached in `build_meta`; no-op if unchanged |
| `build [--out DIR] [--incremental]` | DB → Astro markdown → `astro build` | renders `content/concepts/<slug>.md` and `content/courses/<slug>/<lecture>.md`; runs `npm run build` | `--incremental` re-renders only `dirty_concepts`; otherwise full rebuild |
| `serve` | DB | `astro dev` on :4321 with hot reload | — |
| `review [--type T]` | items in `.video-to-notebook/review/` | opens markdown queue files for human disambiguation; writes adjudication back to DB | clears the queue once committed |

**Tagger prompt contract** (versioned in `tag/prompts.py`):

```text
SYSTEM:
You are a course-content tagger. Given a 300-800 token chunk from a
lecture, return 1–3 concept tags as JSON. Constraints:
- Each tag MUST be either:
  (a) an exact slug from the provided ontology, or
  (b) prefixed `proposed:` for new concepts (use sparingly; ≤1 per chunk).
- confidence ∈ [0, 1]; below 0.5 omit the tag entirely.
- Slugs are ALWAYS English kebab-case, even if the chunk is in Chinese
  or mixed Chinese/English. Examples: a chunk saying "注意力机制" or
  "attention 机制" both map to slug `attention`, never `注意力机制`.
- DO NOT explain.

ONTOLOGY (top 200 by usage):
self-attention, multi-head-attention, kv-cache, ...

USER:
<chunk text>

OUTPUT:
{ "tags": [ {"slug": "...", "confidence": 0.92}, ... ] }
```

---

## 7. HTML Output Structure

| Route | Content | Key interaction |
|-------|---------|-----------------|
| `/` | landing: counts, search box | Pagefind full-text search (client-side) |
| `/courses/` | grid of all courses | filter by platform / tag |
| `/courses/<slug>/` | course overview + lecture timeline | expand lecture → see chunks |
| `/courses/<slug>/<lecture-slug>/` | embedded video + synchronized transcript | click a chunk → seek video; right rail lists this chunk's concepts |
| `/concepts/` | A–Z index + word cloud | — |
| `/concepts/<slug>/` | **flagship page**: definition + occurrences table (course / lecture / timestamp / excerpt) | per-row expand for full chunk; "Compare across courses" CTA |
| `/concepts/<slug>/compare/` | multi-course side-by-side excerpts | URL `?courses=cs336,gpu-mode` controls columns; chip selection persisted in localStorage |
| `/about/` | auto-generated build info, version, git SHA | — |

**Interactive components** (Astro + vanilla JS / Web Components only — no React/Vue):

- `<LectureTranscript>` — synced scroll video↔transcript with URL hash deep-linking.
- `<ConceptOccurrenceTable>` — client-sortable, filterable by course.
- `<CompareView>` — N-column side-by-side; selectable courses, lockable columns, shared font-size control.
- Pagefind index injected at build, zero-backend search.

**Deliberately not used:** React, Next.js, dynamic API. Static HTML keeps GitHub Pages deployment trivial and removes runtime cost.

---

## 8. Error Handling

Following the principle: *one bad lecture should not abort a 30-lecture batch.*

| Stage | Failure | Handling |
|-------|---------|----------|
| crawl | yt-dlp failure (private / members-only / no subs) | `lectures.transcript=NULL`, `status='paywalled'\|'no_subs'\|'error'`; UI shows badge; CLI summary reports "3/17 failed" |
| crawl | playlist contains members-only entry mid-batch | warn + skip, continue; build emits a notice on the course page |
| crawl | Bilibili HTTP 403 (cookie expired) | abort with actionable error "cookies invalid for browser `<name>` — log in to bilibili.com in that browser, or pass `--cookies-from edge`"; do not silently fail |
| crawl | entire course has 0 lectures with usable subtitles | emit a warning summary recommending the user wait for v2 (whisper fallback) or pick a course with auto-captions enabled; do not write a stub course row |
| tag | rate limit (HTTP 429) | exponential backoff `2s, 4s, 8s, 32s` then abort with resumable state |
| tag | JSON parse failure | retry once; on second failure write `chunk_concepts` row with `tagger_model='ERROR'` and skip |
| tag | excessive `proposed:` tags from one course | accumulate to cluster pass; do not auto-create concepts in tag stage |
| cluster | LLM ambiguous (merge-vs-new uncertain) | write `.video-to-notebook/review/cluster_<hash>.md` with options; CLI prints "N items pending review — run `video-to-notebook review`" |
| build | concept page references missing chunk (data inconsistency) | warn, render placeholder, log; do not abort |
| build | `astro build` non-zero exit | pass stderr through; preserve previous `dist/` |

All commands accept `--dry-run` and `--verbose`; progress goes to stderr via `rich` with colored bars.

---

## 9. Testing Strategy

| Layer | Scope | Tooling | Goal |
|-------|-------|---------|------|
| Unit | pure functions: chunker, slug normalization, alias rules, cluster threshold | pytest | high coverage of business logic |
| Tagger contract | mock Anthropic SDK; assert prompt construction, JSON parsing, confidence filter | pytest + responses | no real model calls |
| Integration | fixture course (3 lectures × 5 chunks) full pipeline | pytest + vcrpy cassettes for Anthropic | end-to-end DB state assertions |
| Snapshot | post-build HTML for fixture corpus | pytest-snapshot | concept-page structure stable |
| E2E | `astro dev` + Playwright drives core interactions (chunk → seek; compare-view chip toggle) | playwright-pytest | UI regressions caught |
| CI | lint + typecheck + above 4 layers on PR | uv + ruff + pyright + GitHub Actions | green required to merge |

`tests/fixtures/mini_course/` ships with the repo; `pytest -m integration` runs in <1 minute on contributor machines.

---

## 10. Defaults & Choices Locked In

| Decision | Choice | Rationale |
|----------|--------|-----------|
| HTML framework | **Astro + Pagefind** | static, content-collection-friendly, built-in search, GitHub-Pages-ready |
| v1 platforms | **YouTube + Bilibili** | reuses video-course-notes' yt-dlp work; covers author's corpus |
| Tagging LLM | **Claude Haiku 4.5** | high-volume, cheap (`$0.80 / MTok` input), fast |
| Cluster review LLM | **Claude Sonnet 4.6** | higher reasoning needed at the cluster boundary; called <100 times |
| Embedding | **all-MiniLM-L6-v2** (sentence-transformers) | local, 384-dim, fast on CPU |
| Ontology mode | **cold-start auto-discover** by default; `--ontology FILE` for seed mode | demo case feeds the author's vault concepts as seed |
| Demo corpus | 5–8 World-Models × Agents courses curated from author's vault | aligned with Frontier Notebook editorial line |
| License | **MIT** | OSS standard for tools |
| Distribution | `pip install video-to-notebook` + Claude Code skill plugin | one CLI, two entry points |
| Repo name | `video-to-notebook` (working title; bikeshedding allowed) | descriptive |

---

## 11. Out of Scope for v1 (deferred backlog)

- **Whisper / audio transcription fallback** for videos without subtitles. Planned for v2 with three provider options: `mlx-whisper` (local, Mac M-series), `openai-whisper` (CPU/CUDA), `groq-whisper` (API). Behind a `--whisper` flag, default off; would add `lectures.transcript_source` column to record provenance and surface a "🎙️ Auto-transcribed" badge in the UI.
- Coursera / edX / MIT-OCW adapters (define a `Crawler` ABC in v1, implement v2).
- Full-text synthesis ("AI-rewritten textbook" mode).
- Multi-language concept aliasing beyond slug normalization (e.g. dedicated zh ↔ en concept name pairs surfaced in UI).
- User auth, progress tracking, spaced-repetition.
- A SaaS hosted version.

---

## 12. Open Questions to Resolve in Implementation Plan

- **Chunker boundary heuristic**: how aggressive to honor explicit chapter markers vs. uniform sliding windows when both are present? — to settle in TDD with sample courses.
- **Ontology cold-start cost**: for a project with 0 seed concepts, the first `tag` pass produces almost all `proposed:` tags. Need a budget cap and pace-limiting in `tag` to avoid runaway LLM cost on day 1.
- **Compare-view layout density**: 4 courses side-by-side gets cramped on a laptop; mobile layout TBD.
- **Build-time deduplication of near-identical excerpts**: e.g. if two chunks within one lecture both tag `attention`, do we show both?

These are design points to validate during implementation, not unresolved before starting.
