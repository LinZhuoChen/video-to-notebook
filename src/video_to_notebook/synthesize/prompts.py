"""Versioned style guide for chapter synthesizer.

Supports both Chinese (default) and English output via `language` parameter.
The language-specific tokens (audience, length unit, section numbering,
tone, author-note label) are factored into `_LANGUAGE_PARAMS` and
substituted into a single shared template — so edits to pedagogy stay
in one place.
"""
from __future__ import annotations

SYNTHESIZER_VERSION = "v3"


_LANGUAGE_PARAMS = {
    "zh": {
        "LANG_NAME": "Chinese",
        "LENGTH_UNIT_LONG": "中文字",
        "LENGTH_UNIT_SHORT": "字",
        "LENGTH_RANGE": "5,000–8,000",
        "LENGTH_UNDER": "4,000",
        "LENGTH_OVER": "10,000",
        "TLDR_RANGE": "200–400",
        "SECTION_NUMBERING": "一二三四五 (大写中文)",
        "TONE": 'Conversational Chinese. Direct, second-person ("你"). Short sentences.',
        "AUTHOR_NOTE_LABEL": "教材外补充",
        "AUTHOR_NOTE_EXAMPLE": "（教材外补充：……）",
        "CONCRETE_EXAMPLE_BAD": '"经过计算可得 X"',
    },
    "en": {
        "LANG_NAME": "English",
        "LENGTH_UNIT_LONG": "words",
        "LENGTH_UNIT_SHORT": "words",
        "LENGTH_RANGE": "3,000–5,000",
        "LENGTH_UNDER": "2,500",
        "LENGTH_OVER": "7,000",
        "TLDR_RANGE": "120–250",
        "SECTION_NUMBERING": "I / II / III / IV / V (Roman numerals) or 1. / 2. / 3.",
        "TONE": 'Conversational English. Direct, second-person ("you"). Short sentences.',
        "AUTHOR_NOTE_LABEL": "Author's note",
        "AUTHOR_NOTE_EXAMPLE": "(Author's note: …)",
        "CONCRETE_EXAMPLE_BAD": '"after some algebra, X follows"',
    },
}


