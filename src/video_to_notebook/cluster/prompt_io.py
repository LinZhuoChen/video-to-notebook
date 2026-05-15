"""In-session cluster mode: collect cluster prompts as JSON, apply decisions to DB.

See `video_to_notebook.tag.prompt_io` for the rationale (Claude Max subscribers).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol

import numpy as np

from video_to_notebook.cluster.clusterer import Cluster, cluster_by_cosine
from video_to_notebook.cluster.runner import (
    ClusterReport,
    _collect_proposed_tags,
    _sample_chunks_for_cluster,
    attach_chunks_to_concept,
    consume_proposed_for_cluster,
    mark_dirty,
)
from video_to_notebook.db.session import connect
from video_to_notebook.tag.ontology import Ontology

SCHEMA_VERSION = "1"
DEFAULT_REVIEWER_MODEL_ID = "claude-code-max:v1"

_CLUSTER_INSTRUCTIONS = (
    "For each cluster, decide one of: "
    "(a) merge — provide `target_slug` from the existing ontology; "
    "(b) create — provide `new_concept: {slug, canonical_name, description}`; "
    "(c) reject — cluster is noise; "
    "(d) ambiguous — flag for human review. "
    "Slugs are kebab-case English even if cluster items are in another language."
)


class _EmbedderLike(Protocol):
    def embed_batch(self, texts: list[str]) -> np.ndarray: ...


def collect_cluster_prompts(
    *,
    db_path: Path,
    ontology: Ontology,
    embedder: _EmbedderLike,
    threshold: float = 0.75,
) -> dict[str, Any]:
    """Embed proposed tags, run cosine clustering, emit envelope."""
    with connect(db_path) as conn:
        tag_pairs = _collect_proposed_tags(conn)

    if not tag_pairs:
        return {
            "schema_version": SCHEMA_VERSION,
            "kind": "cluster_prompts",
            "ontology": [
                {"slug": c.slug, "canonical_name": c.canonical_name}
                for c in ontology.concepts
            ],
            "instructions": _CLUSTER_INSTRUCTIONS,
            "clusters": [],
            "_tag_to_chunks": {},
        }

    raw_tags = [t for t, _ in tag_pairs]
    tag_to_chunks: dict[str, list[int]] = dict(tag_pairs)
    vectors = embedder.embed_batch(raw_tags)
    clusters = cluster_by_cosine(raw_tags, vectors, threshold=threshold)

    envelope_clusters: list[dict[str, Any]] = []
    with connect(db_path) as conn:
        for idx, cluster in enumerate(clusters):
            sample = _sample_chunks_for_cluster(conn, cluster, tag_to_chunks)
            envelope_clusters.append({
                "cluster_id": idx,
                "items": list(cluster.items),
                "sample_chunks": sample,
            })

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "cluster_prompts",
        "ontology": [
            {"slug": c.slug, "canonical_name": c.canonical_name}
            for c in ontology.concepts
        ],
        "instructions": _CLUSTER_INSTRUCTIONS,
        "clusters": envelope_clusters,
        "_tag_to_chunks": tag_to_chunks,
    }


def apply_cluster_results(
    *,
    db_path: Path,
    ontology: Ontology,
    prompts: dict[str, Any],
    decisions: dict[str, Any],
) -> ClusterReport:
    if decisions.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"cluster decisions schema_version {decisions.get('schema_version')!r} "
            f"is not supported (expected {SCHEMA_VERSION!r})"
        )
    if decisions.get("kind") != "cluster_results":
        raise ValueError(
            f"cluster decisions kind {decisions.get('kind')!r} is not 'cluster_results'"
        )

    reviewer_model_id = decisions.get("reviewer_model_id", DEFAULT_REVIEWER_MODEL_ID)
    tag_to_chunks: dict[str, list[int]] = prompts.get("_tag_to_chunks", {})
    clusters_by_id = {c["cluster_id"]: c for c in prompts.get("clusters", [])}

    merged = created = rejected = ambiguous = 0
    dirty: list[str] = []

    with connect(db_path) as conn:
        for entry in decisions.get("decisions", []):
            cluster_id = entry.get("cluster_id")
            envelope_cluster = clusters_by_id.get(cluster_id)
            if envelope_cluster is None:
                ambiguous += 1
                continue
            cluster = Cluster(
                items=list(envelope_cluster["items"]),
                indices=list(range(len(envelope_cluster["items"]))),
            )
            kind = entry.get("decision")

            if kind == "merge":
                target = conn.execute(
                    "SELECT id, slug FROM concepts WHERE slug = ?",
                    (entry.get("target_slug"),),
                ).fetchone()
                if target is None:
                    ambiguous += 1
                    continue
                target_id, slug_in_db = target
                for raw_tag in cluster.items:
                    conn.execute(
                        "INSERT OR IGNORE INTO concept_aliases (concept_id, alias) "
                        "VALUES (?, ?)",
                        (target_id, raw_tag),
                    )
                attach_chunks_to_concept(conn, cluster, tag_to_chunks, target_id, reviewer_model_id)
                consume_proposed_for_cluster(conn, cluster)
                dirty.append(slug_in_db)
                merged += 1

            elif kind == "create":
                new = entry.get("new_concept")
                if not new or not new.get("slug") or not new.get("canonical_name"):
                    ambiguous += 1
                    continue
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
                attach_chunks_to_concept(conn, cluster, tag_to_chunks, new_id, reviewer_model_id)
                consume_proposed_for_cluster(conn, cluster)
                dirty.append(new["slug"])
                created += 1

            elif kind == "reject":
                consume_proposed_for_cluster(conn, cluster)
                rejected += 1

            else:
                ambiguous += 1

        if dirty:
            mark_dirty(conn, dirty)

    return ClusterReport(
        clusters_reviewed=len(decisions.get("decisions", [])),
        merged=merged,
        created=created,
        rejected=rejected,
        ambiguous=ambiguous,
    )
