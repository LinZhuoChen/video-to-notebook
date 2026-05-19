from __future__ import annotations

import json
from pathlib import Path

from video_to_notebook.build.concept_writer import write_concept_explainer_assets
from video_to_notebook.db.session import connect, init_db


def _seed(db_path: Path, state_dir: Path) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES "
            "(1, 'linear-algebra', 'Linear Algebra', 'seed'),"
            "(2, 'backpropagation', 'Backpropagation', 'seed'),"
            "(3, 'no-explainer', 'No Explainer', 'seed')"
        )
        conn.execute(
            "INSERT INTO concept_explanations "
            "(concept_id, html_fragment, explainer, generated_at) "
            "VALUES "
            "(1, 'linear-algebra.html', 'claude-code-max:v2', '2026-05-14'),"
            "(2, 'backpropagation.html', 'claude-code-max:v2', '2026-05-14')"
        )
    concepts_dir = state_dir / "concepts"
    concepts_dir.mkdir(parents=True, exist_ok=True)
    (concepts_dir / "linear-algebra.html").write_text("<article>la</article>")
    (concepts_dir / "backpropagation.html").write_text("<article>bp</article>")


def test_writes_manifest_and_copies_explained_concepts(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site = tmp_path / "site"
    _seed(db, state)

    write_concept_explainer_assets(db_path=db, state_dir=state, site_dir=site)

    target = site / "src" / "content" / "concept-explainers" / "zh"
    manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
    slugs = [e["slug"] for e in manifest["explainers"]]
    assert sorted(slugs) == ["backpropagation", "linear-algebra"]
    assert (target / "linear-algebra.html").is_file()
    assert (target / "backpropagation.html").is_file()
    # No file for un-explained concept
    assert not (target / "no-explainer.html").exists()


def test_idempotent(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site = tmp_path / "site"
    _seed(db, state)
    write_concept_explainer_assets(db_path=db, state_dir=state, site_dir=site)
    write_concept_explainer_assets(db_path=db, state_dir=state, site_dir=site)
    target = site / "src" / "content" / "concept-explainers" / "zh"
    manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["explainers"]) == 2


def test_handles_no_explainers(tmp_path: Path):
    db = tmp_path / "db.sqlite"
    state = tmp_path / ".video-to-notebook"
    site = tmp_path / "site"
    init_db(db)
    write_concept_explainer_assets(db_path=db, state_dir=state, site_dir=site)
    target = site / "src" / "content" / "concept-explainers" / "zh"
    manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["explainers"] == []
