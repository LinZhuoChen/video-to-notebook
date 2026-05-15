# Plan 4 — Demo + Deploy + SKILL.md Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `video-to-notebook` v1.0 — wrap the CLI as a Claude Code skill plugin so users can drive the pipeline via natural language; ship an `examples/frontier-notebook/` demo config with a one-click pipeline runner; auto-deploy the demo to GitHub Pages on every push to `main`; rewrite the README as a complete v1 walkthrough.

**Architecture:** A `skills/video-to-notebook/SKILL.md` file declares the Claude Code skill with trigger keywords and step-by-step instructions for Claude to execute. `examples/frontier-notebook/` ships a `courses.toml` config + `build.sh` that chains the 5 CLI commands; the GitHub Pages workflow runs this script on a cache miss and uploads `site/dist/` to the gh-pages branch.

**Tech Stack:** Bash (one-click script + skill wrappers) + TOML (course config) + GitHub Actions (pages deploy) + Markdown (skill + docs). No new Python or JS dependencies.

**Repo:** `/Users/chenlinzhuo/code/video-to-notebook/` (at tag `plan-3-done`, commit `3c11400`).

---

## File Structure

```
video-to-notebook/
├── README.md                                       # MODIFY: full v1 walkthrough
├── skills/                                         # NEW directory
│   └── video-to-notebook/
│       ├── SKILL.md                                # NEW: Claude Code skill plugin
│       └── scripts/
│           ├── run-pipeline.sh                     # NEW: chained crawl→tag→cluster→build
│           └── install-locally.sh                  # NEW: copy skill to ~/.claude/skills/
├── examples/
│   ├── ontology-llm.yaml                           # EXISTS from Plan 2
│   └── frontier-notebook/                          # NEW: showcase config
│       ├── README.md                               # NEW
│       ├── ontology.yaml                           # NEW (World Models × Agents specialized)
│       ├── courses.toml                            # NEW (curated course list)
│       └── build.sh                                # NEW (one-click pipeline)
├── .github/workflows/
│   └── pages.yml                                   # NEW: gh-pages deploy on push to main
└── template-site/
    └── astro.config.mjs                            # MODIFY: support `--site` override for gh-pages base
```

Boundary discipline:
- `skills/video-to-notebook/SKILL.md`: Claude Code skill manifest (markdown + YAML frontmatter).
- `skills/video-to-notebook/scripts/`: lean bash scripts the skill invokes via Claude's Bash tool.
- `examples/frontier-notebook/`: a complete worked example a new user can copy and customize.
- `.github/workflows/pages.yml`: separate from `ci.yml` (CI runs on every PR; pages only on push to main).

---

## Phase 0: Skill Plugin

### Task 1: Write `skills/video-to-notebook/SKILL.md`

**Files:**
- Create: `skills/video-to-notebook/SKILL.md`

The skill manifest. Tells Claude Code when to invoke (trigger phrases), what arguments to expect, and the step-by-step CLI workflow.

- [ ] **Step 1: Create the directory + file**

```bash
mkdir -p /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/scripts
```

- [ ] **Step 2: Write `skills/video-to-notebook/SKILL.md`**

```markdown
---
name: video-to-notebook
description: Use when the user wants to crawl open-courseware (YouTube/Bilibili playlists), tag content with concept labels via Claude, cluster them into a unified ontology across courses, and build an interactive static HTML site for self-study. Triggers include "build a study site from these courses", "merge these courses into one knowledge map", "crawl this playlist and make pages for each concept", "ingest these lectures and let me browse by concept", "做一个跨课程的学习站", "把这些课合并成一个", "爬这门课做知识地图". NOT for: tagging single transcripts (use the user's own scripts), summarizing one video (use video-course-notes), or general note-taking (use obsidian-brain).
---

# video-to-notebook

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
which video-to-notebook 2>/dev/null || echo "MISSING"
node --version 2>/dev/null || echo "MISSING-NODE"
echo "ANTHROPIC_API_KEY: $([ -n "$ANTHROPIC_API_KEY" ] && echo SET || echo MISSING)"
```

If `video-to-notebook` is MISSING: install with `pip install video-to-notebook` or `uv tool install video-to-notebook`.
If Node is MISSING: install Node 20+ (brew install node).
If ANTHROPIC_API_KEY is MISSING: stop and ask the user to set it — without it, tag/cluster fail.

## The 5-step pipeline

After confirming prerequisites, work through this with the user. Confirm each step before running the next; tag and cluster cost real money.

### Step 1: Initialize a project

