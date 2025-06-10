import sqlite3

class UserService:
    def __init__(self, config):
        uri = config.get('DATABASE_URI')      # e.g. "sqlite:///users.db"
        self._db_path = uri.replace('sqlite:///', '')
        conn = sqlite3.connect(self._db_path)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        conn.commit()
        conn.close()

    def create_user(self, name: str, email: str) -> int:
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            (name, email)
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    def get_user(self, user_id: int) -> dict:
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, name, email FROM users WHERE id = ?',
            (user_id,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        return None

    def delete_user(self, user_id: int) -> None:
        conn = sqlite3.connect(self._db_path)
        conn.execute(
            'DELETE FROM users WHERE id = ?',
            (user_id,)
        )
        conn.commit()
        conn.close()

    def list_all_users(self) -> list:
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email FROM users')
        rows = cursor.fetchall()
        conn.close()
        return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]
