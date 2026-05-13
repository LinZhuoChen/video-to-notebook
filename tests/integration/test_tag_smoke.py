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


@pytest.mark.integration
def test_tag_print_prompts_emits_envelope(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'https://x', '2026-05-13')"
        )
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 'L1', 'https://yt/v1', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'hello world')"
        )

    import shutil
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    result = runner.invoke(app, ["tag", "--ontology", str(ont_path), "--print-prompts"])
    assert result.exit_code == 0, result.stdout

    import json as _json
    envelope = _json.loads(result.stdout)
    assert envelope["schema_version"] == "1"
    assert envelope["kind"] == "tag_prompts"
    assert len(envelope["chunks"]) == 1
    assert envelope["chunks"][0]["text"] == "hello world"


@pytest.mark.integration
def test_tag_apply_results_writes_db(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    db = tmp_project / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        cur = conn.execute(
            "INSERT INTO courses (slug, title, platform, source_url, added_at) "
            "VALUES ('c1', 'C1', 'youtube', 'u', '2026-05-13')"
        )
        course_id = cur.lastrowid
        conn.execute(
            "INSERT INTO lectures (course_id, idx, title, video_url, transcript, status) "
            "VALUES (?, 1, 'L1', 'u', 't', 'ok')",
            (course_id,),
        )
        conn.execute(
            "INSERT INTO chunks (lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 0, 0, 60, 'self attention.')"
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('self-attention', 'Self-Attention', 'seed')"
        )

    import shutil, json as _json
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)

    results_path = tmp_project / "results.json"
    results_path.write_text(_json.dumps({
        "schema_version": "1",
        "kind": "tag_results",
        "tagger_model_id": "claude-code-max:v1",
        "results": [{"chunk_id": 1, "tags": [{"slug": "self-attention", "confidence": 0.9}]}],
    }))

    result = runner.invoke(
        app,
        ["tag", "--ontology", str(ont_path), "--apply-results", str(results_path)],
    )
    assert result.exit_code == 0, result.stdout
    assert "1 known tags" in result.stdout

    with connect(db) as conn:
        (n,) = conn.execute("SELECT COUNT(*) FROM chunk_concepts").fetchone()
    assert n == 1


@pytest.mark.integration
def test_tag_print_and_apply_mutually_exclusive(tmp_project: Path, fixtures_dir: Path):
    runner.invoke(app, ["init"])
    import shutil
    ont_path = tmp_project / "ontology.yaml"
    shutil.copy(fixtures_dir / "ontology.yaml", ont_path)
    results_path = tmp_project / "fake.json"
    results_path.write_text("{}")

    result = runner.invoke(
        app,
        ["tag", "--ontology", str(ont_path),
         "--print-prompts", "--apply-results", str(results_path)],
    )
    assert result.exit_code != 0
    assert "mutually exclusive" in result.stdout.lower()
