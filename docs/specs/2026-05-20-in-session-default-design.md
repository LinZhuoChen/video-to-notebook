# In-Session-Default for LLM Commands — Design Spec

**Date:** 2026-05-20
**Author:** chenlinzhuo
**Status:** Draft (post-brainstorming)
**Related:** [video-to-notebook design spec](./2026-05-09-video-to-notebook-skill-design.md)

---

## 1. Goal

Flip the project's default execution path so the five LLM-driven commands (`tag`, `cluster`, `curriculum`, `synthesize`, `explain`) run **in-session by default** — emitting a prompt envelope to disk and exiting, expecting a conversation-driven agent (Claude Code / Codex) to write decisions and apply them. The Anthropic-SDK-driven "API mode" remains available behind an opt-in `--use-api` flag for `tag` and `cluster` only (the only two commands that ever had an API path).

This change makes the no-API-key path the primary, documented workflow. The current README, example scripts, and CLI defaults all assume an API key — that assumption is inverted here.

### Non-Goals

- No change to the per-step business logic. `collect_*_prompts` and `apply_*_results` functions stay byte-identical.
- No change to non-LLM commands: `init`, `crawl`, `build`, `serve`, `version`.
- No change to DB schema.
- API mode is **not** removed (user explicitly chose "keep API mode behind `--use-api`").
- No rewrite of `ClaudeTagger` / `Reviewer` (the API-mode classes). They keep working as-is.
- Not designing a programmatic agent loop yet (no `video-to-notebook agent-run` meta-command). The agent follows a markdown runbook.

---

## 2. Current Behavior (baseline)

| Command | Current default (no flags) | In-session entry today | API-mode entry today |
|---|---|---|---|
| `tag` | calls `anthropic.Anthropic()` | `--print-prompts` → stdout JSON; `--apply-results <path>` writes back | default |
| `cluster` | calls `anthropic.Anthropic()` | `--print-prompts` → stdout; `--apply-results <path>` | default |
| `curriculum` | prints prompts to stdout | already default; `--apply-results <path>` | n/a |
| `synthesize` | prints prompts to stdout | already default; `--apply-results <path>` | n/a |
| `explain` | prints prompts to stdout | already default; `--apply-results <path>` | n/a |
| `examples/frontier-notebook/build.sh` | calls `tag` / `cluster` plainly → API path | n/a | implicit |

Two inconsistencies in the current code:
1. **Default split**: `tag` / `cluster` default to API; `curriculum` / `synthesize` / `explain` default to in-session-stdout.
2. **Output channel**: all in-session paths print to **stdout**. For 1500+ chunks this produces multi-MB JSON in the conversation transcript.

---

## 3. Target Behavior

### 3.1. Default path layout

All in-session prompt / decision files live under `.video-to-notebook/prompts/`:

```
.video-to-notebook/prompts/
├── tag.json                          ← prompts (CLI writes)
├── tag.decisions.json                ← decisions (agent writes)
├── cluster.json
├── cluster.decisions.json
├── curriculum.json
├── curriculum.decisions.json
├── synthesize/
│   ├── chapter-1.json
│   ├── chapter-1.decisions.json
│   ├── chapter-2.json
│   └── ...
└── explain/
    ├── attention.json                ← filename = concept slug
    ├── attention.decisions.json
    └── ...
```

Rationale: per-chapter and per-concept files (rather than one big file per command) means an agent can apply results one at a time and keep partial progress on rerun.

The `.video-to-notebook/prompts/` directory is auto-created by each command's first invocation.

### 3.2. Flag matrix

For each command, default (no flag) is **write-prompts-to-default-path-and-exit-0**. The full flag matrix:

