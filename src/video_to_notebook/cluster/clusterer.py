"""Pure clustering algorithm: cosine similarity + union-find single-linkage."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, slots=True)
class Cluster:
    items: list[str]
    indices: list[int]


def cluster_by_cosine(
    items: list[str],
    embeddings: np.ndarray,
    threshold: float,
) -> list[Cluster]:
    """Cluster `items` such that every pair within a cluster has cosine >= threshold.

    Single-linkage union-find: for each pair (i, j) with sim >= threshold, union i and j.
    Embeddings must be L2-normalized so cosine reduces to dot product.
    """
    n = len(items)
    if n == 0:
        return []

    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    sim = embeddings @ embeddings.T  # (n, n) since embeddings are normalized
    for i in range(n):
        for j in range(i + 1, n):
            if sim[i, j] >= threshold:
                union(i, j)

    groups: dict[int, list[int]] = {}
    for i in range(n):
        root = find(i)
        groups.setdefault(root, []).append(i)

    return [
        Cluster(items=[items[i] for i in idxs], indices=idxs)
        for idxs in groups.values()
    ]
