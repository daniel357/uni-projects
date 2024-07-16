import random
import sqlite3

import psycopg2
from faker import Faker
from psycopg2 import sql
from django.utils import timezone

# from myapp.models import Airline

fake = Faker()
# conn = sqlite3.connect('C:\\Users\\User\\Desktop\\lab-5x-917ZnaceniDaniel\\django-backend\\db.sqlite3')
conn = psycopg2.connect(
    host="127.0.0.1",
    port="",
    database="db.sqlite3",
    user="",
    password=""
)
cur = conn.cursor()

# delete all the existing records
cur.execute('TRUNCATE TABLE base_aircraft RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 10
num_batches = 10
total_records = batch_size * num_batches
models = ['A320', 'B737', 'A380', 'B747', 'B777', 'E190', 'CRJ700']
for i in range(num_batches):
    print(f'Generating batch {i + 1}/{num_batches}')

    values = []
    for j in range(batch_size):
        # generate fake data for aircraft fields
        name = "Aircraft" + fake.word()[:100]
        manufacturer = fake.company()[:100]
        # model = fake.word()[:100]
        model = fake.word()[:3].upper() + random.choice(models)[1:]

        max_speed = fake.random_int(min=100, max=1000)
        seating_capacity = fake.random_int(min=50, max=500)
        fuel_capacity = fake.random_int(min=5000, max=50000)
        wing_span = fake.random_int(min=20, max=100)
        length = fake.random_int(min=30, max=150)
        no_engines = fake.random_int(min=1, max=4)
        airline_name_id = fake.random_int(min=1, max=1000000)

        # escape any special characters or quotes in the data
        values.append(
            sql.SQL("({}, {}, {}, {}, {}, {}, {}, {}, {}, {})").format(
                sql.Literal(name),
                sql.Literal(manufacturer),
                sql.Literal(model),
                sql.Literal(max_speed),
                sql.Literal(seating_capacity),
                sql.Literal(fuel_capacity),
                sql.Literal(wing_span),
                sql.Literal(length),
                sql.Literal(no_engines),
                sql.Literal(airline_name_id)
            )
        )

    # join the values and generate the SQL statement
    sql_statement = sql.SQL(
        "INSERT INTO base_aircraft (name, manufacturer, model, max_speed, seating_capacity, fuel_capacity, wing_span, length, no_engines, airline_name_id) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
