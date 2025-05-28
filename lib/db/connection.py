import sqlite3

def get_connection():
    return sqlite3.connect('f1.db')
    conn.row_factory = sqlite3.Row  