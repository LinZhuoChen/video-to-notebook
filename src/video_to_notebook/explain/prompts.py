"""Versioned style guide for the concept explainer.

Supports zh + en via `get_explain_style_guide(language)`. The big
template uses {LANG_NAME} / {TONE_LANGUAGE} / {TONE_PRONOUN} /
{LENGTH_UNIT_PARENTHETICAL} / {BAD_METAPHOR_EXAMPLE} placeholders for
the language-specific bits — everything else (structural skeleton,
namespace rules, colour discipline) is language-agnostic.
"""
from __future__ import annotations

EXPLAINER_VERSION = "v4"


_LANG_PARAMS = {
    "zh": {
        "LANG_NAME": "Chinese",
        "TONE_LANGUAGE": "Chinese",
        "TONE_PRONOUN": '"你"',
        "LENGTH_UNIT_PARENTHETICAL": "字 (Chinese characters)",
        "BAD_METAPHOR_EXAMPLE": '你自己造一个 "DDPM 像炒菜" 的比喻，而源讲师没说过。',
        "GOOD_METAPHOR_EXAMPLE": '"Vizuara 把扩散过程比作「往汤里慢慢撒胡椒」（L7 @04:47）"\n         — 引用源讲师的实际用语。',
    },
    "en": {
        "LANG_NAME": "English",
        "TONE_LANGUAGE": "English",
        "TONE_PRONOUN": '"you"',
        "LENGTH_UNIT_PARENTHETICAL": "words",
        "BAD_METAPHOR_EXAMPLE": 'You invent your own "DDPM is like cooking" metaphor that no source lecturer used.',
        "GOOD_METAPHOR_EXAMPLE": '"Vizuara compares the diffusion process to «slowly sprinkling pepper into soup» (L7 @04:47)"\n         — quote the lecturer\'s actual phrasing.',
    },
}


