from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from course_merger.tag.claude_tagger import (
    ClaudeTagger,
    TagResult,
    parse_tagger_response,
)
from course_merger.tag.ontology import load_ontology
from tests.fixtures.tagger_responses import (
    EMPTY,
    GOOD_TWO_TAGS,
    LOW_CONFIDENCE_FILTERED,
    MALFORMED,
)


def test_parse_tagger_response_splits_known_and_proposed(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    result = parse_tagger_response(GOOD_TWO_TAGS.content[0].text, onto)

    assert isinstance(result, TagResult)
    assert any(t.slug == "self-attention" and t.is_proposed is False for t in result.tags)
    assert any(t.slug == "rotary-embedding" and t.is_proposed is True for t in result.tags)


def test_parse_filters_low_confidence(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    result = parse_tagger_response(LOW_CONFIDENCE_FILTERED.content[0].text, onto)
    assert result.tags == ()


def test_parse_empty_tags(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    result = parse_tagger_response(EMPTY.content[0].text, onto)
    assert result.tags == ()


def test_parse_malformed_raises(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    with pytest.raises(ValueError, match="parse"):
        parse_tagger_response(MALFORMED.content[0].text, onto)


def test_tagger_uses_prompt_caching(fixtures_dir: Path):
    """The system prompt must include cache_control to enable Anthropic caching."""
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    fake_client = MagicMock()
    fake_client.messages.create.return_value = GOOD_TWO_TAGS

    tagger = ClaudeTagger(client=fake_client, model="claude-haiku-4-5", ontology=onto)
    tagger.tag_chunk("This chunk talks about self-attention and rotary embeddings.")

    call_kwargs = fake_client.messages.create.call_args.kwargs
    system_blocks = call_kwargs["system"]
    assert isinstance(system_blocks, list)
    assert any(
        b.get("cache_control", {}).get("type") == "ephemeral" for b in system_blocks
    )


def test_tagger_retries_once_on_parse_failure(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    fake_client = MagicMock()
    fake_client.messages.create.side_effect = [MALFORMED, GOOD_TWO_TAGS]

    tagger = ClaudeTagger(client=fake_client, model="claude-haiku-4-5", ontology=onto)
    result = tagger.tag_chunk("anything")

    assert len(result.tags) > 0
    assert fake_client.messages.create.call_count == 2


def test_tagger_returns_empty_after_two_failures(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    fake_client = MagicMock()
    fake_client.messages.create.side_effect = [MALFORMED, MALFORMED]

    tagger = ClaudeTagger(client=fake_client, model="claude-haiku-4-5", ontology=onto)
    result = tagger.tag_chunk("anything")

    assert result.tags == ()
    assert result.error == "parse_failure"
