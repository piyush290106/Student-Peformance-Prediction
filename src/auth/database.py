import sqlite3
import pandas as pd


def create_users_table():

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user'
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
    cursor.execute(
    """
    INSERT OR IGNORE INTO users
    (username,password,role)
    VALUES
    ('admin','admin123','admin')
    """
)

    conn.commit()
    conn.close()
def get_all_users():

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, role FROM users"
    )

    data = cursor.fetchall()

    conn.close()

    return data


def delete_user(user_id):

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()


def update_user_role(user_id, role):

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET role=? WHERE id=?",
        (role, user_id)
    )

    conn.commit()
    conn.close()
def get_all_prediction_history():

    conn = sqlite3.connect("src/auth/users.db")

    df = pd.read_sql_query(
        "SELECT * FROM prediction_history ORDER BY created_at DESC",
        conn
    )

    conn.close()

    return df