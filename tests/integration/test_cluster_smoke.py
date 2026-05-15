from __future__ import annotations

import shutil
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from typer.testing import CliRunner

from video_to_notebook.cli import app
from video_to_notebook.cluster.llm_review import ReviewDecision
from video_to_notebook.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_cluster_cli_end_to_end(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])

    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-09')"
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'u', 't', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'rope content')",
            (lecture_id,),
        )
        chunk_id = cur.lastrowid
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (?, 'RoPE-thing', 0.8, 'haiku:v1')",
            (chunk_id,),
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('rotary-positional-encoding', 'RoPE', 'seed')"
        )

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    fake_decision = ReviewDecision(
        decision="merge", target_slug="rotary-positional-encoding"
    )
    fake_embedder = MagicMock()
    fake_embedder.embed_batch.return_value = np.ones((1, 384), dtype=np.float32)
    fake_reviewer = MagicMock()
    fake_reviewer.reviewer_model_id = "sonnet:v1"
    fake_reviewer.review.return_value = fake_decision

    with (
        patch("video_to_notebook.cli.Embedder", return_value=fake_embedder),
        patch("video_to_notebook.cli.Reviewer", return_value=fake_reviewer),
        patch("anthropic.Anthropic", return_value=object()),
    ):
        result = runner.invoke(
            app,
            ["cluster", "--ontology", str(ont_path), "--threshold", "0.5"],
        )

    assert result.exit_code == 0, result.stdout
    assert "merged" in result.stdout.lower()

    with connect(db) as conn:
        (n,) = conn.execute(
            "SELECT COUNT(*) FROM concept_aliases WHERE alias='RoPE-thing'"
        ).fetchone()
    assert n == 1


@pytest.mark.integration
def test_cluster_print_prompts_emits_envelope(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".video-to-notebook" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 'L1', 'u', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'rope text')"
        )
        conn.execute(
            "INSERT INTO proposed_tags (chunk_id, raw_tag, confidence, tagger_model) "
            "VALUES (1, 'RoPE-thing', 0.8, 'haiku:v1')"
        )

    import shutil
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    with patch(
        "video_to_notebook.cluster.embedding.Embedder.embed_batch",
        return_value=np.ones((1, 384), dtype=np.float32),
    ):
        result = runner.invoke(
            app,
            ["cluster", "--ontology", str(ont_path),
             "--threshold", "0.5", "--print-prompts"],
        )

    assert result.exit_code == 0, result.stdout
    import json as _json
    envelope = _json.loads(result.stdout)
    assert envelope["kind"] == "cluster_prompts"
    assert len(envelope["clusters"]) == 1
    assert envelope["clusters"][0]["items"] == ["RoPE-thing"]