```bash
cd <project-dir>     # ask the user where to set up the project
video-to-notebook init
```

If the directory already has `.video-to-notebook/`, ask whether to use it or `--force` re-init.

### Step 2: Crawl each course

For each course URL the user provides:

```bash
# YouTube
video-to-notebook crawl "<url>" --name "<slug>"

# Bilibili (requires logged-in browser)
video-to-notebook crawl "<url>" --name "<slug>" --cookies-from edge
```

Use `--name` to give a human-readable slug (e.g. `cs336`, `gpu-mode`). Without it the slug is derived from the URL's playlist/video ID, which is ugly.

Report counts after each crawl: `done: N ok, M no-subs, K errors`.

### Step 3: Tag with concept labels (costs ~$0.10/course)

The user MUST provide an ontology YAML. If they don't have one:
- For LLM/Transformer/GPU courses, point them at `examples/ontology-llm.yaml` in the repo.
- For other domains, ask them to draft 10-30 seed concepts in the YAML format (see `examples/ontology-llm.yaml` for shape).

```bash
video-to-notebook tag --ontology <path-to-ontology.yaml> --limit 100
```

Use `--limit 100` for the first run to cost-cap the API spend. After they're happy with the tags, run without `--limit` to tag the rest.

### Step 4: Cluster proposed tags (costs ~$0.30/run)

```bash
video-to-notebook cluster --ontology <path-to-ontology.yaml>
```

Reports merged/created/rejected/ambiguous counts. If many are ambiguous, the user may want to enlarge their seed ontology and re-run.

### Step 5: Build the static site

```bash
video-to-notebook build           # produces site/dist/
video-to-notebook serve           # local preview at http://localhost:4321
```

The user can browse and tell you what to tweak. Common follow-ups:
- "Tag more chunks": re-run step 3 with a higher `--limit`.
- "Re-render after editing ontology": `video-to-notebook build --incremental` only re-renders concepts marked dirty by the last `cluster` run.
- "Deploy": see `examples/frontier-notebook/` for the GitHub Pages pattern.

## Quick recipes

### Run the whole pipeline at once (small corpus, you trust the defaults)

```bash
bash <skill-dir>/scripts/run-pipeline.sh <project-dir> <ontology.yaml> <url1> [<url2> ...]
```

### Cost estimation before running tag

```bash
# How many chunks need tagging?
sqlite3 .video-to-notebook/db.sqlite "SELECT COUNT(*) FROM chunks WHERE NOT EXISTS (SELECT 1 FROM chunk_concepts WHERE chunk_concepts.chunk_id = chunks.id)"
```

At ~$0.0008/chunk (Claude Haiku with prompt caching), 1000 untagged chunks ≈ $0.80.

## Anti-patterns

- **Don't tag the same project twice without `--limit`** — the second run will skip tagged chunks but still iterate the whole DB. Use `--course <slug>` to scope.
- **Don't rebuild ontology mid-pipeline without thought** — if you change the seed YAML between `tag` and `cluster`, proposed tags may not cluster well.
- **Don't deploy a demo without a `.gitignore` that excludes `.video-to-notebook/db.sqlite`** — the DB has raw transcripts which may be large or include problematic content.
```

- [ ] **Step 3: Verify file**

```bash
ls -la /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/SKILL.md
head -3 /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/SKILL.md
```

Expected: file exists, starts with `---` (YAML frontmatter delimiter).

- [ ] **Step 4: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add skills/video-to-notebook/SKILL.md
git commit -m "feat(skill): Claude Code skill plugin manifest for video-to-notebook"
```

---

### Task 2: Pipeline runner script

**Files:**
- Create: `skills/video-to-notebook/scripts/run-pipeline.sh`

A one-shot wrapper Claude can suggest for users who want to chain the full pipeline.

- [ ] **Step 1: Write `skills/video-to-notebook/scripts/run-pipeline.sh`**

