"""SQLite connection lifecycle and transaction helpers."""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

_SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def init_db(db_path: Path) -> None:
    """Create the database file and apply the schema. Idempotent."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    schema = _SCHEMA_PATH.read_text(encoding="utf-8")
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()


@contextmanager
def connect(db_path: Path) -> Iterator[sqlite3.Connection]:
    """Open a connection with sane defaults inside a transaction.

    Auto-commits on clean exit; rolls back on exception.
    """
    conn = sqlite3.connect(db_path, isolation_level=None)  # autocommit off via BEGIN
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
