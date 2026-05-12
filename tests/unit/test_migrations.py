from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from course_merger.db.session import _migration_files, connect, init_db


def test_fresh_db_runs_all_migrations(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (version,) = conn.execute("PRAGMA user_version").fetchone()
    # After Task 4 there is one migration: 0001. After Task 5 there will be 0002.
    assert version >= 1


def test_init_db_is_idempotent_for_migrations(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (version_first,) = conn.execute("PRAGMA user_version").fetchone()

    init_db(db_path)
    with connect(db_path) as conn:
        (version_second,) = conn.execute("PRAGMA user_version").fetchone()

    assert version_first == version_second


def test_migration_files_are_ordered():
    files = _migration_files()
    nums = [int(f.name.split("_")[0]) for f in files]
    assert nums == sorted(nums)
    assert nums[0] == 1  # numbering starts at 0001


def test_0002_creates_concept_tables(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        names = [
            r[0]
            for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            ).fetchall()
        ]
        (version,) = conn.execute("PRAGMA user_version").fetchone()

    for required in ["concepts", "concept_aliases", "chunk_concepts", "build_meta", "proposed_tags"]:
        assert required in names, f"table {required} missing"
    assert version == 2


def test_concept_aliases_enforce_unique(tmp_path: Path):
    """An alias string can only point to one concept."""
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('a', 'A', 'seed')"
        )
        conn.execute(
            "INSERT INTO concepts (slug, canonical_name, ontology_source) "
            "VALUES ('b', 'B', 'seed')"
        )
        conn.execute(
            "INSERT INTO concept_aliases (concept_id, alias) "
            "VALUES (1, 'shared-alias')"
        )

    with pytest.raises(sqlite3.IntegrityError):
        with connect(db_path) as conn:
            conn.execute(
                "INSERT INTO concept_aliases (concept_id, alias) "
                "VALUES (2, 'shared-alias')"
            )
