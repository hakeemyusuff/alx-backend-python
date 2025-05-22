import time
import sqlite3
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs["query"]
        if query in query_cache:
            return query_cache[query]
        else:
            result = func(*args, **kwargs)
            query_cache[query] = result
            return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#first call with cache result
users = print(fetch_users_with_cache(query="SELECT * FROM users"))

#Second call wwill use cached results
users_again = print(fetch_users_with_cache(query="SELECT * FROM users"))