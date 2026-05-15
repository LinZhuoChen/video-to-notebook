# Plan 6 — Textbook Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Pivot video-to-notebook from "concept index" to "textbook generator". Given N crawled+tagged+clustered courses, produce a beginner-friendly multi-chapter HTML textbook with pedagogical sequencing, inline SVG diagrams, CSS animations, embedded source-video clips, per-chapter takeaways.

**Architecture:** Two new CLI subcommands (`curriculum`, `synthesize`) with in-session mode for Max users. `curriculum` designs chapter sequence; `synthesize` writes one chapter at a time as HTML fragment file. New Astro `/textbook/` route group reads `curriculum.json` manifest + HTML fragments and renders pages inside Base.astro with sidebar nav + prev/next. Existing `/courses/` and `/concepts/` routes stay as "lookup" feature.

**Tech Stack:** Same as v1.1 + KaTeX for math rendering. No new Python deps.

**Repo:** `/Users/chenlinzhuo/code/video-to-notebook/` (at tag `v1.1.0`).

---

See plan text in earlier draft (kept brief due to length constraints). The 7 tasks are:

- **T1**: DB migration `0003_textbook.sql` adding `curriculum_chapters` table with `order_idx`, `module`, `title`, `blurb`, `primary_concept_slug`, `related_concept_slugs`, `status`, `synthesized_path`.
- **T2**: `curriculum/prompt_io.py` with `collect_curriculum_prompts` + `apply_curriculum_results`. CLI: `video-to-notebook curriculum --print-prompts/--apply-results`.
- **T3**: `synthesize/prompt_io.py` with `collect_synthesize_prompts(chapter_order_idx)` + `apply_synthesize_results`. CLI: `video-to-notebook synthesize --chapter N --print-prompts/--apply-results <path>`.
- **T4**: `build/textbook_writer.py` copies `.video-to-notebook/textbook/N.html` → `site/src/content/textbook/N.html`, writes `curriculum.json` manifest. Wired into `run_build`.
- **T5**: Astro `/textbook/index.astro` (TOC) + `/textbook/[order].astro` (per-chapter, reads manifest + fragment via `import.meta.glob`). New components `TextbookNav.astro` + `ChapterNav.astro`. KaTeX CSS + browser-side `$..$` / `$$..$$` renderer in `Base.astro`. Home page features textbook over concept index.
- **T6**: SKILL.md + README updates for curriculum/synthesize workflow.
- **T7**: Live verification — design curriculum + synthesize 3 chapters end-to-end + build + browse.

JSON schemas locked: `curriculum_prompts/results`, `synthesize_prompts/results` — all `schema_version="1"`, in-session designer/synthesizer id `"claude-code-max:v1"`.

Out of scope, deferred to Plan 7+: generate all 21 chapters for frontier-notebook demo, quiz/exercise components, API mode (Anthropic SDK) for curriculum+synthesize (in-session is priority for Max users), chapter-scoped Pagefind facets.
