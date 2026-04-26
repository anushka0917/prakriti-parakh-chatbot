import sqlite3
from contextlib import contextmanager

from config import DATABASE_URL, DB_PATH

try:
    import psycopg
    from psycopg.rows import dict_row
except Exception:  # pragma: no cover
    psycopg = None
    dict_row = None


def using_postgres() -> bool:
    return bool(DATABASE_URL)


@contextmanager
def db_connection():
    if using_postgres():
        if psycopg is None:
            raise RuntimeError("psycopg is not installed")
        conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
    else:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()


def placeholder() -> str:
    return "%s" if using_postgres() else "?"
