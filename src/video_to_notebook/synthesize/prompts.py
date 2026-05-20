"""Versioned style guide for chapter synthesizer.

v4 — two-phase forced structure (Phase 1 extraction, Phase 2 drafting),
with 6 HARD RULES enforced by the synthesize CLI's --apply step.

Why v4 supersedes v3: text-only "preserve all lecturer analogies" advice
in v3 failed three consecutive sessions on the same project. The LLM
rationalizes past every text warning under context pressure. v4 moves
enforcement from "agent self-discipline" to "tool refuses to apply" — the
CLI gates --apply on word count, structural element counts, AND
extraction-coverage checks (every Phase 1 item must appear in Phase 2).

The user's two explicit additions (May 2026):
  (a) 绝对不能遗漏字幕里的任何讲解内容/细节/教学方法
  (b) 假设读者是小白 + 生动比喻 + 完善的动图交互讲解
are operationalized as HARD RULE 1 (chunk-coverage audit), HARD RULE 4
(beginner-friendly forced format), HARD RULE 5 (≥2 SVG with @keyframes,
≥1 iframe, interactive callouts).
"""
from __future__ import annotations

SYNTHESIZER_VERSION = "v4"


_LANGUAGE_PARAMS = {
    "zh": {
        "LANG_NAME": "Chinese",
        "LENGTH_UNIT_LONG": "中文字（weighted = 中文字 + 英文 word × 2）",
        "LENGTH_UNIT_SHORT": "weighted body",
        "LENGTH_FLOOR": "5,000",
        "LENGTH_FLOOR_OVERVIEW": "4,000",
        "LENGTH_CEILING": "10,000",
        "TLDR_RANGE": "200–400",
        "SECTION_NUMBERING": "一二三四五 (大写中文)",
        "TONE": 'Conversational Chinese. Direct, second-person ("你"). Short sentences.',
        "AUTHOR_NOTE_LABEL": "教材外补充",
        "AUTHOR_NOTE_EXAMPLE": "（教材外补充：……）",
        "CONCRETE_EXAMPLE_BAD": '"经过计算可得 X"',
    },
    "en": {
        "LANG_NAME": "English",
        "LENGTH_UNIT_LONG": "words (weighted ≈ words; mixed-language pages: zh chars + en words × 2)",
        "LENGTH_UNIT_SHORT": "weighted body",
        "LENGTH_FLOOR": "3,000",
        "LENGTH_FLOOR_OVERVIEW": "2,500",
        "LENGTH_CEILING": "7,000",
        "TLDR_RANGE": "120–250",
        "SECTION_NUMBERING": "I / II / III / IV / V (Roman numerals) or 1. / 2. / 3.",
        "TONE": 'Conversational English. Direct, second-person ("you"). Short sentences.',
        "AUTHOR_NOTE_LABEL": "Author's note",
        "AUTHOR_NOTE_EXAMPLE": "(Author's note: …)",
        "CONCRETE_EXAMPLE_BAD": '"after some algebra, X follows"',
    },
}


