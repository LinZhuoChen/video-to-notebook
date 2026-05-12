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
