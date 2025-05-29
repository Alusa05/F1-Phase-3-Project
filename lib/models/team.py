from lib.db.connection import get_connection

class Team:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, team_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
        team_data = cursor.fetchone()
        conn.close()
        return cls(team_data['name']) if team_data else None

    def drivers(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drivers WHERE team_id = ?", (self.id,))
        return cursor.fetchall()
