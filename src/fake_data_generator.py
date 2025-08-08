from faker import Faker
import psycopg2
from psycopg2 import extras

def generate_and_insert_fake_data():
    # Establish connection
    conn = None
    cursor = None

    try:
        conn = psycopg2.connect(
            host="postgres",
            port=5432,
            database="fraud_db",
            user="fraud_user",
            password="fraud_pass"
        )

        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)

        # Initialize Faker
        fake = Faker()

        # Prepare data to insert
        users = [(fake.name(), fake.email()) for _ in range(10)]

        # Insert data in bulk
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        extras.execute_batch(cursor, query, users)

        # Commit changes to database
        conn.commit()

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        # Ensure resources are closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()
