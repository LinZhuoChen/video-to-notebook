"""Sonnet review pass: per-cluster merge/create/reject decision."""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Literal

from course_merger.cluster.clusterer import Cluster
from course_merger.cluster.prompts import (
    CLUSTER_REVIEW_PROMPT_VERSION,
    REVIEW_SYSTEM,
    REVIEW_USER_TEMPLATE,
)
from course_merger.tag.ontology import Ontology


Decision = Literal["merge", "create", "reject", "ambiguous"]


@dataclass(frozen=True, slots=True)
class ReviewDecision:
    decision: Decision
    target_slug: str | None = None
    new_concept: dict[str, str] | None = None
    reason: str = ""


def parse_review_response(text: str) -> ReviewDecision:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"failed to parse review response as JSON: {e}") from e

    decision = data.get("decision")
    if decision not in ("merge", "create", "reject", "ambiguous"):
        raise ValueError(f"invalid decision: {decision!r}")

    return ReviewDecision(
        decision=decision,
        target_slug=data.get("target_slug"),
        new_concept=data.get("new_concept"),
        reason=data.get("reason", ""),
    )


def _build_system_blocks(ontology: Ontology) -> list[dict[str, Any]]:
    ontology_block = "\n".join(
        f"{c.slug} — {c.canonical_name}" for c in ontology.concepts
    ) or "(empty)"
    return [
        {
            "type": "text",
            "text": REVIEW_SYSTEM.format(ontology_block=ontology_block),
            "cache_control": {"type": "ephemeral"},
        }
    ]


class Reviewer:
    def __init__(
        self,
        *,
        client: Any,
        model: str,
        ontology: Ontology,
        max_tokens: int = 512,
    ) -> None:
        self.client = client
        self.model = model
        self.ontology = ontology
        self.max_tokens = max_tokens
        self._system_blocks = _build_system_blocks(ontology)

    @property
    def reviewer_model_id(self) -> str:
        return f"{self.model}:{CLUSTER_REVIEW_PROMPT_VERSION}"

    def review(self, cluster: Cluster, sample_chunks: list[str]) -> ReviewDecision:
        user_text = REVIEW_USER_TEMPLATE.format(
            cluster_items="\n".join(f"- {item}" for item in cluster.items),
            sample_chunks="\n".join(f"- {c[:200]}" for c in sample_chunks[:3]),
        )

        for _ in range(2):  # one retry on parse error
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=self._system_blocks,
                    messages=[{"role": "user", "content": user_text}],
                )
            except Exception:
                continue
            text = resp.content[0].text if resp.content else ""
            try:
                return parse_review_response(text)
            except ValueError:
                continue

        return ReviewDecision(decision="ambiguous", reason="parse_failure")
