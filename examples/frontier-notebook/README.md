# Frontier Notebook — World Models × Agents

A curated `course-merger` demo project. Crawls 5 open courses, tags them with a 30-concept ontology, and produces an interactive knowledge map.

This directory is **shipped as a template**: copy it, edit `courses.toml` and `ontology.yaml` for your own corpus, then run `build.sh`.

## Quick start

```bash
# from the repo root
export ANTHROPIC_API_KEY=sk-ant-...
bash examples/frontier-notebook/build.sh
```

After ~30 min (depending on network + Claude latency), open `examples/frontier-notebook/.course-merger-project/site/dist/index.html` in a browser.

## Cost estimate

| Stage | Approximate cost |
|-------|-----------------|
| Crawl (5 courses) | $0 (yt-dlp subtitle fetch) |
| Tag (~1500 chunks × Haiku) | ~$1.20 |
| Cluster (~50 clusters × Sonnet) | ~$0.50 |
| Build (Astro + Pagefind) | $0 |
| **Total** | **~$1.70** |

## Customize for your corpus

1. Edit `courses.toml` — replace the 5 YouTube URLs with your own playlists. For Bilibili, set `platform = "bilibili"` and pass `--cookies-from edge` to `course-merger crawl`.
2. Edit `ontology.yaml` — add seed concepts that match your domain. ~30 concepts is a good starting point; the cluster pass will discover more.
3. Re-run `bash build.sh`.

## Deploy to GitHub Pages

This repo has `.github/workflows/pages.yml` configured to:
1. Cache the SQLite DB across runs (so `crawl` + `tag` don't re-run on every push)
2. Run `build.sh` if the cache is stale or the ontology changed
3. Push `site/dist/` to the `gh-pages` branch

Enable Pages in repo settings → set source to `gh-pages` branch. Demo will live at `<your-username>.github.io/<repo>/`.
