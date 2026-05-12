from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from course_merger.db.session import init_db, connect


def test_init_db_creates_tables(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    with connect(db_path) as conn:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        names = [r[0] for r in rows]

    assert "courses" in names
    assert "lectures" in names
    assert "chunks" in names


def test_init_db_idempotent(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    init_db(db_path)  # second call must not raise


def test_connect_enables_foreign_keys(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (val,) = conn.execute("PRAGMA foreign_keys").fetchone()
        assert val == 1


def test_transaction_rolls_back_on_error(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)

    with pytest.raises(sqlite3.IntegrityError):
        with connect(db_path) as conn:
            conn.execute(
                "INSERT INTO courses (slug, title, platform, source_url, added_at) "
                "VALUES (?, ?, ?, ?, ?)",
                ("cs336", "CS336", "youtube", "https://x", "2026-01-01"),
            )
            conn.execute(
                "INSERT INTO courses (slug, title, platform, source_url, added_at) "
                "VALUES (?, ?, ?, ?, ?)",
                ("cs336", "duplicate slug", "youtube", "https://y", "2026-01-01"),
            )

    # The first insert should also have rolled back.
    with connect(db_path) as conn:
        (cnt,) = conn.execute("SELECT COUNT(*) FROM courses").fetchone()
    assert cnt == 0
