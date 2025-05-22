import time
import sqlite3
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection


def retry_on_failure(retries:int, delay:int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"Error: {err}")
                    if attempt < retries - 1:
                        print(f"retrying in {delay} seconds.")
                        time.sleep(delay)
                    else:
                        print("All retries failed.")    
        return wrapper
    return decorator
    


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

users = fetch_users_with_retry()
print(users)