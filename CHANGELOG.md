# Changelog

All notable changes to course-merger. Follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.3.0] — 2026-05-14

### Added

- **Concept explainer pipeline** — new `course-merger explain --concept <slug> --print-prompts/--apply-results` command produces a rich illustrated HTML entry per concept: definition, intuition, SVG diagram, interactive widget, worked example, three counter-example misconceptions, and cross-links. Migration 0004 adds `concept_explanations` table.
- **Explainer v2 style guide** (`src/course_merger/explain/prompts.py`) — hard contract for LLM output: per-concept CSS namespace prefix, CSS-variable-only color palette (works in light + dark + per-module accent), fixed 9-section skeleton with character budgets, three interactive widget templates (keyframe SVG / slider / step-button), anti-bias opener rule, equation-chain rule, counter-example pitfalls rule.
- **Astro `/concepts/[slug]/` page** rewritten — when an explainer exists, the rich HTML fragment is the primary content with globally styled sections (`.concept-intuition`, `.concept-quickref`, `.concept-deepdive`, `.concept-interact`, `.concept-example`, `.concept-pitfalls`, `.concept-seealso`, `.concept-sources`). When absent, a stub explains what's coming and prints the CLI invocation.
- **Astro `/concepts/` index** rewritten — featured "已详解" grid of explainer cards with per-module accent borders + module-grouped lists; planned concepts surface but dim.

### Site polish

- 🌓 **Dark mode** — `html.dark` class with `prefers-color-scheme` fallback, theme toggle in header, localStorage persistence, full token set for surfaces/ink/borders/shadows.
- 🎨 **Per-module accent palette** — `m1` green / `m2` blue / `m3` purple / `m4` amber / `m5` rose, scoped via `[data-module-idx="N"]`. Chapter num, reading progress bar, sidebar dot+border, drop cap inherit `--module-accent`.
- 📊 **Chapter mini-map** — third column on chapter pages tracks `h2`/`h3` headings with `IntersectionObserver`, clicks scroll-to anchor. Hidden under 1200 px viewport.
- 🌐 **Branded header** — `.site-logo` (cm mark + serif wordmark), underline-on-hover nav, search + theme toggle + mobile-menu in `.site-actions`.
- ⌨️ **Keyboard navigation** — ← / → arrows jump prev/next chapter, ignored in inputs and with modifier keys. Floating hint chip at bottom-right (desktop).
- 📱 **Mobile drawer** — hamburger button on <900 px opens slide-in panel, mirrors textbook sidebar when present, Escape/backdrop closes.

### Fixed

- `init_db` was creating but not propagating new tables to existing DB files. Migrations now auto-apply by `PRAGMA user_version` comparison.

## [1.2.0] — 2026-05-13

### Added

- **Textbook generator** — pivot from "concept index" to "merged textbook for self-study". New commands:
  - `course-merger curriculum --print-prompts/--apply-results` designs the chapter order from all tagged concepts + sample chunks (in-session Claude).
  - `course-merger synthesize --chapter N --print-prompts/--apply-results` per-chapter HTML fragment with inline SVG, CSS animations, embedded source-video iframes (timestamp-deep-linked), LaTeX (KaTeX), and takeaway blocks.
- New migration 0003 adds `curriculum_chapters` table.
- New Astro routes: `/textbook/` (table of contents + sticky sidebar) and `/textbook/[order]/` (chapter reading view + prev/next nav + reading-progress bar).
- Site visual refresh — serif headings, design tokens (`--accent`, `--surface`, `--border`, etc.), polished sidebar + chapter cards.

## [1.1.0] — 2026-05-13

### Added

- **In-session mode** for Claude Max users — `course-merger tag` and `course-merger cluster` accept `--print-prompts` (emit JSON envelope of pending work to stdout) and `--apply-results <file>` (read decisions JSON, write to DB). No API key needed.
- Schema versioning: `schema_version: "1"`, `kind: "tag_prompts" | "tag_results" | "cluster_prompts" | "cluster_results"`.
- Tagger model id convention `"claude-code-max:v1"` for in-session writes.
- `skills/course-merger/SKILL.md` automates the in-session loop.

### Fixed

- `OperationalError: database is locked` on parallel crawls — fixed by adding `busy_timeout=300000` (5 min) PRAGMA in `db/session.py`.

## [1.0.0] — 2026-05-12

### Added

- Initial release. Foundation: crawl (YouTube + Bilibili via yt-dlp), tag (Claude Haiku + prompt caching), cluster (SentenceTransformer all-MiniLM-L6-v2 embeddings + LLM-reviewed merges), build (Astro 5 content collections, Pagefind search).
- Skill-driven UX via Claude Code (install with `bash skills/course-merger/scripts/install-locally.sh`).
- Example corpus: `examples/frontier-notebook/` with 5 World-Models × Agents courses.

[Unreleased]: https://github.com/chenlinzhuo/course-merger/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/chenlinzhuo/course-merger/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/chenlinzhuo/course-merger/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/chenlinzhuo/course-merger/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/chenlinzhuo/course-merger/releases/tag/v1.0.0
