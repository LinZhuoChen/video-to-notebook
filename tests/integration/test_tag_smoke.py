from __future__ import annotations

import shutil
from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from course_merger.cli import app
from course_merger.db.session import connect
from course_merger.tag.claude_tagger import Tag, TagResult

runner = CliRunner()


@pytest.mark.integration
def test_tag_cli_end_to_end(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-09')"
        )
        course_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'https://yt/v1', 'about self-attention', 'ok')",
            (course_id,),
        )
        lecture_id = cur.lastrowid
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (?, 0, 0, 10, 'self-attention is key.')",
            (lecture_id,),
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )

    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    fake_result = TagResult(
        tags=(Tag(slug="self-attention", confidence=0.95, is_proposed=False),)
    )
    with (
        patch(
            "course_merger.tag.claude_tagger.ClaudeTagger.tag_chunk",
            return_value=fake_result,
        ),
        patch("anthropic.Anthropic", return_value=object()),
    ):
        result = runner.invoke(
            app, ["tag", "--ontology", str(ont_path), "--model", "claude-haiku-4-5"]
        )

    assert result.exit_code == 0, result.stdout
    assert "chunks tagged" in result.stdout.lower() or "1 tagged" in result.stdout.lower()

    with connect(db) as conn:
        (n_cc,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n_cc == 1


@pytest.mark.integration
def test_tag_errors_when_not_initialized(tmp_project: Path, fixtures_dir: Path):
    result = runner.invoke(
        app, ["tag", "--ontology", str(fixtures_dir / "ontology.yaml")]
    )
    assert result.exit_code != 0
    assert "init" in result.stdout.lower()
