import os
import sqlite3

from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT    NOT NULL,
            email         TEXT    NOT NULL UNIQUE,
            password_hash TEXT    NOT NULL,
            created_at    TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            amount      REAL    NOT NULL,
            category    TEXT    NOT NULL,
            description TEXT,
            date        TEXT    NOT NULL,
            created_at  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()


def seed_db():
    conn = get_db()
    conn.execute(
        "INSERT OR IGNORE INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@example.com", generate_password_hash("password123")),
    )
    conn.commit()
    user = conn.execute(
        "SELECT id FROM users WHERE email = 'demo@example.com'"
    ).fetchone()
    uid = user["id"]
    sample_expenses = [
        (uid, 12.50,  "Food",     "Lunch at cafe",     "2026-05-01"),
        (uid, 45.00,  "Bills",    "Electricity bill",  "2026-05-02"),
        (uid, 120.00, "Travel",   "Train tickets",     "2026-05-03"),
        (uid, 30.00,  "Shopping", "Books",             "2026-05-05"),
        (uid, 25.00,  "Health",   "Pharmacy",          "2026-05-07"),
    ]
    has_expenses = conn.execute(
        "SELECT 1 FROM expenses WHERE user_id = ?", (uid,)
    ).fetchone()
    if not has_expenses:
        conn.executemany(
            "INSERT INTO expenses"
            " (user_id, amount, category, description, date)"
            " VALUES (?, ?, ?, ?, ?)",
            sample_expenses,
        )
    conn.commit()
    conn.close()
