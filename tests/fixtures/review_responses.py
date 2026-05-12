"""Canned Anthropic responses for cluster-review tests."""
from __future__ import annotations

from types import SimpleNamespace


def _make(text: str) -> SimpleNamespace:
    return SimpleNamespace(
        content=[SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(
            input_tokens=1, output_tokens=1,
            cache_creation_input_tokens=0, cache_read_input_tokens=0
        ),
        stop_reason="end_turn",
    )


MERGE_DECISION = _make(
    '{"decision":"merge","target_slug":"rotary-positional-encoding","new_concept":null,"reason":"RoPE aliases"}'
)

CREATE_DECISION = _make(
    '{"decision":"create","target_slug":null,'
    '"new_concept":{"slug":"speculative-decoding","canonical_name":"Speculative Decoding","description":"An inference acceleration technique using a draft model."},'
    '"reason":"new concept"}'
)

REJECT_DECISION = _make(
    '{"decision":"reject","target_slug":null,"new_concept":null,"reason":"presenter intro phrase"}'
)

AMBIGUOUS_DECISION = _make(
    '{"decision":"ambiguous","target_slug":null,"new_concept":null,"reason":"could be either x or y"}'
)
