from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import numpy as np
import pytest

from video_to_notebook.cluster.prompt_io import (
    apply_cluster_results,
    collect_cluster_prompts,
)
from video_to_notebook.cluster.runner import ClusterReport
from video_to_notebook.db.session import connect, init_db
from video_to_notebook.tag.ontology import load_ontology


def _seed(db_path: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'rotary content')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (2, 1, 1, 60, 120, 'rope content')"
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (1, 'rotary-embedding', 0.8, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (2, 'RoPE', 0.85, 'haiku:v1')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'rotary-positional-encoding', 'Rotary Positional Encoding', 'seed')"
        )


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def _same_vec(seed: int = 1) -> np.ndarray:
    rng = np.random.default_rng(seed)
    v = rng.normal(size=384).astype(np.float32)
    return v / np.linalg.norm(v)


def _fake_embedder(vecs: dict[str, np.ndarray]):
    m = MagicMock()
    m.embed_batch.side_effect = lambda texts: np.stack([vecs[t] for t in texts])
    return m


def test_collect_emits_clusters_and_samples(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec()
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "cluster_prompts"
    assert any(c["slug"] == "rotary-positional-encoding" for c in envelope["ontology"])
    assert len(envelope["clusters"]) == 1
    cluster = envelope["clusters"][0]
    assert cluster["cluster_id"] == 0
    assert set(cluster["items"]) == {"rotary-embedding", "RoPE"}
    assert "_tag_to_chunks" in envelope


def test_collect_empty_when_no_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    init_db(db)
    embedder = MagicMock()
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    assert envelope["clusters"] == []
    embedder.embed_batch.assert_not_called()


def test_apply_merge_writes_aliases_and_chunk_concepts(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec()
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "merge",
            "target_slug": "rotary-positional-encoding",
        }],
    }
    report = apply_cluster_results(
        db_path=db, ontology=onto, prompts=envelope, decisions=decisions,
    )
    assert isinstance(report, ClusterReport)
    assert report.merged == 1
    with connect(db) as conn:
        aliases = [r[0] for r in conn.execute("SELECT alias FROM concept_aliases").fetchall()]
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
    assert set(aliases) == {"rotary-embedding", "RoPE"}
    assert n_cc == 2
    assert n_pt == 0


def test_apply_create_makes_new_concept(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec(2)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "create",
            "new_concept": {
                "slug": "rope-encoding",
                "canonical_name": "RoPE Encoding",
                "description": "Rotary position encoding.",
            },
        }],
    }
    apply_cluster_results(db_path=db, ontology=onto, prompts=envelope, decisions=decisions)
    with connect(db) as conn:
        c = conn.execute(
            "SELECT canonical_name, ontology_source FROM concepts WHERE slug='rope-encoding'"
        ).fetchone()
    assert c == ("RoPE Encoding", "discovered")


def test_apply_reject_drops_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec(3)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "reject",
            "reason": "noise",
        }],
    }
    apply_cluster_results(db_path=db, ontology=onto, prompts=envelope, decisions=decisions)
    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_pt == 0
    assert n_cc == 0


def test_apply_ambiguous_keeps_proposed_tags(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)
    same = _same_vec(4)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})
    envelope = collect_cluster_prompts(
        db_path=db, ontology=onto, embedder=embedder, threshold=0.7,
    )
    decisions = {
        "schema_version": "1",
        "kind": "cluster_results",
        "reviewer_model_id": "claude-code-max:v1",
        "decisions": [{
            "cluster_id": envelope["clusters"][0]["cluster_id"],
            "decision": "ambiguous",
            "reason": "?",
        }],
    }
    report = apply_cluster_results(
        db_path=db, ontology=onto, prompts=envelope, decisions=decisions,
    )
    assert report.ambiguous == 1
    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
    assert n_pt == 2


def test_apply_rejects_wrong_schema_version(tmp_path: Path, onto):
    decisions = {
        "schema_version": "999",
        "kind": "cluster_results",
        "reviewer_model_id": "x",
        "decisions": [],
    }
    with pytest.raises(ValueError, match="schema_version"):
        apply_cluster_results(
            db_path=tmp_path / "db.sqlite", ontology=onto,
            prompts={"schema_version": "1", "kind": "cluster_prompts", "clusters": [], "_tag_to_chunks": {}},
            decisions=decisions,
        )


def test_apply_rejects_wrong_kind(tmp_path: Path, onto):
    decisions = {
        "schema_version": "1",
        "kind": "tag_results",
        "reviewer_model_id": "x",
        "decisions": [],
    }
    with pytest.raises(ValueError, match="kind"):
        apply_cluster_results(
            db_path=tmp_path / "db.sqlite", ontology=onto,
            prompts={"schema_version": "1", "kind": "cluster_prompts", "clusters": [], "_tag_to_chunks": {}},
            decisions=decisions,
        )
