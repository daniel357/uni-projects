# from datetime import timedelta
# import random
#
# from django.conf import settings
# from django.utils import timezone
# import pytz
# from faker import Faker
# import psycopg2
# from psycopg2 import sql
# from psycopg2.extras import execute_values
#
# fake = Faker()
#
# # connect to the database
# conn = psycopg2.connect(
#     host="ec2-16-170-35-243.eu-north-1.compute.amazonaws.com",
#     port="5432",
#     database="airport_management",
#     user="db_user",
#     password="db_pass"
# )
# conn.autocommit = True
# cur = conn.cursor()
#
# # delete all the existing records
# cur.execute('TRUNCATE TABLE base_ticket RESTART IDENTITY CASCADE;')
#
# # generate new records to insert
# batch_size = 1000
# num_batches = 10000
# total_records = batch_size * num_batches
#
# # set the timezone to use
# tz = pytz.timezone('Europe/London')
#
# # list to keep track of the (flight_id, passenger_id) pairs
# used_pairs = set()
#
# # prepare the SQL statement for bulk insert
# sql_statement = sql.SQL(
#     "INSERT INTO base_ticket (flight_id, passenger_id, seat_number, booking_date) VALUES %s")
#
# # insert records in batches
# for i in range(num_batches):
#     print(f'Generating batch {i + 1}/{num_batches}')
#
#     batch_values = []
#     for j in range(batch_size):
#         # generate fake data for ticket fields
#         flight_id = fake.random_int(min=1, max=1000000)
#         passenger_id = fake.random_int(min=1, max=1000000)
#         while (flight_id, passenger_id) in used_pairs:
#             flight_id = fake.random_int(min=1, max=1000000)
#             passenger_id = fake.random_int(min=1, max=1000000)
#         seat_row = random.randint(1, 100)
#         seat_letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
#         seat_number = f"{seat_row}-{seat_letter}"
#         booking_date = fake.date_between(start_date='-1y', end_date='today')
#
#         # add the (flight_id, passenger_id) pair to the used_pairs list
#         used_pairs.add((flight_id, passenger_id))
#
#         # append the values to the batch_values list
#         batch_values.append((flight_id, passenger_id, seat_number, booking_date))
#
#     # execute the SQL statement with the batch_values
#     execute_values(cur, sql_statement, batch_values, page_size=batch_size)
#
# # close the cursor and connection
# cur.close()
# conn.close()
