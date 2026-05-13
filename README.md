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

## Textbook generation (v1.2+)

After `tag` and `cluster`, you can synthesize the merged corpus into a beginner-friendly multi-chapter HTML textbook:

```bash
# 1. Design the chapter sequence (in-session in Claude Code)
course-merger curriculum --print-prompts > curr.json
# Claude reads curr.json, designs the chapter order, writes curr-results.json
course-merger curriculum --apply-results curr-results.json

# 2. For each chapter:
course-merger synthesize --chapter N --print-prompts > chN.json
# Claude reads + writes /tmp/chN.html with anti-bias opening, SVG diagrams,
# CSS animations, embedded source clip, LaTeX, takeaways
course-merger synthesize --chapter N --apply-results apply-chN.json

# 3. Build & view
course-merger build
course-merger serve  # http://localhost:4321/textbook/
```

Each chapter is a self-contained HTML fragment with inline SVG, CSS animations, embedded source-video iframes (timestamp-deep-linked), and LaTeX math (KaTeX-rendered).

See `skills/course-merger/SKILL.md` for the full workflow inside Claude Code.

## Concept encyclopedia (v1.3+)

In addition to the linear textbook, you can generate a rich illustrated entry per concept — definition + intuition + SVG + interactive demo + worked example + common misconceptions + cross-links:

```bash
course-merger explain --concept linear-algebra --print-prompts > la.json
# Claude reads la.json (concept + occurrences + co-occurring related slugs),
# writes /tmp/la.html following the v2 style guide (namespace-prefixed
# CSS, CSS-var color palette, one of three interactive widget templates)
course-merger explain --concept linear-algebra --apply-results la-results.json

course-merger build  # /concepts/<slug>/ now serves the rich explainer
```

The v2 style guide (`src/course_merger/explain/prompts.py`) enforces:
- per-concept CSS namespace prefix to avoid collisions when multiple explainers share a page
- CSS-variable-only colors (works in light + dark + per-module accent)
- fixed section order: header + quickref + intuition + deepdive + interact + example + pitfalls + see-also + sources
- anti-bias opener, one-invariant-per-animation, equation-chain math, counter-example misconceptions

## Site features

The built site (`course-merger build && course-merger serve`) ships with:

- 🌓 dark mode (`prefers-color-scheme` + manual toggle in header, localStorage persistence)
- 🎨 per-module accent palette (green / blue / purple / amber / rose) auto-applied via `data-module-idx`
- 📊 chapter mini-map (right rail tracks `h2`/`h3` headings with `IntersectionObserver`)
- ⌨️ keyboard navigation (← / → arrows step through chapters)
- 📱 mobile drawer (hamburger menu, slide-in from left, mirrors textbook sidebar)
- 🔍 client-side search via [Pagefind](https://pagefind.app/)
- 🧮 LaTeX math via [KaTeX](https://katex.org/) (write `$...$` or `$$...$$` in fragments)

---

## Disclaimer

`course-merger` is a **tool**. The user is responsible for ensuring they have the right to crawl, process, and redistribute any content fed through this pipeline. This includes YouTube/Bilibili Terms of Service governing programmatic content access, the original creator's license on the lecture content, and fair use / transformative use considerations in the user's jurisdiction.

The tool's authors disclaim responsibility for content generated by users. **Personal study use is generally low risk. Public redistribution or commercial use of synthesized content may not be.** Consult the source materials' licenses before going beyond personal use.

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

## Roadmap

**Shipped:** v1.0 foundation · v1.1 in-session mode · v1.2 textbook generator · v1.3 concept explainer + design-system polish (see [CHANGELOG.md](CHANGELOG.md)).

**Deferred:**

- **Whisper fallback**: transcribe videos with no subtitles via mlx-whisper / Groq.
- **Coursera/edX/MIT-OCW adapters**: more crawlers behind the `Crawler` Protocol.
- **Live filter on compare view**: client-side `?courses=cs336,gpu-mode` selection.
- **`review` CLI**: human-in-the-loop dispatch for `ambiguous` cluster decisions.
- **Multi-language concept aliasing**: dedicated Chinese ↔ English concept name pairs.
- **Automatic incremental rebuild**: `init_db()` on every CLI command + `ensure_site_dir` template sync on each `build`.

## Architecture & design

- Design spec: [`docs/specs/2026-05-09-course-merger-skill-design.md`](docs/specs/2026-05-09-course-merger-skill-design.md)
- Implementation plans (TDD-decomposed):
  - Plan 1: [Foundation + Crawl](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
  - Plan 2: [Tag + Cluster](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)
  - Plan 3: [Build + HTML](docs/superpowers/plans/2026-05-09-plan-3-build-and-html.md)
  - Plan 4: [Demo + Deploy + Skill](docs/superpowers/plans/2026-05-09-plan-4-demo-deploy-skill.md)
  - Plan 6: [Textbook generator](docs/superpowers/plans/2026-05-13-plan-6-textbook-generator.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome — particularly new crawler adapters and ontology files for non-AI/CS domains.

## License

MIT
