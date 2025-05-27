from lib.db.connection import get_connection

class Team:
    def __init__ (self, name, country, id=None):
        self.id = id
        self.name = name
        self.country = country
        def save(self):
            conn = get_connection()
            cursor = conn.cursor()
            try:
                if self.id:
                    cursor.execute(
                        "UPDATE teams SET name=?, country=? WHERE id=?",
                        (self.name, self.country, self.id)

                    )
                else:
                    cursor.execute(
                        "INSERT INTO teams (name, country) VALUES (?, ?) "
                        (self.name, self.country)
                    )
                    self.id = cursor.lastrowid
                conn.commit()
            finally:
                conn.close()

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE name=?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(name=row['name'], country=row['country'], id=row['id'])
        return None
    
    def drivers (self):
        """Get all drivers who raced for this team."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT DISTINCT d. * FROM drivers d
                       JOIN results res ON d.id = res.driver_id
                          WHERE res.team_id = ?
                       """, (self.id,))
        return cursor.fetchall()
    
    def races(self):
        """Get all races this team participated in."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT DISTINCT r. * FROM races r
                       JOIN results res ON r.id = res.race_id
                          WHERE res.team_id = ?
                       """, (self.id,))
        return cursor.fetchall()
    
    def best_drivers(self):
        """Get drivers from this team with more than 100 points."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT d.*, SUM(res.points) AS total_points
                       FROM drivers d
                       JOIN results res ON d.id = res.driver_id
                       WHERE res.team_id = ?
                       GROUP BY d.id
                       HAVING total_points > 100
                       """, (self.id,))
        return cursor.fetchall()