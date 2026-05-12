from __future__ import annotations

import numpy as np

from course_merger.cluster.clusterer import Cluster, cluster_by_cosine


def _orthogonal_vector(seed: int, dim: int = 384) -> np.ndarray:
    rng = np.random.default_rng(seed)
    v = rng.normal(size=dim).astype(np.float32)
    return v / np.linalg.norm(v)


def test_cluster_separates_dissimilar_vectors():
    items = ["a", "b", "c"]
    vecs = np.array([_orthogonal_vector(s) for s in (1, 2, 3)])
    clusters = cluster_by_cosine(items, vecs, threshold=0.5)
    assert len(clusters) == 3
    for c in clusters:
        assert isinstance(c, Cluster)
        assert len(c.items) == 1


def test_cluster_merges_near_duplicates():
    v0 = _orthogonal_vector(1)
    v1 = (v0 + 0.01 * _orthogonal_vector(99)).astype(np.float32)
    v1 = v1 / np.linalg.norm(v1)
    v2 = _orthogonal_vector(2)

    items = ["x", "x_alias", "y"]
    vecs = np.stack([v0, v1, v2])
    clusters = cluster_by_cosine(items, vecs, threshold=0.7)

    sizes = sorted(len(c.items) for c in clusters)
    assert sizes == [1, 2]


def test_cluster_empty_input():
    clusters = cluster_by_cosine([], np.zeros((0, 384), dtype=np.float32), threshold=0.5)
    assert clusters == []


def test_cluster_single_item():
    clusters = cluster_by_cosine(["only"], np.array([_orthogonal_vector(0)]), threshold=0.5)
    assert len(clusters) == 1
    assert clusters[0].items == ["only"]
