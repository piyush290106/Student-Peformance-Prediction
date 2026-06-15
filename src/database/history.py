import sqlite3
import pandas as pd


def save_prediction(
    username,
    gender,
    race,
    education,
    lunch,
    prep,
    math_score,
    reading_score,
    writing_score,
    average_score
):

    conn = sqlite3.connect(
        "src/auth/users.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history
        (
            username,
            gender,
            race,
            education,
            lunch,
            prep,
            math_score,
            reading_score,
            writing_score,
            average_score
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,
        (
            username,
            gender,
            race,
            education,
            lunch,
            prep,
            math_score,
            reading_score,
            writing_score,
            average_score
        )
    )

    conn.commit()
    conn.close()


def get_history(username):

    conn = sqlite3.connect(
        "src/auth/users.db"
    )

    query = f"""
    SELECT *
    FROM prediction_history
    WHERE username='{username}'
    ORDER BY created_at DESC
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df