_TEMPLATE = """\
You are writing one rich, illustrated entry of an online concept encyclopedia
that supports a beginner-friendly {LANG_NAME} ML textbook.

══════════════════════════════════════════════════════════════════════
0. PRINCIPLE — SOURCE FIDELITY FIRST (read before drafting)
══════════════════════════════════════════════════════════════════════

The concept page's primary job is to faithfully transmit how the
lecturer ACTUALLY taught this concept in the `occurrences` envelope.
Your own framing comes SECOND, layered on top.

🛑 NO-FABRICATION RULE
If `occurrences` don't actually contain pedagogy on this concept
(e.g. they're course logistics, off-topic asides, or chunks tagged
by alias-collision rather than real discussion), **STOP and report a
pipeline bug to the caller** — do NOT generate plausible-sounding
content from your own training-data knowledge to fill the gap.

Concrete failure signals that mean "stop and debug, don't write":
- All `occurrences` chunks are from one lecture's intro/admin section.
- The concept's name never appears in any chunk's text.
- One course dominates the occurrences while another course has
  obvious in-depth coverage (likely a chunk-selection or
  `--max-chunks` bug).

Diagnostic steps when source feels thin:
1) Re-tag with stricter alias matching.
2) Bump `--max-chunks` higher.
3) Check the DB: `SELECT COUNT(*) FROM chunk_concepts WHERE
   concept_id = ?` — if high but envelope is empty, it's a
   `collect_explain_prompts` SQL bug.
4) Only resume writing after `occurrences` actually contain the topic.

Before drafting:

1) READ every `occurrences` chunk. The YouTube auto-captions are noisy
   with triplicated lines — mentally dedupe but read all of them.

2) EXTRACT (in your reasoning, not the output):
   - **Metaphors / analogies** the lecturer used. Reuse the lecturer's
     concrete imagery, not generic substitutes you happen to know.
   - **Numbers, code, derivations** the lecturer demonstrated. Keep
     their exact choices (T values, β schedules, example dimensions).
   - **Misconceptions** the lecturer explicitly called out. These
     often become your anti-bias opener and your three pitfalls.
   - **Named citations** (Ho 2020, Karpathy tweet, Tweedie 1956,
     Yang Song, etc.) the lecturer mentioned. Keep them.
   - **Verbatim phrasings**: short distinctive turns the lecturer
     uses ("the magic trick", "simple loss", "this is the punchline").
     Preserve as quoted text where it fits.

3) DRAFT the page as: (a) the lecturer's own scaffolding, reorganised
   for reference use; (b) YOUR additions on top — cross-course
   comparison, modern follow-ups (LCM, SD3, etc.), corrections of
   outdated framings.

4) If two source courses give different metaphors, present BOTH and
   label them (e.g. "Vizuara 把它比作 X；CMU 把它比作 Y"). Don't blend
   into a generic average.

Failure mode to avoid: writing a Wikipedia-style entry that paraphrases
what you (the LLM) already knew, ignoring the specific classroom voice
in `occurrences`. If a reader who watched the lectures can't recognise
the entry, you over-generalised.

══════════════════════════════════════════════════════════════════════
1. OUTPUT FORMAT (hard contract)
══════════════════════════════════════════════════════════════════════

- Emit a self-contained HTML fragment ONLY. No <html>/<head>/<body>.
- Root element MUST be `<article class="concept-entry">`.
- Audience: complete ML beginner reading in {LANG_NAME}, basic high-school math.
- Tone: precise, second-person ({TONE_PRONOUN}), short sentences. No editorialising
  ("是不是很优美!" / "其实超简单"), no rhetorical filler. Reference-grade
  prose — the reader landed here from search and wants the truth fast.
- Length budget for the whole fragment: 1800–3200 字 (excluding code/SVG).
  Stay inside the bound. Skim, don't sprawl. Concept pages are
  reference-style — shorter than chapters but still source-faithful.

- **Preserve ALL distinctive lecturer analogies the source gave for
  this concept**. If the lecturer used 3 different metaphors (e.g.
  "secret recipe", "古董旋钮机器", "潜水员潜入海底" for latent
  variables), reproduce all 3 — different mental models hit different
  readers. Don't collapse to one.

- **Engineering details embedded, not deferred**. If the concept has
  known training gotchas (`log σ²` for stability, `reduction='sum'`
  for KL weighting, cosine schedule offsets), put them inline as
  callout-style notes. Don't write "details deferred to later" — give
  them here.

- **Use `<div class="callout-quote">` for direct lecturer quotations**
  in the intuition section. Anchor them to the source (lecture # +
  timestamp from `occurrences`).

══════════════════════════════════════════════════════════════════════
2. NAMESPACE PREFIX (hard rule — prevents collisions when several
   explainer fragments are inlined on the same page, e.g. search results
   or a future /random surface)
══════════════════════════════════════════════════════════════════════

- Pick a 2-4 letter prefix derived from the concept slug. Examples:
    linear-algebra        → `la-`
    backpropagation       → `bp-`
    gradient-descent      → `gd-`
    convolutional-...     → `cn-`
    attention-mechanism   → `att-`
- EVERY class name and every `id` you introduce inside this fragment
  MUST start with this prefix (except the 8 "shared" class names listed
  in section 4, which the site's global stylesheet styles).
- Inside `<script>`, every `document.getElementById(...)` and every
  `document.querySelector(...)` MUST target a prefixed id/class.
- Declare your prefix as a comment on the first line of your `<style>`:
    `/* prefix: la- */`

══════════════════════════════════════════════════════════════════════
3. COLOR DISCIPLINE (hard rule — supports dark mode + per-module accent)
══════════════════════════════════════════════════════════════════════

Allowed colour tokens (use these and ONLY these in `style=` and `<style>`):
    var(--text)            主文字
    var(--text-muted)      次要文字 / 坐标轴
    var(--text-faint)      占位 / 极弱标签
    var(--surface)         卡片底色
    var(--surface-soft)    输入框 / readout 底色
    var(--border)          一般描边
    var(--border-strong)   强调描边
    var(--module-accent)         强调色（自动跟随章节模块色）
    var(--module-accent-soft)    强调色低饱和（卡片背景）
    var(--accent), var(--accent-soft)   后备主题色
    var(--red), var(--red-soft)         错误 / 误区强调
    var(--blue), var(--blue-soft)       次要叙事色（仅当三色对比需要时）

FORBIDDEN: hard-coded hex / rgb / hsl ANYWHERE — even inside `<svg>`.
A pure black/white (`#000` / `#fff`) is acceptable ONLY for marker arrowheads.

══════════════════════════════════════════════════════════════════════
4. STRUCTURAL SKELETON (hard order, fixed class names)
══════════════════════════════════════════════════════════════════════

Sections must appear in THIS order. Each is required unless marked
[optional]. Length budgets in {LENGTH_UNIT_PARENTHETICAL} — overruns get
truncated by the build pipeline.

A) <header class="concept-header">
     <span class="concept-eyebrow">概念</span>
     <h1>{canonical_name}</h1>
     <p class="concept-tagline">— 一句话本质 (≤30 字)</p>
   </header>

B) <aside class="concept-quickref">
     一行小卡片：定义 / 最常用公式 / 最易错点 — 这是搜索结果的摘要锚点。
     <div><strong>定义</strong> · ……</div>
     <div><strong>公式</strong> · $……$ （没有公式则写 "无公式"）</div>
     <div><strong>易错</strong> · ……</div>
   </aside>

C) <section class="concept-intuition">  [200–400 字]
     必须以「反偏见开场」开头：先说"很多人以为 X 是 Y，其实……"，
     再引入正式定义。最后一句必须把概念定位到机器学习的上下文里
     （"在训练里，这件事对应……"）。

D) <section class="concept-deepdive">  [300–600 字]
     主要图示 + 解释。包含 ≥1 个 inline <svg>，使用 viewBox。SVG 必须有
     `role="img"` 和 `aria-label="..."`。SVG 内的所有 stroke/fill 必须
     用 CSS 变量。viewBox 上限 600×400，确保 720px 列宽不横向滚动。

E) <section class="concept-interact">  [指令 ≤100 字]
     恰好一个交互组件。三选一（见 §5），不要混合，不要多个。组件前
     必须有一句话说明"注意看什么不变量"（one-invariant rule）。

F) <section class="concept-example">  [100–200 字，optional —— 仅当概念
   有公式/可手算时给出]
     给一个用小数字（≤10）的手算示例。必须给出等式链：
       $L = (\\hat y - y)^2 = (1.5 - 4)^2 = 6.25$
     不允许 "经过计算可得 X"。读者要能拿笔跟着算。

G) <section class="concept-pitfalls">  [恰好 3 条]
     <ol> 列表，每条 ≤80 字。每条必须包含一个具体反例（一个数字或一张
     图都行）。格式：「<strong>{误区标签}</strong>。{反例}」。

H) <section class="concept-seealso">  [2–4 条]
     交叉链接。<a> 的 slug 必须存在于输入 envelope 的 `related_concepts`
     字段。<strong>不允许编造 slug</strong>；envelope 不够就少写几条。

I) <section class="concept-sources">  [1–3 条，optional —— 仅当
   `occurrences` 非空时出现]
     每条一行 <a href="{video_url}&t={start_sec}s" target="_blank"
     rel="noopener">{course_slug} · L{lecture_idx} · {lecture_title} ·
     ({mm:ss})</a>。时间戳必须是真实的 occurrence start_sec。

══════════════════════════════════════════════════════════════════════
5. INTERACTIVE WIDGET — choose exactly ONE template
══════════════════════════════════════════════════════════════════════

Pick the template that fits the concept; don't combine them, don't invent
new patterns.

TEMPLATE A — CSS-keyframe SVG animation (no JS)
  Use when: the invariant is "看一个过程随时间展开"
  Example concepts: vector growing, gradient descending, dropout masking
  Skeleton:
    <style>
      @keyframes {prefix}-grow { 0% {...} 100% {...} }
      .{prefix}-arrow { animation: {prefix}-grow 1.2s ease-out forwards; }
    </style>
    <svg viewBox="0 0 ...">…</svg>

TEMPLATE B — Slider mutating SVG attributes (vanilla JS, 1 listener)
  Use when: the invariant is "改变一个连续参数，看输出怎么变"
  Example concepts: scalar multiplication, learning rate, temperature
  Skeleton:
    <input type="range" id="{prefix}-slider" min="..." max="..." step="..." value="...">
    <span id="{prefix}-readout">…</span>
    <svg>…<element id="{prefix}-shape" /></svg>
    <script>
      (function () {
        const s = document.getElementById('{prefix}-slider');
        const r = document.getElementById('{prefix}-readout');
        const shape = document.getElementById('{prefix}-shape');
        function render() { /* set shape attributes, update r.textContent */ }
        s.addEventListener('input', render);
        render();
      })();
    </script>

TEMPLATE C — Step-button bank (vanilla JS, toggle .active on lines)
  Use when: the invariant is "公式按顺序展开成一条等式链"
  Example concepts: backprop chain rule, EM algorithm, Bayes derivation
  Skeleton:
    <div class="{prefix}-controls">
      <button data-step="0" class="active">① …</button>
      <button data-step="1">② …</button>
      …
    </div>
    <div id="{prefix}-readout">
      <div class="{prefix}-line" data-line="0">…</div>
      <div class="{prefix}-line" data-line="1">…</div>
      …
    </div>
    <script>
      (function () {
        const btns = document.querySelectorAll('.{prefix}-controls button');
        const lines = document.querySelectorAll('#{prefix}-readout .{prefix}-line');
        function show(step) {
          btns.forEach(b => b.classList.toggle('active', +b.dataset.step === step));
          lines.forEach(l => l.classList.toggle('cd-active-line', +l.dataset.line === step));
        }
        btns.forEach(b => b.addEventListener('click', () => show(+b.dataset.step)));
        show(0);
      })();
    </script>

In all three templates:
- Wrap script in `(function () { ... })();` — no top-level state.
- Never query `document` without a namespace prefix in the selector.
- Don't import external libraries.

══════════════════════════════════════════════════════════════════════
6. PEDAGOGY (the rules that make this an explainer, not a glossary)
══════════════════════════════════════════════════════════════════════

- SOURCE-FIRST METAPHORS: if `occurrences` contains a metaphor or
  analogy the lecturer used (e.g. "noise is like…", "score is like…"),
  REUSE it. Don't substitute a more textbook-y analogy you happened
  to know. Cross-course conflict → present both, labelled by course.
  Bad:  {BAD_METAPHOR_EXAMPLE}
  Good: {GOOD_METAPHOR_EXAMPLE}

- ONE-INVARIANT RULE: every animation/interaction makes exactly ONE
  invariant visible. State it explicitly in prose BEFORE the widget.
  Bad:  "下面是一个互动演示。"
  Good: "拖动滑块时，注意箭头的方向不变，只有长度按 $k$ 倍缩放。"

- ANTI-BIAS OPENER: the intuition section must begin by naming the
  most common misunderstanding, then correcting it. Recalibrates the
  reader before any formal definition. PREFER misconceptions the
  lecturer themselves called out in `occurrences`.
  Bad:  "向量是一个有方向、有大小的量。"
  Good: "很多人以为向量就是带箭头的有向线段；其实箭头只是几何直觉，
         向量更本质的定义是……"

- EQUATION CHAIN: every formula must show the substitution chain, not
  just the result. The reader should be able to follow with a pencil.
  Bad:  "代入可得 $L = 6.25$。"
  Good: "$L = (\\hat y - y)^2 = (1.5 - 4)^2 = (-2.5)^2 = 6.25$。"

- COUNTER-EXAMPLE PITFALLS: each of the 3 pitfalls must include a
  specific numerical or visual counter-example. No vague warnings.
  Bad:  "不要把维度想成长度。"
  Good: "把维度想成长度。反例：$(1000, 0, 0)$ 是 3 维向量，不是 1000
        维——分量个数 ≠ 模长。"

- SEE-ALSO CONSTRAINT: every slug in concept-seealso MUST appear in the
  input envelope's `related_concepts` list. If `related_concepts` has
  only 1 entry, you write 1 see-also link. Don't invent slugs.

══════════════════════════════════════════════════════════════════════
7. MATH NOTATION
══════════════════════════════════════════════════════════════════════

- Inline math: `$...$`
- Block math:  `$$...$$`
- Renderer is KaTeX (auto-rendered client-side).
- Use `\\cdot` for multiplication, not `*`.
- Use `\\hat{y}` for predictions, `\\bar{x}` for means.
- Partial derivatives use `\\partial`, total derivatives use `d`.
- Vectors typeset with `\\vec{v}` or bold via `\\mathbf{v}`.

══════════════════════════════════════════════════════════════════════
8. ACCESSIBILITY MINIMUMS
══════════════════════════════════════════════════════════════════════

- All <svg> need `role="img"` + `aria-label="..."`.
- All slider/button widgets need <label> tied via `for` / nested.
- All external <a> need `target="_blank" rel="noopener"`.
- Keep text contrast inside the CSS-var palette (already AA-compliant
  in both light and dark mode — that's why hard-coded colors are
  forbidden).

══════════════════════════════════════════════════════════════════════
9. WHAT THE LLM RECEIVES IN THE ENVELOPE (for reference)
══════════════════════════════════════════════════════════════════════

The prompts envelope you'll be given contains:
  concept            { slug, canonical_name, description, aliases,
                       module_hint }
  occurrences        list of source-chunk dicts with video_url,
                     start_sec, lecture title — for §I (sources) and
                     for inspiration on the concept's pedagogical framing
  related_concepts   list of { slug, canonical_name, co_occurrence }
                     — the ONLY slugs you may link to in §H

Output an HTML fragment file path; the CLI's --apply-results stage
hashes it into the database and copies it into the Astro content tree.
"""


def get_explain_style_guide(language: str = "zh") -> str:
    """Return the explain style guide rendered in the requested language.

    Uses str.replace() rather than .format() because the template body
    contains many literal `{...}` braces (CSS / JS / HTML examples).
    """
    if language not in _LANG_PARAMS:
        raise ValueError(f"language must be 'zh' or 'en', got {language!r}")
    text = _TEMPLATE
    for k, v in _LANG_PARAMS[language].items():
        text = text.replace("{" + k + "}", v)
    return text


# Back-compat: existing callers see the same default-zh string.
EXPLAIN_STYLE_GUIDE = get_explain_style_guide("zh")
