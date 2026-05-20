# Changelog

All notable changes to video-to-notebook (formerly `course-merger`). Follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [2.2.1] — 2026-05-20

### Fixed — language toggle now honours `BASE_URL` on Pages

The `lang-toggle` JS was reading the site's base path from a `<base href="…">` tag — but Astro doesn't emit one — so the lookup always fell back to `/`. On Pages (`BASE_PATH=/video-to-notebook/`) this produced 404s on every toggle:

| Was on | Click toggle | Used to go to | Now correctly goes to |
|---|---|---|---|
| `/video-to-notebook/textbook/1/` | EN | `/en/textbook/1/` (404) | `/video-to-notebook/en/textbook/1/` |
| `/video-to-notebook/en/textbook/1/` | 中 | `/textbook/1/` (404) | `/video-to-notebook/textbook/1/` |

Fix: bake `import.meta.env.BASE_URL` into the button as `data-base` at build time. The JS now reads `data-base` directly, computes the sub-path, and prefixes the sibling deployment's base. Search and hash are preserved.

## [2.2.0] — 2026-05-20

### Added — bilingual demo scaffolding (Phase 1)

Wire the codebase to host **zh** and **en** demo sites side-by-side on Pages (`/` ↔ `/en/`) with a header language switcher. Content for both languages lives in parallel sub-folders; an empty `en/` still builds cleanly (empty-state pages). Content regeneration is Phase 2 and runs separately via in-session synthesize/explain.

- **Astro content layout** re-organised to `<area>/<lang>/*`:
  - `template-site/src/content/textbook/{zh,en}/` (HTML fragments + `curriculum.json`)
  - `template-site/src/content/concept-explainers/{zh,en}/` (HTML fragments + `manifest.json`)
  - Existing 21 zh chapter fragments + 33 zh concept fragments moved via `git mv` (history preserved). Empty `en/curriculum.json` + `en/manifest.json` placeholders so en build doesn't 404.
- **Astro pages dispatch on language**: `pages/textbook/index.astro`, `[order].astro`, `pages/concepts/index.astro`, `[slug]/index.astro`, `components/TextbookNav.astro`, `pages/index.astro` all read `currentLanguage` from `i18n.ts` (driven by `PUBLIC_LANGUAGE` env) and pick the right folder.
- **Header language toggle**: new `.lang-toggle` button in `Base.astro` between search and theme-toggle. Renders `EN` on zh pages, `中` on en pages. JS preserves current sub-path while navigating to the sibling deployment.
- **Python build writers**: `textbook_writer.py` + `concept_writer.py` read `build_meta.language` from the project DB (defaulting to `'zh'` for legacy projects) and write into `template-site/src/content/<area>/<lang>/`. New test `test_respects_build_meta_language`.
- **Pages workflow** runs `npm run build` twice — once with `PUBLIC_LANGUAGE=zh BASE_PATH=/<repo>/`, once with `PUBLIC_LANGUAGE=en BASE_PATH=/<repo>/en/` — and merges the en dist into `dist-zh/en/` before upload.
- **Frontier example** `build.sh` gains `--language` and `--bilingual` flags. `--bilingual` swings `build_meta.language` and reruns the build writers twice. The in-session synthesize/explain still needs to be driven separately per language by an agent.

### Added — English Module 1 demo content (Phase 2 partial)

First three chapters of the bilingual demo's English half, regenerated from the original English source transcripts (not machine-translated from Chinese):

- Ch 1 "Why Diffusion? AR vs Diffusion" (~3000 words)
- Ch 2 "VAE: Compressing Data into a Latent Space" (~3500 words)
- Ch 3 "ELBO: The Evidence Lower Bound" (~3000 words)

Each follows the v3 synthesizer style guide: TL;DR callout, 8–14 numbered sections, every non-trivial formula in a `deriv-step` block with `**Why**:`, multiple coloured callouts, source quotes verbatim from the English video lectures, takeaway block. Curriculum metadata (titles + blurbs) for all 21 chapters already translated in-place so the textbook nav doesn't break on the en build. **Remaining 18 chapters + 39 concept explainers ship in subsequent batches.**

### Docs

