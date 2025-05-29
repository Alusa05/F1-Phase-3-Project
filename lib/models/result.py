from lib.db.connection import get_connection

class Result:
    def __init__(self, race_id, driver_id, position):
        self.race_id = race_id
        self.driver_id = driver_id
        self.position = position

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO results (race_id, driver_id, position) VALUES (?, ?, ?)", 
                       (self.race_id, self.driver_id, self.position))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, result_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results WHERE id = ?", (result_id,))
        result_data = cursor.fetchone()
        conn.close()
        return cls(result_data['race_id'], result_data['driver_id'], result_data['position']) if result_data else None
