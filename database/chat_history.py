import json
import sqlite3
from datetime import datetime, timezone

from database.users import db_connection


def init_chat_history():
    with db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chat_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
                content TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )
            """
        )
        conn.execute("CREATE INDEX IF NOT EXISTS idx_chat_messages_user_id ON chat_messages(user_id, id)")


def load_chat_history(user_id: int) -> list[dict]:
    with db_connection() as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT role, content
            FROM chat_messages
            WHERE user_id = ?
            ORDER BY id ASC
            """,
            (user_id,),
        ).fetchall()

    return [{"role": row["role"], "content": row["content"]} for row in rows]


def save_chat_message(user_id: int, role: str, content: str):
    with db_connection() as conn:
        conn.execute(
            """
            INSERT INTO chat_messages (user_id, role, content, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, role, content, datetime.now(timezone.utc).isoformat()),
        )


def replace_chat_history(user_id: int, messages: list[dict]):
    with db_connection() as conn:
        conn.execute("DELETE FROM chat_messages WHERE user_id = ?", (user_id,))
        conn.executemany(
            """
            INSERT INTO chat_messages (user_id, role, content, created_at)
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    user_id,
                    message["role"],
                    message["content"],
                    datetime.now(timezone.utc).isoformat(),
                )
                for message in messages
            ],
        )


def clear_chat_history(user_id: int):
    with db_connection() as conn:
        conn.execute("DELETE FROM chat_messages WHERE user_id = ?", (user_id,))


def export_chat_history(user_id: int) -> str:
    return json.dumps(load_chat_history(user_id), ensure_ascii=False)
