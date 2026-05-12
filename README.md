# course-merger

Crawl open-courseware (YouTube / Bilibili), tag chunks with concept labels via Claude, cluster labels into a unified ontology across courses, and emit an interactive static HTML site for self-study.

> [!warning] Status: design phase (no implementation yet)
> The design lives in [`docs/specs/2026-05-09-course-merger-skill-design.md`](docs/specs/2026-05-09-course-merger-skill-design.md). Implementation plan is being drafted.

## What this does (when finished)

```bash
course-merger init
course-merger crawl <CS336 url>
course-merger crawl <GPU-MODE url>
course-merger crawl <bilibili url> --cookies-from edge
course-merger tag
course-merger cluster
course-merger build
```

→ static site under `site/dist/`, deployable to GitHub Pages. Every concept page lists where each course explains it; a "Compare across courses" view shows them side-by-side with timestamped video links.

## Roadmap

- **v1** (current design): YouTube + Bilibili, subtitle-only ingestion, concept-anchored merging, Astro static site.
- **v2** (deferred): Whisper fallback (mlx / openai / groq), Coursera/edX/MIT-OCW adapters, multi-language concept aliasing.

## Showcase

The `examples/frontier-notebook/` directory will host a curated World-Models × Agents corpus (5–8 courses) auto-deployed to GitHub Pages on every push to `main`.

## License

MIT
