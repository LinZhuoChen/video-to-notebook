from __future__ import annotations

from pathlib import Path

import pytest

from video_to_notebook.tag.ontology import (
    Concept,
    Ontology,
    load_ontology,
)


def test_load_ontology_parses_concepts(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    assert isinstance(onto, Ontology)
    assert len(onto.concepts) == 3

    sa = onto.by_slug("self-attention")
    assert isinstance(sa, Concept)
    assert sa.canonical_name == "Self-Attention"
    assert "SA" in sa.aliases


def test_ontology_lookup_by_alias(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    rope = onto.find_by_alias("RoPE")
    assert rope is not None and rope.slug == "rotary-positional-encoding"
    rope2 = onto.find_by_alias("rotary embedding")
    assert rope2 is not None and rope2.slug == "rotary-positional-encoding"
    assert onto.find_by_alias("nonexistent") is None


def test_ontology_top_n_for_prompt(fixtures_dir: Path):
    onto = load_ontology(fixtures_dir / "ontology.yaml")
    slugs = onto.top_n_slugs(n=2)
    assert len(slugs) == 2
    assert all(isinstance(s, str) for s in slugs)


def test_load_ontology_empty_file(tmp_path: Path):
    p = tmp_path / "empty.yaml"
    p.write_text("concepts: []\n")
    onto = load_ontology(p)
    assert onto.concepts == ()


def test_load_ontology_rejects_duplicate_slug(tmp_path: Path):
    p = tmp_path / "dup.yaml"
    p.write_text(
        "concepts:\n"
        "  - slug: foo\n"
        "    canonical_name: Foo\n"
        "  - slug: foo\n"
        "    canonical_name: Foo Two\n"
    )
    with pytest.raises(ValueError, match="duplicate slug"):
        load_ontology(p)
