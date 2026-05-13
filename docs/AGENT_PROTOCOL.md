# Agent protocol

course-merger's LLM stages are designed to be **agent-agnostic**. Any agent that can read JSON, reason, and write JSON can drive the pipeline.

This document defines the JSON envelope schemas, expected agent behavior, and conventions for the `--print-prompts` / `--apply-results` flow. It's the source of truth for any client (Claude Code, Codex, Cursor, Continue, your own script).

## Workflow shape

Every LLM-driven stage shares the same shape:

```
                       ┌─────────────────────────────────┐
       course-merger   │  *_prompts envelope  (JSON)     │   ──── stdout
   --print-prompts    →└─────────────────────────────────┘
                                      │
                                      ▼
                         agent reads, reasons, writes
                                      │
                                      ▼
                       ┌─────────────────────────────────┐
       course-merger   │  *_results  envelope  (JSON)    │   ──── file path
   --apply-results    ←└─────────────────────────────────┘
```

The CLI never depends on which agent generates the results. It validates the schema, applies to SQLite, and reports.

## Universal envelope fields

Every envelope (prompts and results) MUST include:

| Field            | Type   | Description                                                          |
|------------------|--------|----------------------------------------------------------------------|
| `schema_version` | string | Currently `"1"`. The CLI rejects envelopes with versions it doesn't know. |
| `kind`           | string | One of: `tag_prompts`, `tag_results`, `cluster_prompts`, `cluster_results`, `curriculum_prompts`, `curriculum_results`, `synthesize_prompts`, `synthesize_results`, `explain_prompts`, `explain_results`. |

Results envelopes additionally specify the **agent identifier** in a field named after the stage (`tagger_model_id`, `reviewer_model_id`, `designer`, `synthesizer`, `explainer`). Convention:

| Agent             | Identifier convention   |
|-------------------|-------------------------|
| Anthropic API key | `claude-haiku-4-5`, `claude-sonnet-4-6`, etc. (literal model id) |
| Claude Code       | `claude-code-max:v1`    |
| OpenAI Codex CLI  | `codex-cli:v1`          |
| Cursor / Continue | `cursor:v1` / `continue:v1` |
| Your own script   | `<your-name>:v1`        |

These are free-form strings. The CLI doesn't validate them, but they're persisted in the DB so future audits can tell which agent produced which decision.

## Stage 1 — `tag` (per-chunk concept labeling)

### Prompts envelope

`course-merger tag --ontology <ont.yaml> --print-prompts [--limit N] [--course SLUG]`

```json
{
  "schema_version": "1",
  "kind": "tag_prompts",
  "ontology_slugs": ["self-attention", "rotary-positional-encoding", "..."],
  "chunks": [
    {"chunk_id": 1, "text": "...transcript chunk..."},
    {"chunk_id": 2, "text": "..."}
  ]
}
```

The agent's job: read each chunk, decide which ontology slugs apply (multi-label OK), assign a confidence in `[0, 1]`.

### Results envelope

```json
{
  "schema_version": "1",
  "kind": "tag_results",
  "tagger_model_id": "codex-cli:v1",
  "results": [
    {
      "chunk_id": 1,
      "tags": [
        {"slug": "self-attention", "confidence": 0.9},
        {"slug": "kv-cache", "confidence": 0.4}
      ]
    },
    {"chunk_id": 2, "tags": []}
  ]
}
```

**Confidence semantics:** entries with confidence < 0.55 are stored in `proposed_tags` (uncertain, surface in cluster review); ≥ 0.55 are written to `chunk_concepts` (high-confidence, indexed in the site).

**Loop:** re-run `--print-prompts` to get the next batch. The envelope's `chunks` array shrinks as you tag. Empty `chunks` = done.

## Stage 2 — `cluster` (merge proposed tags into the ontology)

### Prompts envelope

`course-merger cluster --ontology <ont.yaml> --print-prompts`

