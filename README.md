# course-merger

Crawl open-courseware (YouTube / Bilibili), tag chunks with concept labels via Claude, cluster labels into a unified ontology across courses, and emit an interactive static HTML site for self-study.

> [!warning] Status: under construction (Plan 2 of 4 — Foundation + Crawl + Tag + Cluster).
> The current build supports `init`, `crawl`, `tag`, `cluster`. HTML build lands in Plan 3.

## Quickstart

```bash
# 1. Install
git clone https://github.com/chenlinzhuo/course-merger.git
cd course-merger
uv venv && uv pip install -e ".[dev]"

# 2. Initialize a project
mkdir my-courses && cd my-courses
uv run course-merger init

# 3. Crawl one or more courses
uv run course-merger crawl \
    "https://www.youtube.com/playlist?list=PLxxx" --name cs336
uv run course-merger crawl \
    "https://www.bilibili.com/video/BVxxx/" --name "vizuara-llm" \
    --cookies-from edge

# 4. Tag chunks with concept labels (Claude Haiku, ~$0.10 per course)
export ANTHROPIC_API_KEY=sk-ant-...
uv run course-merger tag --ontology /path/to/ontology.yaml

# 5. Cluster proposed tags into the canonical ontology (Claude Sonnet, ~$0.30 per pass)
uv run course-merger cluster --ontology /path/to/ontology.yaml
```

After these steps, `.course-merger/db.sqlite` contains:
- Courses, lectures, chunks (Plan 1)
- Concepts, concept_aliases, chunk_concepts, build_meta, proposed_tags (Plan 2)

Inspect the resulting concept assignments:

```bash
sqlite3 .course-merger/db.sqlite \
    "SELECT canonical_name, COUNT(*) AS occurrences \
     FROM concepts c JOIN chunk_concepts cc ON c.id = cc.concept_id \
     GROUP BY c.id ORDER BY occurrences DESC LIMIT 10;"
```

A starter ontology lives at `examples/ontology-llm.yaml` (15 LLM concepts to seed the corpus).

## Roadmap

- **Plan 1:** Foundation + crawl. `init`, `crawl` for YouTube & Bilibili. ✅
- **Plan 2:** Tag + cluster. `tag`, `cluster`. Claude Haiku tagging + Sonnet cluster review. ✅
- **Plan 3 (next):** Build + HTML. `build`, `serve`. Astro static site with cross-course concept pages.
- **Plan 4:** Demo + deploy + Claude Code skill wrapper. `examples/frontier-notebook/` auto-deploys to GitHub Pages. `skills/course-merger/SKILL.md` lets Claude Code users trigger crawl/tag/build via natural language.

## Design

Full design spec: [`docs/specs/2026-05-09-course-merger-skill-design.md`](docs/specs/2026-05-09-course-merger-skill-design.md).

Implementation plans:
- Plan 1: [`docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md`](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
- Plan 2: [`docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md`](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)

## License

MIT
