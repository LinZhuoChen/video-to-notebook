"""SQLite connection lifecycle, transaction helpers, and migration runner."""
from __future__ import annotations

import re
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

_MIGRATIONS_DIR = Path(__file__).parent / "migrations"
_MIGRATION_FILE_RE = re.compile(r"^(\d{4})_[a-z0-9_]+\.sql$")


def _migration_files() -> list[Path]:
    """Return migration files sorted by numeric prefix."""
    files = [
        p for p in _MIGRATIONS_DIR.glob("*.sql")
        if _MIGRATION_FILE_RE.match(p.name)
    ]
    return sorted(files, key=lambda p: int(p.name.split("_")[0]))


def _migration_number(path: Path) -> int:
    return int(path.name.split("_")[0])


def _run_migrations(conn: sqlite3.Connection) -> None:
    """Apply every migration with number > current PRAGMA user_version."""
    (current,) = conn.execute("PRAGMA user_version").fetchone()
    for path in _migration_files():
        num = _migration_number(path)
        if num <= current:
            continue
        sql = path.read_text(encoding="utf-8")
        conn.executescript(sql)
        conn.execute(f"PRAGMA user_version = {num}")


def init_db(db_path: Path) -> None:
    """Create or upgrade the database. Runs all pending migrations in order. Idempotent."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA journal_mode = WAL")
        _run_migrations(conn)
        conn.commit()
    finally:
        conn.close()


@contextmanager
def connect(db_path: Path) -> Iterator[sqlite3.Connection]:
    """Open a connection with sane defaults inside a transaction.

    Auto-commits on clean exit; rolls back on exception.
    """
    conn = sqlite3.connect(db_path, isolation_level=None)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("BEGIN")
    try:
        yield conn
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
