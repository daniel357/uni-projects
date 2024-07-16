import psycopg2
from faker import Faker
from psycopg2 import sql
from django.utils import timezone

fake = Faker()

conn = psycopg2.connect(
    host="ec2-16-170-7-214.eu-north-1.compute.amazonaws.com",
    port="5432",
    database="airport_management",
    user="db_user",
    password="db_pass"
)
cur = conn.cursor()

# delete all the existing records
cur.execute('TRUNCATE TABLE base_passenger RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i + 1}/{num_batches}')

    values = []
    for j in range(batch_size):
        # generate fake data for passenger fields
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()[:20]
        citizenship = fake.country()
        description = "I am from " + fake.city()

        # escape any special characters or quotes in the data
        values.append(
            sql.SQL("({}, {}, {}, {}, {},{})").format(
                sql.Literal(first_name),
                sql.Literal(last_name),
                sql.Literal(email),
                sql.Literal(phone_number),
                sql.Literal(citizenship),
                sql.Literal(description),
            )
        )

    # join the values and generate the SQL statement
    sql_statement = sql.SQL(
        "INSERT INTO base_passenger (first_name, last_name, email, phone_number, citizenship,description) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
