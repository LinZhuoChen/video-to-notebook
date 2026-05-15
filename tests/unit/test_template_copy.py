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
