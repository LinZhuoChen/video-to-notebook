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

## In-session mode (Claude Max users — no API key)

If the user has Claude Max (or any Claude Code subscription), they should NOT need a separate Anthropic API key. The tag and cluster commands each support a two-step pattern: emit work to JSON, decide in this conversation, apply back.

### When to recommend this mode

After Step 2 (crawl), check chunk count:

```bash
sqlite3 .course-merger/db.sqlite "SELECT COUNT(*) FROM chunks"
```

| Chunk count | Mode |
|-------------|------|
| **< 200** | **In-session** (no API key, free via subscription) |
| 200–1000 | Either; in-session is slower but free |
| > 1000 | **API mode** — too slow to batch through conversation |

If the user explicitly says "I have Max" or "no API key", default to in-session regardless of size.

### In-session tag loop

```bash
course-merger tag --ontology <ont.yaml> --print-prompts --limit 20 > /tmp/cm-prompts.json
```

Read `/tmp/cm-prompts.json`:

```json
{
  "schema_version": "1",
  "kind": "tag_prompts",
  "ontology_slugs": ["self-attention", "..."],
  "chunks": [{"chunk_id": 1, "text": "..."}]
}
```

For each chunk, decide tags (your own reasoning) and write `/tmp/cm-results.json`:

```json
{
  "schema_version": "1",
  "kind": "tag_results",
  "tagger_model_id": "claude-code-max:v1",
  "results": [
    {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.9}]}
  ]
}
```

Apply:

```bash
course-merger tag --ontology <ont.yaml> --apply-results /tmp/cm-results.json
```

Repeat until `--print-prompts` returns empty `chunks` array.

### In-session cluster

```bash
course-merger cluster --ontology <ont.yaml> --print-prompts > /tmp/cm-cluster-prompts.json
```

Read the envelope. For each cluster, decide merge / create / reject / ambiguous.

Construct apply bundle (single file with BOTH envelopes):

```json
{
  "_prompts_envelope": { ... full /tmp/cm-cluster-prompts.json content ... },
  "decisions_envelope": {
    "schema_version": "1",
    "kind": "cluster_results",
    "reviewer_model_id": "claude-code-max:v1",
    "decisions": [
      {"cluster_id": 0, "decision": "merge", "target_slug": "rotary-positional-encoding"}
    ]
  }
}
```

Apply:

```bash
course-merger cluster --ontology <ont.yaml> --apply-results /tmp/cm-cluster-apply.json
```

## Textbook generation (v1.2+, Plan 6)

After tag + cluster complete, you can synthesize the corpus into a beginner-friendly textbook. This is the "pivot mode" — instead of indexing concepts, you produce a multi-chapter HTML reader for someone learning the topic from scratch.

### Step T1: Design the curriculum

```bash
course-merger curriculum --print-prompts > /tmp/cm-curr.json
```

Read `/tmp/cm-curr.json`. It contains every concept that has chunks + sample chunks per concept. Decide a beginner-pedagogical chapter order. Write `/tmp/cm-curr-results.json`:

```json
{
  "schema_version": "1",
  "kind": "curriculum_results",
  "designer": "claude-code-max:v1",
  "chapters": [
    {
      "order_idx": 1,
      "module": "Module 1: 数学直觉",
      "title": "什么是向量",
      "blurb": "数 ≠ 向量。向量是带方向的位移。",
      "primary_concept_slug": "linear-algebra",
      "related_concept_slugs": []
    }
  ]
}
```

Apply:

```bash
course-merger curriculum --apply-results /tmp/cm-curr-results.json
```

### Step T2: Synthesize each chapter (one at a time)

For each chapter N:

```bash
course-merger synthesize --chapter N --print-prompts > /tmp/cm-chN.json
```

Read the envelope: chapter spec + all source chunks for the chapter's primary + related concepts + style guide. Following the style guide:
- Anti-bias opening
- Inline SVG diagrams + CSS animations
- One embedded source clip with `?start=N` timestamp
- LaTeX math via `$...$` / `$$...$$`
- End with `<div class="takeaways">` (3 bullets)

Write the HTML fragment to `/tmp/cm-chN.html` (just `<article>...</article>` body content; no `<html><head><body>` wrapper).

Apply:

```bash
cat > /tmp/cm-apply.json <<EOF
{
  "schema_version": "1",
  "kind": "synthesize_results",
  "synthesizer": "claude-code-max:v1",
  "chapter_order_idx": N,
  "html_fragment_path": "/tmp/cm-chN.html"
}
EOF
course-merger synthesize --chapter N --apply-results /tmp/cm-apply.json
```

### Step T3: Build & view

```bash
course-merger build
course-merger serve     # http://localhost:4321/textbook/
```

The textbook lives at `/textbook/<order>/` with sidebar nav + prev/next. Re-run `synthesize` on any chapter to overwrite. Re-run `build` after each `synthesize` to refresh the site.

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