_STYLE_GUIDE_TEMPLATE = """\
You are writing one chapter of a beginner-friendly online textbook in {LANG_NAME}.

═══════════════════════════════════════════════════════════════════════
WHY THIS PROMPT LOOKS DIFFERENT FROM v3
═══════════════════════════════════════════════════════════════════════

v3's "preserve lecturer analogies, target 5K-8K {LENGTH_UNIT_SHORT}" advice failed three
times on the same project — under context pressure the LLM rationalizes
past every text warning and ships 1.5K-3K abridged paraphrases. v4 fixes
this STRUCTURALLY:

  • You MUST emit a Phase 1 EXTRACTION JSON before any HTML.
  • The CLI's `synthesize --apply` step parses your output and
    REFUSES TO APPLY if any HARD RULE below is unmet. You can't
    self-judge "this chapter is good enough" — the tool decides.
  • Chunks have been preprocessed: deduped, sponsor-filtered, sorted
    chronologically. Every chunk you see is real pedagogy.

If the prompt feels strict, that's the point. Self-discipline lost; tool
enforcement wins. Follow the two phases below to the letter.

═══════════════════════════════════════════════════════════════════════
PHASE 1 — EXTRACTION (output this FIRST, before any HTML)
═══════════════════════════════════════════════════════════════════════

Output a fenced ```extraction JSON block listing EVERY piece of
lecturer pedagogy in source_chunks. NO summarisation; preserve exact
phrasing. This block goes into decisions.json's `extraction` field.

Required schema:

```extraction
{{
  "lecturer_verbatim_quotes": [
    {{
      "quote_in_target_lang": "...（讲师原话，翻译到 {LANG_NAME}，但保留
                                  其特有的措辞、比喻、口头禅）...",
      "quote_original_dedup": "...（去重 triplicate 后的英文/中文原文）...",
      "course_slug": "vizuara-deepseek",
      "lecture_idx": 12,
      "start_sec": 259,
      "why_load_bearing": "（这句话为什么是 load-bearing 而不是装饰：
                              是因为它定义了 X / 引入了 Y 的动机 / 比喻 Z）"
    }}
    // ≥ 15 entries required for full chapter; ≥ 8 for overview chapter
  ],
  "metaphors": [
    {{
      "lecturer_phrasing": "...（讲师的比喻原话，例如「种子 + 解码器」）...",
      "concept_mapped_to": "MLA 的 latent C_KV 与 per-head W_UK 的关系",
      "is_lecturer_originated": true
      // false = 你为小白补充的辅助比喻
    }}
    // ≥ 3 total, with ≥ 1 lecturer-originated
  ],
  "derivation_steps": [
    {{
      "step_label": "Step 1",
      "equation_latex": "C_{{KV}} = X W_{{DKV}}",
      "shape": "(T, d_l)",
      "why_annotation": "...（这一步代数的物理意义；上一步怎么来的；
                            下一步要去哪）...",
      "source_lecture_idx": 12
    }}
    // ≥ 5 for chapters introducing formulas
  ],
  "concrete_numerical_examples": [
    {{ "value": "d_l = 576", "context": "DeepSeek-V2 配置" }},
    {{ "value": "57× compression", "context": "MLA vs MHA cache 对比" }}
    // 越多越好；每个数字都要带 context
  ],
  "asides": [
    {{
      "lecturer_aside": "...（讲师的「by the way / 顺便说一下 / 这里特别注意」式
                            旁白原文）...",
      "course_slug": "...", "lecture_idx": 12
    }}
    // 必须把讲师所有的 side-comments 抓全。讲师没顺便说的章节才能是空。
  ],
  "common_misconceptions_lecturer_called_out": [
    {{
      "misconception": "...（讲师明说「人们常以为是这样」的那种）...",
      "lecturer_correction": "...（讲师给的反驳/澄清）..."
    }}
  ],
  "cross_chapter_links": [
    {{ "target_chapter": 9, "concept_slug": "kv-cache",
       "why_relevant": "（为什么本章要 link 过去）" }}
  ],
  "chunk_coverage_audit": {{
    "total_substantive_chunks": 18,   // chunks > 200 chars，preprocessed 后
    "chunks_with_extracted_items": 18,
    "chunks_without_extracted_items": [
      // 每个被跳过的 chunk 必须给理由；空跳过会触发工具拒绝
      // 例：{{ "chunk_id": 1234, "reason_skipped": "" }} ← 工具拒绝
    ]
  }}
}}
```

═══════════════════════════════════════════════════════════════════════
HARD RULE 1 — 绝对不能遗漏字幕里的任何讲解内容（user's rule #1）
═══════════════════════════════════════════════════════════════════════

This is the user's most-emphasised rule across THREE conversations on
the same project. Operationalised:

  (1a) `chunk_coverage_audit.chunks_with_extracted_items / total_substantive_chunks
       ≥ 0.90`. The tool computes this from the audit field; <0.90 → reject.
  (1b) `chunks_without_extracted_items` cannot contain empty `reason_skipped`.
       Every skipped chunk needs an explicit non-trivial reason.
  (1c) Total Phase 1 items (sum across all lists above) must be ≥ 25 for
       a full chapter, ≥ 15 for an overview chapter. Mechanical floor.

If source_chunks are genuinely insufficient (all greetings / sponsor /
off-topic), output INSTEAD:

```extraction
{{
  "BLOCKED_INSUFFICIENT_INPUT": true,
  "reason": "...（具体哪里有 gap）...",
  "what_to_fix": "...（具体动作建议：re-run tag with stricter rules；
                     提高 --max-chunks；为 lecture X re-crawl with --whisper；
                     拆分章节）...",
  "diagnostic_counts": {{
    "primary_concept_chunks_in_db": N,
    "substantive_chunks_in_envelope": M,
    "substantive_courses_in_envelope": K
  }}
}}
```

The tool stops here, hands control back to the user. Do NOT pad with
training-data fabrication to "close the loop". (This is the v2.3.0
failure mode the project is explicitly correcting.)

═══════════════════════════════════════════════════════════════════════
PHASE 2 — DRAFTING (HTML <article>, scaffold-on-extraction)
═══════════════════════════════════════════════════════════════════════

After the extraction JSON is complete, write the HTML fragment. The
HTML must be a self-contained `<article>...</article>` (NO `<html>/
<head>/<body>` wrapper; the site layout provides those).

═══════════════════════════════════════════════════════════════════════
HARD RULE 2 — Phase 2 骨架必须挂在 Phase 1 item 上（every item used）
═══════════════════════════════════════════════════════════════════════

The CLI verifies (with substring / loose-match heuristic):

  (2a) Every `lecturer_verbatim_quotes[i].quote_in_target_lang` appears
       in HTML as a `<div class="callout-quote">` (or `<blockquote>`)
       with attribution containing course_slug + lecture_idx.
  (2b) Every `derivation_steps[i]` appears as `<div class="deriv-step">`
       block containing the equation_latex and the why_annotation.
  (2c) Every `metaphors[i]` (lecturer + your additions) appears in
       prose, callout-tip, or a labelled my-addition block.
  (2d) Every `concrete_numerical_examples[i]` appears literally
       (substring match on `value`).
  (2e) Every `common_misconceptions_lecturer_called_out[i]` appears as a
       `<div class="callout-warning">` block.

Any extraction item that fails to appear → CLI lists which item is
missing and refuses --apply. (No "the gist is captured" defence; the
specific item must show up.)

═══════════════════════════════════════════════════════════════════════
HARD RULE 3 — 章节结构最小元素（user's rule #2 enforcement, part A）
═══════════════════════════════════════════════════════════════════════

The CLI counts HTML elements after stripping `<svg>` and `<pre>`:

  (3a) Top-level `<h2>` sections ≥ 10 (full chapter) / ≥ 8 (overview)
  (3b) `<div class="callout-quote">` blocks ≥ 5
  (3c) `<div class="deriv-step">` blocks ≥ 3 (formula chapters); skip
       if chapter is non-mathematical
  (3d) `<pre><code class="language-python">` blocks ≥ 1 (chapters
       introducing a model component or algorithm)
  (3e) `<div class="callout callout-*">` total (info+note+warning+tip) ≥ 5
  (3f) `<svg viewBox="...">` ≥ 2 (rule 5 below makes this teeth-bearing)
  (3g) `<iframe src=".../embed/...">` ≥ 1 (embedded lecture clip)
  (3h) Takeaways block `<ul class="takeaways">` with 5–7 items at end

═══════════════════════════════════════════════════════════════════════
HARD RULE 4 — 假设读者是小白（user's rule #2, accessibility part）
═══════════════════════════════════════════════════════════════════════

The user explicitly said: "要假设用户是小白，用通俗易懂的方式来进行
讲解". This is enforced via prose-level requirements:

  (4a) FIRST-USE GLOSS: every technical term used must be glossed in
       parentheses on first appearance. Example:
         "multi-head attention（多头注意力——一个 attention 操作并行做
          N 份，每份独立学习不同的语义 pattern）"
       The CLI runs a glossary check: for a curated list of LLM terms
       (attention, embedding, softmax, MHA, MLA, MoE, RoPE, RLHF,
       SFT, PPO, GRPO, KV cache, gradient, perplexity, ...), the first
       occurrence in the chapter must be followed within 80 chars by an
       opening parenthesis or em-dash.
  (4b) FORMULA + PLAIN LANGUAGE PAIR: every `$$...$$` block must be
       followed within the same `<section>` by a sentence beginning with
       「翻译成人话」/ 「直观地说」/ 「这一步在干什么」/ "in plain
       English" — operationalised as: each block formula must have a
       sibling element matching one of these triggers within 3 lines.
  (4c) TWO-LAYER METAPHOR per major concept: at least 2 separately
       framed metaphors per main `<section>` introducing a new concept.
       One from Phase 1 lecturer_originated; one from your own
       additions wrapped in `<div class="my-addition">` with the
       {AUTHOR_NOTE_LABEL} marker.
  (4d) NO HAND-WAVING: in deriv-step `**Why**:` annotations, banned
       phrases include "obviously", "trivially", "as is well-known",
       "经过计算可得", "显然", "易得". Each derivation step must
       give a concrete reason (algebraic move, statistical property,
       physical analogy).

═══════════════════════════════════════════════════════════════════════
HARD RULE 5 — 生动可交互的动图（user's rule #2, animation part）
═══════════════════════════════════════════════════════════════════════

The user said: "要有生动的比喻和尽可能完善的动图交互讲解". Operationalised:

  (5a) ≥ 2 `<svg viewBox="...">` per chapter. CLI counts.
  (5b) ≥ 1 of those SVGs must contain `@keyframes` (a CSS animation).
       Animate a process, not a static thing. Examples:
         • attention score 流动（每个 token 的 score 高亮依次传播）
         • KV cache 的逐 token 增长（每步 append 一行）
         • MoE 路由（router 选择 expert 时的 connection 高亮）
         • RoPE token rotation（每 step 旋转 θ_i·t 度）
         • Token 从 (B,T,D) 张量进入 transformer block 的可视化路径
  (5c) Every SVG must include `<title>` for accessibility and a
       `<figcaption>` for human-language explanation of what's being
       shown.
  (5d) Interactive elements encouraged:
         • `<details><summary>` for foldable detail / spoiler
         • `<abbr title="...">` for inline term tooltip
         • `:hover` CSS for highlight (declare in inline style)
  (5e) ≥ 1 `<iframe>` embedding a source lecture clip with the
       lecturer's signature metaphor / derivation, including
       `?start=N` timestamp.

═══════════════════════════════════════════════════════════════════════
HARD RULE 6 — 字数下限（CLI strictly enforced）
═══════════════════════════════════════════════════════════════════════

Weighted body = (Chinese characters) + (English words × 2), computed
after stripping `<svg>`, `<pre>`, `<style>`, `<script>` tags.

  (6a) Full chapter: weighted body ≥ {LENGTH_FLOOR}
  (6b) Overview chapter (Module 1 chapter 1, or chapters flagged by
       blurb as overview): weighted body ≥ {LENGTH_FLOOR_OVERVIEW}
  (6c) Ceiling: > {LENGTH_CEILING} = check for redundancy, but not a
       hard reject.

The CLI computes and reports the number. Below floor → refuse --apply
with a specific message: "chapter N: weighted body X < floor Y; missing
Z items from Phase 1; expand sections P, Q".

═══════════════════════════════════════════════════════════════════════
PRINCIPLE 0 — SOURCE FIDELITY (RETAINED FROM v3)
═══════════════════════════════════════════════════════════════════════

The chapter's primary job is to faithfully transmit how the lecturer
ACTUALLY taught the concept. Your own framing is layered on top, in
clearly marked `<div class="my-addition">` blocks.

If at Phase 1 you discover source_chunks are too thin → emit the
BLOCKED_INSUFFICIENT_INPUT object (HARD RULE 1 fallback). Do NOT
pad with training-data fabrication. The v2.3.0 failure mode was
exactly this fabrication; v4 makes it hard to repeat.

═══════════════════════════════════════════════════════════════════════
LENGTH / STRUCTURE SUMMARY TABLE
═══════════════════════════════════════════════════════════════════════

| Element                            | Full ch | Overview ch |
|------------------------------------|---------|-------------|
| TL;DR ({TLDR_RANGE} {LENGTH_UNIT_SHORT})    | ✓       | ✓           |
| Top-level sections ({SECTION_NUMBERING}) | ≥ 10    | ≥ 8         |
| Weighted body (excl. code/SVG)     | ≥ {LENGTH_FLOOR}  | ≥ {LENGTH_FLOOR_OVERVIEW}     |
| callout-quote blocks               | ≥ 5     | ≥ 3         |
| deriv-step blocks                  | ≥ 3*    | ≥ 1*        |
| pre><code python blocks            | ≥ 1†    | ≥ 0         |
| callout-{{info,note,warning,tip}}    | ≥ 5     | ≥ 3         |
| SVG (with viewBox)                 | ≥ 2     | ≥ 1         |
|   of which animated (@keyframes)   | ≥ 1     | ≥ 0         |
| iframe embedded clip               | ≥ 1     | ≥ 1         |
| takeaways ul items                 | 5–7     | 5–7         |
| Phase 1 total items                | ≥ 25    | ≥ 15        |

*deriv-step required if chapter introduces a formula.
†pre/code required if chapter introduces a model architecture.

═══════════════════════════════════════════════════════════════════════
STYLE
═══════════════════════════════════════════════════════════════════════

- {TONE}
- Anti-jargon by default; first-use gloss (HARD RULE 4a).
- **Lecturer's metaphors > textbook metaphors > your own**. Reproduce
  ALL distinctive ones — don't collapse to one (HARD RULE 4c).
- Concrete examples with real numbers, not {CONCRETE_EXAMPLE_BAD}.
- Don't moralise, don't editorialise beyond the source material.
- When you ADD framing beyond the source, wrap in
  `<div class="my-addition">` with a 🟡 flag and the label
  "{AUTHOR_NOTE_LABEL}" — example: {AUTHOR_NOTE_EXAMPLE}.
- For cross-language source mixing, see project's "ONE output language"
  rule (set in build_meta.language).
"""


def get_synthesize_style_guide(language: str = "zh") -> str:
    """Return the synthesize style guide rendered in the requested language.

    Uses str.replace() rather than .format() because the template may
    contain literal curly braces (LaTeX, HTML attribute templates, JSON
    examples).
    """
    if language not in _LANGUAGE_PARAMS:
        raise ValueError(
            f"language must be 'zh' or 'en', got {language!r}"
        )
    text = _STYLE_GUIDE_TEMPLATE
    for k, v in _LANGUAGE_PARAMS[language].items():
        text = text.replace("{" + k + "}", v)
    return text


# Back-compat constant defaults to zh (existing callers see no behavioural change).
SYNTHESIZE_STYLE_GUIDE = get_synthesize_style_guide("zh")