```bash
#!/usr/bin/env bash
# run-pipeline.sh — chain crawl/tag/cluster/build for a fresh corpus
#
# Usage:
#   bash run-pipeline.sh <project-dir> <ontology.yaml> <course-url> [<course-url> ...]
#
# Each course URL gets crawled into a slug derived from its playlist/video ID.
# Requires: video-to-notebook installed, ANTHROPIC_API_KEY set, Node 20+ for build.

set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "usage: $0 <project-dir> <ontology.yaml> <course-url> [<course-url> ...]" >&2
  exit 1
fi

PROJECT_DIR="$1"
ONTOLOGY="$2"
shift 2

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "error: ANTHROPIC_API_KEY is not set" >&2
  exit 2
fi

if [ ! -f "$ONTOLOGY" ]; then
  echo "error: ontology file not found at $ONTOLOGY" >&2
  exit 3
fi

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

if [ ! -d ".video-to-notebook" ]; then
  echo ">>> video-to-notebook init"
  video-to-notebook init
else
  echo ">>> reusing existing .video-to-notebook/"
fi

for url in "$@"; do
  echo ">>> video-to-notebook crawl $url"
  video-to-notebook crawl "$url"
done

echo ">>> video-to-notebook tag --ontology $ONTOLOGY"
video-to-notebook tag --ontology "$ONTOLOGY"

echo ">>> video-to-notebook cluster --ontology $ONTOLOGY"
video-to-notebook cluster --ontology "$ONTOLOGY"

echo ">>> video-to-notebook build"
video-to-notebook build

echo ""
echo "DONE. Open site/dist/index.html or run 'video-to-notebook serve'."
```

- [ ] **Step 2: Make executable + verify**

```bash
chmod +x /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/scripts/run-pipeline.sh
bash -n /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/scripts/run-pipeline.sh
```

`bash -n` is syntax-only check; should exit 0 with no output.

- [ ] **Step 3: Smoke test the usage error path**

```bash
bash /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/scripts/run-pipeline.sh 2>&1
```

Expected: prints usage line, exits 1.

- [ ] **Step 4: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add skills/video-to-notebook/scripts/run-pipeline.sh
git commit -m "feat(skill): one-click pipeline runner script"
```

---

### Task 3: Local install script

**Files:**
- Create: `skills/video-to-notebook/scripts/install-locally.sh`

A small helper that symlinks (or copies) the skill into `~/.claude/skills/` so it's pickable by Claude Code without publishing to a marketplace.

- [ ] **Step 1: Write the script**

```bash
#!/usr/bin/env bash
# install-locally.sh — symlink the video-to-notebook skill into ~/.claude/skills/
#
# After running this, Claude Code will discover the skill on next session start.
# Use this before there's a public marketplace listing.

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_PARENT="$HOME/.claude/skills"
TARGET="$TARGET_PARENT/video-to-notebook"

mkdir -p "$TARGET_PARENT"

if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
  echo ">>> Existing skill at $TARGET — replacing"
  rm -rf "$TARGET"
fi

ln -s "$SKILL_DIR" "$TARGET"
echo "installed: $TARGET → $SKILL_DIR"
echo ""
echo "Restart Claude Code (or wait for next session start) to pick up the skill."
echo "Verify with: ls -la $TARGET"
```

- [ ] **Step 2: Make executable + smoke test**

```bash
chmod +x /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/scripts/install-locally.sh
bash -n /Users/chenlinzhuo/code/video-to-notebook/skills/video-to-notebook/scripts/install-locally.sh
```

- [ ] **Step 3: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add skills/video-to-notebook/scripts/install-locally.sh
git commit -m "feat(skill): install-locally.sh symlinks skill into ~/.claude/skills/"
```

---

## Phase 1: Demo Config (`examples/frontier-notebook/`)

### Task 4: Frontier Notebook ontology + courses config

**Files:**
- Create: `examples/frontier-notebook/README.md`
- Create: `examples/frontier-notebook/ontology.yaml`
- Create: `examples/frontier-notebook/courses.toml`

A curated example for the author's "World Models × Agents" knowledge product. Other users copy this dir as a starting point and edit.

- [ ] **Step 1: Write `examples/frontier-notebook/courses.toml`**

```toml
# Frontier Notebook — curated open-courseware corpus
#
# Each [[course]] entry maps to one `video-to-notebook crawl` invocation.
# Slug becomes the URL path on the site (e.g. /courses/cs336/).

[[course]]
slug = "cs336"
url = "https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_"
platform = "youtube"
# Stanford CS336 — Language Modeling from Scratch

[[course]]
slug = "gpu-mode"
url = "https://www.youtube.com/playlist?list=PLVEjdmwEDkgcjr6esfQEcJzhRSi-NgyOh"
platform = "youtube"
# GPU MODE — community lectures on CUDA / GPU programming

[[course]]
slug = "principles-of-diffusion"
url = "https://www.youtube.com/playlist?list=PLB6OKWxCQTM6vOTKxqaO9Bks-WD8q3xMy"
platform = "youtube"
# Stanford / MIT Principles of Diffusion Models

[[course]]
slug = "vizuara-build-claude-code"
url = "https://www.youtube.com/playlist?list=PLPTV0NXA_ZShnka8uVzF3mSvZdilfiGWG"
platform = "youtube"
# Vizuara — Build Claude Code from Scratch

[[course]]
slug = "vizuara-build-deepseek"
url = "https://www.youtube.com/playlist?list=PLPTV0NXA_ZSiOpKKlHA8AntpYR-zaBlSF"
platform = "youtube"
# Vizuara — Build DeepSeek from Scratch

# To add more: append [[course]] blocks. Bilibili courses set
# platform = "bilibili" and require --cookies-from at run-time.
```

