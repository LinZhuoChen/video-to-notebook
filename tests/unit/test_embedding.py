from __future__ import annotations

import numpy as np
import pytest

from video_to_notebook.cluster.embedding import Embedder, cosine_similarity


@pytest.fixture(scope="session")
def embedder():
    """Load the SentenceTransformer model once per session.

    Downloads ~80 MB on first run from huggingface.co. If the network is
    unavailable AND the model isn't cached, skip these tests rather than
    failing the whole suite — CI runners reach huggingface fine.

    We probe with one `.embed()` call here so partially-loaded states (some
    config fetched, some not) also produce a clean skip instead of a
    mid-test RuntimeError.
    """
    try:
        e = Embedder()
        _ = e.embed("probe")  # trigger any deferred huggingface fetch
        return e
    except Exception as exc:  # network / SSL / disk — anything that prevents use
        pytest.skip(f"Embedder unavailable (model not cached, network failed): {exc}")


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
