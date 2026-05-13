from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import numpy as np
import pytest

from course_merger.cluster.llm_review import ReviewDecision
from course_merger.cluster.runner import ClusterReport, run_cluster
from course_merger.db.session import connect, init_db
from course_merger.tag.ontology import load_ontology


def _seed(db_path: Path) -> int:
    """Seed: 1 course, 1 lecture, 2 chunks, 2 proposed_tags entries."""
    init_db(db_path)
    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-09')"
        )
        course_id: int = cur.lastrowid  # type: ignore[assignment]
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'u', 't', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'about rotary')",
            (lecture_id,),
        )
        c1 = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 1, 10, 20, 'about rope')",
            (lecture_id,),
        )
        c2 = cur.lastrowid
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (?, 'rotary-embedding', 0.8, 'haiku:v1')",
            (c1,),
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (?, 'RoPE', 0.85, 'haiku:v1')",
            (c2,),
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('rotary-positional-encoding', 'Rotary Positional Encoding', 'seed')"
        )
    return course_id


@pytest.fixture
def onto(fixtures_dir: Path):
    return load_ontology(fixtures_dir / "ontology.yaml")


def _fake_embedder(vectors_per_text: dict[str, np.ndarray]):
    m = MagicMock()
    def _embed(text: str) -> np.ndarray:
        return vectors_per_text[text]
    def _embed_batch(texts: list[str]) -> np.ndarray:
        return np.stack([vectors_per_text[t] for t in texts])
    m.embed.side_effect = _embed
    m.embed_batch.side_effect = _embed_batch
    return m


def _identical_vec(seed: int = 1) -> np.ndarray:
    rng = np.random.default_rng(seed)
    v = rng.normal(size=384).astype(np.float32)
    return v / np.linalg.norm(v)


def test_cluster_merge_creates_aliases_and_chunk_concepts(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec()
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(
        decision="merge", target_slug="rotary-positional-encoding"
    )

    report = run_cluster(
        db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7
    )

    assert isinstance(report, ClusterReport)
    assert report.clusters_reviewed == 1
    assert report.merged == 1
    assert report.created == 0

    with connect(db) as conn:
        aliases = [
            r[0] for r in conn.execute("SELECT alias FROM concept_aliases").fetchall()
        ]
        assert set(aliases) == {"rotary-embedding", "RoPE"}
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
        assert n == 2
        (left,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
        assert left == 0

        # Plan 3 contract: dirty_concepts JSON array should include the merged slug.
        import json
        row = conn.execute(
            "SELECT value FROM build_meta WHERE key='dirty_concepts'"
        ).fetchone()
        assert row is not None, "build_meta.dirty_concepts missing after merge"
        dirty = json.loads(row[0])
        assert "rotary-positional-encoding" in dirty


def test_cluster_create_makes_new_concept(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec(2)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(
        decision="create",
        new_concept={
            "slug": "rope-encoding",
            "canonical_name": "RoPE Encoding",
            "description": "Rotary position encoding.",
        },
    )

    run_cluster(db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7)

    with connect(db) as conn:
        c = conn.execute(
            "SELECT canonical_name, ontology_source FROM concepts WHERE slug='rope-encoding'"
        ).fetchone()
    assert c == ("RoPE Encoding", "discovered")


def test_cluster_reject_skips_writes(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec(3)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(decision="reject", reason="noise")

    run_cluster(db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7)

    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_pt == 0
    assert n_cc == 0


def test_cluster_ambiguous_queues_review(tmp_path: Path, onto):
    db = tmp_path / "db.sqlite"
    _seed(db)

    same = _identical_vec(4)
    embedder = _fake_embedder({"rotary-embedding": same, "RoPE": same})

    reviewer = MagicMock()
    reviewer.reviewer_model_id = "sonnet:v1"
    reviewer.review.return_value = ReviewDecision(decision="ambiguous", reason="?")

    report = run_cluster(
        db_path=db, embedder=embedder, reviewer=reviewer, threshold=0.7
    )

    assert report.ambiguous == 1
    with connect(db) as conn:
        (n_pt,) = conn.execute("SELECT COUNT(*) FROM proposed_tags").fetchone()
    assert n_pt == 2
