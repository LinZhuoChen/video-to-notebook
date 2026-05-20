# Bilingual demo plan

> Goal: ship a Pages demo where readers can switch between **中文** and **English** versions of the diffusion textbook + concept encyclopedia, with the English content **regenerated from the same English source transcripts** (not machine-translated from the existing Chinese fragments).

## Status (as of 2026-05-20)

| Phase | Status | Shipped in |
|---|---|---|
| **Phase 1 — code changes** (Astro content split, Python writers per-lang, Pages workflow build-twice, header toggle, frontier `build.sh --bilingual`) | ✅ **done** | v2.2.0 (commit `8b35535`) + v2.2.1 hotfix for the toggle's `BASE_URL` handling (commit `5c84244`) |
| **Phase 2 — content regeneration** (21 chapters + 33 concepts in en, from English source transcripts) | 🟡 **partial (3 / 21 chapters)** | v2.2.0 (commit `0f0c831`): Module 1 = Why Diffusion / VAE / ELBO. Remaining 18 chapters + all 33 concepts pending. |
| **Phase 3 — deploy + verify** | ✅ Pages auto-deploys both `/` and `/en/` on each push; verified live at `https://linzhuochen.github.io/video-to-notebook/en/textbook/`. |

Open questions resolved (originally listed at the bottom of this doc):
- **A.** Run en regen in a fresh Codex/Claude Code session? → **Yes**, but Module 1's three chapters were authored in the same session that wrote this plan, as quality benchmark. Modules 2–6 + concepts are left for fresh sessions.
- **B.** Regenerate the *curriculum* too (en titles)? → **Yes**, full en regen. Curriculum metadata (titles + blurbs for all 21 chapters) was translated in-place via SQL in the demo project so the en textbook nav doesn't break even before all bodies land.
- **C.** Upgrade `examples/frontier-notebook/build.sh` to drive bilingual builds? → **Yes**, the script gained `--language` and `--bilingual` flags in Phase 1.

## Current state (snapshot before the work started)

- Demo corpus: 4 diffusion courses, all original lecture audio is in English (Karpathy / Dr. Raj / CMU 10-799 / chuguo-aigc).
- Demo project: `~/note/courses/diffusion-merged/.video-to-notebook/` (separate from the source repo).
- Checked-in content fragments in the source repo: `template-site/src/content/textbook/*.html` (21 zh chapters) + `template-site/src/content/concept-explainers/*.html` (33 zh concepts).
- `i18n.ts` already supports zh + en UI dictionaries via build-time `PUBLIC_LANGUAGE` env.
- `build_meta.language = zh` in the demo project DB → drives both prompt language (chapter prose) and Astro UI strings.
- Pages workflow builds **once** with `PUBLIC_LANGUAGE=zh` and deploys to `/`.

## Target

```
https://linzhuochen.github.io/video-to-notebook/        ← zh (current)
https://linzhuochen.github.io/video-to-notebook/en/     ← new en build (regenerated content)

Header has a 中 / EN toggle.
Either build serves the same chrome (logo, search, dark mode) — only content + UI strings differ.
```

## Work breakdown

### Phase 1 — code changes (~2-4 hours engineering)

1. **Astro content layout** — split per-language content folders:
   ```
   template-site/src/content/textbook/zh/*.html
   template-site/src/content/textbook/en/*.html
   template-site/src/content/concept-explainers/zh/*.html
   template-site/src/content/concept-explainers/en/*.html
   ```
   `template-site/src/pages/textbook/[order]/index.astro` reads `PUBLIC_LANGUAGE` and picks the right folder.

2. **Build writer** — `src/video_to_notebook/build/textbook_writer.py` + `concept_writer.py` write to `<lang>/*.html` instead of flat. Read `build_meta.language` from DB.

3. **Pages workflow** — replace single build with:
   ```yaml
   - name: Build zh
     env: { PUBLIC_LANGUAGE: zh, BASE_PATH: /video-to-notebook/ }
     run: npm run build
   - name: Save zh dist
     run: cp -r dist dist-zh
   - name: Build en
     env: { PUBLIC_LANGUAGE: en, BASE_PATH: /video-to-notebook/en/ }
     run: npm run build
   - name: Merge
     run: mkdir -p dist-zh/en && cp -r dist/* dist-zh/en/
   - name: Upload
     uses: actions/upload-pages-artifact@v3
     with: { path: dist-zh }
   ```

