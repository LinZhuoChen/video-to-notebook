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

## Agent-driven workflow

Every LLM stage (`tag`, `cluster`, `curriculum`, `synthesize`, `explain`) supports a two-phase **`--print-prompts` / `--apply-results`** pattern. The CLI emits a JSON envelope describing pending work; you (the agent) read it, decide, write a results JSON; the CLI applies that to SQLite.

The protocol is **agent-agnostic**. Schemas, conventions, idempotency guarantees, error semantics all live in [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md). Read that file before driving the pipeline for the first time.

### Quick start for Codex / any agent

```bash
mkdir my-study-site && cd my-study-site
video-to-notebook init
video-to-notebook crawl "<youtube-or-bilibili-url>" --name <slug>
# Repeat crawl for each course

# Then, for each LLM stage:
video-to-notebook <stage> [args] --print-prompts > /tmp/cm-prompts.json
# (you read the envelope, reason, write /tmp/cm-results.json)
video-to-notebook <stage> [args] --apply-results /tmp/cm-results.json
```

For `tag` this is a batch loop (small `--limit`, repeat until `chunks` array empty in the prompts envelope). For `cluster`, `curriculum` it's one-shot. For `synthesize` it's per-chapter; for `explain` it's per-concept.

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
- **Design spec**: `docs/specs/2026-05-09-video-to-notebook-skill-design.md`.
- **Implementation plans** (TDD-decomposed): `docs/superpowers/plans/`.
- **Examples**: `examples/frontier-notebook/` (5-course World-Models corpus).
- **Changelog**: `CHANGELOG.md` (v1.0 → v1.3 ).

## In one line

> *Drive the pipeline through `--print-prompts` / `--apply-results`. Read `docs/AGENT_PROTOCOL.md` for the schemas. Set your agent-id so audits work. Don't commit synthesized HTML — it's derived from copyrighted source.*
