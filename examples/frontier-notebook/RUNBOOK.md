# RUNBOOK — drive video-to-notebook from inside Claude Code / Codex

This is the **default, no-API-key path** for building a course-merger site.
You — the in-session agent — drive each LLM stage by reading the prompt
envelope the CLI writes to disk, producing decisions JSON, and re-invoking
the CLI with `--apply`.

If the user has an `ANTHROPIC_API_KEY` and prefers a one-shot script, point
them at `build.sh` instead.

---

## Prereqs

- `video-to-notebook` on PATH (`pip install video-to-notebook`).
- `yt-dlp` and Node 20+ on PATH.
- For Bilibili courses: an exported browser session (`--cookies-from edge` /
  `chrome` / `firefox` / `safari` is set in `courses.toml`).

## File locations (single source of truth)

```
.video-to-notebook-project/
└── .video-to-notebook/
    ├── db.sqlite               ← all state
    └── prompts/
        ├── tag.json            ← CLI writes
        ├── tag.decisions.json  ← you write
        ├── cluster.json
        ├── cluster.decisions.json
        ├── curriculum.json
        ├── curriculum.decisions.json
        ├── synthesize/chapter-N.json
        ├── synthesize/chapter-N.decisions.json
        ├── explain/<slug>.json
        └── explain/<slug>.decisions.json
```

Every CLI step prints a three-line stderr hint telling you the exact path
it wrote and the exact follow-up command. Read it after each invocation.

---

## Step 0 — bootstrap (no LLM)

```bash
cd examples/frontier-notebook
bash bootstrap.sh                  # or: bash bootstrap.sh --language en
cd .video-to-notebook-project
```

`bootstrap.sh` runs `init` + `crawl` for every entry in `courses.toml`.
Re-running is idempotent (already-crawled videos are skipped).

## Step 1 — draft the ontology

Peek a few transcripts to ground the ontology in the actual corpus:

```bash
sqlite3 .video-to-notebook/db.sqlite \
  "SELECT substr(text, 1, 200) FROM chunks ORDER BY RANDOM() LIMIT 8;"
```

Edit `../ontology.yaml`. Aim for 20-30 seed concepts covering the editorial
scope of the courses; `cluster` will discover more.

## Step 2 — tag

```bash
video-to-notebook tag --ontology ../ontology.yaml
```

The CLI writes `prompts/tag.json`. Open it and follow the embedded
`instructions` field: for each chunk return 1-3 tags, each with `slug` and
`confidence`. Use the `proposed:` prefix sparingly for genuinely missing
concepts. Slugs must be kebab-case English even when the chunk is Chinese.

**Decisions JSON shape** (write to `prompts/tag.decisions.json`):

```json
{
  "schema_version": "1",
  "kind": "tag_results",
  "tagger_model_id": "claude-code-max:v1",
  "results": [
    {"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.95}]},
    {"chunk_id": 2, "tags": [{"slug": "proposed:rope-vs-alibi", "confidence": 0.8}]}
  ]
}
```

Then:

```bash
video-to-notebook tag --ontology ../ontology.yaml --apply
```

> **Batching:** if `tag.json` is too large to hold in context, re-run the
> tag command with `--limit 200 --course <slug>` to scope the envelope.

## Step 3 — cluster

```bash
video-to-notebook cluster --ontology ../ontology.yaml
```

The CLI writes `prompts/cluster.json` listing near-duplicate `proposed:`
tags grouped by cosine similarity. For each cluster, decide:
- `merge` (target an existing concept slug),
- `create` (promote to a new canonical concept),
- `reject` (drop low-quality proposals),
- `ambiguous` (re-examine later).

**Decisions JSON shape** (write to `prompts/cluster.decisions.json`):

```json
{
  "_prompts_envelope": <verbatim copy of prompts/cluster.json>,
  "decisions_envelope": {
    "schema_version": "1",
    "kind": "cluster_decisions",
    "decisions": [
      {"cluster_id": 0, "decision": "merge", "target_slug": "rope"},
      {"cluster_id": 1, "decision": "create", "new_slug": "lora", "canonical_name": "LoRA"}
    ]
  }
}
```