_STYLE_GUIDE_TEMPLATE = """\
You are writing one chapter of a beginner-friendly online textbook.

OUTPUT FORMAT: a self-contained HTML fragment (NO <html><head><body> wrapper —
just the body content starting with <article>). The fragment will be wrapped
in a site layout that already provides nav, search, footer, and global styles.

Audience: complete ML beginner reading in {LANG_NAME}. They have basic high-school
math. No prior coding experience required for this chapter's intuition.

══════════════════════════════════════════════════════════════════════
PRINCIPLE 0 — SOURCE FIDELITY FIRST (read before drafting)
══════════════════════════════════════════════════════════════════════

The chapter's primary job is to faithfully transmit how the lecturer
ACTUALLY taught the concept in the source_chunks. Your own framing comes
SECOND, layered on top.

🛑 NO-FABRICATION RULE
If the source_chunks don't actually contain pedagogy on the chapter's
primary concept (e.g. they're course logistics, admin chatter, off-topic
asides, or a different concept), **STOP and report a pipeline bug to the
caller** — do NOT paper over the gap by generating plausible-sounding
content from your own training-data knowledge.

Concrete failure signals that mean "stop and debug, don't write":
- All 20 source_chunks are from the same lecture about something else.
- Chunks are entirely course intro / TA introductions / homework rules.
- The chapter's primary concept is never named or shown in any chunk.
- One course dominates the chunk list while another course has hours
  of lecture on the exact topic (likely a chunk-selection bug:
  `LIMIT 20 ORDER BY course_slug` filling up from the alphabetically
  first course).

Diagnostic steps when source feels thin:
1) Count chunk_concepts in the DB for the primary slug — if it's high
   but the envelope is bad, it's a synthesize SQL bug.
2) Check `--max-source-chunks` and per-course caps.
3) Check that tagging actually picked up that concept in the right
   lectures (not just one course's intro lecture by title-keyword
   accident).
4) Re-run tag with stricter rules; re-cluster; re-collect prompts.

Only resume drafting AFTER the source feed is real.

Before drafting a single sentence:

1) READ every source_chunk in the envelope (the YouTube auto-captions
   are noisy with triplicated lines — mentally dedupe but read every chunk).

2) EXTRACT and explicitly list (in your scratch reasoning, not in output):
   - **Metaphors**: every analogy the lecturer used ("noise is like X",
     "score is like Y", "diffusion is like Z"). Use the lecturer's
     concrete imagery, not your generic substitutes.
   - **Worked examples**: any specific numbers, code snippets,
     whiteboard derivations the lecturer demonstrated. Keep their
     exact choice (e.g. if they used T=10 and β=0.1, use those).
   - **Pedagogical moves**: the order in which they introduced ideas;
     the specific misconceptions they called out; the side-comments
     ("by the way…", "an interesting note is…", "people often think…")
     that frame how the topic feels in practice.
   - **Named papers / authors / tweets / dates**: when the lecturer
     name-checks Ho 2020, a Karpathy tweet, Yang Song, Sohl-Dickstein,
     etc., that citation is part of the pedagogy — keep it.
   - **Verbatim phrasings**: short distinctive turns of phrase the
     lecturer uses repeatedly ("the simple loss", "this is the magic
     trick", etc.). Preserve them as quoted text.

3) Now DRAFT the chapter as: (a) the lecturer's own scaffolding,
   reorganised for written prose; (b) YOUR additions clearly layered
   on top — comparisons across multiple courses, modern context
   (post-publication developments), corrections of outdated framings.

4) If two source courses give different metaphors for the same concept,
   present BOTH and label them ("Vizuara frames it as X; CMU frames it
   as Y"). Don't blend into a generic average.

Failure mode to avoid: writing a textbook-shaped paraphrase of what
you (the LLM) already knew about the topic, ignoring the specific
classroom voice in the source. If a reader who watched the lectures
can't recognise the chapter, you over-generalised.

══════════════════════════════════════════════════════════════════════
PRINCIPLE 1 — TEXTBOOK-NOTE DEPTH (target: ~{LENGTH_RANGE} {LENGTH_UNIT_LONG} per chapter)
══════════════════════════════════════════════════════════════════════

The chapter should read like a graduate student's hand-written Obsidian
study notes after watching the lecture — *not* a magazine article
summary. Concrete depth checklist:

- **TL;DR block at the top** ({TLDR_RANGE} {LENGTH_UNIT_SHORT}): one paragraph plain-language
  intro + the chapter's central formula + a "why open with this concept"
  hook. Wrap it in a visually distinct callout box at the very start.

- **Long chapter, many sections**. Use {SECTION_NUMBERING} for top-
  level sections and 4.1 / 4.2 for sub-sections. Target 8–14 top-level
  sections per chapter, not 4–6. Each section is a self-contained mini-
  essay on one idea.

- **Show the derivation step-by-step**, not just the final formula. For
  every non-trivial equation, give a "Step N" block with the equation +
  a "**Why**: …" annotation explaining the algebra move. The reader
  should be able to follow with a pencil. Example structure:
    Step 3: Apply Jensen's inequality
      $\\log \\mathbb{E}[Y] \\geq \\mathbb{E}[\\log Y]$
      **Why**: log is concave, so "expectation of log" ≤ "log of expectation".
      **Cost**: turned equality into inequality — that's the gap we'll quantify.

- **Preserve ALL distinctive lecturer analogies**. If the lecturer gave
  4 different metaphors for the same concept (e.g. "hello machine",
  "knob hardware", "underwater diver", "Earth-to-Mars teleport"),
  reproduce ALL 4 — don't collapse to one. Different metaphors hit
  different mental models; the lecturer chose them for a reason.

- **Callout boxes for tone differentiation**. Use four colour-coded
  classes inline:
    • `<div class="callout callout-info">` — neutral background info
    • `<div class="callout callout-note">` — pedagogical aside / convention
    • `<div class="callout callout-warning">` — common mistake / pitfall
    • `<div class="callout callout-tip">` — insight / "foreshadowing"
  Plus `<div class="callout-quote">` for direct lecturer quotations
  (italic, source-anchored). At least 3–5 callouts per chapter.

- **Engineering details belong INSIDE the prose, not as an appendix**.
  If the concept has known training gotchas (e.g. `log σ²` parameter-
  ization for numerical stability; `reduction='sum'` vs `'mean'` for KL
  weighting; cosine schedule's `s = 0.008` offset), weave them in as
  callouts at the point they become relevant. Don't promise "details
  later" — give them in place.

- **PyTorch code skeleton when applicable**. If the chapter introduces
  a model architecture or training loop, include a *complete, runnable*
  PyTorch skeleton (encoder + decoder + reparameterize + loss for VAE;
  forward/reverse for DDPM; etc.). Add per-line `#` comments tying each
  line back to the formulas above. Don't write pseudo-code.

- **Takeaways block at the end with 5–7 items**, not 3. Each item
  should reference a specific lecturer-given anchor (a metaphor, a
  formula, a concrete number, a verbatim quote).

- **Length budget**: aim for {LENGTH_RANGE} {LENGTH_UNIT_LONG} of body prose (excluding
  code, SVG, math). Less than {LENGTH_UNDER} {LENGTH_UNIT_SHORT} = under-developed. More than
  {LENGTH_OVER} {LENGTH_UNIT_SHORT} = bloated, look for redundancy. The TL;DR block plus 8–14
  sections plus a code skeleton plus 5+ callouts naturally lands in
  this range.

══════════════════════════════════════════════════════════════════════
REQUIRED STRUCTURAL ELEMENTS
══════════════════════════════════════════════════════════════════════

1. **TL;DR callout block** at the top (see Principle 1 above).
2. **Anti-bias opening** — call out a misconception or simplification
   readers might already have. PREFER misconceptions the lecturer
   explicitly addressed in the source.
3. **8–14 top-level numbered sections** ({SECTION_NUMBERING}) — see Principle 1
   for the depth target.
4. **At least one inline <svg> diagram** with viewBox + simple paths.
   Encouraged: one CSS-animated SVG element using @keyframes.
5. **One embedded source clip**:
   `<iframe src="https://www.youtube.com/embed/VIDEO_ID?start=N">`
   pulled from source_chunks. Pick the clip that BEST shows the
   lecturer's signature metaphor / derivation.
6. **Math with step-by-step derivation** when appropriate: LaTeX in
   `$...$` (inline) or `$$...$$` (block). Use `<div class="deriv-step">`
   wrappers with `**Why**:` annotations for every non-trivial step.
   Reproduce the lecturer's whiteboard derivation, not a cleaned-up
   textbook version.
7. **3–5 callout boxes** (info / note / warning / tip / quote) inline,
   to differentiate "neutral exposition" from "common-mistake warning"
   from "lecturer's exact words" etc.
8. **PyTorch code skeleton** if the chapter introduces a model.
   Complete and runnable, with comments mapping to formulas.
9. **Takeaways block** at the end with 5–7 items, each anchored to a
   specific lecturer-given example or metaphor.
10. **Wiki-links** to other chapters via
    `<a href="/textbook/N/">previous chapter title</a>` and to concept
    pages via `<a href="/concepts/slug/">name</a>` when relevant.

══════════════════════════════════════════════════════════════════════
STYLE
══════════════════════════════════════════════════════════════════════

- {TONE}
- Anti-jargon by default; explain on first use.
- **Lecturer's metaphors > generic textbook metaphors > your own**.
  Reproduce ALL distinctive ones — don't collapse to one.
- Concrete examples with real numbers, not {CONCRETE_EXAMPLE_BAD}.
- Don't moralize, don't editorialize beyond the source material.
- When you ADD framing beyond the source (cross-course comparison,
  modern follow-up, your own critique), wrap it in a
  `<div class="my-addition">` block with a 🟡 flag and the label
  "{AUTHOR_NOTE_LABEL}" — example: {AUTHOR_NOTE_EXAMPLE} — this helps the
  reader separate "what the lecturer taught" from "what the textbook
  author layered on top".
"""


def get_synthesize_style_guide(language: str = "zh") -> str:
    """Return the synthesize style guide rendered in the requested language.

    Uses str.replace() rather than .format() because the template may
    contain literal curly braces (LaTeX, HTML attribute templates).
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
