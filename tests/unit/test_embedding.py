from __future__ import annotations

import numpy as np
import pytest

from course_merger.cluster.embedding import Embedder, cosine_similarity


@pytest.fixture(scope="session")
def embedder():
    return Embedder()  # loads the model once per test session


def test_embedder_returns_384_dim_vector(embedder):
    v = embedder.embed("self-attention")
    assert isinstance(v, np.ndarray)
    assert v.shape == (384,)
    assert v.dtype == np.float32


def test_embed_batch(embedder):
    out = embedder.embed_batch(["self-attention", "RoPE", "kv cache"])
    assert out.shape == (3, 384)


def test_similar_concepts_have_high_cosine(embedder):
    v1 = embedder.embed("rotary positional encoding")
    v2 = embedder.embed("RoPE")
    v3 = embedder.embed("memory bandwidth")
    assert cosine_similarity(v1, v2) > cosine_similarity(v1, v3)


def test_cosine_self_is_one(embedder):
    v = embedder.embed("attention")
    assert cosine_similarity(v, v) == pytest.approx(1.0, abs=1e-5)
