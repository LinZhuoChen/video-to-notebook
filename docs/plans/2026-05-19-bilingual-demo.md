# Bilingual demo plan

> Goal: ship a Pages demo where readers can switch between **中文** and **English** versions of the diffusion textbook + concept encyclopedia, with the English content **regenerated from the same English source transcripts** (not machine-translated from the existing Chinese fragments).

## Current state

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

## Open questions for user (decide before Phase 2)

- **A.** Run the en regeneration in this conversation (slow, eats context) or in a fresh Codex/Claude Code session (recommended — agent runs the in-session loop autonomously)?
- **B.** Should the en version regenerate the *curriculum* too (en chapter titles like "Why diffusion? AR vs Diffusion") or keep zh chapter titles even on the en page? Recommended: full en regen of curriculum + chapter bodies + concepts for consistency.
- **C.** Acceptable to leave the in-progress zh demo's `examples/frontier-notebook/` build script alone, or update it to drive bilingual builds too?

## Estimated total work

| Phase | Time | Risk |
|---|---|---|
| 1 — code (Astro split + workflow + switcher) | 2-4 h | low |
| 2 — content regen (21 ch + 33 concepts in en) | 1-3 h LLM | medium (quality varies) |
| 3 — deploy + verify | 30 min | low |

**~4-8 hours total**, of which ~half is LLM-driven content regen that's hard to parallelize and benefits from a fresh agent session.
