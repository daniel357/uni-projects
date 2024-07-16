import psycopg2
from faker import Faker
from psycopg2 import sql

fake = Faker()

conn = psycopg2.connect(
    host="ec2-13-50-17-123.eu-north-1.compute.amazonaws.com",
    port="5432",
    database="airport_management",
    user="db_user",
    password="db_pass"
)
cur = conn.cursor()

# delete all the existing records
cur.execute('TRUNCATE TABLE base_airport RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')

    values = []
    for j in range(batch_size):
        # generate fake data for airport fields
        name = fake.name()[:100] + " Airport"
        city = fake.city()
        country = fake.country()
        timezone = fake.timezone()
        elevation = fake.random_int(min=0, max=5000)
        capacity = fake.random_int(min=0, max=5000)
        noGates = fake.random_int(min=0, max=20)
        noTerminals = fake.random_int(min=0, max=5)

        # escape any special characters or quotes in the data
        values.append(
            sql.SQL("({}, {}, {}, {}, {}, {}, {}, {})").format(
                sql.Literal(name),
                sql.Literal(city),
                sql.Literal(country),
                sql.Literal(timezone),
                sql.Literal(elevation),
                sql.Literal(capacity),
                sql.Literal(noGates),
                sql.Literal(noTerminals)
            )
        )

    # join the values and generate the SQL statement
    sql_statement = sql.SQL("INSERT INTO base_airport (name, city, country, timezone, elevation, capacity, no_gates, no_terminals) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
