import sqlite3


def register_user(username, password):
    """
    Register a new user.
    Returns True if successful.
    Returns False if username already exists.
    """

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            (username, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()