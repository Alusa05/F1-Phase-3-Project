import sqlite3
from lib.db.connection import get_connection


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
       
        cursor.execute("DROP TABLE IF EXISTS teams")
        cursor.execute("DROP TABLE IF EXISTS drivers")
        cursor.execute("DROP TABLE IF EXISTS results")
        cursor.execute("DROP TABLE IF EXISTS races")

       
        with open('lib/db/schema.sql', 'r') as f:
            schema = f.read()
        cursor.executescript(schema)
        print("F1 Database schema created successfully.")

     
        try:
            from lib.db.seed import seed_data
            seed_data()
            print(" Test data seeded successfully.")
        except Exception as e:
            print(f"Error seeding test data: {e}")

        conn.commit()
    except Exception as e:
        print(f" Error setting up database: {e}")
        conn.rollback()
    finally:
        conn.close()