> URLs above are real public YouTube playlists from the author's vault. The build.sh script reads this file and loops crawl over each entry.

- [ ] **Step 2: Write `examples/frontier-notebook/ontology.yaml`**

```yaml
# Frontier Notebook — World Models × Agents ontology
#
# 30 seed concepts covering the editorial scope of frontiernotebook.dev.
# Tune for your own corpus by adding / renaming entries.

concepts:
  # === Foundations ===
  - slug: tokenization
    canonical_name: Tokenization
    description: Splitting text into subword tokens (BPE, SentencePiece).
    aliases: [BPE, byte-pair encoding, tokenizer]

  - slug: embedding
    canonical_name: Embedding
    description: Mapping tokens or features to dense vectors.
    aliases: [token embedding, word embedding]

  - slug: positional-encoding
    canonical_name: Positional Encoding
    description: Injecting position information into otherwise permutation-invariant attention.
    aliases: [position embedding]

  # === Attention family ===
  - slug: attention
    canonical_name: Attention
    description: Weighted aggregation over context.
    aliases: [attention mechanism]

  - slug: self-attention
    canonical_name: Self-Attention
    description: Attention applied within a single sequence (Q, K, V from the same input).
    aliases: [SA, scaled dot-product attention]

  - slug: multi-head-attention
    canonical_name: Multi-Head Attention
    description: Multiple attention heads in parallel.
    aliases: [MHA]

  - slug: cross-attention
    canonical_name: Cross-Attention
    description: Q from one sequence, K/V from another.

  - slug: rotary-positional-encoding
    canonical_name: Rotary Positional Encoding
    description: RoPE — rotates Q/K projections by position.
    aliases: [RoPE, rotary embedding]

  - slug: flash-attention
    canonical_name: Flash Attention
    description: IO-aware attention algorithm in a single fused CUDA kernel.
    aliases: [FlashAttn]

  # === Transformer architecture ===
  - slug: transformer-block
    canonical_name: Transformer Block
    description: One attention + MLP layer with residuals and norm.

  - slug: mlp
    canonical_name: MLP / Feed-Forward Network
    description: Two-layer FFN applied position-wise.
    aliases: [FFN, feed-forward]

  - slug: layer-norm
    canonical_name: Layer Normalization
    aliases: [LayerNorm, LN]

  - slug: rms-norm
    canonical_name: RMS Normalization
    aliases: [RMSNorm]

  # === Inference ===
  - slug: kv-cache
    canonical_name: KV Cache
    description: Reusing previously computed keys and values during autoregressive decoding.

  - slug: speculative-decoding
    canonical_name: Speculative Decoding
    aliases: [spec decoding]

  - slug: prompt-caching
    canonical_name: Prompt Caching
    description: Reuse pre-computed KV for shared prompt prefixes to cut cost.

  - slug: pagedattention
    canonical_name: PagedAttention
    description: vLLM's block-paged KV cache memory management.

  # === Training ===
  - slug: pretraining
    canonical_name: Pretraining
    description: Self-supervised next-token training on large unlabeled corpora.

  - slug: fine-tuning
    canonical_name: Fine-Tuning
    aliases: [SFT, supervised fine-tuning]

  - slug: rlhf
    canonical_name: RLHF
    description: Reinforcement Learning from Human Feedback.

  - slug: dpo
    canonical_name: Direct Preference Optimization
    aliases: [DPO]

  # === Diffusion / generative ===
  - slug: diffusion-model
    canonical_name: Diffusion Model
    description: Iterative denoising generative model.

  - slug: flow-matching
    canonical_name: Flow Matching
    description: Training continuous normalizing flows by regressing on a target vector field.

  - slug: classifier-free-guidance
    canonical_name: Classifier-Free Guidance
    aliases: [CFG]

  # === World models / agents ===
  - slug: world-model
    canonical_name: World Model
    description: A learned predictive model of an environment, used for planning / imagination.

  - slug: agent
    canonical_name: Agent
    description: A system that perceives, plans, and acts in an environment.
    aliases: [LLM agent]

  - slug: tool-use
    canonical_name: Tool Use
    description: LLMs invoking external functions via JSON output.
    aliases: [function calling]

  - slug: context-engineering
    canonical_name: Context Engineering
    description: Designing what goes into the LLM's context window.

  # === GPU / systems ===
  - slug: gpu-memory-hierarchy
    canonical_name: GPU Memory Hierarchy
    description: Registers, shared memory, L1/L2, HBM.

  - slug: tensor-parallelism
    canonical_name: Tensor Parallelism
    description: Splitting individual operators across GPUs.

  - slug: pipeline-parallelism
    canonical_name: Pipeline Parallelism
    description: Splitting model layers across stages.
```

