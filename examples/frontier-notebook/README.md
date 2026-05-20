# Frontier Notebook — World Models × Agents

A curated `video-to-notebook` demo project. Crawls 5 open courses, tags them with a 30-concept ontology, and produces an interactive knowledge map.

This directory is **shipped as a template**: copy it, edit `courses.toml` and `ontology.yaml` for your own corpus, then drive the pipeline by either of two paths.

## Two paths

### Default — no API key, drive from an in-session agent

```bash
cd examples/frontier-notebook
bash bootstrap.sh                          # init + crawl only (no LLM)
# then, inside Claude Code or Codex, follow RUNBOOK.md step by step
```

`bootstrap.sh` populates the SQLite DB with subtitles. `RUNBOOK.md` walks the agent through tag → cluster → curriculum → synthesize → explain → build, one stage at a time. The CLI writes a prompt envelope to `.video-to-notebook/prompts/<step>.json` and the agent writes the matching `.decisions.json`.

### Shortcut — you have an API key, want one command

```bash
export ANTHROPIC_API_KEY=sk-ant-...
bash build.sh                              # also: --language en, --bilingual
```

`build.sh` runs the full pipeline with `--use-api` on `tag` and `cluster` so Claude is called directly. `curriculum`, `synthesize`, and `explain` are in-session only and are **not** driven by `build.sh` — those still require an agent.

## Cost estimate

| Stage | Approximate cost |
|-------|-----------------|
| Crawl (5 courses) | $0 (yt-dlp subtitle fetch) |
| Tag (~1500 chunks × Haiku) | ~$1.20 |
| Cluster (~50 clusters × Sonnet) | ~$0.50 |
| Build (Astro + Pagefind) | $0 |
| **Total (tag + cluster only)** | **~$1.70** |

Costs for synthesize / explain depend entirely on how much textbook content you generate. A 30-chapter / 80-concept site is typically $10-25 if driven via Claude API; $0 if driven by Claude Max / Codex inside a session.

## Customize for your corpus

1. Edit `courses.toml` — replace the 5 entries with your own playlists. For Bilibili, set `platform = "bilibili"` and `cookies_from = "edge"` (or `chrome` / `firefox` / `safari`).
2. Edit `ontology.yaml` — add seed concepts that match your domain. ~30 concepts is a good starting point; the cluster pass will discover more.
3. Re-run `bash bootstrap.sh` (or `bash build.sh`).

## Deploy to GitHub Pages

This repo has `.github/workflows/pages.yml` configured to:
1. Cache the SQLite DB across runs (so `crawl` + `tag` don't re-run on every push)
2. Run `build.sh` if the cache is stale or the ontology changed
3. Push `site/dist/` to the `gh-pages` branch

Enable Pages in repo settings → set source to `gh-pages` branch. Demo will live at `<your-username>.github.io/<repo>/`.