- README: real demo screenshots (3-shot grid: textbook TOC, concept encyclopedia, single chapter reading view) replace the placeholder upload image. Bilibili parity restored across tagline, early-days note, quickstart Option B, disclaimer, footer.
- README.zh-CN.md added — full Chinese translation, with `English · 中文` switcher at the top of both files.
- `docs/plans/2026-05-19-bilingual-demo.md` — 3-phase architecture sketch for the bilingual demo.

## [2.1.1] — 2026-05-19

### Fixed — Bilibili season URLs were silently downloading the same video N times

`BilibiliCrawler.list_playlist` always emitted `<playlist_url>?p=N` as the per-entry `video_url`, regardless of URL shape. On `space.bilibili.com/<uid>/lists/<id>?type=season` (and similar list / series / favlist pages) the entries are DISTINCT videos with their own BV ids, NOT parts of a single multi-part video — yt-dlp silently fell back to the default video and inserted N duplicate transcript rows. Hit during real-world end-to-end testing on a 14-video 楚国刮大风 AI 第三季 course: all 13 lectures landed with identical 8855-char transcripts.

New `_entry_url(playlist_url, video_id, idx)` helper distinguishes by URL shape:
- `bilibili.com/video/BV…/` (multi-part single video) → keep legacy `?p=N`
- Anything else (`space.bilibili.com`, `/list/`, `/season/`, `/favlist/`, search) → emit `https://www.bilibili.com/video/<BV>/`

New test `test_list_playlist_season_yields_canonical_per_bv_urls` covers the season case with three distinct BV ids; the existing multi-part test still passes.

### Added — `--cookies-file <path>` flag for portable Netscape-format auth

macOS Chrome stores SESSDATA v10-encrypted in Keychain; `--cookies-from-browser chrome` routinely fails silently on stock setups when TCC denies the `security` daemon's `find-generic-password` call. Compounded by bilibili tightening anti-scraping (every URL returns HTTP 412 unauthenticated, even single-video pages), `--cookies-from-browser` becomes a hard block. Workaround: export cookies via a browser extension and pass the file path directly.

```bash
video-to-notebook crawl <url> --name <slug> \
    --cookies-file ~/path/to/bilibili-cookies.txt --whisper
```

- New `yt_dlp_cookie_args(cookies_from, cookies_file)` helper in `crawl/base.py`; `cookies_file` wins when both are passed.
- `list_playlist`, `download_subtitle_vtt`, `download_audio`, `transcribe_video_to_vtt` all gain `cookies_file: Path | None = None`. `bilibili.list_playlist` now also threads cookies through — previously it called yt-dlp unauthenticated, which bilibili now rejects.
- `BilibiliCookieError` message updated to mention `--cookies-file` as an alternative.
- CLI: `--cookies-file <path>` Typer option with `exists=True, dir_okay=False` validation. Mutually-exclusive by precedence (file wins).

### Docs

