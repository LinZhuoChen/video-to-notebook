"""Unit tests for the in-session prompt/decision path helpers."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from video_to_notebook import inflow


def test_path_helpers_return_sibling_prompts_and_decisions(tmp_path: Path):
    """All five path helpers return a (prompts, decisions) pair under prompts/."""
    state = tmp_path / ".video-to-notebook"
    pairs = {
        "tag": inflow.tag_paths(state),
        "cluster": inflow.cluster_paths(state),
        "curriculum": inflow.curriculum_paths(state),
        "synthesize": inflow.synthesize_paths(state, chapter=7),
        "explain": inflow.explain_paths(state, concept_slug="attention"),
    }
    for kind, (prompts, decisions) in pairs.items():
        assert prompts.parent == decisions.parent, kind
        assert prompts.parent.is_relative_to(state / "prompts"), kind
        assert decisions.name.endswith(".decisions.json"), kind
        assert prompts.suffix == ".json"


def test_synthesize_path_uses_chapter_subdir(tmp_path: Path):
    state = tmp_path / ".video-to-notebook"
    prompts, decisions = inflow.synthesize_paths(state, chapter=3)
    assert prompts == state / "prompts" / "synthesize" / "chapter-3.json"
    assert decisions == state / "prompts" / "synthesize" / "chapter-3.decisions.json"


def test_explain_path_uses_concept_subdir(tmp_path: Path):
    state = tmp_path / ".video-to-notebook"
    prompts, decisions = inflow.explain_paths(state, concept_slug="kv-cache")
    assert prompts == state / "prompts" / "explain" / "kv-cache.json"
    assert decisions == state / "prompts" / "explain" / "kv-cache.decisions.json"


def test_write_envelope_creates_parent_dirs(tmp_path: Path):
    target = tmp_path / "a" / "b" / "c" / "tag.json"
    inflow.write_envelope(target, {"hello": "世界", "n": 1})
    assert target.is_file()
    assert json.loads(target.read_text(encoding="utf-8")) == {"hello": "世界", "n": 1}


def test_write_envelope_overwrites_existing(tmp_path: Path):
    target = tmp_path / "tag.json"
    inflow.write_envelope(target, {"v": 1})
    inflow.write_envelope(target, {"v": 2})
    assert json.loads(target.read_text())["v"] == 2


def test_write_envelope_atomic_no_partial_on_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """If serialization blows up mid-write, the target file is not created."""
    target = tmp_path / "tag.json"
    target.write_text('{"old": true}')

    class Unjsonable:
        pass

    with pytest.raises(TypeError):
        inflow.write_envelope(target, {"bad": Unjsonable()})

    # Original content preserved; no tempfile leaked in the parent.
    assert json.loads(target.read_text())["old"] is True
    leaked = [p for p in tmp_path.iterdir() if p.name.startswith(".tag.json.")]
    assert leaked == [], f"unexpected leftover tempfiles: {leaked}"


def test_read_decisions_returns_parsed_json(tmp_path: Path):
    target = tmp_path / "tag.decisions.json"
    target.write_text(json.dumps({"results": [{"chunk_id": 1}]}))
    assert inflow.read_decisions(target) == {"results": [{"chunk_id": 1}]}


def test_read_decisions_raises_friendly_error(tmp_path: Path):
    target = tmp_path / "missing.json"
    with pytest.raises(FileNotFoundError) as exc:
        inflow.read_decisions(target)
    msg = str(exc.value)
    assert str(target) in msg
    assert "--apply" in msg


def test_emit_hint_writes_three_lines_to_stderr(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
):
    inflow.emit_hint(
        prompts_path=tmp_path / "tag.json",
        decisions_path=tmp_path / "tag.decisions.json",
        size_summary="42 chunks",
        next_command="video-to-notebook tag --apply",
    )
    captured = capsys.readouterr()
    assert captured.out == ""
    lines = captured.err.strip().splitlines()
    assert len(lines) == 3
    assert "tag.json (42 chunks)" in lines[0]
    assert "tag.decisions.json" in lines[1]
    assert lines[2].endswith("video-to-notebook tag --apply")


def test_warn_print_prompts_deprecated_goes_to_stderr(
    capsys: pytest.CaptureFixture[str],
):
    inflow.warn_print_prompts_deprecated()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "deprecated" in captured.err.lower()