- [ ] **Step 3: Write `examples/frontier-notebook/README.md`**

```markdown
# Frontier Notebook — World Models × Agents

A curated `video-to-notebook` demo project. Crawls 5 open courses, tags them with a 30-concept ontology, and produces an interactive knowledge map.

This directory is **shipped as a template**: copy it, edit `courses.toml` and `ontology.yaml` for your own corpus, then run `build.sh`.

## Quick start

```bash
# from the repo root
export ANTHROPIC_API_KEY=sk-ant-...
bash examples/frontier-notebook/build.sh
```

After ~30 min (depending on network + Claude latency), open `examples/frontier-notebook/.video-to-notebook-project/site/dist/index.html` in a browser.

## Cost estimate

| Stage | Approximate cost |
|-------|-----------------|
| Crawl (5 courses) | $0 (yt-dlp subtitle fetch) |
| Tag (~1500 chunks × Haiku) | ~$1.20 |
| Cluster (~50 clusters × Sonnet) | ~$0.50 |
| Build (Astro + Pagefind) | $0 |
| **Total** | **~$1.70** |

## Customize for your corpus

1. Edit `courses.toml` — replace the 5 YouTube URLs with your own playlists. For Bilibili, set `platform = "bilibili"` and pass `--cookies-from edge` to `video-to-notebook crawl`.
2. Edit `ontology.yaml` — add seed concepts that match your domain. ~30 concepts is a good starting point; the cluster pass will discover more.
3. Re-run `bash build.sh`.

## Deploy to GitHub Pages

This repo has `.github/workflows/pages.yml` configured to:
1. Cache the SQLite DB across runs (so `crawl` + `tag` don't re-run on every push)
2. Run `build.sh` if the cache is stale or the ontology changed
3. Push `site/dist/` to the `gh-pages` branch

Enable Pages in repo settings → set source to `gh-pages` branch. Demo will live at `<your-username>.github.io/<repo>/`.
```

- [ ] **Step 4: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add examples/frontier-notebook/
git commit -m "feat(examples): frontier-notebook demo config (ontology + courses.toml + README)"
```

---

### Task 5: Demo build script

**Files:**
- Create: `examples/frontier-notebook/build.sh`

The one-click pipeline runner for this specific demo. Reads `courses.toml`, runs the full pipeline, lands a built site under `.video-to-notebook-project/site/dist/`.

- [ ] **Step 1: Write `examples/frontier-notebook/build.sh`**

```bash
#!/usr/bin/env bash
# build.sh — run the full video-to-notebook pipeline for the Frontier Notebook demo
#
# Reads courses.toml in this directory, crawls every entry, tags & clusters
# using ontology.yaml, builds the static site.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$HERE/.video-to-notebook-project"
ONTOLOGY="$HERE/ontology.yaml"
COURSES="$HERE/courses.toml"

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "error: ANTHROPIC_API_KEY is not set" >&2
  exit 1
fi

if ! command -v video-to-notebook >/dev/null 2>&1; then
  echo "error: video-to-notebook not on PATH. Install with: pip install video-to-notebook" >&2
  exit 2
fi

if ! command -v node >/dev/null 2>&1; then
  echo "error: node not on PATH. Need Node 20+." >&2
  exit 3
fi

mkdir -p "$PROJECT"
cd "$PROJECT"

if [ ! -d ".video-to-notebook" ]; then
  video-to-notebook init
fi

# Parse courses.toml — extract slug + url pairs.
# We use a small inline Python here rather than a TOML CLI to avoid extra deps.
python3 <<PY > /tmp/cm-courses.txt
import sys, tomllib
with open("$COURSES", "rb") as f:
    data = tomllib.load(f)
for c in data.get("course", []):
    slug = c["slug"]
    url = c["url"]
    platform = c.get("platform", "youtube")
    cookies = c.get("cookies_from", "")
    print(f"{slug}|{url}|{platform}|{cookies}")
