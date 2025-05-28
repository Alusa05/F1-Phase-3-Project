from lib.db.connection import get_connection


class Driver:
    def __init__(self, name, nationality, id=None):
        self.id = id
        self.name = name
        self.nationality = nationality

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute(
                    "UPDATE drivers SET name=?, nationality=? WHERE id=?",
                    (self.name, self.nationality, self.id)
                )
            else:
                cursor.execute(
                    "INSERT INTO drivers (name, nationality) VALUES (?, ?)",
                    (self.name, self.nationality)
                )
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, driver_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drivers WHERE id=?", (driver_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(name=row['name'], nationality=row['nationality'], id=row['id'])
        return None

    def races(self):
        """Get all races for this driver."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.* FROM races r
            JOIN results res ON r.id = res.race_id
            WHERE res.driver_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def add_race_result(self, team_id, race_id, position, points):
        """Add a new race result for this driver."""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO results (driver_id, team_id, race_id, position, points)
                VALUES (?, ?, ?, ?, ?)
            """, (self.id, team_id, race_id, position, points))
            conn.commit()
        finally:
            conn.close()