4. **Language switcher** — add a button in `Base.astro` next to the theme toggle. Links to the sibling deployment (`/en/` ↔ `/`).

### Phase 2 — content regeneration (~1-3 hours LLM in-session)

This is where the bulk of the work happens. Run inside the demo project:

```bash
cd ~/note/courses/diffusion-merged/
# Switch project language to en (rewrites build_meta + style guides emit en prompts)
video-to-notebook init --force --language en   # WARNING: destroys current state
```

That's destructive. Better:

```bash
# Clone the project DB to a parallel en project
cp -r .video-to-notebook .video-to-notebook.zh-backup
sqlite3 .video-to-notebook/db.sqlite "UPDATE build_meta SET value='en' WHERE key='language';"

# Wipe synthesized + explained content (re-runs synthesize/explain from scratch)
rm -rf .video-to-notebook/textbook/ .video-to-notebook/concepts/
sqlite3 .video-to-notebook/db.sqlite "UPDATE curriculum_chapters SET status='planned'; DELETE FROM concept_explanations;"

# Re-run synthesize + explain in en
# (in-session via Claude Code / Codex)
for n in 1..21; do
  video-to-notebook synthesize --chapter $n --print-prompts > /tmp/chN.json
  # agent reads, writes en HTML
  video-to-notebook synthesize --chapter $n --apply-results /tmp/applyN.json
done
# Same for 33 concepts.
```

Cost: 0 extra (in-session via Claude Max / Codex subscription). Time: ~1-3 hours wall clock.

### Phase 3 — commit content + deploy

1. Copy en fragments out of demo project into source repo:
   ```bash
   mkdir -p template-site/src/content/textbook/en
   cp ~/note/courses/diffusion-merged/.video-to-notebook/textbook/*.html template-site/src/content/textbook/en/
   # Move existing zh fragments into zh/
   mkdir -p template-site/src/content/textbook/zh
   git mv template-site/src/content/textbook/*.html template-site/src/content/textbook/zh/
   # Same for concept-explainers/
   ```

2. Commit + push. Pages workflow builds both, switcher works.

## Remaining work for Phase 2

To finish the en demo, drive an in-session agent (Codex or Claude Code) through the remaining 18 chapters and 33 concepts. The demo project DB is already in the `language='en'` state with curriculum metadata translated and Module 1 (chapters 1–3) marked `synthesized`; from there:

```bash
cd ~/note/courses/diffusion-merged

# Synthesize chapters 4..21
for n in 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21; do
  video-to-notebook synthesize --chapter $n --print-prompts > /tmp/en/ch${n}.json
  # agent reads, writes /tmp/en/ch${n}.html, then:
  video-to-notebook synthesize --chapter $n --apply-results /tmp/en/apply-ch${n}.json
done

# Explain all 33 concepts
sqlite3 .video-to-notebook/db.sqlite "SELECT slug FROM concepts;" | while read slug; do
  video-to-notebook explain --concept "$slug" --print-prompts > /tmp/en/c-$slug.json
  # agent writes /tmp/en/c-$slug.html, then:
  video-to-notebook explain --concept "$slug" --apply-results /tmp/en/apply-c-$slug.json
done

# Build (copies into <project>/site/src/content/<area>/en/), then mirror into source repo:
video-to-notebook build --no-npm
cp site/src/content/textbook/en/*  <repo>/template-site/src/content/textbook/en/
cp site/src/content/concept-explainers/en/* <repo>/template-site/src/content/concept-explainers/en/
git -C <repo> add template-site/src/content/textbook/en/ template-site/src/content/concept-explainers/en/
git -C <repo> commit -m "content(en): Module 2..6 + concepts"
git -C <repo> push
```

Pages will auto-rebuild both `/` and `/en/` on push (see `.github/workflows/pages.yml`).

## Estimated total work

| Phase | Time | Risk |
|---|---|---|
| 1 — code (Astro split + workflow + switcher) | 2-4 h | low |
| 2 — content regen (21 ch + 33 concepts in en) | 1-3 h LLM | medium (quality varies) |
| 3 — deploy + verify | 30 min | low |

**~4-8 hours total**, of which ~half is LLM-driven content regen that's hard to parallelize and benefits from a fresh agent session.
