import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def execute(self, query, params=None, fetch=False, fetchone=False):
        if params is None:
            params = ()
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            if fetchone:
                return cur.fetchone()
            if fetch:
                return cur.fetchall()
            return None
