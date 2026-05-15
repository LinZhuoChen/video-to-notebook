from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from video_to_notebook.db.session import connect, init_db


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

    with pytest.raises(sqlite3.IntegrityError), connect(db_path) as conn:
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


def test_wal_mode_enabled(tmp_path: Path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (mode,) = conn.execute("PRAGMA journal_mode").fetchone()
    assert mode == "wal"


def test_busy_timeout_at_least_5_minutes(tmp_path: Path):
    """Concurrent crawls must wait politely, not fail immediately."""
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        (timeout_ms,) = conn.execute("PRAGMA busy_timeout").fetchone()
    assert timeout_ms >= 300_000  # 5 min