PY

while IFS='|' read -r SLUG URL PLATFORM COOKIES; do
  echo ""
  echo "=== crawl: $SLUG ($PLATFORM) ==="
  EXTRA=""
  if [ -n "$COOKIES" ]; then
    EXTRA="--cookies-from $COOKIES"
  fi
  video-to-notebook crawl "$URL" --name "$SLUG" $EXTRA
done < /tmp/cm-courses.txt

echo ""
echo "=== tag ==="
video-to-notebook tag --ontology "$ONTOLOGY"

echo ""
echo "=== cluster ==="
video-to-notebook cluster --ontology "$ONTOLOGY"

echo ""
echo "=== build ==="
video-to-notebook build

echo ""
echo "DONE. Open: file://$PROJECT/site/dist/index.html"
echo "       Or: cd '$PROJECT' && video-to-notebook serve"
```

- [ ] **Step 2: Make executable + syntax-check**

```bash
chmod +x /Users/chenlinzhuo/code/video-to-notebook/examples/frontier-notebook/build.sh
bash -n /Users/chenlinzhuo/code/video-to-notebook/examples/frontier-notebook/build.sh
```

- [ ] **Step 3: Smoke-test missing-API-key path**

```bash
( unset ANTHROPIC_API_KEY && bash /Users/chenlinzhuo/code/video-to-notebook/examples/frontier-notebook/build.sh 2>&1 ) | head
```

Expected: `error: ANTHROPIC_API_KEY is not set` + exit code 1.

- [ ] **Step 4: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add examples/frontier-notebook/build.sh
git commit -m "feat(examples): build.sh for one-click Frontier Notebook pipeline"
```

---

## Phase 2: GitHub Pages Auto-Deploy

### Task 6: Astro base path config

**Files:**
- Modify: `template-site/astro.config.mjs`

GitHub Pages serves at `https://<user>.github.io/<repo>/`. Astro needs `site` + `base` config to generate correct asset URLs at build time.

- [ ] **Step 1: Modify `template-site/astro.config.mjs`**

Replace the entire file content:

```js
import { defineConfig } from 'astro/config';

// `SITE_URL` and `BASE_PATH` can be set at build time (e.g. by the GitHub Pages
// workflow). Defaults are sensible for local dev.
const siteUrl = process.env.SITE_URL || 'http://localhost:4321';
const basePath = process.env.BASE_PATH || '/';

export default defineConfig({
  site: siteUrl,
  base: basePath,
  output: 'static',
  build: {
    format: 'directory',
  },
  vite: {
    build: { sourcemap: false },
  },
});
```

- [ ] **Step 2: Verify local dev still builds with defaults**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook/template-site
npm run build 2>&1 | tail -5
```

Expected: build succeeds (the empty content collections produce 4 static pages: index, about, courses index, concepts index).

- [ ] **Step 3: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add template-site/astro.config.mjs
git commit -m "feat(site): SITE_URL + BASE_PATH env vars for GitHub Pages deployment"
```

---

### Task 7: GitHub Pages workflow

**Files:**
- Create: `.github/workflows/pages.yml`

Triggers on push to `main` AND on manual `workflow_dispatch`. Caches the SQLite DB across runs (key includes the courses.toml + ontology.yaml hashes) so unchanged inputs skip crawl/tag/cluster.

- [ ] **Step 1: Write `.github/workflows/pages.yml`**

```yaml
name: Deploy demo to GitHub Pages

on:
  push:
    branches: [main]
    paths:
      - 'examples/frontier-notebook/**'
      - 'template-site/**'
      - 'src/video_to_notebook/**'
      - '.github/workflows/pages.yml'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages-deploy
  cancel-in-progress: false

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"

      - name: Set up Python
        run: uv python install 3.12

      - name: Install video-to-notebook
        run: uv pip install --system -e ".[dev]"

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Restore corpus cache
        id: cache-corpus
        uses: actions/cache@v4
        with:
          path: examples/frontier-notebook/.video-to-notebook-project/.video-to-notebook
          key: corpus-${{ hashFiles('examples/frontier-notebook/courses.toml', 'examples/frontier-notebook/ontology.yaml') }}-v1

      - name: Build the demo
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SITE_URL: https://${{ github.repository_owner }}.github.io
          BASE_PATH: /${{ github.event.repository.name }}/
        run: bash examples/frontier-notebook/build.sh

      - name: Upload pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: examples/frontier-notebook/.video-to-notebook-project/site/dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

> The cache key changes when courses.toml or ontology.yaml change; otherwise the SQLite DB is restored and crawl/tag/cluster all become no-ops (idempotent). Only `video-to-notebook build` runs.

- [ ] **Step 2: Verify YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('/Users/chenlinzhuo/code/video-to-notebook/.github/workflows/pages.yml'))"
```

