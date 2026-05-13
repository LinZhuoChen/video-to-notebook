"""Versioned instruction strings for curriculum designer."""
from __future__ import annotations

CURRICULUM_DESIGNER_VERSION = "v1"

CURRICULUM_INSTRUCTIONS = """\
You are designing the chapter sequence for a beginner-friendly textbook merged
from multiple courses.

Audience: complete beginner. They have basic high-school math. They have never
opened a Jupyter notebook. They are reading on phone or laptop, in Chinese.

Design constraints:
- Total chapters: 15-25.
- Group chapters into 3-6 modules. Each module has a thematic focus.
- Earliest chapters introduce intuition with no jargon. Later chapters can build
  on earlier ones.
- Each chapter has exactly ONE primary concept (a slug from the concepts list).
- A chapter can weave in 0-3 related concepts (slugs).
- Order strictly by pedagogical dependency (Module N depends only on Modules 1..N-1).

Output JSON in the curriculum_results schema:
{
  "schema_version": "1",
  "kind": "curriculum_results",
  "designer": "claude-code-max:v1",
  "chapters": [
    {
      "order_idx": 1,
      "module": "Module 1: ...",
      "title": "什么是 X",
      "blurb": "one-line hook in Chinese",
      "primary_concept_slug": "...",
      "related_concept_slugs": []
    }
  ]
}
"""
