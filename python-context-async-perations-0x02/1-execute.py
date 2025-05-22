import  sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params = None):
        self.query = query
        self.db_name = db_name
        self.params = params or ()

    def __enter__(self):
        connection = sqlite3.connect(self.db_name)
        self.conn = connection
        cursor = connection.cursor()
        cursor.execute(self.query, self.params)
        result = cursor.fetchall()
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
        finally:
            self.conn.close()
            return None

with ExecuteQuery("users.db","SELECT * FROM users where age > ?", (25,)) as users:
    print(users)