Expected: no output (no errors).

- [ ] **Step 3: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add .github/workflows/pages.yml
git commit -m "ci(pages): auto-deploy demo to GitHub Pages on push to main"
```

> **Note:** for the workflow to actually deploy, the repo owner needs to (a) enable Pages in repo settings with source = "GitHub Actions"; (b) add `ANTHROPIC_API_KEY` as a repo secret. Both are one-time manual steps in the GitHub UI.

---

## Phase 3: README Rewrite

### Task 8: Full v1 README

**Files:**
- Modify: `README.md`

Replace with a complete walkthrough now that the v1 surface is shipped.

- [ ] **Step 1: Replace `README.md` entirely**

```markdown
# video-to-notebook

> Crawl open-courseware, tag chunks with concept labels via Claude, and render an interactive cross-course concept-anchored static site for self-study.

[![CI](https://github.com/chenlinzhuo/video-to-notebook/actions/workflows/ci.yml/badge.svg)](https://github.com/chenlinzhuo/video-to-notebook/actions/workflows/ci.yml)

The killer feature: a **"Compare across courses"** view. Pick any concept (e.g. *Self-Attention*), see how Stanford CS336, GPU MODE, and Vizuara each teach it — side by side, with click-to-seek timestamped video.

## Demo

Live demo: [chenlinzhuo.github.io/video-to-notebook/](https://chenlinzhuo.github.io/video-to-notebook/) — built from the 5 World-Models × Agents courses in `examples/frontier-notebook/`.

## Install

```bash
# 1. Python CLI (3.12+)
pip install video-to-notebook
# or: uv tool install video-to-notebook

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
video-to-notebook init

# 2. Crawl one or more courses
video-to-notebook crawl "https://www.youtube.com/playlist?list=PLxxx" --name cs336
video-to-notebook crawl "https://www.bilibili.com/video/BVxxx/" --name "vizuara-llm" --cookies-from edge

# 3. Tag chunks with concept labels (Claude Haiku, ~$0.10/course)
video-to-notebook tag --ontology examples/ontology-llm.yaml --limit 200

# 4. Cluster proposed tags (Claude Sonnet, ~$0.30/run)
video-to-notebook cluster --ontology examples/ontology-llm.yaml

# 5. Build the static site
video-to-notebook build

# Preview locally at http://localhost:4321
video-to-notebook serve
```

After step 5, `site/dist/` is a complete static site you can serve from any HTTP server or deploy to GitHub Pages.

## How it works

```
                 ┌──────────────────────────────────────┐
                 │           SQLite (.video-to-notebook/db) │
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
git clone https://github.com/chenlinzhuo/video-to-notebook.git
bash video-to-notebook/skills/video-to-notebook/scripts/install-locally.sh
```

Then in Claude Code:

> Build me a study site from these courses: <playlist1> <playlist2> <playlist3> using examples/ontology-llm.yaml

Claude will walk through the 5 steps with you, asking for confirmation before tag/cluster (which cost money).

The full skill manifest is at `skills/video-to-notebook/SKILL.md`.

## Customize for your own corpus

The `examples/frontier-notebook/` directory is the recommended starting point:

```bash
cp -r examples/frontier-notebook examples/my-corpus
# Edit examples/my-corpus/courses.toml and examples/my-corpus/ontology.yaml
bash examples/my-corpus/build.sh
```

The build script chains crawl/tag/cluster/build, reads `courses.toml`, and lands a working site at `examples/my-corpus/.video-to-notebook-project/site/dist/`.

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

- Design spec: [`docs/specs/2026-05-09-video-to-notebook-skill-design.md`](docs/specs/2026-05-09-video-to-notebook-skill-design.md)
- Implementation plans (TDD-decomposed):
  - Plan 1: [Foundation + Crawl](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
  - Plan 2: [Tag + Cluster](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)
  - Plan 3: [Build + HTML](docs/superpowers/plans/2026-05-09-plan-3-build-and-html.md)
  - Plan 4: [Demo + Deploy + Skill](docs/superpowers/plans/2026-05-09-plan-4-demo-deploy-skill.md)

## Contributing

PRs welcome — particularly new crawler adapters and ontology files for non-AI/CS domains. Run `pytest -v` before sending.

## License

MIT
```

- [ ] **Step 2: Verify file is well-formed Markdown**

```bash
head -20 /Users/chenlinzhuo/code/video-to-notebook/README.md
```

Expected: starts with `# video-to-notebook`, contains the link to demo, no markdown syntax errors.

- [ ] **Step 3: Commit**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
git add README.md
git commit -m "docs: full v1 README — install, quickstart, skill, demo, costs, roadmap"
```

---

## Phase 4: Tag v1.0

### Task 9: Final verification + tag

This task is a manual end-to-end sanity check before tagging v1.0.

- [ ] **Step 1: Run the full test suite (non-e2e)**

```bash
cd /Users/chenlinzhuo/code/video-to-notebook
.venv/bin/pytest -v -m "not e2e"
.venv/bin/pyright src tests
```

Expected: all green.

- [ ] **Step 2: Smoke-test the install-locally script**

```bash
bash skills/video-to-notebook/scripts/install-locally.sh
ls -la ~/.claude/skills/video-to-notebook
```

Expected: symlink exists pointing back to repo.

- [ ] **Step 3: Smoke-test the demo build script (no API key path)**

```bash
( unset ANTHROPIC_API_KEY && bash examples/frontier-notebook/build.sh 2>&1 ) | head -3
```

Expected: clear error message about missing API key, exit code 1.

- [ ] **Step 4: Verify the Pages workflow YAML parses**

```bash
python3 -c "import yaml; print('OK' if yaml.safe_load(open('.github/workflows/pages.yml')) else 'EMPTY')"
```

Expected: `OK`.

- [ ] **Step 5: Tag the v1.0 release**

```bash
git tag plan-4-done
git tag -a v1.0.0 -m "v1.0.0 — Foundation + Crawl + Tag + Cluster + Build + Demo + Skill"
git log --oneline plan-3-done..plan-4-done
```

- [ ] **Step 6: Print a final summary**

```bash
echo ""
echo "video-to-notebook v1.0.0 SHIPPED"
echo "============================"
echo "Commits (Plan 1 → Plan 4): $(git rev-list --count plan-1-done~..plan-4-done)"
echo "Tests passing: $(.venv/bin/pytest -m 'not e2e' --collect-only -q 2>/dev/null | tail -1)"
echo ""
echo "Try the skill:"
echo "  bash skills/video-to-notebook/scripts/install-locally.sh"
echo ""
echo "Try the demo:"
echo "  export ANTHROPIC_API_KEY=..."
echo "  bash examples/frontier-notebook/build.sh"
```

---

## Self-Review Notes

**Spec coverage (Plan 4 portion):**

- §4 `skills/video-to-notebook/SKILL.md`: ✅ Task 1.
- §4 `skills/video-to-notebook/scripts/`: ✅ Task 2 (`run-pipeline.sh`), Task 3 (`install-locally.sh`).
- §4 `examples/frontier-notebook/`: ✅ Tasks 4 (config) + 5 (script).
- §4 `.github/workflows/pages.yml`: ✅ Task 7.
- §10 distribution: `pip install video-to-notebook` already in pyproject (Plan 1); Claude Code skill plugin path established here. ✅

**Out of scope (correctly deferred):**

- Public marketplace listing for the Claude Code skill — requires Anthropic-side publishing flow, not a code task. The `install-locally.sh` script gives users the manual route in the meantime.
- npm/PyPI publish workflow — not in the spec. Out of scope for v1.
- Bilibili crawl in the GitHub Pages workflow — would require committing cookies (security hole). Demo defaults to YouTube-only courses.

**Placeholder scan:** no "TBD", "TODO", or unresolved placeholders. All bash scripts have explicit error paths; the demo URLs in `courses.toml` are real public YouTube playlists.

**Type / signature consistency:**

- `courses.toml` schema (`[[course]] slug = ... url = ... platform = ... cookies_from = ...`) matches what `build.sh` parses in its inline Python TOML loader.
- The `SITE_URL` + `BASE_PATH` env vars in `astro.config.mjs` (Task 6) match what `pages.yml` (Task 7) sets.
- The skill description's prerequisite checks (Task 1) match the actual CLI requirements (video-to-notebook, node, ANTHROPIC_API_KEY).
- `install-locally.sh` (Task 3) writes a symlink at `~/.claude/skills/video-to-notebook/` — Claude Code's documented skill discovery path.

**No backlog from Plan 3** to address — the slug-frontmatter bug already landed as part of Plan 3's hotfix.
