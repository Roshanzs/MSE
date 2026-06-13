import sqlite3

DB_NAME = "system.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                full_name TEXT NOT NULL,
                birthdate TEXT NOT NULL
            )
        ''')
        conn.commit()

def insert_user(email: str, password_hash: str, name: str, birthdate: str) -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (email, password_hash, full_name, birthdate) VALUES (?, ?, ?, ?)",
                (email.lower(), password_hash, name, birthdate)
            )
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False  # Failed if email already exists

def query_user_by_login(email: str, password_hash: str) -> tuple or None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT email, full_name, birthdate FROM users WHERE email = ? AND password_hash = ?",
            (email.lower(), password_hash)
        )
        return cursor.fetchone()

def verify_user_for_reset(email: str, birthdate: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE email = ? AND birthdate = ?", 
            (email.lower(), birthdate)
        )
        return cursor.fetchone() is not None

def update_password(email: str, new_password_hash: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET password_hash = ? WHERE email = ?", 
            (new_password_hash, email.lower())
        )
        conn.commit()