from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from course_merger.cluster.clusterer import Cluster
from course_merger.cluster.llm_review import (
    ReviewDecision,
    Reviewer,
    parse_review_response,
)
from course_merger.tag.ontology import load_ontology
from tests.fixtures.review_responses import (
    AMBIGUOUS_DECISION,
    CREATE_DECISION,
    MERGE_DECISION,
    REJECT_DECISION,
)


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def test_parse_merge(onto):
    d = parse_review_response(MERGE_DECISION.content[0].text)
    assert d.decision == "merge"
    assert d.target_slug == "rotary-positional-encoding"


def test_parse_create(onto):
    d = parse_review_response(CREATE_DECISION.content[0].text)
    assert d.decision == "create"
    assert d.new_concept is not None
    assert d.new_concept["slug"] == "speculative-decoding"


def test_parse_reject(onto):
    d = parse_review_response(REJECT_DECISION.content[0].text)
    assert d.decision == "reject"


def test_parse_ambiguous(onto):
    d = parse_review_response(AMBIGUOUS_DECISION.content[0].text)
    assert d.decision == "ambiguous"


def test_reviewer_calls_sonnet(onto):
    fake_client = MagicMock()
    fake_client.messages.create.return_value = MERGE_DECISION

    reviewer = Reviewer(client=fake_client, model="claude-sonnet-4-6", ontology=onto)
    cluster = Cluster(items=["RoPE", "rotary embedding"], indices=[0, 1])
    decision = reviewer.review(cluster, sample_chunks=["...we use RoPE..."])

    assert isinstance(decision, ReviewDecision)
    assert decision.decision == "merge"

    call_kwargs = fake_client.messages.create.call_args.kwargs
    assert isinstance(call_kwargs["system"], list)
    assert any(
        b.get("cache_control", {}).get("type") == "ephemeral"
        for b in call_kwargs["system"]
    )
