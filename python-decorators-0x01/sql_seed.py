def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS users(
                       user_id CHAR(36) PRIMARY KEY,
                       name VARCHAR(255) NOT NULL,
                       email VARCHAR(255) UNIQUE NOT NULL,
                       age INTEGER NOT NULL
                   )
                   """
    )
    conn.commit()
    cursor.close()
    conn.close


create_table()


def seed_data(csv_file):
    conn = sqlite3.connect("users.db")

    if not os.path.exists(csv_file):
        print(f"{csv_file} doesn't exist")
        return

    try:
        cursor = conn.cursor()
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                user_id = str(uuid.uuid4())
                name = row[0]
                email = row[1]
                age = row[2]

                cursor.execute(
                    "SELECT user_id FROM users WHERE user_id = ?", (user_id,)
                )

                if not cursor.fetchone():
                    cursor.execute(
                        "INSERT INTO users (user_id, name, email, age) VALUES (?, ?, ?, ?)",
                        (user_id, name, email, age),
                    )

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")
    except sqlite3.Error as err:
        print(f"Error inserting data: {err}")
    except Exception as e:
        print(f"Error processing csv file: {e}")


seed_data("user_data.csv")
