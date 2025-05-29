from lib.db.connection import get_connection

class Race:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO races (name, date) VALUES (?, ?)", (self.name, self.date))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, race_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM races WHERE id = ?", (race_id,))
        race_data = cursor.fetchone()
        conn.close()
        return cls(race_data['name'], race_data['date']) if race_data else None

    def results(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results WHERE race_id = ?", (self.id,))
        return cursor.fetchall()
