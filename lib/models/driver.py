from lib.db.connection import get_connection

class Driver:
    def __init__(self, name, nationality, id=None):
        self.id = id
        self.name = name
        self.nationality = nationality

        def 