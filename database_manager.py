import sqlite3
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_name="pets.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                species TEXT NOT NULL,
                base_hunger INTEGER NOT NULL,
                base_energy INTEGER NOT NULL,
                base_happiness INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activities_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_id INTEGER NOT NULL,
                action TEXT NOT NULL,
                delta_hunger INTEGER NOT NULL DEFAULT 0,
                delta_energy INTEGER NOT NULL DEFAULT 0,
                delta_happiness INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                FOREIGN KEY (pet_id) REFERENCES pets(id)
            )
            """
        )
        self.conn.commit()

    def create_pet(self, name, species, hunger=50, energy=50, happiness=50):
        self.cursor.execute("SELECT id FROM pets WHERE name = ?", (name,))
        row = self.cursor.fetchone()
        if row:
            return row[0]
        now = datetime.now().isoformat(timespec="seconds")
        self.cursor.execute(
            """
            INSERT INTO pets(name, species, base_hunger, base_energy, base_happiness, created_at)
            VALUES (?,?,?,?,?,?)
            """,
            (name, species, hunger, energy, happiness, now),
        )
        self.conn.commit()

        self.cursor.execute("SELECT id FROM pets WHERE name = ?", (name,))
        return self.cursor.fetchone()[0]

    def log_activity(self, pet_id, action, dh=0, de=0, dhap=0):
        now = datetime.now().isoformat(timespec="seconds")
        self.cursor.execute(
            """
            INSERT INTO activities_log(pet_id, action, delta_hunger, delta_energy, delta_happiness, created_at)
            VALUES (?,?,?,?,?,?)
            """,
            (pet_id, action, dh, de, dhap, now),
        )
        self.conn.commit()

    def get_current_state(self, pet_id):
        self.cursor.execute(
            "SELECT base_hunger, base_energy, base_happiness FROM pets WHERE id=?",
            (pet_id,),
        )
        base = self.cursor.fetchone()
        if not base:
            return None
        hunger, energy, happiness = base

        self.cursor.execute(
            """
            SELECT
                COALESCE(SUM(delta_hunger), 0),
                COALESCE(SUM(delta_energy), 0),
                COALESCE(SUM(delta_happiness), 0)
            FROM activities_log
            WHERE pet_id=?
            """,
            (pet_id,),
        )
        dh, de, dhap = self.cursor.fetchone()

        return {
            "hunger": hunger + dh,
            "energy": energy + de,
            "happiness": happiness + dhap,
        }

    def close(self):
        self.conn.close()
