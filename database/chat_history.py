import json
from datetime import datetime, timezone
from typing import Dict, List

from database.engine import db_connection, placeholder


def load_chat_history(user_id: int) -> List[Dict]:
    with db_connection() as conn:
        rows = conn.execute(
            f"""
            SELECT role, content
            FROM chat_messages
            WHERE user_id = {placeholder()}
            ORDER BY id ASC
            """,
            (user_id,),
        ).fetchall()

    return [{"role": row["role"], "content": row["content"]} for row in rows]


def save_chat_message(user_id: int, role: str, content: str):
    with db_connection() as conn:
        conn.execute(
            f"""
            INSERT INTO chat_messages (user_id, role, content, created_at)
            VALUES ({placeholder()}, {placeholder()}, {placeholder()}, {placeholder()})
            """,
            (user_id, role, content, datetime.now(timezone.utc).isoformat()),
        )


def replace_chat_history(user_id: int, messages: List[Dict]):
    with db_connection() as conn:
        conn.execute(f"DELETE FROM chat_messages WHERE user_id = {placeholder()}", (user_id,))
        for message in messages:
            conn.execute(
                f"""
                INSERT INTO chat_messages (user_id, role, content, created_at)
                VALUES ({placeholder()}, {placeholder()}, {placeholder()}, {placeholder()})
                """,
                (
                    user_id,
                    message["role"],
                    message["content"],
                    datetime.now(timezone.utc).isoformat(),
                ),
            )


def clear_chat_history(user_id: int):
    with db_connection() as conn:
        conn.execute(f"DELETE FROM chat_messages WHERE user_id = {placeholder()}", (user_id,))


def export_chat_history(user_id: int) -> str:
    return json.dumps(load_chat_history(user_id), ensure_ascii=False)
