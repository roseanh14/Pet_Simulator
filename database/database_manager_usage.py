from database.database_manager import DatabaseManager
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).with_name("pets.db")
db = DatabaseManager(str(DB_PATH))


def create_tables():
    db.execute(
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

    db.execute(
        """
CREATE TABLE IF NOT EXISTS activities_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    action TEXT NOT NULL,
    delta_hunger INTEGER NOT NULL DEFAULT 0,
    delta_energy INTEGER NOT NULL DEFAULT 0,
    delta_happiness INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE
)
"""
    )


def create_pet(name, species, hunger=50, energy=50, happiness=50):
    row = db.execute("SELECT id FROM pets WHERE name=?", (name,), fetchone=True)
    if row:
        return row[0]
    now = datetime.now().isoformat(timespec="seconds")
    db.execute(
        """INSERT INTO pets(name, species, base_hunger, base_energy, base_happiness, created_at)
           VALUES (?,?,?,?,?,?)""",
        (name, species, hunger, energy, happiness, now),
    )
    return db.execute("SELECT id FROM pets WHERE name=?", (name,), fetchone=True)[0]


def log_activity(pet_id, action, dh=0, de=0, dhap=0):
    now = datetime.now().isoformat(timespec="seconds")
    db.execute(
        """INSERT INTO activities_log(pet_id, action, delta_hunger, delta_energy, delta_happiness, created_at)
           VALUES (?,?,?,?,?,?)""",
        (pet_id, action, dh, de, dhap, now),
    )


def get_current_state(pet_id):
    base = db.execute(
        "SELECT base_hunger, base_energy, base_happiness FROM pets WHERE id=?",
        (pet_id,),
        fetchone=True,
    )
    if not base:
        return None
    hunger, energy, happiness = base
    sums = db.execute(
        """SELECT
               COALESCE(SUM(delta_hunger),0),
               COALESCE(SUM(delta_energy),0),
               COALESCE(SUM(delta_happiness),0)
           FROM activities_log WHERE pet_id=?""",
        (pet_id,),
        fetchone=True,
    )
    dh, de, dhap = sums
    return {
        "hunger": hunger + dh,
        "energy": energy + de,
        "happiness": happiness + dhap,
    }


if __name__ == "__main__":
    pid = create_pet("Micka", "cat")
    log_activity(pid, "play", dh=-10, de=-20, dhap=+30)
    print(get_current_state(pid))
