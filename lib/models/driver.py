from lib.db.connection import get_connection
class Driver:
    def __init__(self, name, team_id=None):
        self.name = name
        self.team_id = team_id
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO drivers (name, team_id) VALUES (?, ?)", (self.name, self.team_id))
        conn.commit()
        conn.close()
    @classmethod
    def find_by_id(cls, driver_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drivers WHERE id = ?", (driver_id,))
        driver_data = cursor.fetchone()
        conn.close()
        return cls(driver_data['name'], driver_data['team_id']) if driver_data else None
    def results(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results WHERE driver_id = ?", (self.id,))
        return cursor.fetchall()