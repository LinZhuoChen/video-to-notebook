# Plan 7 — Bilingual Demo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Ship a Pages demo where readers can switch between **中文** and **English** versions of the diffusion textbook + concept encyclopedia, with the English content **regenerated from the same English source transcripts** (not machine-translated from the existing Chinese fragments).

**Architecture:** Per-language content sub-folders under `template-site/src/content/<area>/<lang>/`. Astro pages dispatch on `currentLanguage` from `i18n.ts` (driven by build-time `PUBLIC_LANGUAGE` env). Pages CI builds twice — once for zh at `/`, once for en at `/en/` — and merges into one artifact. Header carries an `EN`/`中` toggle that navigates between sibling deployments preserving the current sub-path (`data-base` attribute baked at build time via `import.meta.env.BASE_URL`). Python build writers route to `<lang>/` based on `build_meta.language`.

**Tech Stack:** Same as v2.1.1. No new dependencies.

**Repo:** `/Users/chenlinzhuo/code/course-merger/` (at tag `v2.1.1` when planning began).

---

## File structure

```
template-site/src/content/textbook/                   # NEW per-language sub-folders
├── zh/  ← existing 21 chapter fragments + curriculum.json `git mv`d here
└── en/  ← new (Module 1 shipped; M2-M6 deferred to subsequent batches)

template-site/src/content/concept-explainers/          # NEW per-language sub-folders
├── zh/  ← existing 33 concept fragments + manifest.json `git mv`d here
└── en/  ← new (all 33 concepts deferred)

src/video_to_notebook/build/textbook_writer.py        # MODIFY — read build_meta.language, route to <lang>/
src/video_to_notebook/build/concept_writer.py         # MODIFY — same

template-site/src/layouts/Base.astro                  # MODIFY — add .lang-toggle button + JS handler reading data-base
template-site/src/pages/textbook/index.astro          # MODIFY — pick <lang>/curriculum.json
template-site/src/pages/textbook/[order].astro        # MODIFY — pick fragments from <lang>/*.html
template-site/src/pages/concepts/index.astro          # MODIFY — pick <lang>/manifest.json
template-site/src/pages/concepts/[slug]/index.astro   # MODIFY — pick fragments from <lang>/*.html
template-site/src/pages/index.astro                   # MODIFY — pick <lang>/curriculum.json for stats
template-site/src/components/TextbookNav.astro        # MODIFY — pick <lang>/curriculum.json
template-site/src/styles/global.css                   # MODIFY — share .lang-toggle styling with .theme-toggle

.github/workflows/pages.yml                           # MODIFY — build twice (zh + en) and merge dist

examples/frontier-notebook/build.sh                   # MODIFY — add --language / --bilingual flags

tests/unit/test_textbook_writer.py                    # MODIFY — assert <lang>/ paths
tests/unit/test_concept_writer.py                     # MODIFY — same
                                                       # ADD `test_respects_build_meta_language`
```

---

## Task decomposition

### Phase 1 — code changes (~2–4 h)

#### Task 1 — Astro content layout

**Files:**
- Move: `template-site/src/content/textbook/*.html` → `textbook/zh/*.html`
- Move: `template-site/src/content/textbook/curriculum.json` → `textbook/zh/curriculum.json`
- Move: `template-site/src/content/concept-explainers/*.html` → `concept-explainers/zh/*.html`
- Move: `template-site/src/content/concept-explainers/manifest.json` → `concept-explainers/zh/manifest.json`
- Create: `template-site/src/content/textbook/en/curriculum.json` (empty placeholder `{"schema_version":"1","chapters":[]}`)
- Create: `template-site/src/content/concept-explainers/en/manifest.json` (empty placeholder `{"schema_version":"1","explainers":[]}`)

- [ ] **Step 1: Move via `git mv` to preserve history**

```bash
cd template-site/src/content
mkdir -p textbook/{zh,en} concept-explainers/{zh,en}
git mv textbook/*.html textbook/curriculum.json textbook/zh/
git mv concept-explainers/*.html concept-explainers/manifest.json concept-explainers/zh/
echo '{"schema_version":"1","chapters":[]}' > textbook/en/curriculum.json
echo '{"schema_version":"1","explainers":[]}' > concept-explainers/en/manifest.json
```

- [ ] **Step 2: Update all 6 Astro consumers to dispatch on `currentLanguage`**

Each consumer reads `currentLanguage` from `i18n.ts` and picks the matching `<lang>/` folder. Pattern:

```ts
const data = currentLanguage === 'en'
  ? await import('../../content/textbook/en/curriculum.json')
  : await import('../../content/textbook/zh/curriculum.json');
```

For `import.meta.glob` (chapter fragments), eager-load both folders and select at runtime:

```ts
const zhFragments = import.meta.glob('../../content/textbook/zh/*.html', { query: '?raw', import: 'default', eager: true });
const enFragments = import.meta.glob('../../content/textbook/en/*.html', { query: '?raw', import: 'default', eager: true });
const fragments = currentLanguage === 'en' ? enFragments : zhFragments;
```

#### Task 2 — Python build writers

**Files:** `src/video_to_notebook/build/textbook_writer.py`, `src/video_to_notebook/build/concept_writer.py`

- [ ] **Step 1: Add a `_read_project_language(db_path)` helper** that reads `build_meta.language` (defaulting to `'zh'` for legacy projects)
- [ ] **Step 2: Route output to `<area>/<lang>/`** instead of flat
- [ ] **Step 3: New test `test_respects_build_meta_language`** seeds `build_meta.language='en'` and asserts content lands under `en/` not `zh/`
- [ ] **Step 4: Update existing writer tests** to assert `<lang>/` paths

#### Task 3 — Pages workflow build-twice

**File:** `.github/workflows/pages.yml`

