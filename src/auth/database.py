import sqlite3


def create_users_table():

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        gender TEXT,
        race TEXT,
        education TEXT,
        lunch TEXT,
        prep TEXT,
        math_score REAL,
        reading_score REAL,
        writing_score REAL,
        average_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()