(Yes, the prompts envelope is required inside the decisions file — the
apply step needs the original cluster grouping to find chunks to update.
Easiest path: `cp prompts/cluster.json prompts/cluster.decisions.json`,
then edit, wrapping the original under `_prompts_envelope`.)

Then:

```bash
video-to-notebook cluster --ontology ../ontology.yaml --apply
```

## Step 4 — curriculum

```bash
video-to-notebook curriculum
```

Reads which concepts have tagged chunks and how many. You design the chapter
sequence: each chapter has `order_idx`, `module`, `title`, `blurb`,
`primary_concept_slug`, `related_concept_slugs`. The embedded
`instructions` in `prompts/curriculum.json` describes the constraints.

**Decisions JSON shape** (write to `prompts/curriculum.decisions.json`):

```json
{
  "schema_version": "1",
  "kind": "curriculum_results",
  "curriculum_designer": "claude-code:v1",
  "chapters": [
    {
      "order_idx": 1,
      "module": "Module 1: Foundations",
      "title": "Attention from scratch",
      "blurb": "What attention computes and why.",
      "primary_concept_slug": "self-attention",
      "related_concept_slugs": ["embedding", "transformer-block"]
    }
  ]
}
```

Then:

```bash
video-to-notebook curriculum --apply
```

## Step 5 — synthesize (loop over chapters)

List pending chapters:

```bash
sqlite3 .video-to-notebook/db.sqlite \
  "SELECT order_idx, title FROM curriculum_chapters WHERE status = 'planned' ORDER BY order_idx;"
```

For each `order_idx N`:

```bash
video-to-notebook synthesize --chapter N
# write prompts/synthesize/chapter-N.decisions.json
video-to-notebook synthesize --chapter N --apply
```

The prompts envelope contains the chapter spec plus up to `--max-chunks`
source excerpts. Your job: produce one self-contained HTML chapter (under
`results.html`) following the embedded `style_guide`. Decisions JSON shape:

```json
{
  "schema_version": "1",
  "kind": "synthesize_results",
  "chapter_order_idx": N,
  "html": "<section>...</section>",
  "synthesizer_model_id": "claude-code:v1"
}
```

## Step 6 — explain (loop over concepts)

List concept slugs that have tagged occurrences:

```bash
sqlite3 .video-to-notebook/db.sqlite \
  "SELECT c.slug FROM concepts c JOIN chunk_concepts cc ON c.id = cc.concept_id GROUP BY c.slug;"
```

For each `<slug>`:

```bash
video-to-notebook explain --concept <slug>
# write prompts/explain/<slug>.decisions.json
video-to-notebook explain --concept <slug> --apply
```

Decisions JSON shape:

```json
{
  "schema_version": "1",
  "kind": "explain_results",
  "concept_slug": "<slug>",
  "html": "<article>...</article>",
  "explainer_model_id": "claude-code:v1"
}
```

## Step 7 — build the static site

```bash
video-to-notebook build
video-to-notebook serve    # opens http://localhost:4321
```

---

## Bilingual addendum

For a zh + en site, run steps 5-7 twice — once per language. Flip the
project language by editing the `build_meta` row before each rebuild:

```bash
sqlite3 .video-to-notebook/db.sqlite \
  "INSERT INTO build_meta (key, value) VALUES ('language', 'en') \
   ON CONFLICT(key) DO UPDATE SET value=excluded.value;"
# regenerate synthesize/explain decisions in English, then:
video-to-notebook build
```

The crawl + tag + cluster + curriculum results are language-agnostic and
do not need to be redone.

---

## When something goes sideways

- **Envelope is empty** (`0 chunks`, `0 concepts`, ...) — the previous
  stage hasn't populated the DB. Check `bootstrap.sh` output and verify
  `chunks` / `proposed_tags` / `chunk_concepts` row counts.
- **`--apply` says "decisions file not found"** — you wrote the decisions
  to the wrong path. The stderr hint from the previous step has the exact
  path.
- **Wrong language output** — run steps 5-7 again after flipping
  `build_meta.language`.
- **Want to redo a single chapter** — delete the decisions file and re-run
  `synthesize --chapter N` to get a fresh envelope.
