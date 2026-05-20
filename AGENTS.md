# Agents guide

> This file orients AI coding agents (OpenAI Codex CLI, Cursor, Continue, Aider, …) to the video-to-notebook codebase. Claude Code users: see `skills/video-to-notebook/SKILL.md` for the equivalent skill-format walkthrough — the two files cover the same ground.

## What this repo is

A Python CLI + Astro static-site generator that:

1. **Crawls** YouTube + Bilibili playlists with `yt-dlp` → SQLite.
2. **Tags** transcript chunks with concept labels via Claude (or any agent).
3. **Clusters** proposed tags into a unified ontology.
4. **Synthesizes** a beginner-friendly textbook (one HTML chapter per concept group).
5. **Explains** each concept as a rich illustrated encyclopedia entry.
6. **Builds** the lot into a static Astro site you can host on GitHub Pages.

## Agent-driven workflow (default in v2.3+)

Every LLM stage (`tag`, `cluster`, `curriculum`, `synthesize`, `explain`) runs **in-session by default** — no `ANTHROPIC_API_KEY` required. The CLI writes a JSON prompts envelope to `<state_dir>/prompts/<step>.json` and exits. You read the envelope, reason, write a decisions JSON to the sibling `.decisions.json` path, then re-invoke the same command with `--apply`. The CLI applies your decisions to SQLite.

`tag` and `cluster` also expose an opt-in `--use-api` flag that drives the Anthropic SDK directly (if you have a key). `curriculum`, `synthesize`, `explain` are in-session-only — they have no API path.

The protocol is **agent-agnostic**. Schemas, conventions, idempotency guarantees, error semantics all live in [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md). Read that file before driving the pipeline for the first time.

### Quick start for Codex / any agent

```bash
mkdir my-study-site && cd my-study-site
video-to-notebook init
video-to-notebook crawl "<youtube-or-bilibili-url>" --name <slug>
# Repeat crawl for each course

# Then, for each LLM stage:
video-to-notebook <stage> [args]
# CLI writes <state_dir>/prompts/<step>.json and prints a 3-line stderr hint.
# You read the envelope, reason, write <state_dir>/prompts/<step>.decisions.json.
video-to-notebook <stage> [args] --apply
```

For `tag` this is a batch loop (small `--limit`, repeat until `chunks` array empty in the prompts envelope). For `cluster`, `curriculum` it's one-shot. For `synthesize` it's per-chapter; for `explain` it's per-concept.

For a worked end-to-end recipe, see [`examples/frontier-notebook/RUNBOOK.md`](examples/frontier-notebook/RUNBOOK.md).

#### Bilibili requires cookies — playbook for the agent

