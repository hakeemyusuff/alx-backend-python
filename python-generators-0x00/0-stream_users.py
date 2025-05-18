import mysql.connector
from seed import connect_to_prodev
# def connect_to_prodev():
#     """
#     Connect specifically to ALX_Prodev database

#     Returns:
#         connection: MySQL connection object to ALX_prodev or None if connection fails
#     """
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="@Folarinwa25",
#             database="ALX_Prodev",
#         )
#         return connection
#     except mysql.connector.Error as err:
#         print(f"Error connecting to the ALX_prodev database: {err}")
#         return None


def stream_users():
    connection = connect_to_prodev()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM user_data")
            rows = cursor.fetchall()
            for row in rows:
                yield row
        finally:
            cursor.close()
            connection.close()
