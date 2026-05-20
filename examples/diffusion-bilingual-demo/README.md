# Diffusion-Bilingual Demo (v2.2 showcase)

The rendered content of the original `video-to-notebook` showcase site —
a Chinese / English bilingual textbook on **diffusion models**, sourced
from three open courses (CMU 10-799, Diffusion Principles, Diffusion LM).

This directory used to live under `template-site/src/content/`. In
v2.3.0 the template-site was reset to a clean scaffold so new projects
no longer inherit demo content. The data was moved here, intact.

## What's in `content/`

| Path | Files | Description |
|------|-------|-------------|
| `content/concept/*.md` | 33 | Concept Markdown — frontmatter (canonical_name, description, occurrence_count) + body listing every occurrence across the 3 source courses |
| `content/course/*.md` | 3 | Course Markdown — title / platform / source_url / lecture_count |
| `content/lecture/*.md` | 40 | Lecture Markdown — per-lecture chunks with concept_slugs |
| `content/textbook/zh/*.html` | 21 | Full Chinese textbook, one chapter per HTML fragment |
| `content/textbook/zh/curriculum.json` | 1 | Chapter order, titles, primary concept slugs |
| `content/textbook/en/*.html` | 3 | English Module 1 only (chapters 1-3: Why Diffusion / VAE / ELBO) |
| `content/textbook/en/curriculum.json` | 1 | English chapter metadata |
| `content/concept-explainers/zh/*.html` | 33 | Rich illustrated concept pages with 9-section structure, SVGs, interactive widgets |
| `content/concept-explainers/zh/manifest.json` | 1 | Concept explainer index |
| `content/concept-explainers/en/manifest.json` | 1 | English placeholder (no explainers ported yet) |

Total: ~7 MB. Authored mostly by Claude Code over the v1.0 → v2.2
release cycle. Style guide compliance varies by vintage — chapters 1-3
of the English version follow the v3 synthesizer style guide (5000-8000
characters, 8-14 sections, full deriv-steps); some earlier zh chapters
predate that guideline.

## Source courses

Listed in `content/course/`:

- `cmu-10799-diffusion-flow` — CMU 10-799 "Diffusion & Flow Matching" S26
- `diffusion-lm-vizuara` — Vizuara "Diffusion Language Models from Scratch"
- `diffusion-principles-vizuara` — Vizuara "Principles of Diffusion Models"

The raw transcripts and tagging history are not preserved in this
snapshot — only the rendered output. To regenerate from scratch you
would need to crawl the three playlists, tag against the diffusion
ontology, cluster, write a curriculum, synthesize each chapter, and
explain each concept. See `examples/frontier-notebook/RUNBOOK.md` for
the equivalent agent-driven flow.

## Restoring this demo into a project

If you want to see the rendered site locally:

```bash
# 1. Start a fresh project
mkdir my-diffusion-demo && cd my-diffusion-demo
video-to-notebook init --language zh

# 2. Drop the demo content into the project's Astro content tree
cp -R /path/to/course-merger/examples/diffusion-bilingual-demo/content/. \
      .video-to-notebook/../site/src/content/

# 3. Build
video-to-notebook build
video-to-notebook serve
```

> **Caveat**: because the SQLite DB is empty in your fresh project,
> the build writers will overwrite manifest.json / curriculum.json with
> empty arrays on the next `video-to-notebook build`. The HTML fragments
> stay (they're file-level data), but the page index will go blank.
> If you want to truly restore the demo as a project, you'd need to
> also regenerate the DB (out of scope for this snapshot).

For pure read-only inspection, just open the HTML fragments in a
browser directly — they include inline SVG and styles that render
standalone.

## Why we kept it

Three reasons:

1. **It's a quality reference.** The English Module 1 (Why Diffusion /
   VAE / ELBO) is the canonical worked example of the v3 synthesizer
   style guide — 5000-8000 char chapters with full deriv-steps,
   colour-coded callouts, PyTorch skeletons.
2. **It's a regression baseline.** Comparing future build output
   against this snapshot catches style-guide drift.
3. **It's the only OSS-licensed corpus that ships with the repo.**
   Other courses (Vizuara DeepSeek in `frontier-notebook`, etc.) are
   pointed at via URL — this is the only one where the rendered
   product is in the repo.
