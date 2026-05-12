---
name: course-merger
description: Use when the user wants to crawl open-courseware (YouTube/Bilibili playlists), tag content with concept labels via Claude, cluster them into a unified ontology across courses, and build an interactive static HTML site for self-study. Triggers include "build a study site from these courses", "merge these courses into one knowledge map", "crawl this playlist and make pages for each concept", "ingest these lectures and let me browse by concept", "做一个跨课程的学习站", "把这些课合并成一个", "爬这门课做知识地图". NOT for: tagging single transcripts (use the user's own scripts), summarizing one video (use video-course-notes), or general note-taking (use obsidian-brain).
---

# course-merger

A Python CLI that crawls open-courseware, tags it with Claude, and renders a cross-course concept-anchored static site. The skill walks the user through the 5-step pipeline.

## When to invoke this skill

The user wants to **merge multiple courses into one navigable site organized by concept**, NOT just transcribe or summarize one video.

Concrete triggers:
- "Crawl these 3 YouTube playlists and let me browse by concept"
- "Build a study site from CS336 + GPU-MODE + Vizuara"
- "我想把 X、Y、Z 三门课合并成一个网站，按概念组织"
- The user mentions both **crawl** + **multiple courses** + **concept** in one breath

NOT this skill if the request is:
- "Take notes on this one lecture" → use `video-course-notes`
- "Summarize this video" → user's own tools
- "Add this concept to my vault" → `obsidian-wiki`

## Prerequisites — check before starting

```bash
which course-merger 2>/dev/null || echo "MISSING"
node --version 2>/dev/null || echo "MISSING-NODE"
echo "ANTHROPIC_API_KEY: $([ -n "$ANTHROPIC_API_KEY" ] && echo SET || echo MISSING)"
```

If `course-merger` is MISSING: install with `pip install course-merger` or `uv tool install course-merger`.
If Node is MISSING: install Node 20+ (brew install node).
If ANTHROPIC_API_KEY is MISSING: stop and ask the user to set it — without it, tag/cluster fail.

## The 5-step pipeline

After confirming prerequisites, work through this with the user. Confirm each step before running the next; tag and cluster cost real money.

### Step 1: Initialize a project

```bash
cd <project-dir>     # ask the user where to set up the project
course-merger init
```

If the directory already has `.course-merger/`, ask whether to use it or `--force` re-init.

### Step 2: Crawl each course

For each course URL the user provides:

```bash
# YouTube
course-merger crawl "<url>" --name "<slug>"

# Bilibili (requires logged-in browser)
course-merger crawl "<url>" --name "<slug>" --cookies-from edge
```

Use `--name` to give a human-readable slug (e.g. `cs336`, `gpu-mode`). Without it the slug is derived from the URL's playlist/video ID, which is ugly.

Report counts after each crawl: `done: N ok, M no-subs, K errors`.

### Step 3: Tag with concept labels (costs ~$0.10/course)

The user MUST provide an ontology YAML. If they don't have one:
- For LLM/Transformer/GPU courses, point them at `examples/ontology-llm.yaml` in the repo.
- For other domains, ask them to draft 10-30 seed concepts in the YAML format (see `examples/ontology-llm.yaml` for shape).

```bash
course-merger tag --ontology <path-to-ontology.yaml> --limit 100
```

Use `--limit 100` for the first run to cost-cap the API spend. After they're happy with the tags, run without `--limit` to tag the rest.

### Step 4: Cluster proposed tags (costs ~$0.30/run)

```bash
course-merger cluster --ontology <path-to-ontology.yaml>
```

Reports merged/created/rejected/ambiguous counts. If many are ambiguous, the user may want to enlarge their seed ontology and re-run.

### Step 5: Build the static site

```bash
course-merger build           # produces site/dist/
course-merger serve           # local preview at http://localhost:4321
```

The user can browse and tell you what to tweak. Common follow-ups:
- "Tag more chunks": re-run step 3 with a higher `--limit`.
- "Re-render after editing ontology": `course-merger build --incremental` only re-renders concepts marked dirty by the last `cluster` run.
- "Deploy": see `examples/frontier-notebook/` for the GitHub Pages pattern.

## Quick recipes

### Run the whole pipeline at once (small corpus, you trust the defaults)

```bash
bash <skill-dir>/scripts/run-pipeline.sh <project-dir> <ontology.yaml> <url1> [<url2> ...]
```

### Cost estimation before running tag

```bash
# How many chunks need tagging?
sqlite3 .course-merger/db.sqlite "SELECT COUNT(*) FROM chunks WHERE NOT EXISTS (SELECT 1 FROM chunk_concepts WHERE chunk_concepts.chunk_id = chunks.id)"
```

At ~$0.0008/chunk (Claude Haiku with prompt caching), 1000 untagged chunks ≈ $0.80.

## Anti-patterns

- **Don't tag the same project twice without `--limit`** — the second run will skip tagged chunks but still iterate the whole DB. Use `--course <slug>` to scope.
- **Don't rebuild ontology mid-pipeline without thought** — if you change the seed YAML between `tag` and `cluster`, proposed tags may not cluster well.
- **Don't deploy a demo without a `.gitignore` that excludes `.course-merger/db.sqlite`** — the DB has raw transcripts which may be large or include problematic content.
