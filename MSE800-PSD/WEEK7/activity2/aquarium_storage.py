# SQLite storage for Aquarium
import sqlite3
import os

DB_NAME = "aquarium.db"

class AquariumStorage:
    def __init__(self, db_path=DB_NAME):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS fish (
                category TEXT PRIMARY KEY,
                count INTEGER NOT NULL
            )
        ''')
        for fish in ["Goldfish", "Shark", "Angelfish", "Tuna", "Salmon"]:
            self.cursor.execute('''
                INSERT OR IGNORE INTO fish (category, count) VALUES (?, 0)
            ''', (fish,))
        self.conn.commit()

    def add_fish(self, fish_type, count=1):
        self.cursor.execute('''
            UPDATE fish SET count = count + ? WHERE category = ?
        ''', (count, fish_type))
        if self.cursor.rowcount == 0:
            raise ValueError(f"Fish type {fish_type} not recognized.")
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT category, count FROM fish ORDER BY category')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
