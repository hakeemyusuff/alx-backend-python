import os
import csv
import uuid
import mysql.connector
import sqlite3


def connect_db():
    """
    Connect to the MySQL database server

    Returns:
        connection: MySQL connection object or None if connection fails
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Folarinwa25",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL server: {err}")
        return None


def create_database(connection):
    """
    Create the ALX_prodev database if it doesn't exist

    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_Prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def connect_to_prodev():
    """
    Connect specifically to ALX_Prodev database

    Returns:
        connection: MySQL connection object to ALX_prodev or None if connection fails
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Folarinwa25",
            database="ALX_Prodev",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the ALX_prodev database: {err}")
        return None


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data(
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                age INTEGER NOT NULL,
                INDEX (user_id)
            )
            """
        )
        connection.commit()
        cursor.close()
        print(f"Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
        return None


def insert_data(connection, csv_file):
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found")
        return

    try:
        cursor = connection.cursor()

        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                if len(row) >= 3:
                    user_id = str(uuid.uuid4())
                    name = row[0]
                    email = row[1]
                    age = row[2]

                    cursor.execute(
                        "SELECT user_id FROM user_data WHERE user_id = %s", (user_id,)
                    )
                    if not cursor.fetchone():
                        cursor.execute(
                            "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                            (user_id, name, email, age),
                        )

        connection.commit()
        cursor.close()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error Inserting data: {err}")
    except Exception as e:
        print(f"Error processing csv file: {e}")
