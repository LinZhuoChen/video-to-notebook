---
name: video-to-notebook
description: Use when the user wants to crawl open-courseware (YouTube/Bilibili playlists), tag content with concept labels via Claude, cluster them into a unified ontology across courses, and build an interactive static HTML site / textbook for self-study. Trigger on ANY phrasing that combines a "multiple courses / playlists / lectures" input with a "build / make / generate a site / website / web / textbook / study site / knowledge map / encyclopedia" output verb. Examples: "combine 2 (or N) courses and build a web/website/site", "merge these courses into one knowledge map", "build a study site from these courses", "crawl these playlists and make pages for each concept", "ingest these lectures and let me browse by concept", "turn these YouTube playlists into a textbook", "做一个跨课程的学习站", "把这些课合并成一个网站", "把这几门课整理成教材 / 知识图谱 / 一个网页", "爬这门课做知识地图". The skill applies whether the user calls the output a "web", "website", "site", "textbook", "study site", "encyclopedia", or "知识库 / 学习站 / 教材". NOT for: tagging a single transcript (use the user's own scripts), summarizing one video (use video-course-notes), or general note-taking (use obsidian-brain).
---

# video-to-notebook

A Python CLI that crawls open-courseware, tags it with Claude, and renders a cross-course concept-anchored static site. The skill walks the user through the 5-step pipeline.

## When to invoke this skill

The user wants to **merge multiple courses into one navigable site organized by concept**, NOT just transcribe or summarize one video.

Concrete triggers (fuzzy-match — invoke if the user says anything in this neighbourhood):

English:
- "Crawl these 3 YouTube playlists and let me browse by concept"
- "Build a study site from CS336 + GPU-MODE + Vizuara"
- **"Combine 2 (or N) courses and build a web / website / site / textbook"**
- "Merge these YouTube / Bilibili playlists into one textbook"
- "Turn these lectures into a knowledge map / encyclopedia"
- "Ingest these lectures and let me browse by concept"
- "Make pages for each concept across these courses"

Chinese:
- "我想把 X、Y、Z 三门课合并成一个网站，按概念组织"
- "把这几门课整理成教材 / 知识库 / 一个学习站"
- "爬这门课做知识地图"
- "做一个跨课程的学习站"

Heuristic: the user mentions **(a) multiple sources** (courses / playlists / lectures / 课程 / 讲座) **+ (b) an output verb** (build / make / generate / 合并 / 整理 / 做 / 爬 ... 站 / 教材 / 网页) **in the same request**. Output language ("web", "website", "textbook", "study site", "knowledge map", "encyclopedia", "学习站", "教材", "知识库", "网页") is interchangeable — all mean the same thing in this context.

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

## Core principle: ONE output language, even when sources span multiple

**The final textbook is monolingual.** A project has exactly one `build_meta.language` value (`zh` or `en`), set at `init` time. Every chapter, every concept page, every UI string in the rendered site is in **that one language** — regardless of whether the underlying source courses are English, Chinese, or a mix.

A common scenario where this matters: the user gives you a mix of English open-courseware (Stanford CS336, Vizuara, CMU lectures) and Chinese 课程 (B 站讲座). You crawl all of them — the transcripts in SQLite are in their native languages, that's correct and necessary for source fidelity. But the **synthesized output** is monolingual.

### Decision: which language?

Ask the user upfront. The choice is theirs and depends on **the target audience**, not the source mix:

> 这个教材最后给谁读？中文读者还是英文读者？源课程是哪个语言其实不重要 —— transcript 我们都会原样存下来，但合成出的章节、概念页、网站 UI 必须统一成一种语言。

If they hesitate, ask follow-ups: who's the primary reader, what's the user themselves more comfortable reading, is there an English-speaking audience for the deployed site. Don't default — make them pick.

Pass the choice to `init`:

```bash
video-to-notebook init --language zh    # or --language en
```

This sets `build_meta.language` in SQLite. The synthesize and explain envelopes will carry this value in their `language` field, telling you what language to write the HTML fragment in.

### When source and target language differ

If the chapter's source_chunks (or a concept page's occurrences) include text in a language different from the target — e.g. a zh textbook synthesizing from an English lecture, or vice versa — the rule is:

