from __future__ import annotations

import json
from pathlib import Path

from video_to_notebook.build.textbook_writer import write_textbook_assets
from video_to_notebook.db.session import connect, init_db


def _seed(db_path: Path, state_dir: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('a', 'A', 'seed'),('b', 'B', 'seed')"
        )
        conn.execute(
            "INSERT INTO curriculum_chapters "
            "(order_idx, module, title, blurb, primary_concept_slug, "
            "related_concept_slugs, curriculum_designer, status, synthesized_path) "
            "VALUES "
            "(1, 'Module 1', '什么是 A', 'b1', 'a', '[]', 'haiku:v1', 'synthesized', '1.html'),"
            "(2, 'Module 1', '什么是 B', 'b2', 'b', '[\"a\"]', 'haiku:v1', 'planned', NULL)"
        )
    # Fragment for chapter 1 only
    textbook_dir = state_dir / "textbook"
    textbook_dir.mkdir(parents=True, exist_ok=True)
    (textbook_dir / "1.html").write_text("<article><h1>A</h1></article>")


def test_writes_manifest_and_copies_synthesized_only(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site_dir = tmp_path / "site"
    _seed(db, state)

    write_textbook_assets(db_path=db, state_dir=state, site_dir=site_dir)

    # v2.2: content lives under <lang>/ subdir; default language is zh
    target = site_dir / "src" / "content" / "textbook" / "zh"
    manifest = target / "curriculum.json"
    assert manifest.is_file()
    data = json.loads(manifest.read_text())
    assert data["schema_version"] == "1"
    assert len(data["chapters"]) == 2

    ch1 = next(c for c in data["chapters"] if c["order_idx"] == 1)
    assert ch1["status"] == "synthesized"
    assert (target / "1.html").is_file()
    assert "<h1>A</h1>" in (target / "1.html").read_text()

    ch2 = next(c for c in data["chapters"] if c["order_idx"] == 2)
    assert ch2["status"] == "planned"
    # No fragment for chapter 2
    assert not (target / "2.html").exists()


def test_idempotent(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site_dir = tmp_path / "site"
    _seed(db, state)

    write_textbook_assets(db_path=db, state_dir=state, site_dir=site_dir)
    write_textbook_assets(db_path=db, state_dir=state, site_dir=site_dir)

    target = site_dir / "src" / "content" / "textbook" / "zh"
    assert (target / "1.html").is_file()
    files = sorted(p.name for p in target.iterdir())
    assert "1.html" in files
    assert "curriculum.json" in files


def test_handles_no_chapters(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site_dir = tmp_path / "site"
    init_db(db)  # no chapters seeded
    write_textbook_assets(db_path=db, state_dir=state, site_dir=site_dir)
    manifest = site_dir / "src" / "content" / "textbook" / "zh" / "curriculum.json"
    data = json.loads(manifest.read_text())
    assert data["chapters"] == []


def test_respects_build_meta_language(tmp_path: Path):
    """When build_meta.language='en', content goes to en/ instead of zh/."""
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site_dir = tmp_path / "site"
    _seed(db, state)
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO build_meta (key, value) VALUES ('language', 'en')"
        )

    write_textbook_assets(db_path=db, state_dir=state, site_dir=site_dir)

    en_target = site_dir / "src" / "content" / "textbook" / "en"
    zh_target = site_dir / "src" / "content" / "textbook" / "zh"
    assert (en_target / "curriculum.json").is_file()
    assert (en_target / "1.html").is_file()
    assert not zh_target.exists()
