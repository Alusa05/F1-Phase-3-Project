from lib.db.connection import get_connection

class Race:
    def __init__(self, name, date, location, id=None):
        self.id = id
        self.name = name
        self.date = date
        self.location = location

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute(
                    "UPDATE races SET name=?, date=?, location=? WHERE id=?",
                    (self.name, self.date, self.location, self.id)
                )
            else:
                cursor.execute(
                    "INSERT INTO races (name, date, location) VALUES (?, ?, ?)",
                    (self.name, self.date, self.location)
                )
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

            @classmethod
            def find_by_location(cls, location):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM races WHERE location=?", (location,))
                row = cursor.fetchone()
                conn.close()
                if row:
                    return cls(name=row['name'], date=row['date'], location=row['location'], id=row['id'])
                return None
            
            def participants(self):
                """Get all drivers who participated in this race."""
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT DISTINCT d.* FROM drivers d
                    JOIN results res ON d.id = res.driver_id
                               WHERE res.race_id = ?
                """, (self.id,))
                return cursor.fetchall()