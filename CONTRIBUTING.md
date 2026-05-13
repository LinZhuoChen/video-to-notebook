# Contributing to course-merger

Thanks for your interest! course-merger is a small project, but we welcome contributions in three places especially:

1. **New crawler adapters** — Coursera, edX, MIT-OCW, B站 collections, etc.
2. **Ontology files** for non-AI/CS domains (biology, history, music theory, …) under `examples/`.
3. **Bug fixes + tests** for any reported issue.

## Development setup

```bash
git clone https://github.com/chenlinzhuo/course-merger.git
cd course-merger

# Install with dev dependencies. We use uv but pip works too.
uv pip install -e ".[dev]"
# or: python -m venv .venv && .venv/bin/pip install -e ".[dev]"

# Run the test suite (skips e2e + embedding-network tests if model isn't cached)
pytest -v -m "not e2e"

# Static checks
ruff check .
pyright src tests
```

Node 20+ is required for the Astro build (the `template-site/` package). To exercise the full build pipeline:

```bash
cd template-site && npm install && cd ..
mkdir /tmp/cm-dev && cd /tmp/cm-dev
course-merger init
# (crawl / tag / cluster / build to your taste)
```

## Code style

- **Python**: ruff + pyright must be green. We use `select = ["E", "F", "I", "B", "UP", "SIM"]`. Per-file ignores for `typer.Option` in `cli.py` are intentional.
- **Type hints required** on all new functions. `from __future__ import annotations` at the top of every module.
- **Tests required** for new behavior. Pattern: one test file per module under `tests/unit/`, fixture-seeding for DB integration.
- **No new dependencies** without raising an issue first.

## Architecture sketch

```
course_merger/
├── cli.py              # typer entrypoint (init, crawl, tag, cluster, build, curriculum, synthesize, explain, serve)
├── config.py           # PROJECT_MARKER, find_project_root
├── crawl/              # yt-dlp adapters: YouTube, Bilibili
├── tag/                # Claude Haiku per-chunk tagging
├── cluster/            # MiniLM embeddings + LLM-reviewed merges
├── curriculum/         # chapter sequence design (Plan 6)
├── synthesize/         # per-chapter HTML generator (Plan 6)
├── explain/            # per-concept HTML explainer (v1.3)
├── build/              # SQLite → Markdown/JSON → Astro
└── db/                 # session.py + migrations/*.sql (linear, user_version)
```

Every CLI subcommand is **idempotent and resumable**. Re-running a stage should not corrupt or duplicate data; it should pick up where the previous run left off.

## Style guide for LLM prompts

The `tag`, `curriculum`, `synthesize`, `explain` modules each have a `prompts.py` file that's **versioned** (`TAGGER_PROMPT_VERSION`, `EXPLAINER_VERSION`, etc.). When you change a prompt's behavior:

- Bump the version number.
- The version is emitted in the prompt envelope so downstream graders / reruns can distinguish v1 vs v2 output.
- Don't silently change tone or output format — past synthesized content was authored under a specific contract; readers and tests will rely on it.

## Pull request checklist

Before sending:

- [ ] `pytest -m "not e2e"` is green
- [ ] `ruff check .` is clean
- [ ] `pyright src tests` is clean
- [ ] If you added a new CLI command, you've also added at least one test under `tests/unit/`
- [ ] If you added a new migration, you've also added a test under `tests/unit/test_migrations.py`
- [ ] If you added a user-visible change, you've added a `[Unreleased]` entry in `CHANGELOG.md`

## Reporting bugs

Open an issue with:

- What you ran (full command line)
- What you expected
- What happened (paste error tracebacks verbatim in a `<details>` block)
- `course-merger version` output
- OS + Python version

For crawl/tag bugs, please include the corresponding `course-merger crawl --debug` or `tag --print-prompts` JSON output if redactable.

## License

By contributing, you agree your contribution is licensed under the same [MIT License](LICENSE) as the project.
