import sqlite3

class DatabaseConnection:
    """
    Manages a context-based SQLite database connection.

    This class provides functionality to establish a SQLite database connection
    using a context manager. It ensures that the database connection is properly
    opened and safely closed after performing operations, committing changes if
    successful or rolling back in case of an error.

    Attributes:
        db_name (str): The name of the SQLite database file to connect to.
        conn (sqlite3.Connection): The SQLite connection object used for database
            operations within the context.
    """
    def __init__(self, db_name):
        self.db_name = db_name
    def __enter__(self):
        connection = sqlite3.connect(self.db_name)
        self.conn = connection
        return connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
        finally:
                self.conn.close()
                return None


with DatabaseConnection("users.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
