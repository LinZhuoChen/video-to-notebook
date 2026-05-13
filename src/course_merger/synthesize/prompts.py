"""Versioned style guide for chapter synthesizer."""
from __future__ import annotations

SYNTHESIZER_VERSION = "v1"


SYNTHESIZE_STYLE_GUIDE = """\
You are writing one chapter of a beginner-friendly online textbook.

OUTPUT FORMAT: a self-contained HTML fragment (NO <html><head><body> wrapper —
just the body content starting with <article>). The fragment will be wrapped
in a site layout that already provides nav, search, footer, and global styles.

Audience: complete ML beginner reading in Chinese. They have basic high-school
math. No prior coding experience required for this chapter's intuition.

Required structural elements per chapter:
1. Anti-bias opening — call out a misconception or simplification readers might
   already have ("If you only think of X as Y, you don't really understand it").
2. At least one inline <svg> diagram. Use viewBox + simple paths/lines/text.
3. Optional but encouraged: one CSS-animated SVG element using @keyframes,
   inline in a <style> block at the top of the article.
4. One embedded source clip: <iframe src="https://www.youtube.com/embed/VIDEO_ID?start=N">
   pulled from one of the source_chunks.
5. Math when appropriate: write LaTeX inside `$...$` (inline) or `$$...$$` (block).
   The site renders with KaTeX automatically.
6. End with a `<div class="takeaways">` containing 3 bullet points of "what to
   remember from this chapter".
7. Use `<a href="/textbook/N/">previous chapter title</a>` style wiki links to
   reference earlier chapters when conceptually relevant.

Style:
- Conversational Chinese. Direct, second-person ("你"). Short sentences.
- Anti-jargon by default; explain on first use.
- One concrete example or analogy per major point.
- Don't moralize, don't editorialize beyond the source material.
"""
