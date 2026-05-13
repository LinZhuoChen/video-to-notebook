<div align="center">

# 📚 course-merger

**Crawl open-courseware. Tag with Claude. Read as a unified textbook + encyclopedia.**

Turn a pile of YouTube / Bilibili playlists into a beginner-friendly merged course — illustrated chapters, interactive concept explainers, source-video deep links, fully searchable.

[![CI](https://github.com/chenlinzhuo/course-merger/actions/workflows/ci.yml/badge.svg)](https://github.com/chenlinzhuo/course-merger/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Astro](https://img.shields.io/badge/Astro-5-FF5D01?logo=astro&logoColor=white)](https://astro.build/)
[![Claude](https://img.shields.io/badge/powered_by-Claude-D97757)](https://anthropic.com/)

[**Live demo**](https://chenlinzhuo.github.io/course-merger/) · [**Quickstart**](#-quickstart) · [**How it works**](#-how-it-works) · [**Use as Claude Code skill**](#-use-as-a-claude-code-skill) · [**Roadmap**](#-roadmap)

---

</div>

## ✨ What you get

```
Input:  ─────►  YouTube + Bilibili playlists (3+ courses on the same topic)
                                  │
                                  ▼
                ┌─────────────────────────────────────────┐
                │  📥  crawl   →   yt-dlp + subtitles      │
                │  🏷️   tag     →   Claude Haiku (per chunk)│
                │  🔗  cluster →   MiniLM + Claude Sonnet  │
                │  📐  curriculum  →  in-session Claude    │
                │  ✍️   synthesize  →  in-session Claude    │
                │  💡  explain  →   in-session Claude      │
                │  🎨  build   →   Astro 5 static site     │
                └─────────────────────────────────────────┘
                                  │
                                  ▼
Output: ─────►  📖 A merged textbook (chapters in pedagogical order)
                💡 A concept encyclopedia (one rich page per concept)
                🔎 Cross-course "compare" view + Pagefind search
                🎬 Click-to-seek deep links into source videos
```

## 📸 Showcase

<table>
<tr>
<td width="50%" valign="top">

### 📖 Merged textbook

Chapters laid out in pedagogical order — your beginner reads top-to-bottom and gets a complete arc, not a mosaic of fragments.

- Inline SVG figures + CSS animations
- KaTeX-rendered LaTeX math
- Embedded source-video clips with timestamps
- Anti-bias opener + 3 takeaways per chapter
- ← / → keyboard nav · 📊 mini-map sidebar

</td>
<td width="50%" valign="top">

### 💡 Concept encyclopedia

Every important concept gets its own rich page — for the reader who wants depth on one idea.

- Definition / formula / pitfall **quickref card**
- Interactive widgets: sliders, step-buttons, animated SVG
- Worked numerical example with equation chain
- 3 counter-example misconceptions
- Cross-links to related concepts
- Source-clip deep links

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌓 Dark mode + per-module accent

```
Module 1  · Math intuition       🟢 green
Module 2  · Training intuition   🔵 blue
Module 3  · Vision origins       🟣 purple
Module 4  · Modern deep learning 🟡 amber
Module 5  · Architecture + future 🌸 rose
```

Auto-applied via `data-module-idx` on layout root. Cards, sidebars, drop caps, progress bars all inherit `--module-accent`.

</td>
<td width="50%" valign="top">

### 📱 Mobile-first, no JS framework

```
@media (max-width: 900px)
  → hamburger drawer slides in from left
  → textbook sidebar mirrors inside drawer
  → reading column expands to full viewport
```

No React, no Vue. Astro + 200 lines of vanilla JS. The whole concept page weighs ~30 KB gzipped (including SVG + interaction).

</td>
</tr>
</table>

## 🚀 Quickstart

### Option A — with an Anthropic API key

```bash
# Install the CLI (Python 3.12+)
pip install course-merger      # or: uv tool install course-merger
brew install node yt-dlp       # Node 20+ for the build, yt-dlp for crawling

# Run the pipeline
export ANTHROPIC_API_KEY=sk-ant-...
mkdir my-study-site && cd my-study-site

course-merger init
course-merger crawl "https://www.youtube.com/playlist?list=PLxxx" --name cs336
course-merger crawl "https://www.bilibili.com/video/BVxxx/"  --name vizuara-llm --cookies-from edge
course-merger tag      --ontology examples/ontology-llm.yaml  # ~$0.10/course
course-merger cluster  --ontology examples/ontology-llm.yaml  # ~$0.30/run
course-merger build
course-merger serve    # http://localhost:4321
```

Total cost for a 5-course corpus: **~$2-4** first run, **$0** on re-runs (idempotent).

### Option B — no API key, Claude Max subscription

Every LLM stage (`tag`, `cluster`, `curriculum`, `synthesize`, `explain`) has `--print-prompts` / `--apply-results` flags. Drive the pipeline from inside Claude Code using your Max subscription — no separate API key needed. See [**§ In-session mode**](#-in-session-mode-claude-max-users--no-api-key) below.

## 🏗 How it works

```
                  ┌──────────────────────────────────────────────┐
                  │           SQLite (.course-merger/db.sqlite)  │
                  │  courses · lectures · chunks                 │
                  │  concepts · chunk_concepts · aliases         │
                  │  curriculum_chapters · concept_explanations  │
                  └──────────────────────────────────────────────┘
                          ↑              ↑              ↑
   ┌──────────┐   crawl   │              │ tag          │ cluster   ┌──────────┐
   │ yt-dlp   │──────────▶│              │ (Haiku)      │ (Sonnet)  │  build   │
   │ subtitles│           │              │              │           │ (Astro)  │
   └──────────┘           │              │              │           └────┬─────┘
                          │              │              │                │
                          │  ┌───────────┴──────────────┴─┐              ▼
                          │  │  curriculum / synthesize /  │      ┌──────────┐
                          │  │  explain (in-session Claude)│      │ dist/    │ → GitHub Pages
                          │  └─────────────────────────────┘      └──────────┘
```

Each subcommand is **idempotent and resumable**:

- Add a new course → only that course gets crawled/tagged.
- Re-run `cluster` → picks up new proposed tags, doesn't re-process settled ones.
- `build --incremental` → re-renders only what changed.

**Output is a static site** — deploy anywhere (GitHub Pages, S3, Vercel, Netlify, your own nginx).

## 📦 Install

```bash
# 1. Python CLI (3.12+)
pip install course-merger
# or: uv tool install course-merger

# 2. External requirements
brew install node yt-dlp       # Node 20+ for the HTML build; yt-dlp for crawling
playwright install chromium    # only if running e2e tests
```

For Bilibili crawling you also need a logged-in browser (`--cookies-from edge|chrome|firefox`).

## 🤖 Use as a Claude Code skill

Install once:

```bash
git clone https://github.com/chenlinzhuo/course-merger.git
bash course-merger/skills/course-merger/scripts/install-locally.sh
```

Then in Claude Code:

> Build me a study site from these courses: `<playlist1>` `<playlist2>` `<playlist3>` using `examples/ontology-llm.yaml`.

Claude walks through the pipeline, asking for confirmation before each paid step (tag/cluster).

The full skill manifest is at [`skills/course-merger/SKILL.md`](skills/course-merger/SKILL.md).

## 🌐 In-session mode (Claude Max users — no API key)

If you have a Claude Max subscription, skip the Anthropic API key. Every LLM stage accepts two flags:

- `--print-prompts` — emits a JSON envelope of pending work to stdout.
- `--apply-results <file>` — reads a decisions JSON and writes results to the DB.

Inside Claude Code:

```
You: "Crawl this playlist and tag using examples/ontology-llm.yaml. I have Max."

Claude:
  - course-merger init && course-merger crawl <url>
  - course-merger tag --ontology ... --print-prompts --limit 20 > p.json
  - (reads p.json, decides tags via its own reasoning)
  - writes r.json with decisions
  - course-merger tag --ontology ... --apply-results r.json
  - (repeats batch by batch until all chunks tagged)
  - same loop for cluster, curriculum, synthesize, explain
  - course-merger build
```

The skill at [`skills/course-merger/SKILL.md`](skills/course-merger/SKILL.md) automates this loop.

### Trade-offs

|                          | API mode | In-session mode |
|--------------------------|----------|-----------------|
| API key required         | ✅ yes   | ❌ no           |
| Cost for demo corpus     | ~$2-4   | $0 extra (covered by Max) |
| Speed for 1000 chunks    | ~5-10 min | ~1-2 hours    |
| Speed for 100 chunks     | ~30 sec | ~5-10 min       |
| Best for                 | Large corpora | Small experiments |

## 📖 Textbook generation (v1.2+)

After `tag` + `cluster`, synthesize the corpus into a merged textbook:

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

## 💡 Concept encyclopedia (v1.3+)

Linear textbooks are great for first-time readers. The concept encyclopedia is for the reader looking up *one* idea in depth:

```bash
course-merger explain --concept linear-algebra --print-prompts > la.json
# Claude writes /tmp/la.html following the v2 style guide:
#   - per-concept CSS namespace prefix (la-)
#   - CSS-variable-only colors (works in light + dark + per-module accent)
#   - 9 fixed sections in order
#   - one of 3 interactive widget templates
course-merger explain --concept linear-algebra --apply-results la-results.json

course-merger build  # /concepts/<slug>/ now serves the rich explainer
```

The v2 style guide in [`src/course_merger/explain/prompts.py`](src/course_merger/explain/prompts.py) enforces:

- **Anti-bias opener** every entry must begin by naming a common misunderstanding and correcting it
- **One-invariant rule** every animation/interaction must make exactly ONE invariant visible
- **Equation-chain rule** every formula shows the substitution chain (no "可以推出 X")
- **Counter-example pitfalls** each of 3 misconceptions must include a specific numerical or visual counter-example
- **See-also constraint** all linked slugs must exist in `related_concepts` envelope

## 🎨 Site features

The built site (`course-merger build && course-merger serve`) ships with:

| Feature | What it does |
|---|---|
| 🌓 **Dark mode** | `html.dark` class + `prefers-color-scheme` fallback; toggle in header; `localStorage` persistence |
| 🎨 **Per-module accent** | Green / blue / purple / amber / rose, scoped via `data-module-idx`; cards, sidebars, drop caps all inherit |
| 📊 **Chapter mini-map** | Right rail tracks `h2`/`h3` headings with `IntersectionObserver`; click to scroll-anchor |
| ⌨️ **Keyboard nav** | `←` / `→` step through chapters; ignored in inputs; floating hint chip |
| 📱 **Mobile drawer** | Hamburger button <900 px opens slide-in panel; mirrors textbook sidebar; Escape/backdrop closes |
| 🔍 **Search** | Client-side via [Pagefind](https://pagefind.app/) |
| 🧮 **LaTeX math** | [KaTeX](https://katex.org/) auto-renders `$...$` inline / `$$...$$` block |
| 🎬 **Video deep links** | Every concept page lists source clips with timestamp-deep-linked iframes |

## 💵 Cost reality check

Per course (50-100 lectures, ~1500 chunks):

| Stage | Model | Cost |
|-------|-------|------|
| Crawl | n/a (yt-dlp) | $0 |
| Tag | Claude Haiku (prompt caching) | ~$0.10-0.30 |
| Cluster | Claude Sonnet | ~$0.20-0.50 |
| Curriculum | in-session Claude | $0 extra |
| Synthesize (per chapter) | in-session Claude | $0 extra |
| Explain (per concept) | in-session Claude | $0 extra |
| Build | n/a (Astro) | $0 |
| **Total per course** | | **~$0.30-0.80** |

For a 5-course corpus expect ~$2-4 first run. Re-runs are free thanks to per-chunk idempotency.

## 📐 Customize for your own corpus

The `examples/frontier-notebook/` directory is the recommended starting point:

```bash
cp -r examples/frontier-notebook examples/my-corpus
# Edit examples/my-corpus/courses.toml and examples/my-corpus/ontology.yaml
bash examples/my-corpus/build.sh
```

The build script chains crawl/tag/cluster/build, reads `courses.toml`, and lands a working site at `examples/my-corpus/.course-merger-project/site/dist/`.

## 🗺 Roadmap

**Shipped:** v1.0 foundation · v1.1 in-session mode · v1.2 textbook generator · v1.3 concept encyclopedia + design-system polish (see [CHANGELOG.md](CHANGELOG.md)).

**Deferred:**

- [ ] **Whisper fallback** transcribe videos with no subtitles via mlx-whisper / Groq
- [ ] **Coursera/edX/MIT-OCW adapters** more crawlers behind the `Crawler` Protocol
- [ ] **Live filter on compare view** client-side `?courses=cs336,gpu-mode` selection
- [ ] **`review` CLI** human-in-the-loop dispatch for `ambiguous` cluster decisions
- [ ] **Multi-language concept aliasing** dedicated Chinese ↔ English concept name pairs
- [ ] **Automatic incremental rebuild** `init_db()` on every CLI command, `ensure_site_dir` template sync on each `build`

## 🏛 Architecture & design

- Design spec: [`docs/specs/2026-05-09-course-merger-skill-design.md`](docs/specs/2026-05-09-course-merger-skill-design.md)
- Implementation plans (TDD-decomposed):
  - Plan 1: [Foundation + Crawl](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
  - Plan 2: [Tag + Cluster](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)
  - Plan 3: [Build + HTML](docs/superpowers/plans/2026-05-09-plan-3-build-and-html.md)
  - Plan 4: [Demo + Deploy + Skill](docs/superpowers/plans/2026-05-09-plan-4-demo-deploy-skill.md)
  - Plan 6: [Textbook generator](docs/superpowers/plans/2026-05-13-plan-6-textbook-generator.md)

## ⚖️ Disclaimer

`course-merger` is a **tool**. The user is responsible for ensuring they have the right to crawl, process, and redistribute any content fed through this pipeline. This includes YouTube/Bilibili Terms of Service governing programmatic content access, the original creator's license on the lecture content, and fair use / transformative use considerations in the user's jurisdiction.

The tool's authors disclaim responsibility for content generated by users. **Personal study use is generally low risk. Public redistribution or commercial use of synthesized content may not be.** Consult the source materials' licenses before going beyond personal use.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome — particularly new crawler adapters and ontology files for non-AI/CS domains.

## 📄 License

[MIT](LICENSE) — see file for details.

---

<div align="center">

Made with 🤖 + ☕ by [chenlinzhuo](https://github.com/chenlinzhuo).
Built atop [Claude Code](https://claude.com/claude-code), [Astro](https://astro.build/), [yt-dlp](https://github.com/yt-dlp/yt-dlp), [Pagefind](https://pagefind.app/), [KaTeX](https://katex.org/).

If `course-merger` saved you a weekend of YouTube binging, give it a ⭐ on GitHub.

</div>
