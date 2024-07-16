import random
import pytz
from faker import Faker
import psycopg2
from psycopg2 import sql

fake = Faker()

# connect to the database
conn = psycopg2.connect(
    host="ec2-13-49-231-160.eu-north-1.compute.amazonaws.com",
    port="5432",
    database="airport_management",
    user="db_user",
    password="db_pass"
)
cur = conn.cursor()

# delete all the existing records
cur.execute('TRUNCATE TABLE base_ticket RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 10000
total_records = batch_size * num_batches

# list to keep track of the (flight_id, passenger_id) pairs
# used_pairs = set()

for i in range(num_batches):
    print(f'Generating batch {i + 1}/{num_batches}')
    flight_id = fake.random_int(min=i * 100 + 1, max=(i + 1) * 100)
    '''
    set flight id such that it changes every 1000 entries and there will be no need to check for 2 same pair (flight_id,passenger_id)
    '''
    values = []
    for j in range(batch_size):
        # generate fake data for ticket fields
        passenger_id = fake.random_int(min=j * 1000 + 1, max=(j + 1) * 1000)
        '''
            passenger id each time will be a value that for each iteration of j will be multiplied by 1000 therefore no conflicts will appear
        '''
        # while (flight_id, passenger_id) in used_pairs:
        #     flight_id = fake.random_int(min=1, max=1000000)
        #     passenger_id = fake.random_int(min=1, max=1000000)
        seat_row = random.randint(1, 100)
        seat_letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        seat_number = f"{seat_row}-{seat_letter}"
        booking_date = fake.date_between(start_date='-1y', end_date='today')

        # add the (flight_id, passenger_id) pair to the used_pairs list
        # used_pairs.add((flight_id, passenger_id))

        # escape any special characters or quotes in the data
        values.append(
            sql.SQL("({}, {}, {}, {})").format(
                sql.Literal(flight_id),
                sql.Literal(passenger_id),
                sql.Literal(seat_number),
                sql.Literal(booking_date),
                # sql.SQL("now() at time zone 'utc'")
            )
        )

    # join the values and generate the SQL statement
    sql_statement = sql.SQL(
        "INSERT INTO base_ticket (flight_id, passenger_id, seat_number, booking_date) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
