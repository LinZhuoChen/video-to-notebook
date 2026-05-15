"""sentence-transformers wrapper for embedding short text strings (tags, concept names).

The model is loaded lazily on first use, kept in process memory thereafter.
"""
from __future__ import annotations

from functools import cached_property

import numpy as np

_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
_DIM = 384


class Embedder:
    """Wraps a sentence-transformers model. Single-process; not thread-safe."""

    def __init__(self, model_name: str = _MODEL_NAME) -> None:
        self.model_name = model_name

    @cached_property
    def _model(self):
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(self.model_name)

    def embed(self, text: str) -> np.ndarray:
        """Embed a single string, return a 384-dim float32 vector."""
        v = self._model.encode([text], convert_to_numpy=True, normalize_embeddings=True)
        return v[0].astype(np.float32)

    def embed_batch(self, texts: list[str]) -> np.ndarray:
        """Embed a batch of strings, return an (N, 384) float32 array."""
        v = self._model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return v.astype(np.float32)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity. Assumes the vectors are pre-normalized."""
    return float(np.dot(a, b))
