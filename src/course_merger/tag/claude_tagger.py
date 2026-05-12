"""Claude Haiku tagger: builds prompts, calls Anthropic API with caching, parses JSON.

The Anthropic SDK is used at the boundary; this module is otherwise pure Python.
Tests inject a MagicMock client to avoid network.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from course_merger.tag.ontology import Ontology
from course_merger.tag.prompts import TAGGER_PROMPT_VERSION, TAGGER_SYSTEM_TEMPLATE


_PROPOSED_PREFIX = "proposed:"
_MIN_CONFIDENCE = 0.5
_MAX_RETRIES = 1  # one retry, so total attempts is 2


@dataclass(frozen=True, slots=True)
class Tag:
    slug: str
    confidence: float
    is_proposed: bool


@dataclass(frozen=True, slots=True)
class TagResult:
    tags: tuple[Tag, ...] = ()
    error: str = ""  # "" | "parse_failure" | "api_error"


def _build_system_blocks(ontology: Ontology) -> list[dict[str, Any]]:
    """Build the system message with the ontology, marked cache-control: ephemeral."""
    ontology_block = "\n".join(c.slug for c in ontology.concepts) or "(no seed concepts)"
    system_text = TAGGER_SYSTEM_TEMPLATE.format(ontology_block=ontology_block)
    return [
        {
            "type": "text",
            "text": system_text,
            "cache_control": {"type": "ephemeral"},
        }
    ]


def parse_tagger_response(text: str, ontology: Ontology) -> TagResult:
    """Parse the JSON output from Claude into a TagResult.

    - Raises ValueError if the text is not valid JSON or shape doesn't match.
    - Filters tags below the confidence threshold.
    - Marks tags with `proposed:` prefix.
    """
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"failed to parse tagger response as JSON: {e}") from e

    if not isinstance(data, dict) or "tags" not in data:
        raise ValueError(f"tagger response missing 'tags' key: {data!r}")

    out: list[Tag] = []
    for entry in data["tags"]:
        if not isinstance(entry, dict):
            continue
        slug = entry.get("slug", "")
        confidence = float(entry.get("confidence", 0.0))
        if confidence < _MIN_CONFIDENCE:
            continue
        is_proposed = slug.startswith(_PROPOSED_PREFIX)
        clean_slug = slug[len(_PROPOSED_PREFIX):] if is_proposed else slug
        if not clean_slug:
            continue
        out.append(Tag(slug=clean_slug, confidence=confidence, is_proposed=is_proposed))

    return TagResult(tags=tuple(out))


class ClaudeTagger:
    """Wraps the Anthropic client; tag_chunk(text) returns a TagResult."""

    def __init__(
        self,
        *,
        client: Any,  # anthropic.Anthropic
        model: str,
        ontology: Ontology,
        max_tokens: int = 256,
    ) -> None:
        self.client = client
        self.model = model
        self.ontology = ontology
        self.max_tokens = max_tokens
        self._system_blocks = _build_system_blocks(ontology)

    @property
    def tagger_model_id(self) -> str:
        """Identifier written to chunk_concepts.tagger_model — model + prompt version."""
        return f"{self.model}:{TAGGER_PROMPT_VERSION}"

    def tag_chunk(self, chunk_text: str) -> TagResult:
        last_error = ""
        for attempt in range(_MAX_RETRIES + 1):
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=self._system_blocks,
                    messages=[{"role": "user", "content": chunk_text}],
                )
            except Exception as e:
                last_error = f"api_error: {e}"
                continue

            text = resp.content[0].text if resp.content else ""
            try:
                return parse_tagger_response(text, self.ontology)
            except ValueError:
                last_error = "parse_failure"
                continue

        return TagResult(tags=(), error=last_error or "parse_failure")