Bilibili crawls **always** need cookies; an unauthenticated request gets HTTP 412 before yt-dlp can even list a playlist. The full playbook is in [`skills/video-to-notebook/SKILL.md`](skills/video-to-notebook/SKILL.md#bilibili-cookies-playbook-required--bilibili-always-needs-cookies). Short version:

1. Try `--cookies-from chrome` (or firefox / safari / edge) first. On Linux this usually works. On macOS, Chrome v10 cookies are Keychain-encrypted and yt-dlp typically can't read them.
2. If you see `HTTP 412`, `cannot decrypt v10 cookies`, or `expected string or bytes-like object, got 'bool'`, **stop retrying** — those failures are deterministic. Switch to step 3.
3. Ask the user to install the **"Get cookies.txt LOCALLY"** browser extension, log into bilibili.com, export Netscape-format cookies, and save the file **outside** `~/Downloads/`, `~/Desktop/`, and the root of `~/Documents/` (those are TCC-protected on macOS and yt-dlp can't read them). Then run with `--cookies-file <absolute-path>`.

For videos without official subtitles, also add `--whisper` to fall back to local transcription.

### Agent identifier

When you write a results envelope, set the agent-id field (`tagger_model_id`, `reviewer_model_id`, `designer`, `synthesizer`, `explainer`) so the DB records which agent produced each decision. Convention:

| Agent             | Identifier              |
|-------------------|-------------------------|
| Anthropic API     | `claude-haiku-4-5`, etc. (literal model id) |
| Claude Code       | `claude-code-max:v1`    |
| OpenAI Codex CLI  | `codex-cli:v1`          |
| Cursor / Continue | `cursor:v1` / `continue:v1` |

Free-form strings. Pick something distinct so future audits can attribute decisions.

## Codebase layout

```
src/video_to_notebook/
├── cli.py              # typer entrypoint
├── config.py           # PROJECT_MARKER, find_project_root
├── crawl/              # yt-dlp adapters: YouTube, Bilibili
├── tag/                # Claude Haiku per-chunk tagging
├── cluster/            # MiniLM embeddings + LLM-reviewed merges
├── curriculum/         # chapter sequence design
├── synthesize/         # per-chapter HTML generator
├── explain/            # per-concept HTML explainer (v1.3+)
├── build/              # SQLite → Astro content collections
└── db/                 # session.py + migrations/*.sql

template-site/          # Astro 5 site template (copied to project on `init`)
skills/video-to-notebook/   # Claude Code skill (parallel to this AGENTS.md)
docs/AGENT_PROTOCOL.md  # canonical JSON envelope schemas
tests/                  # pytest — 148 unit tests
```

Every subcommand is idempotent and resumable. The DB schema lives in `src/video_to_notebook/db/migrations/*.sql` and uses `PRAGMA user_version` for linear migration tracking.

## Output language: ONE per project, even with cross-language sources

A project has exactly one `build_meta.language` value (`zh` or `en`). Every chapter, every concept page, every UI string on the rendered site is in **that one language** — regardless of source mix.

If the user crawls a mix of English and Chinese courses into the same project (e.g. Stanford CS336 + a B 站 讲座), the transcripts in SQLite stay in their native languages (correct, for source fidelity), but the synthesized output is monolingual. Cross-language lecturer quotes get **translated to the target language** with source-course attribution; never ship a `<blockquote>` in the source language inside a chapter whose prose is in another language. Code, formulas, slugs, lecturer names pass through verbatim. Full rationale and examples in [`skills/video-to-notebook/SKILL.md`](skills/video-to-notebook/SKILL.md#core-principle-one-output-language-even-when-sources-span-multiple).

## Bilingual content layout (v2.2+)

The site supports parallel zh and en builds. **Content (HTML fragments + manifest/curriculum JSON) lives per-language under `<lang>/` sub-folders, not flat.** Astro routes dispatch on `PUBLIC_LANGUAGE` (build-time env). Pages CI builds twice — once with `PUBLIC_LANGUAGE=zh` mounted at `/`, once with `PUBLIC_LANGUAGE=en` mounted at `/en/` — and merges into a single artifact.

```
template-site/src/content/textbook/
├── zh/
│   ├── 1.html ... 21.html
│   └── curriculum.json
└── en/
    ├── 1.html ... 21.html
    └── curriculum.json

template-site/src/content/concept-explainers/
├── zh/
│   ├── <slug>.html ...
│   └── manifest.json
└── en/
    ├── <slug>.html ...
    └── manifest.json
```

### How the Python writers behave

`build/textbook_writer.py` and `build/concept_writer.py` read `build_meta.language` from the project's SQLite (defaulting to `'zh'` for legacy projects) and write into the matching `<lang>/` folder. One demo project corresponds to one language. **Bilingual demos need two projects (or one project that swings `build_meta.language` between runs)** — see `examples/frontier-notebook/build.sh --bilingual` for a reference implementation.

### How to drive Phase-2 content regeneration (en chapters + concepts)

The zh demo is the source of structural truth — its 21 chapters and 33 concepts define the topology. The en version regenerates *bodies* from the same English source transcripts (not machine-translation), preserving chapter order and concept slugs:

```bash
cd <project-dir>
# 1. Back up zh, flip the project to en, wipe synth outputs
cp -r .video-to-notebook .video-to-notebook.zh-backup
sqlite3 .video-to-notebook/db.sqlite "INSERT INTO build_meta (key, value) VALUES ('language', 'en') ON CONFLICT(key) DO UPDATE SET value=excluded.value;"
rm -rf .video-to-notebook/textbook/*.html .video-to-notebook/concepts/*.html
sqlite3 .video-to-notebook/db.sqlite "UPDATE curriculum_chapters SET status='planned', synthesized_path=NULL, synthesized_at=NULL; DELETE FROM concept_explanations;"

# 2. Translate curriculum titles + blurbs in-place via SQL (preserves order/slugs)
#    OR re-run `video-to-notebook curriculum` (writes prompts/curriculum.json),
#    edit decisions, then `video-to-notebook curriculum --apply`.
# 3. Loop: synthesize chapters 1..21 + explain all concepts via in-session agent.
# 4. Build → fragments land under .video-to-notebook/textbook/ + concepts/, then
#    `video-to-notebook build` copies them into `<project>/site/src/content/<area>/en/`.
# 5. Copy en/*.html + en/manifest.json + en/curriculum.json into the source repo
#    under template-site/src/content/<area>/en/, commit, push → Pages deploys.
```

### Agent-id convention for bilingual writes

When writing en results envelopes, suffix the standard agent-id with `:v2-en` (or just use whatever distinguishable string you like) so audits can tell zh vs en synthesis apart:

```json
{
  "schema_version": "1",
  "kind": "synthesize_results",
  "chapter_order_idx": 1,
  "synthesizer": "claude-code-max:v2-en",
  "html_fragment_path": "/tmp/en/ch1.html"
}
```

### Header language toggle (Astro)

`Base.astro` renders an `EN`/`中` button that navigates between sibling deployments preserving the current sub-path. The button's `data-base` attribute is `import.meta.env.BASE_URL` baked at build time — the JS uses it to construct the target URL. If you change `Base.astro`'s button markup, keep `data-base={base}` intact or the toggle 404s on Pages.

### Don't translate Chinese fragments to en

The en chapters should be authored *from the English source transcripts*, not machine-translated from the zh fragments. The zh chapters' structural decisions (section order, equations, SVG, code) are good scaffolding to follow, but the prose must be sourced from the English lectures' verbatim quotes. Otherwise the en version will read as "translated Chinese," not as native English textbook prose.

## Code style (when you edit the repo)

- **Ruff** with `select = ["E", "F", "I", "B", "UP", "SIM"]`. Must be green.
- **Pyright** strict on `src/` and `tests/`. Must be green.
- **Pytest** suite green excluding `-m "not e2e"` and the embedding tests (which require huggingface network).
- All new behavior needs a test under `tests/unit/`.
- Type hints required on new functions. `from __future__ import annotations` at module top.
- New deps require user discussion first (open an issue).

Pre-PR check:

```bash
ruff check . && pyright src tests && pytest -m "not e2e" --ignore=tests/unit/test_embedding.py
```

CI runs the same three commands.

## Safety boundaries

1. **Don't commit synthesized content.** The textbook/concept HTML fragments live in `.video-to-notebook/` (gitignored). They're derived from copyrighted lecture transcripts; the *tool* is OSS, the *content* isn't redistributable. `.gitignore` already excludes `.video-to-notebook/` — keep it that way.

2. **Don't bump prompt versions casually.** Files like `src/video_to_notebook/explain/prompts.py` have a `_VERSION` constant that's emitted in the envelope. Past synthesized content was authored under a specific contract; readers and tests may rely on it. Bump intentionally + add a CHANGELOG entry.

3. **Don't add network calls outside `crawl/` and `tag/` and `cluster/`.** The other stages are LLM-agnostic by design — they only read/write SQLite and HTML files. Keep them that way so they work offline / with any agent.

4. **Don't modify `template-site/src/content/`.** That directory is *written into* by `video-to-notebook build`. It's not source-of-truth; SQLite is. Editing it directly creates inconsistencies.

## When the user asks for a new feature

1. **Existing crawler adapter?** Coursera/edX/MIT-OCW go in `src/video_to_notebook/crawl/`. Add a class implementing the `Crawler` protocol; wire into `cli.py:_detect_platform`. See `crawl/youtube.py` for the template.

2. **New ontology for a non-AI domain?** Add a YAML under `examples/<domain>/ontology.yaml`. Format: see `examples/ontology-llm.yaml`.

3. **New LLM stage** (e.g., quiz generator)?
   - Create `src/video_to_notebook/<stage>/{prompts.py, prompt_io.py}` following the pattern of `explain/`.
   - Migration if you need new tables.
   - Add CLI subcommand in `cli.py`.
   - Document the envelope in `docs/AGENT_PROTOCOL.md`.
   - Test the apply path under `tests/unit/test_<stage>_prompt_io.py`.

## Pointers

- **Pipeline walkthrough**: `skills/video-to-notebook/SKILL.md` (skill format, but the prose is agent-agnostic).
- **JSON schemas**: `docs/AGENT_PROTOCOL.md`.
- **In-session recipe**: `examples/frontier-notebook/RUNBOOK.md`.
- **Design specs**: `docs/specs/`.
- **Implementation plans** (TDD-decomposed): `docs/superpowers/plans/`.
- **Examples**: `examples/frontier-notebook/` (5-course World-Models corpus).
- **Changelog**: `CHANGELOG.md` (v1.0 → v2.3.0, including in-session-default behavior flip).
- **Bilingual demo plan**: `docs/plans/2026-05-19-bilingual-demo.md`.

## In one line

> *Drive the pipeline by re-invoking each LLM command with `--apply` after writing the decisions JSON. Read `docs/AGENT_PROTOCOL.md` for the schemas. Set your agent-id so audits work. Don't commit synthesized HTML — it's derived from copyrighted source.*
