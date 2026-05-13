# course-merger

> Crawl open-courseware, tag chunks with concept labels via Claude, and render an interactive cross-course concept-anchored static site for self-study.

[![CI](https://github.com/chenlinzhuo/course-merger/actions/workflows/ci.yml/badge.svg)](https://github.com/chenlinzhuo/course-merger/actions/workflows/ci.yml)

The killer feature: a **"Compare across courses"** view. Pick any concept (e.g. *Self-Attention*), see how Stanford CS336, GPU MODE, and Vizuara each teach it — side by side, with click-to-seek timestamped video.

## Demo

Live demo: [chenlinzhuo.github.io/course-merger/](https://chenlinzhuo.github.io/course-merger/) — built from the 5 World-Models × Agents courses in `examples/frontier-notebook/`.

## Install

```bash
# 1. Python CLI (3.12+)
pip install course-merger
# or: uv tool install course-merger

# 2. External requirements
brew install node yt-dlp        # Node 20+ for the HTML build; yt-dlp for crawling
playwright install chromium     # only if running e2e tests
```

For Bilibili crawling you also need a logged-in browser (`--cookies-from edge|chrome|firefox`).

## Quickstart

```bash
export ANTHROPIC_API_KEY=sk-ant-...

mkdir my-study-site && cd my-study-site

# 1. Initialize
course-merger init

# 2. Crawl one or more courses
course-merger crawl "https://www.youtube.com/playlist?list=PLxxx" --name cs336
course-merger crawl "https://www.bilibili.com/video/BVxxx/" --name "vizuara-llm" --cookies-from edge

# 3. Tag chunks with concept labels (Claude Haiku, ~$0.10/course)
course-merger tag --ontology examples/ontology-llm.yaml --limit 200

# 4. Cluster proposed tags (Claude Sonnet, ~$0.30/run)
course-merger cluster --ontology examples/ontology-llm.yaml

# 5. Build the static site
course-merger build

# Preview locally at http://localhost:4321
course-merger serve
```

After step 5, `site/dist/` is a complete static site you can serve from any HTTP server or deploy to GitHub Pages.

## How it works

```
                 ┌──────────────────────────────────────┐
                 │           SQLite (.course-merger/db) │
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

Each subcommand is **idempotent and resumable**. Add a new course → only that course gets crawled/tagged. Re-run `cluster` → it picks up new proposed tags, doesn't re-process settled ones. `build --incremental` re-renders only concepts that changed.

## Use it as a Claude Code skill

Install once:

```bash
git clone https://github.com/chenlinzhuo/course-merger.git
bash course-merger/skills/course-merger/scripts/install-locally.sh
```

Then in Claude Code:

> Build me a study site from these courses: <playlist1> <playlist2> <playlist3> using examples/ontology-llm.yaml

Claude will walk through the 5 steps with you, asking for confirmation before tag/cluster (which cost money).

The full skill manifest is at `skills/course-merger/SKILL.md`.

## In-session mode (Claude Max users — no API key)

If you have a Claude Max subscription (or any Claude Code subscription), you can skip the Anthropic API key. `course-merger tag` and `course-merger cluster` each accept two new flags:

- `--print-prompts` — emits a JSON envelope of pending work to stdout.
- `--apply-results <file>` — reads a decisions JSON and writes results to the DB.

Inside Claude Code, the conversation looks like:

```
You: "Crawl this playlist and tag using examples/ontology-llm.yaml. I have Max."

Claude:
  - course-merger init && course-merger crawl <url>
  - course-merger tag --ontology ... --print-prompts --limit 20 > p.json
  - (reads p.json, decides tags via its own reasoning)
  - writes r.json with decisions
  - course-merger tag --ontology ... --apply-results r.json
  - (repeats batch by batch until all chunks tagged)
  - same loop for cluster (one bundle file with both prompts + decisions)
  - course-merger build
```

The skill at `skills/course-merger/SKILL.md` automates this loop. Install with `bash skills/course-merger/scripts/install-locally.sh`.

**Trade-offs:**

| | API mode | In-session mode |
|---|----------|----------------|
| API key required | Yes | No |
| Cost for demo corpus | ~$2-4 | $0 extra (covered by Max) |
| Speed for 1000 chunks | ~5-10 min | ~1-2 hours |
| Speed for 100 chunks | ~30 sec | ~5-10 min |
| Best for | Large corpora | Small experiments |

**Shipped in v1.1** (2026-05-13): in-session mode for Claude Max users via `--print-prompts` / `--apply-results` flags on `tag` and `cluster`.

## Customize for your own corpus

The `examples/frontier-notebook/` directory is the recommended starting point:

```bash
cp -r examples/frontier-notebook examples/my-corpus
# Edit examples/my-corpus/courses.toml and examples/my-corpus/ontology.yaml
bash examples/my-corpus/build.sh
```

The build script chains crawl/tag/cluster/build, reads `courses.toml`, and lands a working site at `examples/my-corpus/.course-merger-project/site/dist/`.

## Cost reality check

Per course (50-100 lectures, ~1500 chunks):

| Stage | Model | Cost |
|-------|-------|------|
| Crawl | n/a (yt-dlp) | $0 |
| Tag | Claude Haiku (prompt caching) | ~$0.10-0.30 |
| Cluster | Claude Sonnet | ~$0.20-0.50 |
| Build | n/a (Astro) | $0 |
| **Total per course** | | **~$0.30-0.80** |

For a 5-course corpus, expect ~$2-4 first run. Re-runs are free thanks to per-chunk idempotency.

## Roadmap (deferred to v2)

- **Whisper fallback**: transcribe videos with no subtitles via mlx-whisper / Groq.
- **Coursera/edX/MIT-OCW adapters**: more crawlers behind the `Crawler` Protocol.
- **Live filter on compare view**: client-side `?courses=cs336,gpu-mode` selection.
- **`review` CLI**: human-in-the-loop dispatch for `ambiguous` cluster decisions.
- **Multi-language concept aliasing**: dedicated Chinese ↔ English concept name pairs.

## Architecture & design

- Design spec: [`docs/specs/2026-05-09-course-merger-skill-design.md`](docs/specs/2026-05-09-course-merger-skill-design.md)
- Implementation plans (TDD-decomposed):
  - Plan 1: [Foundation + Crawl](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
  - Plan 2: [Tag + Cluster](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)
  - Plan 3: [Build + HTML](docs/superpowers/plans/2026-05-09-plan-3-build-and-html.md)
  - Plan 4: [Demo + Deploy + Skill](docs/superpowers/plans/2026-05-09-plan-4-demo-deploy-skill.md)

## Contributing

PRs welcome — particularly new crawler adapters and ontology files for non-AI/CS domains. Run `pytest -v` before sending.

## License

MIT
