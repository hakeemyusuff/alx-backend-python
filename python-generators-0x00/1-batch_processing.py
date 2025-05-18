from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """
    Generator function that fetches users from the database in batches.

    Connects to the 'prodev' database and retrieves user data in chunks
    of a specified batch size. Each batch is yielded as a list of dictionaries.
    Automatically closes the database connection and cursor after processing.

    Args:
        batch_size (int): The number of user records to fetch per batch.

    Yields:
        List[Dict[str, Any]]: A batch of user records from the database.
    """
    
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    try:
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        cursor.close()
        connection.close()


def batch_processing(batch_size):
    """
    Processes batches of users retrieved from the database.

    Iterates through each user in the yielded batches and prints
    those who are over the age of 25.

    Args:
        batch_size (int): The number of user records to process per batch.
    """
    
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
