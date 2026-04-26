import hashlib
import hmac
import re
import secrets
import sqlite3
from datetime import datetime, timezone

from config import DB_PATH


def db_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    with db_connection() as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                password_salt TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)")

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

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS auth_sessions (
                token TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )
            """
        )
        conn.execute("CREATE INDEX IF NOT EXISTS idx_auth_sessions_user_id ON auth_sessions(user_id)")


def normalize_email(email: str) -> str:
    return email.strip().lower()


def hash_password(password: str, salt: str | None = None) -> tuple[str, str]:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt), 180_000)
    return salt, digest.hex()


def create_user(name: str, email: str, password: str) -> tuple[bool, str, dict | None]:
    name = name.strip()
    email = normalize_email(email)

    if len(name) < 2:
        return False, "Please enter your name.", None
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return False, "Please enter a valid email address.", None
    if len(password) < 8:
        return False, "Password must be at least 8 characters.", None

    salt, password_hash = hash_password(password)
    try:
        with db_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO users (name, email, password_salt, password_hash, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, email, salt, password_hash, datetime.now(timezone.utc).isoformat()),
            )
            user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        return False, "An account with this email already exists. Please log in.", None

    return True, "Account created. You are signed in.", {"id": user_id, "name": name, "email": email}


def verify_user(email: str, password: str) -> tuple[bool, str, dict | None]:
    email = normalize_email(email)
    with db_connection() as conn:
        conn.row_factory = sqlite3.Row
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

    if user is None:
        return False, "No account found with that email.", None

    _, attempted_hash = hash_password(password, user["password_salt"])
    if not hmac.compare_digest(attempted_hash, user["password_hash"]):
        return False, "Incorrect password.", None

    return True, "Welcome back.", {"id": user["id"], "name": user["name"], "email": user["email"]}


def create_login_token(user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    with db_connection() as conn:
        conn.execute(
            """
            INSERT INTO auth_sessions (token, user_id, created_at)
            VALUES (?, ?, ?)
            """,
            (token, user_id, datetime.now(timezone.utc).isoformat()),
        )
    return token


def get_user_by_token(token: str) -> dict | None:
    if not token:
        return None

    with db_connection() as conn:
        conn.row_factory = sqlite3.Row
        user = conn.execute(
            """
            SELECT users.id, users.name, users.email
            FROM auth_sessions
            JOIN users ON users.id = auth_sessions.user_id
            WHERE auth_sessions.token = ?
            """,
            (token,),
        ).fetchone()

    if user is None:
        return None
    return {"id": user["id"], "name": user["name"], "email": user["email"]}


def delete_login_token(token: str):
    if not token:
        return
    with db_connection() as conn:
        conn.execute("DELETE FROM auth_sessions WHERE token = ?", (token,))
