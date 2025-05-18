from seed import connect_to_prodev

def stream_user_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT age FROM user_data")
        for age in cursor:
            yield age
    finally:
        cursor.close()
        connection.close()
        
def calc_avg():
    no_of_age = 0
    age_total=0
    
    ages = stream_user_ages()
    for age in ages:
        age_total += age[0]
        no_of_age += 1
        
    avg_age = age_total / no_of_age
    print(f"Average age of users: {avg_age}")

calc_avg()