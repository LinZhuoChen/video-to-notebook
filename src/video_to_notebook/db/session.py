"""SQLite connection lifecycle, transaction helpers, and migration runner."""
from __future__ import annotations

import re
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

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

    `busy_timeout` is set to 5 minutes so concurrent `course-merger crawl`
    invocations queue politely instead of failing immediately. A single
    course's crawl can take ~10 min on a long playlist, but the 5-min
    window is enough for a parallel crawl to land behind it without errors
    in the common 2-3-course case. (If a user genuinely wants 10+ courses
    crawled simultaneously they should serialize them with a wrapper.)
    """
    conn = sqlite3.connect(db_path, isolation_level=None, timeout=300.0)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA busy_timeout = 300000")
    conn.execute("BEGIN")
    try:
        yield conn
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
