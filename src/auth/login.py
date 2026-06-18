import sqlite3


def login_user(username, password):

    conn = sqlite3.connect("src/auth/users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username, role
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user