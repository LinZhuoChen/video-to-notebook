"""Orchestrator: proposed_tags → embed → cluster → review → write concepts/aliases."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import numpy as np

from course_merger.cluster.clusterer import Cluster, cluster_by_cosine
from course_merger.cluster.llm_review import ReviewDecision
from course_merger.db.session import connect


class _EmbedderLike(Protocol):
    def embed_batch(self, texts: list[str]) -> np.ndarray: ...


class _ReviewerLike(Protocol):
    @property
    def reviewer_model_id(self) -> str: ...

    def review(self, cluster: Cluster, sample_chunks: list[str]) -> ReviewDecision: ...


@dataclass(frozen=True, slots=True)
class ClusterReport:
    clusters_reviewed: int
    merged: int
    created: int
    rejected: int
    ambiguous: int


def _collect_proposed_tags(conn) -> list[tuple[str, list[int]]]:
    """Return list of (raw_tag, [chunk_ids that have this tag]). Skips sentinel rows."""
    rows = conn.execute(
        "SELECT raw_tag, chunk_id FROM proposed_tags "
        "WHERE raw_tag != '__parse_failure__' "
        "ORDER BY raw_tag, chunk_id"
    ).fetchall()
    grouped: dict[str, list[int]] = {}
    for raw_tag, chunk_id in rows:
        grouped.setdefault(raw_tag, []).append(chunk_id)
    return list(grouped.items())


def _sample_chunks_for_cluster(
    conn, cluster: Cluster, tag_to_chunks: dict[str, list[int]], k: int = 3
) -> list[str]:
    chunk_ids: list[int] = []
    for raw_tag in cluster.items:
        chunk_ids.extend(tag_to_chunks.get(raw_tag, []))
    chunk_ids = chunk_ids[:k]
    if not chunk_ids:
        return []
    placeholders = ",".join("?" for _ in chunk_ids)
    rows = conn.execute(
        f"SELECT text FROM chunks WHERE id IN ({placeholders})", chunk_ids
    ).fetchall()
    return [r[0] for r in rows]


def mark_dirty(conn, slugs: list[str]) -> None:
    """Append `slugs` to build_meta.dirty_concepts (JSON array)."""
    row = conn.execute(
        "SELECT value FROM build_meta WHERE key='dirty_concepts'"
    ).fetchone()
    existing: list[str] = json.loads(row[0]) if row else []
    merged = sorted(set(existing) | set(slugs))
    if row:
        conn.execute(
            "UPDATE build_meta SET value=? WHERE key='dirty_concepts'",
            (json.dumps(merged),),
        )
    else:
        conn.execute(
            "INSERT INTO build_meta (key, value) VALUES ('dirty_concepts', ?)",
            (json.dumps(merged),),
        )


def consume_proposed_for_cluster(conn, cluster: Cluster) -> None:
    raw_tags = list(cluster.items)
    if not raw_tags:
        return
    placeholders = ",".join("?" for _ in raw_tags)
    conn.execute(
        f"DELETE FROM proposed_tags WHERE raw_tag IN ({placeholders})",
        raw_tags,
    )


def attach_chunks_to_concept(
    conn,
    cluster: Cluster,
    tag_to_chunks: dict[str, list[int]],
    concept_id: int,
    reviewer_model_id: str,
) -> None:
    for raw_tag in cluster.items:
        for chunk_id in tag_to_chunks.get(raw_tag, []):
            conn.execute(
                "INSERT OR IGNORE INTO chunk_concepts "
                "(chunk_id, concept_id, confidence, tagger_model) "
                "VALUES (?, ?, 0.85, ?)",
                (chunk_id, concept_id, reviewer_model_id),
            )


def run_cluster(
    *,
    db_path: Path,
    embedder: _EmbedderLike,
    reviewer: _ReviewerLike,
    threshold: float = 0.75,
) -> ClusterReport:
    merged = created = rejected = ambiguous = 0
    dirty: list[str] = []

    with connect(db_path) as conn:
        tag_pairs = _collect_proposed_tags(conn)
        if not tag_pairs:
            return ClusterReport(0, 0, 0, 0, 0)

        raw_tags = [t for t, _ in tag_pairs]
        tag_to_chunks = dict(tag_pairs)

        vectors = embedder.embed_batch(raw_tags)
        clusters = cluster_by_cosine(raw_tags, vectors, threshold=threshold)

        for cluster in clusters:
            sample = _sample_chunks_for_cluster(conn, cluster, tag_to_chunks)
            decision = reviewer.review(cluster, sample_chunks=sample)

            if decision.decision == "merge":
                target = conn.execute(
                    "SELECT id, slug FROM concepts WHERE slug = ?", (decision.target_slug,)
                ).fetchone()
                if target is None:
                    ambiguous += 1
                    continue
                target_id, target_slug = target
                for raw_tag in cluster.items:
                    conn.execute(
                        "INSERT OR IGNORE INTO concept_aliases (concept_id, alias) "
                        "VALUES (?, ?)",
                        (target_id, raw_tag),
                    )
                attach_chunks_to_concept(
                    conn, cluster, tag_to_chunks, target_id, reviewer.reviewer_model_id
                )
                consume_proposed_for_cluster(conn, cluster)
                dirty.append(target_slug)
                merged += 1

            elif decision.decision == "create":
                if decision.new_concept is None:
                    ambiguous += 1
                    continue
                new = decision.new_concept
                cur = conn.execute(
                    "INSERT INTO concepts (slug, canonical_name, description, ontology_source) "
                    "VALUES (?, ?, ?, 'discovered')",
                    (new["slug"], new["canonical_name"], new.get("description", "")),
                )
                new_id: int = cur.lastrowid  # type: ignore[assignment]
                for raw_tag in cluster.items:
                    if raw_tag != new["slug"]:
                        conn.execute(
                            "INSERT OR IGNORE INTO concept_aliases (concept_id, alias) "
                            "VALUES (?, ?)",
                            (new_id, raw_tag),
                        )
                attach_chunks_to_concept(
                    conn, cluster, tag_to_chunks, new_id, reviewer.reviewer_model_id
                )
                consume_proposed_for_cluster(conn, cluster)
                dirty.append(new["slug"])
                created += 1

            elif decision.decision == "reject":
                consume_proposed_for_cluster(conn, cluster)
                rejected += 1

            else:  # ambiguous
                ambiguous += 1

        if dirty:
            mark_dirty(conn, dirty)

    return ClusterReport(
        clusters_reviewed=len(clusters),
        merged=merged,
        created=created,
        rejected=rejected,
        ambiguous=ambiguous,
    )
