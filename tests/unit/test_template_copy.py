from __future__ import annotations

from pathlib import Path

from video_to_notebook.build.template_copy import ensure_site_dir


def test_ensure_site_dir_copies_template(tmp_path: Path):
    site_dir = ensure_site_dir(tmp_path)
    assert site_dir == tmp_path / "site"
    assert (site_dir / "package.json").is_file()
    assert (site_dir / "src" / "pages" / "index.astro").is_file()
    # P3-T1 placed content collection schema at src/content.config.ts (Astro 5 standard)
    assert (site_dir / "src" / "content.config.ts").is_file()


def test_ensure_site_dir_is_idempotent(tmp_path: Path):
    site_dir = ensure_site_dir(tmp_path)
    sentinel = site_dir / "user_edit.txt"
    sentinel.write_text("user content")

    ensure_site_dir(tmp_path)
    assert sentinel.exists()
    assert sentinel.read_text() == "user content"


def test_ensure_site_dir_skips_node_modules(tmp_path: Path):
    site_dir = ensure_site_dir(tmp_path)
    nm = site_dir / "node_modules"
    nm.mkdir()
    (nm / "marker").write_text("don't touch")
    ensure_site_dir(tmp_path)
    assert (nm / "marker").exists()


def test_first_init_skips_all_db_derived_collections(tmp_path: Path):
    """A fresh project must not start with the bundled demo's content.

    Regression: before the v2.3 fix, first-init copytree only filtered
    ``node_modules / dist / .astro``, so every new project inherited the
    bilingual-demo's content in five collections — concept (33 MDs),
    course (3 MDs), lecture (40 MDs), textbook/zh (21 HTMLs),
    concept-explainers/zh (33 HTMLs). All five are fully derived from
    the DB by ``build.runner`` and its writers, so they must start
    empty in any new project.
    """
    site_dir = ensure_site_dir(tmp_path)

    derived_collections = [
        ("concept", "*.md"),
        ("course", "*.md"),
        ("lecture", "*.md"),
        ("textbook/zh", "*.html"),
        ("concept-explainers/zh", "*.html"),
    ]
    for sub, pattern in derived_collections:
        collection_dir = site_dir / "src" / "content" / sub
        if not collection_dir.is_dir():
            continue
        leaked = list(collection_dir.glob(pattern))
        assert leaked == [], (
            f"unexpected demo files in fresh project's content/{sub}: "
            f"{[p.name for p in leaked]}"
        )


def test_overlay_sync_preserves_user_concept_explainers(tmp_path: Path):
    """Re-running ensure_site_dir must not overwrite user-written concept HTMLs.

    Regression: ``_PROJECT_OWNED_PREFIXES`` used ``concept-explainer``
    (singular), but the actual directory is ``concept-explainers``
    (plural). The mismatch meant overlay-sync silently re-copied the
    template's demo manifest.json + HTMLs on every build, blowing away
    the user's generated concept pages.
    """
    site_dir = ensure_site_dir(tmp_path)
    concept_dir = site_dir / "src" / "content" / "concept-explainers" / "zh"
    concept_dir.mkdir(parents=True, exist_ok=True)
    user_html = concept_dir / "my-concept.html"
    user_html.write_text("<article>user content</article>", encoding="utf-8")
    user_manifest = concept_dir / "manifest.json"
    user_manifest.write_text(
        '{"schema_version":"1","explainers":[{"slug":"my-concept"}]}',
        encoding="utf-8",
    )

    # Trigger overlay-sync.
    ensure_site_dir(tmp_path)

    assert user_html.exists()
    assert user_html.read_text(encoding="utf-8") == "<article>user content</article>"
    assert "my-concept" in user_manifest.read_text(encoding="utf-8")


def test_overlay_sync_preserves_user_textbook_chapters(tmp_path: Path):
    """Same guarantee for the textbook subtree."""
    site_dir = ensure_site_dir(tmp_path)
    textbook_dir = site_dir / "src" / "content" / "textbook" / "zh"
    textbook_dir.mkdir(parents=True, exist_ok=True)
    user_chapter = textbook_dir / "1.html"
    user_chapter.write_text("<article>chapter one</article>", encoding="utf-8")

    ensure_site_dir(tmp_path)

    assert user_chapter.exists()
    assert user_chapter.read_text(encoding="utf-8") == "<article>chapter one</article>"