- README: new "📺 Bilibili: season playlists & cookie auth" subsection documents URL shapes + auth options + macOS TCC quirks (don't put the cookies.txt in `~/Downloads`, `~/Desktop`, or `~/Documents` root). Roadmap: "Robust Bilibili support" moved from Deferred to Shipped.

## [2.1.0] — 2026-05-18

### Added — Whisper fallback for no-subtitle videos

The `crawl` command can now ingest videos that have no published captions. When yt-dlp's subtitle download returns nothing AND `--whisper` is passed, the pipeline downloads the audio track, runs Whisper locally, and feeds the synthesised VTT back into the existing chunker → DB pipeline. The downstream stages (`tag`, `cluster`, `synthesize`, `explain`, `build`) need no changes.

- **New module** `src/video_to_notebook/crawl/transcribe.py`: `Transcriber` Protocol + `MlxWhisperTranscriber` (Apple Silicon, default on Darwin) + `FasterWhisperTranscriber` (cross-platform CPU/GPU, default elsewhere) + `transcribe_video_to_vtt()` orchestrator. Both backends are lazy-imported — the package imports cleanly without either installed.
- **New CLI flags** on `video-to-notebook crawl`:
  - `--whisper / --no-whisper` (default off; opt-in because it can be slow on long lectures)
  - `--whisper-backend mlx-whisper|faster-whisper` (override the platform default)
  - `--whisper-model <id>` (defaults: `mlx-community/whisper-small-mlx` on mlx, `small` on faster-whisper; pass `medium` or `large-v3` for accuracy)
  - `--whisper-lang <iso639>` (skip auto-detect, e.g. `en` / `zh`)
- **New optional dep group** `[whisper]` in `pyproject.toml`: `mlx-whisper>=0.4.0` (macOS arm64 only, via PEP 508 environment marker) + `faster-whisper>=1.0.0` (everywhere). Install with `pip install 'video-to-notebook[whisper]'`.
- **`CrawlReport.lectures_whisper`** counter (new field) tracks how many lectures used the fallback. The CLI prints `done: 12 ok, 8 via whisper, 0 no-subs, 0 errors` so operators can audit at a glance.
- **VTT round-trip discipline** — the Whisper output goes through `segments_to_vtt()` and is re-parsed by the existing `parse_vtt()`. Same code path as published captions; same chunker behaviour downstream.
- **Status code** for `--whisper setup failed` is exit 5 (distinct from the existing 1/2/3/4 codes).

### Test coverage

20 new unit tests covering: timestamp formatting (edge cases including banker's-rounding, negative clamp), VTT generation (empty cue skip, empty list, round-trip through `parse_vtt`), `download_audio` (success / yt-dlp failure / extension-fallback glob), `build_transcriber` (platform default selection, explicit overrides, unknown backend rejection), and the orchestrator (happy path, download-error → None, silent-transcriber → None). Backend libraries are NOT imported in tests — fakes implement the Protocol.

### Docs

- README: install section gains `pip install 'video-to-notebook[whisper]'` + new "🎤 Crawling videos without subtitles" subsection with a Bilibili example. Roadmap: "No-subtitle video support" moved from Deferred to Shipped.
- CHANGELOG: this entry.

## [2.0.0] — 2026-05-15

### Changed — project renamed to `video-to-notebook` (BREAKING)

- The project formerly known as **course-merger** is now **video-to-notebook**. The name surfaces what the tool actually does: turn a stack of video courses into a single navigable notebook (textbook + concept encyclopedia). Pip package, CLI entry point, Python module, project marker, skill name, and Astro template branding all renamed in lockstep.
- **CLI**: `video-to-notebook ...` is the canonical entry point. A back-compat shim `course-merger` is still installed and forwards to the same Typer app, so existing scripts keep working — but it now prints a one-line deprecation notice on startup and will be removed in 3.0.0.
- **Python module**: `import video_to_notebook` (was `import course_merger`). No re-export shim; if you were importing internals, update your import paths.
- **Project marker directory**: new projects use `.video-to-notebook/` (was `.course-merger/`). On `init`, `tag`, `cluster`, etc., the CLI prefers `.video-to-notebook/`; if it finds only a legacy `.course-merger/`, it errors out with a one-line migration command rather than silently writing into the old marker.

#### Migrating a v1.x project to v2.0.0

```bash
# 1. inside the project dir
mv .course-merger .video-to-notebook

# 2. update the package
uv tool upgrade video-to-notebook    # or: pip install -U video-to-notebook

# 3. re-run any command — same DB, same chunks, no re-crawl, no re-tag
video-to-notebook build
```

The SQLite schema, chunk text, tag tables, curriculum, and synthesized HTML fragments are 100% forwards-compatible — the rename only touches the directory name and the binary name.

#### Files no longer present in v2.0.0

- `src/course_merger/` → `src/video_to_notebook/` (Python package renamed)
- `skills/course-merger/` → `skills/video-to-notebook/` (Claude Code skill renamed)
- All README badges, GitHub URLs, install instructions point at `video-to-notebook`.

### Added — quality discipline for synthesis (shipped with the rename)

- **Source-fidelity rule** (synthesize v3, explain v4) — both style guides now open with a "Source Fidelity First" principle: the agent must extract the lecturer's metaphors, worked examples, named citations, and verbatim phrasings from the chunks BEFORE drafting; layer its own framing on top with an explicit `🟡 教材外补充` flag wrapped in `<div class="my-addition">`. If two courses give different metaphors for the same concept, both get preserved and labelled.
- **No-fabrication rule** — when source chunks come up thin (e.g. all 20 chunks are course-logistics chatter, or one alphabetically-early course dominates the LIMIT), the agent is required to **stop and diagnose the pipeline** rather than paper over the gap with training-data knowledge. Includes a `sqlite3` diagnostic recipe in `SKILL.md`.
- **Textbook-note depth target** (synthesize v3) — new `PRINCIPLE 1` block sets the per-chapter target at 5,000–8,000 中文字 of body prose with: TL;DR callout at the top, 8–14 top-level sections (一二三四 …), step-by-step derivations where every line has `**Why**:` annotation, 3–5 colour-coded callouts (`callout-info / callout-note / callout-warning / callout-tip / callout-quote`), engineering details embedded as inline callouts not deferred, complete runnable PyTorch skeleton when a model is introduced, 5–7 takeaways anchored to specific lecturer-given examples. Under 4,000 字 flagged as under-developed; over 10,000 字 flagged as bloated.
- **Batch-vs-chapter-by-chapter mode** (`SKILL.md` Step T1.5) — every agent-driven textbook generation must first ask the user (via `AskUserQuestion`) which workflow to use: 整本批量做 (continuous run, build once at the end) or 一章一章来 (synthesize chapter 1, build, hand control back for feedback, then repeat). Same choice applied to `course-merger explain` for concept-page generation. Typical pattern recommended in skill: chapter-by-chapter for first 2–3 chapters until style is signed off, then flip to batch.

### Fixed — chunk selection regression

- **`synthesize/prompt_io.py` chunk selection rewritten in Python** — old SQL `LIMIT 20 ORDER BY course_slug, lecture_idx, chunks.idx` caused the alphabetically-first course to monopolise the 20-chunk budget even when another course had much deeper coverage of the chapter's primary concept (e.g. a CMU course-intro lecture won over Vizuara's 91-chunk dedicated VAE lecture for the `vae-encoder` chapter). New `_select_chunks` does (1) one breadth pass — 1 chunk per lecture in primary-coverage-count order; then (2) depth pass — pour the remaining budget into lectures by coverage, fully exhausting the dominant lecture before moving on. Same fix applied to `explain/prompt_io.py` via `_allocate_occurrences`.

### Added — README design-principles section

- New `## 🧭 Design principles` block near the top of README explains the three core differentiators (source fidelity, no fabrication, textbook-note depth) and links them to the style-guide source files.

## [1.4.0] — 2026-05-14

### Added — multi-agent support

- **`AGENTS.md`** at repo root — OpenAI Codex CLI's equivalent of Claude Code's `CLAUDE.md`. Orients any AI coding agent (Codex, Cursor, Continue, Aider, your own script) to the codebase, conventions, and safety rules.
- **`docs/AGENT_PROTOCOL.md`** — canonical JSON envelope schemas for all five LLM stages (tag / cluster / curriculum / synthesize / explain). Documents the `--print-prompts` / `--apply-results` contract in an agent-agnostic way so any client can drive the pipeline. Includes error semantics, idempotency guarantees, agent-id conventions.
- **`skills/course-merger/scripts/install-codex.sh`** — installer for Codex CLI. Two modes: `--project` symlinks `AGENTS.md` into the cwd (default), `--global` appends a course-merger stanza to `~/.codex/AGENTS.md`.
- **Agent-id conventions** documented in protocol — `claude-code-max:v1`, `codex-cli:v1`, `cursor:v1`, etc. Free-form strings, persisted to DB so audits can attribute decisions to the agent that produced them.

### Changed

- README "Use as Claude Code skill" section becomes "Drive it from your AI coding agent" with a 4-quadrant card layout: Claude Code · OpenAI Codex · Cursor/Continue/Aider · plain API key.
- README's "Option B" in quickstart now mentions Codex + Cursor + Continue alongside Claude Code.

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

[Unreleased]: https://github.com/LinZhuoChen/video-to-notebook/compare/v2.2.1...HEAD
[2.2.1]: https://github.com/LinZhuoChen/video-to-notebook/compare/v2.2.0...v2.2.1
[2.2.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v2.1.1...v2.2.0
[2.1.1]: https://github.com/LinZhuoChen/video-to-notebook/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v1.4.0...v2.0.0
[1.4.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/LinZhuoChen/video-to-notebook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/LinZhuoChen/video-to-notebook/releases/tag/v1.0.0