- [ ] **Step 1: Build zh** with `PUBLIC_LANGUAGE=zh BASE_PATH=/<repo>/`, move dist to `dist-zh/`
- [ ] **Step 2: Build en** with `PUBLIC_LANGUAGE=en BASE_PATH=/<repo>/en/`, move dist to `dist-en/`
- [ ] **Step 3: Merge en into zh** at `dist-zh/en/`, upload as single Pages artifact

#### Task 4 — Header language toggle (Base.astro)

**File:** `template-site/src/layouts/Base.astro`

- [ ] **Step 1: Add `.lang-toggle` button** between search and theme-toggle, with `data-current-lang={currentLanguage}` and `data-base={base}` (where `base = import.meta.env.BASE_URL`). Render `EN` on zh pages, `中` on en pages.
- [ ] **Step 2: Inline JS handler** reads `data-base`, computes sub-path = `window.location.pathname.slice(base.length)`, and:
  - on en: target = `base.replace(/en\/$/, '') + sub + search`
  - on zh: target = `base + 'en/' + sub + search`
- [ ] **Step 3: CSS** in `global.css` — share `.theme-toggle` + `.lang-toggle` chip styling (36×36, var(--surface), var(--border)); lang button additionally uses font-mono + font-weight 600.

#### Task 5 — `examples/frontier-notebook/build.sh` bilingual

**File:** `examples/frontier-notebook/build.sh`

- [ ] **Step 1: Parse `--language` / `--bilingual`** flags
- [ ] **Step 2: `build_one(lang)` helper** that swings `build_meta.language` via SQLite + reruns `video-to-notebook build`
- [ ] **Step 3: `--bilingual` mode** calls `build_one zh` and `build_one en` sequentially; prints a reminder that the synthesize/explain step still needs to be driven separately per language

#### Task 6 — Smoke test + commit + push

- [ ] **Step 1:** `ruff check .` clean
- [ ] **Step 2:** `pyright src tests` clean
- [ ] **Step 3:** `pytest -m "not e2e" --ignore=tests/unit/test_embedding.py` — full suite green (target: 170+ passing)
- [ ] **Step 4:** Local Astro build, both `PUBLIC_LANGUAGE=zh` and `PUBLIC_LANGUAGE=en` produce a clean dist (en with empty-state pages)
- [ ] **Step 5:** Commit `feat(bilingual): Phase 1 …` + push; verify Pages workflow logs

### Phase 2 — content regeneration (~1–3 h per module via in-session agent)

This phase is **content authoring**, not engineering. It cannot be automated end-to-end because the LLM-in-session step depends on a human-in-the-loop agent. Per-module estimate: 30–45 min per chapter, 15–20 min per concept, with ~3 chapters + ~6 concepts per module average.

For each en chapter `N`:

- [ ] **Step 1:** `video-to-notebook synthesize --chapter N --print-prompts > /tmp/en/ch${N}.json` (in the demo project, with `build_meta.language='en'`)
- [ ] **Step 2:** Agent reads `/tmp/en/ch${N}.json`, authors a chapter HTML fragment to `/tmp/en/ch${N}.html` following the v3 synthesize style guide. Source quotes are kept verbatim from the **English** lecture transcripts (not back-translated from the zh version). Structural elements (SVG, math, code, callouts) parallel the zh version where appropriate, but prose is freshly authored.
- [ ] **Step 3:** Write `/tmp/en/apply-ch${N}.json` referencing the fragment with `synthesizer="claude-code-max:v2-en"`
- [ ] **Step 4:** `video-to-notebook synthesize --chapter N --apply-results /tmp/en/apply-ch${N}.json`
- [ ] **Step 5:** Commit-batch to source repo when a module completes

For each en concept `<slug>`:

- [ ] Identical loop with `video-to-notebook explain --concept <slug>` instead of synthesize

Module rollout order (recommended):

1. ✅ **Module 1 — Foundations** (Ch 1-3): shipped in v2.2.0 (commit `0f0c831`)
2. **Module 2 — DDPM** (Ch 4-7)
3. **Module 3 — Score perspective** (Ch 8-11)
4. **Module 4 — Flow Matching** (Ch 12-15)
5. **Module 5 — Sampling & guidance** (Ch 16-18)
6. **Module 6 — Discrete & language diffusion** (Ch 19-21)
7. **All 33 concepts** (deepest content per concept ≈ 1500 words; total ~50K words)

### Phase 3 — deploy + verify

- [ ] Copy en fragments from the demo project's `<project>/site/src/content/<area>/en/` into the source repo's `template-site/src/content/<area>/en/`
- [ ] Commit + push; Pages workflow auto-rebuilds zh + en
- [ ] Verify on the live URL: `/textbook/` (zh), `/en/textbook/` (en), `/concepts/` (zh), `/en/concepts/` (en), header toggle navigates between siblings preserving sub-path

---

## Self-review checklist

- [x] All 6 Astro consumers dispatch on `currentLanguage`
- [x] Python writers read `build_meta.language`
- [x] Pages workflow merges both builds into one artifact
- [x] Header toggle preserves the current sub-path on Pages (`data-base` from build-time `BASE_URL`)
- [x] CHANGELOG entry written for v2.2.0 + v2.2.1
- [x] Frontier `build.sh` understands `--bilingual`
- [ ] Phase 2 — 18 / 21 chapters + 33 / 33 concepts still pending

---

## Status (as of 2026-05-20)

| Phase | Status | Shipped in |
|---|---|---|
| Phase 1 — code | ✅ done | v2.2.0 + v2.2.1 |
| Phase 2 — content | 🟡 partial (3 / 21 chapters; 0 / 33 concepts) | v2.2.0 |
| Phase 3 — deploy | ✅ Pages auto-deploys both languages |