| Command | no flags (NEW default) | `--apply` (NEW) | `--apply-results <path>` (kept) | `--use-api` (NEW) | `--print-prompts` (legacy) |
|---|---|---|---|---|---|
| `tag` | writes `prompts/tag.json` | reads `prompts/tag.decisions.json` | reads explicit path | calls SDK (today's default) | no-op + deprecation warning |
| `cluster` | writes `prompts/cluster.json` | reads `prompts/cluster.decisions.json` | reads explicit path | calls SDK (today's default) | no-op + deprecation |
| `curriculum` | writes `prompts/curriculum.json` | reads `prompts/curriculum.decisions.json` | reads explicit path | — (no API path exists) | no-op + deprecation |
| `synthesize --chapter N` | writes `prompts/synthesize/chapter-N.json` | reads `prompts/synthesize/chapter-N.decisions.json` | reads explicit path | — | no-op + deprecation |
| `explain --concept SLUG` | writes `prompts/explain/<SLUG>.json` | reads `prompts/explain/<SLUG>.decisions.json` | reads explicit path | — | no-op + deprecation |

Mutual-exclusion rules (enforced at CLI parse, hard errors with exit 1):
- `--apply` and `--apply-results` cannot both be set.
- `--apply` (or `--apply-results`) and `--use-api` cannot both be set.
- `--print-prompts` is silently accepted but emits a one-line stderr deprecation warning and otherwise behaves identically to no-flag default.

### 3.3. Stderr hint format

Every default-path invocation prints to **stderr** (not stdout — stdout stays clean so it can still be piped):

```
prompts written: .video-to-notebook/prompts/tag.json (1483 chunks)
→ write decisions to: .video-to-notebook/prompts/tag.decisions.json
→ then: video-to-notebook tag --ontology ontology.yaml --apply
```

The hint always includes:
1. The path it wrote.
2. A one-line size summary (`(N chunks)`, `(N clusters)`, `(N chapters)`, `(N occurrences)` — varies by command).
3. The expected decisions path.
4. The exact follow-up command (with the same flags the user passed, plus `--apply`).

`--apply` mode prints a one-line success message to stdout (unchanged from today's `--apply-results` behavior).

### 3.4. `--print-prompts` deprecation

`--print-prompts` is preserved as a no-op alias with the following behavior:
- Accepted by argparse without error.
- Emits to stderr: `warning: --print-prompts is now the default and will be removed in a future release.`
- Then proceeds identically to no-flag default (writes to file, exits 0).
- **Does not** restore the old stdout-print behavior. (User chose "no `--stdout` escape hatch.")

This is mildly lossy for any external script that was piping `video-to-notebook curriculum --print-prompts | jq …`. Those scripts must migrate to reading the file from disk. CHANGELOG must call this out.

### 3.5. `--use-api` (tag / cluster only)

Tag and cluster gain a `--use-api` boolean flag:
- Default: false → in-session path
- `--use-api`: calls `anthropic.Anthropic()` and runs the existing `ClaudeTagger` / `Reviewer` pipeline end-to-end (i.e., today's default behavior, unchanged)
- Mutually exclusive with `--apply` and `--apply-results`

curriculum / synthesize / explain do not get `--use-api` because they have no API-side implementation today and we are not adding one.

---

## 4. Script Reorganization

### 4.1. New file: `examples/frontier-notebook/bootstrap.sh`

Subset of current `build.sh`. Runs:
1. Sanity-check `node`, `yt-dlp`, `video-to-notebook` (but **not** `ANTHROPIC_API_KEY` — bootstrap doesn't need it).
2. `video-to-notebook init --language <zh|en>` if not already initialized.
3. Loop over `courses.toml` and crawl each entry.
4. Print a "next step" pointer to `RUNBOOK.md`.

No `--language` switching, no `--bilingual`, no tag/cluster/build calls. Quiet, fast, idempotent (re-running skips already-crawled videos).

### 4.2. New file: `examples/frontier-notebook/RUNBOOK.md`

Agent-facing recipe. Structure:

1. **Prereqs** — venv with `video-to-notebook`, Node 20+, optional bilibili cookies.
2. **Step 0** — `bash bootstrap.sh` (init + crawl).
3. **Step 1: Draft ontology** — agent reads a sample of crawled chunks (SQL one-liner provided), writes / edits `ontology.yaml`.
4. **Step 2: Tag** — `video-to-notebook tag --ontology ontology.yaml` → read `prompts/tag.json` → write decisions per the embedded tagger instructions → `--apply`. Includes a short worked example of the decisions JSON shape.
5. **Step 3: Cluster** — same pattern.
6. **Step 4: Curriculum** — same.
7. **Step 5: Synthesize** — loop over chapters: `video-to-notebook synthesize --chapter N` for each chapter in `curriculum_chapters`. SQL snippet provided to list pending chapters.
8. **Step 6: Explain** — loop over concepts: `video-to-notebook explain --concept SLUG`. SQL snippet provided.
9. **Step 7: Build** — `video-to-notebook build` then `serve`.
10. **Bilingual addendum** — for `--bilingual`, run steps 5–7 twice with `build_meta.language` toggled.

The runbook is written as imperative checkpoints, not background reading. Each step is a numbered TODO an agent can transcribe into `TaskCreate`.

### 4.3. Modified file: `examples/frontier-notebook/build.sh`

Minimal changes:
1. Header comment block rewritten — first sentence: "API-key path. Requires `ANTHROPIC_API_KEY`. For the no-key path, see `RUNBOOK.md`."
2. Every `video-to-notebook tag …` invocation gets `--use-api` appended.
3. Every `video-to-notebook cluster …` invocation gets `--use-api` appended.
4. The `ANTHROPIC_API_KEY` check stays as-is.
5. The `--bilingual` flag and the in-script note about synthesize/explain being agent-driven also stay (that note is now even more accurate).

Behavior for API-key users is preserved. Behavior for non-API users gets a clear error from the API-key check.

---

## 5. Documentation Updates

### 5.1. `README.md` and `README.zh-CN.md`

- "Quick start" section pivots to: "you do not need an API key. Run `bash examples/frontier-notebook/bootstrap.sh`, then follow `RUNBOOK.md` inside a Claude Code or Codex session."
- A new sub-section "Got an API key? Use the one-shot script" points at `build.sh`.
- Architecture diagram (if present) gets a note about the agent in the loop.

### 5.2. `examples/frontier-notebook/README.md`

Becomes a short index pointing at `RUNBOOK.md` (default) and `build.sh` (API-key shortcut). Cost table stays — it applies to both paths, since cost is dominated by the LLM tokens which are the same regardless of who is calling Claude.

### 5.3. `AGENTS.md` / `docs/AGENT_PROTOCOL.md`

The agent protocol doc should reference the new default paths under `.video-to-notebook/prompts/` and explain the deterministic file naming so agents (or future tooling) can discover work.

### 5.4. `CHANGELOG.md`

A `2.3.0` entry (assuming SemVer minor — this is a behavior change but no removed surface):
- Default flip for `tag` / `cluster`
- New `--use-api` flag (tag / cluster)
- New `--apply` shorthand (all 5 commands)
- New default prompt/decision paths under `.video-to-notebook/prompts/`
- `--print-prompts` deprecation
- New `bootstrap.sh` + `RUNBOOK.md`
- `build.sh` now passes `--use-api` to tag / cluster

---

## 6. Implementation Plan (sketch — full plan via writing-plans)

### 6.1. New helper module

`src/video_to_notebook/inflow.py` — single-source-of-truth for prompt/decision paths:

```python
def prompts_dir(state_dir: Path) -> Path: ...
def tag_paths(state_dir: Path) -> tuple[Path, Path]: ...     # (prompts, decisions)
def cluster_paths(state_dir: Path) -> tuple[Path, Path]: ...
def curriculum_paths(state_dir: Path) -> tuple[Path, Path]: ...
def synthesize_paths(state_dir: Path, chapter: int) -> tuple[Path, Path]: ...
def explain_paths(state_dir: Path, concept_slug: str) -> tuple[Path, Path]: ...
def write_prompts_envelope(path: Path, envelope: dict) -> None: ...   # mkdir -p + atomic write
def emit_hint(*, prompts_path: Path, decisions_path: Path, size_summary: str, next_cmd: str) -> None: ...
```

All five `*_cmd` functions in `cli.py` route through this module — no inline path-building duplicated across commands.

### 6.2. CLI changes (per command)

For each of `tag_cmd`, `cluster_cmd`, `curriculum_cmd`, `synthesize_cmd`, `explain_cmd`:
1. Add `--apply` boolean and (for tag/cluster) `--use-api` boolean.
2. Reorder the body so the dispatch logic is: `--use-api` (tag/cluster only) → `--apply` → `--apply-results <path>` → `--print-prompts` (deprecated no-op) → **default = write to file**.
3. Replace stdout writes with `write_prompts_envelope(...)` calls.
4. Emit hints via `emit_hint(...)` to stderr.

### 6.3. Tests

Add to `tests/`:
- `test_cli_in_session_default.py` — for each of the 5 commands: invoke without flags, assert the expected prompt file exists with valid JSON, assert exit 0, assert hint on stderr, assert nothing on stdout.
- `test_cli_apply_shorthand.py` — `--apply` reads default decisions path; `--apply-results <path>` still works.
- `test_cli_use_api_isolation.py` — `--use-api` on tag/cluster still goes through `ClaudeTagger` / `Reviewer` (mock the SDK).
- `test_cli_mutual_exclusion.py` — `--apply` + `--apply-results`, `--apply` + `--use-api`, etc. all exit 1.
- `test_cli_print_prompts_deprecation.py` — `--print-prompts` still works as no-op but emits stderr warning.

Existing tests that assert stdout JSON output need updating to read from the new file paths.

### 6.4. Scripts

- Author `bootstrap.sh` by copying lines 1–101 of `build.sh` (the pre-tag portion) and trimming the language/bilingual flags.
- Author `RUNBOOK.md` (target ~150 lines including code blocks).
- Edit `build.sh`: ~6 lines changed (header block + two `--use-api` insertions).

### 6.5. Docs

Sweep: `README.md`, `README.zh-CN.md`, `examples/frontier-notebook/README.md`, `AGENTS.md`, `docs/AGENT_PROTOCOL.md`, `CHANGELOG.md`.

---

## 7. Risks & Decisions Log

| Risk | Decision |
|---|---|
| Existing CI / external scripts piping `--print-prompts` output break | Accept. Deprecation warning + CHANGELOG note. |
| 5 commands' prompt files share one directory — collision if user runs the same command twice with different `--course` / `--limit` flags | Overwrite. Last invocation wins. Document this in RUNBOOK. (Alternative — content-hashed filenames — rejected as overkill.) |
| Agent forgets `--apply` after writing decisions | Stderr hint always echoes the exact command. RUNBOOK uses TaskCreate-friendly checkpoints. |
| `.video-to-notebook/prompts/` grows large in long-running projects | Acceptable. Files are small relative to the SQLite DB. No GC needed in v1. |
| `--use-api` flag name conflicts with future env-var conventions | Reviewed — no conflict with existing flags or env vars. |
| Atomic write on cross-filesystem moves (Linux + macOS) | `write_prompts_envelope` uses `tempfile.NamedTemporaryFile(dir=path.parent, delete=False)` + `os.replace`. Same-FS guarantee since parent dir owns the temp. |

---

## 8. Open Questions

None at spec-write time. Brainstorming round resolved:
1. **API mode survives** behind `--use-api`.
2. **Output target** = default file path (not stdout).
3. **All 5 commands** unified (no per-command divergence).
4. **build.sh splits** into `bootstrap.sh` + `RUNBOOK.md` + retrofitted `build.sh`.
5. **No `--stdout` escape hatch.**

---

## 9. Acceptance Criteria

The change is done when:

- [ ] In a project that has been `init` + `crawl`ed, `video-to-notebook tag --ontology X` (no `ANTHROPIC_API_KEY` set in env) writes `prompts/tag.json`, exits 0, prints stderr hint, prints nothing to stdout.
- [ ] Same shape verified for `cluster` (after tag has populated proposed tags), `curriculum` (after cluster), `synthesize --chapter <existing-chapter>` (after curriculum), `explain --concept <existing-slug>` (after tag).
- [ ] If `synthesize --chapter N` is called and chapter N does not exist in `curriculum_chapters`, the command exits non-zero with a clear error (existing behavior — should be preserved, not regressed).
- [ ] `video-to-notebook tag --ontology X --use-api` (with key set) reproduces today's API behavior end-to-end — verified by snapshot comparison of resulting DB rows against a pre-change baseline.
- [ ] `--apply` reads the default decisions path; `--apply-results <path>` still reads an explicit path; both write identical DB state.
- [ ] If `--apply` is invoked but no decisions file exists at the default path, the command exits non-zero with a clear "decisions file not found" error.
- [ ] `--print-prompts` emits a stderr deprecation warning and otherwise behaves like the new default (writes file, exits 0).
- [ ] All four documented mutual-exclusion combinations (`--apply` + `--apply-results`, `--apply` + `--use-api`, `--apply-results` + `--use-api`, `--print-prompts` + `--apply`) exit 1 with clear errors.
- [ ] `bash examples/frontier-notebook/bootstrap.sh` completes (with the existing demo `courses.toml`) on a machine with no API key, producing a populated DB and no other side effects.
- [ ] `bash examples/frontier-notebook/build.sh` (with key set) still produces a site identical to the pre-change baseline.
- [ ] `RUNBOOK.md` walks a fresh agent through the full pipeline; an in-session run produces the same site as `build.sh`.
- [ ] All existing tests pass; new tests in §6.3 pass.
- [ ] README / CHANGELOG / AGENTS.md updated.