```json
{
  "schema_version": "1",
  "kind": "cluster_prompts",
  "ontology_slugs": ["self-attention", "..."],
  "clusters": [
    {
      "cluster_id": 0,
      "proposed_slugs": ["rope", "rotary-pe", "rotary-pos-encoding"],
      "occurrence_counts": [12, 3, 5],
      "sample_chunks": [
        {"chunk_id": 41, "text": "...RoPE rotates the query and key vectors..."}
      ]
    }
  ]
}
```

The clusterer pre-groups proposed tags by embedding similarity. The agent's job: for each cluster, decide one of four actions:

- **merge** → all proposed slugs in this cluster fold into an existing ontology slug
- **create** → promote one of the proposed slugs to a new ontology entry
- **reject** → noise, discard
- **ambiguous** → human review needed (lands in a manual-review queue)

### Results envelope (bundled apply)

The cluster stage requires the prompts envelope back, because `apply` re-derives chunk-level changes from the clustering result. Construct a single bundle file:

```json
{
  "_prompts_envelope": { ...full prompts envelope from --print-prompts... },
  "decisions_envelope": {
    "schema_version": "1",
    "kind": "cluster_results",
    "reviewer_model_id": "codex-cli:v1",
    "decisions": [
      {"cluster_id": 0, "decision": "merge", "target_slug": "rotary-positional-encoding"},
      {"cluster_id": 1, "decision": "create", "target_slug": "qkv-projection"},
      {"cluster_id": 2, "decision": "reject"},
      {"cluster_id": 3, "decision": "ambiguous"}
    ]
  }
}
```

Apply:

```bash
course-merger cluster --ontology <ont.yaml> --apply-results bundle.json
```

## Stage 3 — `curriculum` (chapter ordering for the textbook)

`course-merger curriculum --print-prompts [--samples N]`

### Prompts envelope

```json
{
  "schema_version": "1",
  "kind": "curriculum_prompts",
  "concepts": [
    {"slug": "linear-algebra", "canonical_name": "Linear Algebra", "occurrence_count": 47}
  ],
  "concept_chunks": {
    "linear-algebra": [
      {"course_slug": "cs336", "lecture_idx": 2, "text": "..."}
    ]
  },
  "style_guide": "..."
}
```

The agent designs a **pedagogically ordered** chapter sequence: each chapter has a primary concept + related concepts, grouped into 4-7 modules. Beginners read in order.

### Results envelope