- **Body text**: target language, always. Never mix languages within a chapter's prose.
- **Inline lecturer quotes**: translate to the target language. Cite the original course slug so attribution is preserved. Do **not** ship verbatim English quotes inside a `<blockquote>` in a zh chapter (or vice versa) — that mid-stream language switch breaks reader flow.
- **Code snippets, formulas, technical terms**: pass through verbatim. `LayerNorm`, `softmax`, `Q · K^T` stay the same in any language.
- **Lecturer names, course titles, concept slugs**: pass through verbatim (`Stanford CS336`, `multi-head-latent-attention`, `Vizuara`).
- **Footnote / parenthetical with the original**: optional, for high-fidelity passages where the lecturer's exact wording matters. Use sparingly — too many `<aside>` callouts in original-language break flow as much as untranslated quotes.

Concrete example for a zh chapter sourcing from an English DeepSeek lecture:

> ✅ 好：「Vizuara 老师在 *Build DeepSeek from Scratch* 里的原话翻译过来是：『MLA 不是缓存 K 和 V 本身，而是缓存它们的潜在压缩表示。』」
>
> ❌ 不要：「The lecturer said: 'MLA doesn't cache K and V themselves, but caches their latent compressed representation.'」 —— 在 zh 章节里突然插一段英文 blockquote。

Same rule mirrored for en chapters sourcing from Chinese B 站 lectures: translate the lecturer's words to English, attribute the course.

### Why this matters

The source-fidelity Principle 0 still applies — your obligation is to **faithfully transmit how the lecturer taught it**. Translation is a faithfulness operation, not a fabrication operation, as long as: (a) the meaning is preserved, (b) the source course is attributed, and (c) you're not inventing new pedagogy that the lecturer never said. If a passage feels lossy when translated, find a different passage that survives translation better, rather than dropping back into the source language mid-paragraph.

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
# YouTube — no auth needed
video-to-notebook crawl "<url>" --name "<slug>"

# Bilibili — see "Bilibili cookies playbook" below; always requires cookies
video-to-notebook crawl "<url>" --name "<slug>" --cookies-from chrome
```

Use `--name` to give a human-readable slug (e.g. `cs336`, `gpu-mode`). Without it the slug is derived from the URL's playlist/video ID, which is ugly.

Report counts after each crawl: `done: N ok, M no-subs, K errors`.

#### Bilibili cookies playbook (REQUIRED — Bilibili always needs cookies)

Bilibili's anti-spider returns **HTTP 412** to every unauthenticated request, even for listing a public playlist. You CANNOT crawl Bilibili without a logged-in session. The playbook:

**Attempt 1: try `--cookies-from <browser>` first.** Works reliably on Linux. Works *sometimes* on macOS Chrome. Failure modes you might see:

- `WARNING: find-generic-password failed` / `cannot decrypt v10 cookies: no key found` — macOS Keychain blocks yt-dlp from decrypting Chrome v10 cookies.
- `HTTP Error 412: Precondition Failed` followed by `ERROR: expected string or bytes-like object, got 'bool'` — extractor crashes when cookies are present but invalid/expired, OR when no cookies were extracted at all.

If you see any of those, **STOP and switch to Attempt 2**. Don't keep retrying — the failure is deterministic.

**Attempt 2: ask the user to export cookies.txt manually.** This is the reliable path. Give the user EXACTLY these steps:

> Bilibili 必须要 cookies 才能爬。`--cookies-from <browser>` 在你这台 macOS 上跑不通（Keychain 解密被系统挡了），改用手动导出的 cookies 文件：
>
> 1. **装浏览器扩展** "Get cookies.txt LOCALLY"（Chrome / Edge / Firefox 商店都有，搜这个名字第一个就是）
> 2. **打开 `https://www.bilibili.com`** 任意一个页面，确认右上角是登录态（看得到你的头像）
> 3. **点击扩展图标** → 选 "Export" → 默认是 "Current Site" → 下载得到一个 `bilibili.com_cookies.txt`
> 4. **保存到一个非 TCC 路径**。**重要：不要放在 `~/Downloads/`、`~/Desktop/`、`~/Documents/` 根目录** —— macOS 的 TCC 沙箱会让 yt-dlp 读不到这些文件夹的内容。建议放：
>    - `~/note/bilibili-cookies.txt` ✅
>    - `~/code/.secrets/bilibili-cookies.txt` ✅
>    - `~/Documents/cookies/bilibili.txt` ✅（`Documents/` 的**子文件夹**就行，根目录不行）
>    - `~/Downloads/bilibili.txt` ❌ TCC 会挡
> 5. **告诉我文件的绝对路径**，比如 `/Users/you/note/bilibili-cookies.txt`

