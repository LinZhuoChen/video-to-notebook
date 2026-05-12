# course-merger

Crawl open-courseware (YouTube / Bilibili), tag chunks with concept labels via Claude, cluster labels into a unified ontology across courses, and emit an interactive static HTML site for self-study.

> [!warning] Status: under construction (Plan 1 of 4 — Foundation + Crawl).
> The current build supports `init` and `crawl` only. Tag / cluster / build land in Plans 2-4.

## Quickstart

```bash
# 1. Install
git clone https://github.com/chenlinzhuo/course-merger.git
cd course-merger
uv venv && uv pip install -e ".[dev]"

# 2. Initialize a project
mkdir my-courses && cd my-courses
uv run course-merger init

# 3. Crawl a YouTube playlist
uv run course-merger crawl \
    "https://www.youtube.com/playlist?list=PLxxx" \
    --name cs336

# 4. Crawl a Bilibili playlist (requires logged-in browser)
uv run course-merger crawl \
    "https://www.bilibili.com/video/BVxxx/" \
    --name "vizuara-llm" \
    --cookies-from edge
```

After `crawl`, all transcripts and chunks live in `.course-merger/db.sqlite`. Inspect with:

```bash
sqlite3 .course-merger/db.sqlite "SELECT slug, title FROM courses;"
sqlite3 .course-merger/db.sqlite "SELECT COUNT(*) FROM chunks;"
```

## Roadmap

- **Plan 1 (current):** Foundation + crawl. `init`, `crawl` for YouTube & Bilibili. ✅
- **Plan 2 (next):** Tag + cluster. `tag`, `cluster`. Claude Haiku tagging + Sonnet cluster review.
- **Plan 3:** Build + HTML. `build`, `serve`. Astro static site with cross-course concept pages.
- **Plan 4:** Demo + deploy. `examples/frontier-notebook/` auto-deploys to GitHub Pages.

## Design

Full design spec: [`docs/specs/2026-05-09-course-merger-skill-design.md`](docs/specs/2026-05-09-course-merger-skill-design.md).

Plan 1 implementation plan: [`docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md`](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md).

## License

MIT