```json
{
  "schema_version": "1",
  "kind": "curriculum_results",
  "designer": "codex-cli:v1",
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

Idempotent: re-applying overwrites the chapter list (use this to iterate).

## Stage 4 — `synthesize` (per-chapter HTML fragment)

`course-merger synthesize --chapter N --print-prompts`

### Prompts envelope

```json
{
  "schema_version": "1",
  "kind": "synthesize_prompts",
  "chapter": {
    "order_idx": 1,
    "module": "Module 1: 数学直觉",
    "title": "什么是向量",
    "blurb": "...",
    "primary_concept_slug": "linear-algebra",
    "related_concept_slugs": []
  },
  "source_chunks": [
    {"course_slug": "cs336", "lecture_idx": 2, "video_url": "...", "start_sec": 268.4, "text": "..."}
  ],
  "style_guide": "...",
  "output_path_hint": ".course-merger/textbook/1.html"
}
```

The agent reads the chapter spec + source chunks + style guide, writes a self-contained HTML fragment to disk (`/tmp/cm-ch1.html` or wherever).

The style guide enforces: anti-bias opening · inline SVG diagram · optional CSS animation · one embedded source-clip iframe · LaTeX math · `<div class="takeaways">` at end with 3 bullets.

### Results envelope

```json
{
  "schema_version": "1",
  "kind": "synthesize_results",
  "synthesizer": "codex-cli:v1",
  "chapter_order_idx": 1,
  "html_fragment_path": "/tmp/cm-ch1.html"
}
```

Apply copies the fragment to `.course-merger/textbook/N.html` and marks the chapter `synthesized`. Re-applying overwrites.

## Stage 5 — `explain` (per-concept encyclopedia entry, v1.3+)

`course-merger explain --concept <slug> --print-prompts`

### Prompts envelope

```json
{
  "schema_version": "1",
  "kind": "explain_prompts",
  "explainer_version": "v2",
  "concept": {
    "slug": "linear-algebra",
    "canonical_name": "Linear Algebra",
    "description": "...",
    "aliases": ["..."],
    "module_hint": "Module 1: 数学直觉"
  },
  "occurrences": [
    {"chunk_id": 41, "course_slug": "cs336", "lecture_idx": 2,
     "lecture_title": "...", "video_url": "...", "start_sec": 5.789, "text": "..."}
  ],
  "related_concepts": [
    {"slug": "scalar-multiplication", "canonical_name": "Scalar Multiplication", "co_occurrence": 3}
  ],
  "style_guide": "...",
  "output_path_hint": ".course-merger/concepts/linear-algebra.html"
}
```

### Results envelope

```json
{
  "schema_version": "1",
  "kind": "explain_results",
  "concept_slug": "linear-algebra",
  "explainer": "codex-cli:v1",
  "html_fragment_path": "/tmp/cm-linear-algebra.html"
}
```

Apply copies into `.course-merger/concepts/<slug>.html` and upserts into `concept_explanations`. Re-applying overwrites.

## Style guide source-of-truth

The `style_guide` field of each `*_prompts` envelope is the verbatim version-pinned text from:

- `src/course_merger/tag/prompts.py` (tagger style)
- `src/course_merger/cluster/prompts.py` (clusterer style)
- `src/course_merger/curriculum/prompts.py` (curriculum designer style)
- `src/course_merger/synthesize/prompts.py` (chapter style)
- `src/course_merger/explain/prompts.py` (concept-entry v2 contract)

These files include a `_VERSION` constant (`SYNTHESIZER_VERSION`, `EXPLAINER_VERSION`, etc.). When the contract changes meaningfully the version bumps. Agents should respect the style guide they received — it's the contract for that envelope.

## Error handling

Apply commands validate strictly:

- Wrong `schema_version` → `ValueError: schema_version 'X' unsupported`
- Wrong `kind` → `ValueError: kind 'X' is not '<expected>'`
- Missing referenced file → `FileNotFoundError`
- Unknown slug (for `apply_explain_results` etc.) → `ValueError: no concept with slug='X'`

These are loud and fast. Agents should surface them to the user rather than silently retrying.

## Idempotency guarantees

- **tag** — `chunk_concepts` and `proposed_tags` are upserted by `(chunk_id, concept_id)`. Re-tagging the same chunk doesn't duplicate.
- **cluster** — cluster decisions write to `chunk_concepts` directly; re-running on the same proposed tags is a no-op.
- **curriculum** — `curriculum_chapters` table is a single canonical list. Re-applying replaces.
- **synthesize / explain** — file-copy + DB upsert by chapter/concept id. Re-applying overwrites.

A run can always be retried.

## Agent quality contract

Beyond schema correctness, agents are expected to:

1. **Respect the style guide** in `*_prompts.style_guide`. It's the contract for what you emit.
2. **Use real timestamps** for source-clip deep links. Don't fabricate `start_sec` values.
3. **Cross-link only to existing slugs**. For `explain`, the see-also section MUST link to slugs in the envelope's `related_concepts`. Don't invent.
4. **Keep generated HTML self-contained**. No external CSS/JS imports except KaTeX (already loaded by the layout).
5. **Avoid PII or copyrighted-as-text content**. The transcripts in `source_chunks` are derived works — quote sparingly, attribute via `<a href="...&t=Ns">` deep links instead.

## Versioning

This protocol is at `schema_version: "1"`. Breaking changes will bump to `"2"` and the CLI will reject `"1"` envelopes (with a deprecation window in a minor version). Non-breaking changes (new optional fields) stay at `"1"`.
