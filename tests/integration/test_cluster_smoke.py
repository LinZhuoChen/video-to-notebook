from __future__ import annotations

import shutil
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from typer.testing import CliRunner

from course_merger.cli import app
from course_merger.cluster.llm_review import ReviewDecision
from course_merger.db.session import connect

runner = CliRunner()


@pytest.mark.integration
def test_cluster_cli_end_to_end(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])

    db = tmp_project / ".course-merger" / "db.sqlite"
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
        patch("course_merger.cli.Embedder", return_value=fake_embedder),
        patch("course_merger.cli.Reviewer", return_value=fake_reviewer),
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
