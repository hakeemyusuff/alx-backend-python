import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect("users.db")
            func(conn, *args, **kwargs)
        finally:
            conn.close()
        return 
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

user = get_user_by_id(user_id="2496a00c-3911-45bb-9ebf-d41e57948a8f")
print(user)
