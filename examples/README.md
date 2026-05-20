# examples/

Worked examples that ship with the `video-to-notebook` repo. Each one is
either a runnable scaffold (start here when building your own corpus) or
a rendered-output snapshot (open here when you want to see what a finished
site looks like).

## Index

| Path | Kind | What it is |
|------|------|-----------|
| [`frontier-notebook/`](./frontier-notebook/) | runnable scaffold | The recommended starting point. Five open courses on world-models / agents, a 30-concept ontology, and two entry points: `bootstrap.sh` (no-key, agent-driven via `RUNBOOK.md`) and `build.sh` (one-shot if you have `ANTHROPIC_API_KEY`). Copy this directory, edit `courses.toml` + `ontology.yaml`, then run. |
| [`diffusion-bilingual-demo/`](./diffusion-bilingual-demo/) | rendered snapshot | The v2.2 showcase site — a Chinese / English bilingual textbook on diffusion models, sourced from three open courses (CMU 10-799, Vizuara × 2). ~7 MB of finished HTML + JSON manifests. Used to live inside `template-site/` until v2.3 moved it here. Open the README for restore instructions. |
| [`ontology-llm.yaml`](./ontology-llm.yaml) | standalone file | A general-purpose LLM-flavoured ontology you can point at via `--ontology`. Drop it next to your `courses.toml` and edit to taste. |

## Picking the right starting point

- **Building a new corpus?** Copy `frontier-notebook/` and follow `RUNBOOK.md`.
- **Want to see a finished site before committing time?** Open
  `diffusion-bilingual-demo/content/textbook/zh/1.html` (or any other
  fragment) directly in a browser — they render standalone.
- **Need a ready-to-use LLM ontology?** Grab `ontology-llm.yaml`.

## What `examples/` is *not*

It's not a place for user-generated projects. Per `.gitignore`, every
project's local state lives under `.video-to-notebook/` in its own
working directory — examples here ship only the **inputs** (or, in
the case of `diffusion-bilingual-demo/`, frozen output as a
regression baseline). Do not commit your own crawled corpora here.
