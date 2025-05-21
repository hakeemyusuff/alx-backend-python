import sqlite3
import functools
with_db_connection = __import__("1-with_db_connection").with_db_connection

def transactional(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            conn = args[0]
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except sqlite3.Error as err:
            conn.rollback()
            print(f"Unable to update: {err}")
            return None
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (new_email, user_id))


update_user_email(
    user_id="cc2ab582-ff3b-4791-b5e2-dee64e0f44c3",
    new_email="cartwright@hotmail.com",
)
