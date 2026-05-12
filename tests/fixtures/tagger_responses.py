"""Canned Anthropic API responses for tagger tests."""
from __future__ import annotations

from types import SimpleNamespace


def make_response(text: str, input_tokens: int = 100, output_tokens: int = 20) -> SimpleNamespace:
    """Build a fake anthropic.types.Message with .content[0].text and .usage."""
    return SimpleNamespace(
        content=[SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        ),
        stop_reason="end_turn",
    )


GOOD_TWO_TAGS = make_response(
    '{"tags": [{"slug": "self-attention", "confidence": 0.95},'
    ' {"slug": "proposed:rotary-embedding", "confidence": 0.78}]}'
)

LOW_CONFIDENCE_FILTERED = make_response(
    '{"tags": [{"slug": "self-attention", "confidence": 0.4}]}'
)

EMPTY = make_response('{"tags": []}')

MALFORMED = make_response('not valid json at all')