Then run the crawl with `--cookies-file`:

```bash
video-to-notebook crawl "<bilibili-url>" --name "<slug>" \
  --cookies-file "<absolute-path>"
```

**Sanity checks before running**:
- The cookies.txt must be in **Netscape format** (the extension exports this by default).
- The file must contain a `SESSDATA` line and a `buvid3` line. If neither is present, the user isn't logged in or exported the wrong site.
- If the cookies.txt is older than ~30 days, it's likely expired — ask the user to re-export.

**When the crawl still fails after Attempt 2**:
- `HTTP 412` again → cookies expired. Re-export.
- `Failed to read cookies file` → likely TCC permission. Move the file to one of the suggested paths above.
- `No video formats found` on a specific BV → that video is region-locked or DRM'd. Continue with the rest, report which one failed.

**Whisper for videos without subtitles**: Bilibili often doesn't have official subtitles. Add `--whisper` to fall back to local transcription (mlx-whisper on Apple Silicon, faster-whisper elsewhere):

```bash
video-to-notebook crawl "<bilibili-url>" --name "<slug>" \
  --cookies-file "<path>" --whisper
```

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

## In-session mode (Claude Max users — no API key)

If the user has Claude Max (or any Claude Code subscription), they should NOT need a separate Anthropic API key. The tag and cluster commands each support a two-step pattern: emit work to JSON, decide in this conversation, apply back.

### When to recommend this mode

After Step 2 (crawl), check chunk count:

```bash
sqlite3 .video-to-notebook/db.sqlite "SELECT COUNT(*) FROM chunks"
```

| Chunk count | Mode |
|-------------|------|
| **< 200** | **In-session** (no API key, free via subscription) |
| 200–1000 | Either; in-session is slower but free |
| > 1000 | **API mode** — too slow to batch through conversation |

If the user explicitly says "I have Max" or "no API key", default to in-session regardless of size.

### In-session tag loop

```bash
video-to-notebook tag --ontology <ont.yaml> --limit 20
```

The CLI writes `.video-to-notebook/prompts/tag.json` and prints a 3-line stderr hint. Read that file:

```json
{
  "schema_version": "1",
  "kind": "tag_prompts",
  "ontology_slugs": ["self-attention", "..."],
  "chunks": [{"chunk_id": 1, "text": "..."}]
}
```

