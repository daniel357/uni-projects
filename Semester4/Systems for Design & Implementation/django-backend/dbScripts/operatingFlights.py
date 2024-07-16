# import random
# import pytz
# from faker import Faker
# import psycopg2
# from psycopg2 import sql
#
# fake = Faker()
#
# # connect to the database
# conn = psycopg2.connect(
#     host="ec2-13-51-255-34.eu-north-1.compute.amazonaws.com",  # change the host each time you restart the server
#     port="5432",
#     database="airport_management",
#     user="db_user",
#     password="db_pass"
# )
# cur = conn.cursor()
#
# # delete all the existing records
# cur.execute('TRUNCATE TABLE base_operatingflights RESTART IDENTITY CASCADE;')
#
# # generate new records to insert
# batch_size = 1000
# num_batches = 10000
# total_records = batch_size * num_batches
#
# for i in range(num_batches):
#     print(f'Generating batch {i + 1}/{num_batches}')
#     flight_id = fake.random_int(min=i * 100 + 1, max=(i + 1) * 100)
#     '''
#     set flight id such that it changes every 1000 entries and there will be no need to check for 2 same pair (flight_id,passenger_id)
#     '''
#     values = []
#     for j in range(batch_size):
#         # generate fake data for ticket fields
#         aircraft_id = fake.random_int(min=j * 1000 + 1, max=(j + 1) * 1000)
#         '''
#             aircraft id each time will be a value that for each iteration of j will be multiplied by 1000 therefore no conflicts will appear
#         '''
#         distance = random.randint(10, 100000)
#
#         # escape any special characters or quotes in the data
#         values.append(
#             sql.SQL("({}, {}, {})").format(
#                 sql.Literal(flight_id),
#                 sql.Literal(aircraft_id),
#                 sql.Literal(distance),
#             )
#         )
#
#     # join the values and generate the SQL statement
#     sql_statement = sql.SQL(
#         "INSERT INTO base_operatingflights (flight_id, aircraft_id, distance) VALUES {}").format(
#         sql.SQL(", ").join(values)
#     )
#
#     # execute the SQL statement
#     cur.execute(sql_statement)
#
# # commit the changes and close the cursor and connection
# conn.commit()
# cur.close()
# conn.close()
