from lib.db.connection import get_connection

class Team:
    def __init__(self, name, country=None):
        self.id = None
        self.name = name
        self.country = country  # Add country field

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (name, country) VALUES (?, ?)", 
                       (self.name, self.country))
        conn.commit()
        self.id = cursor.lastrowid  # Get the auto-generated ID
        conn.close()

    @classmethod
    def find_by_id(cls, team_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
        team_data = cursor.fetchone()
        conn.close()
        if team_data:
            team = cls(team_data['name'], team_data['country'])
            team.id = team_data['id']
            return team
        return None

    def drivers(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drivers WHERE team_id = ?", (self.id,))
        return cursor.fetchall()