For each chunk, decide tags (your own reasoning) and write `.video-to-notebook/prompts/tag.decisions.json`:

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
video-to-notebook tag --ontology <ont.yaml> --apply
```

Repeat until re-running `tag` produces an envelope with an empty `chunks` array.

### In-session cluster

```bash
video-to-notebook cluster --ontology <ont.yaml>
```

The CLI writes `.video-to-notebook/prompts/cluster.json`. Read it. For each cluster, decide merge / create / reject / ambiguous.

Construct the decisions file at `.video-to-notebook/prompts/cluster.decisions.json` (single file with BOTH envelopes):

```json
{
  "_prompts_envelope": { ... full content of prompts/cluster.json ... },
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
video-to-notebook cluster --ontology <ont.yaml> --apply
```

## Textbook generation (v1.2+, Plan 6)

After tag + cluster complete, you can synthesize the corpus into a beginner-friendly textbook. This is the "pivot mode" — instead of indexing concepts, you produce a multi-chapter HTML reader for someone learning the topic from scratch.

### Step T1: Design the curriculum

```bash
video-to-notebook curriculum
```

The CLI writes `.video-to-notebook/prompts/curriculum.json` — every concept that has chunks + sample chunks per concept. Decide a beginner-pedagogical chapter order. Write `.video-to-notebook/prompts/curriculum.decisions.json`:

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
video-to-notebook curriculum --apply
```

### Step T1.5: Ask the user which synthesis mode (DEFAULT — do this every time)

After the curriculum is applied and BEFORE you call `synthesize` on any chapter, you MUST ask the user which workflow they want. Each chapter is ~5,000–8,000 字 of careful, source-grounded writing, so batch mode commits the user to a long unattended run; chapter-by-chapter lets them course-correct after seeing the first one. Both are valid — let them choose.

Use `AskUserQuestion` with a 2-option single-select. Suggested phrasing:

```
Question: 这门课怎么生成？
- 整本批量做 (推荐用于已经熟悉风格的复跑) — 我会按章节顺序连续 synthesize 所有 N 章，每章 5–8K 字 + PyTorch 骨架 + 多比喻。中间不停。预计 X 小时。
- 一章一章来 (推荐第一次跑或换了课程主题) — 我先做第 1 章给你看，确认深度 / 排版 / 比喻取舍后再继续下一章。每章之间你可以反馈。
```

When the user picks **batch mode**: loop through chapters 1..N, run `synthesize --chapter N` (which writes the prompts envelope), produce HTML, then `--apply` for each; `build` once at the end. Don't pause between chapters unless an error blocks you.

When the user picks **chapter-by-chapter**: do chapter 1 only, then `build` immediately so they can open the page in browser, then explicitly hand control back ("第 1 章已上线 http://localhost:4321/textbook/1/ — 看完告诉我继续还是改方向"). Wait for their go-ahead before chapter 2.

Either mode follows the same per-chapter style guide (Principle 1 — textbook-note depth, etc.) — the choice is only about pacing, not quality bar.

The same choice applies to `video-to-notebook explain` (concept pages) — ask the same batch-vs-one-at-a-time question before kicking off concept synthesis. Typical pattern: do the textbook in chapter-by-chapter mode for the first 2–3 chapters until the user signs off on the style, then offer to flip to batch mode for the rest.

### Step T2: Synthesize each chapter (one at a time)

For each chapter N:

```bash
video-to-notebook synthesize --chapter N
```

The CLI writes `.video-to-notebook/prompts/synthesize/chapter-N.json`. Read it — chapter spec + all source chunks for the chapter's primary + related concepts + style guide. Following the style guide:
- **Textbook-note depth (target 5,000–8,000 中文字 per chapter)** — the chapter should read like a graduate student's Obsidian study notes after watching the lecture, NOT a magazine summary. Concrete checklist: (1) TL;DR callout block at the top with the central formula + a hook; (2) 8–14 top-level sections using 一二三四 …; (3) step-by-step derivations with `<div class="deriv-step">` blocks containing `**Why**:` annotations for every non-trivial algebra move (reader follows with a pencil); (4) preserve ALL distinctive lecturer analogies — if the lecturer gave 4 metaphors for the same concept, keep all 4; (5) 3–5 callout boxes inline (`callout-info / callout-note / callout-warning / callout-tip / callout-quote`) for tone differentiation; (6) engineering details (numerical stability, training gotchas) embedded as callouts at the point they become relevant, not as appendices; (7) complete, runnable PyTorch skeleton (not pseudo-code) when the chapter introduces a model; (8) 5–7 takeaways at the end, each anchored to a specific lecturer-given example. Under 4,000 字 = under-developed. Over 10,000 字 = bloated.
- **Source fidelity first** — extract the lecturer's metaphors, worked examples, named citations, and verbatim phrasings from the chunks BEFORE drafting. The chapter's job is to faithfully transmit how the lecturer actually taught it; your own framing is layered on top with explicit flags (e.g. "教材外补充：…"). If two courses give different metaphors, present both labelled. Failure mode: writing a generic textbook paraphrase a reader of the lectures wouldn't recognise.
- **🛑 No fabrication — debug the pipeline instead** — if the source_chunks don't actually contain pedagogy on the chapter's primary concept (e.g. all 20 chunks are course logistics, or one alphabetically-early course dominates while another course has the real coverage), **STOP and fix the pipeline**, do NOT paper over the gap with LLM-generated content. Common bugs to check: synthesize SQL `LIMIT 20 ORDER BY course_slug` causes the alphabetically-first course to monopolise; tagging may have matched by lecture-title keyword without the concept actually being discussed; `--max-source-chunks` may be too low. Diagnose first: `sqlite3 .video-to-notebook/db.sqlite "SELECT courses.slug, COUNT(*) FROM chunk_concepts cc JOIN chunks ON chunks.id=cc.chunk_id JOIN lectures ON lectures.id=chunks.lecture_id JOIN courses ON courses.id=lectures.course_id JOIN concepts ON concepts.id=cc.concept_id WHERE concepts.slug='<primary>' GROUP BY courses.slug"`. If the DB has chunks but envelope is thin, the bug is in synthesize SQL; if the DB is empty, the bug is in tag.
- **Output is monolingual in `envelope["language"]`** — even when source_chunks span multiple languages (e.g. some chunks are English from Stanford CS336 and some are Chinese from a B 站 course). The chapter's prose, section headings, callouts, and lecturer quotes are ALL in the target language; you translate cross-language lecturer phrasings to the target language and attribute the source course. See **"Core principle: ONE output language"** earlier in this skill for the full rule. Never ship a mid-paragraph language switch into a `<blockquote>`.
- Anti-bias opening (prefer misconceptions the lecturer themselves called out)
- Inline SVG diagrams + CSS animations
- One embedded source clip with `?start=N` timestamp — pick the clip that best shows the lecturer's signature framing of this concept
- LaTeX math via `$...$` / `$$...$$` — reproduce the lecturer's derivation, not the cleaned-up textbook version
- End with `<div class="takeaways">` (3 bullets)

The same source-fidelity principle applies to `video-to-notebook explain` (concept pages): extract the lecturer's analogies from `occurrences` first, layer your additions on top. And the same monolingual-output rule applies: cross-language occurrences get translated into the target language with course attribution — concept pages don't mix languages either.

Write the HTML fragment to `/tmp/cm-chN.html` (just `<article>...</article>` body content; no `<html><head><body>` wrapper).

Apply:

```bash
cat > .video-to-notebook/prompts/synthesize/chapter-N.decisions.json <<EOF
{
  "schema_version": "1",
  "kind": "synthesize_results",
  "synthesizer": "claude-code-max:v1",
  "chapter_order_idx": N,
  "html_fragment_path": "/tmp/cm-chN.html"
}
EOF
video-to-notebook synthesize --chapter N --apply
```

### Step T3: Build & view

```bash
video-to-notebook build
video-to-notebook serve     # http://localhost:4321/textbook/
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
sqlite3 .video-to-notebook/db.sqlite "SELECT COUNT(*) FROM chunks WHERE NOT EXISTS (SELECT 1 FROM chunk_concepts WHERE chunk_concepts.chunk_id = chunks.id)"
```

At ~$0.0008/chunk (Claude Haiku with prompt caching), 1000 untagged chunks ≈ $0.80.

## Anti-patterns

- **Don't tag the same project twice without `--limit`** — the second run will skip tagged chunks but still iterate the whole DB. Use `--course <slug>` to scope.
- **Don't rebuild ontology mid-pipeline without thought** — if you change the seed YAML between `tag` and `cluster`, proposed tags may not cluster well.
- **Don't deploy a demo without a `.gitignore` that excludes `.video-to-notebook/db.sqlite`** — the DB has raw transcripts which may be large or include problematic content.
