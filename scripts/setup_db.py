import sqlite3

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Drop existing tables to reset
        cursor.execute("DROP TABLE IF EXISTS teams")
        cursor.execute("DROP TABLE IF EXISTS drivers")
        cursor.execute("DROP TABLE IF EXISTS results")
        cursor.execute("DROP TABLE IF EXISTS races")    

        with open('lib/db/schema.sql', 'r') as f:
            schema = f.read()
            cursor.executescript(schema)
            print("F1 Database schema created successfully. ")
            
            try:
                from lib.db.seed import seed_data
                seed_data()
                pr