import psycopg2
from faker import Faker
from psycopg2 import sql
from django.utils import timezone
# from myapp.models import Airline

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
cur.execute('TRUNCATE TABLE base_airline RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')

    values = []
    for j in range(batch_size):
        # generate fake data for airline fields
        name = fake.company()[:100]
        headquarters = fake.city()
        website = fake.url()
        established_date = fake.date_between(start_date='-50y', end_date='today')
        revenue = fake.random_int(min=0, max=1000000000)
        num_employees = fake.random_int(min=0, max=100000)

        # escape any special characters or quotes in the data
        values.append(
            sql.SQL("({}, {}, {}, {}, {}, {})").format(
                sql.Literal(name),
                sql.Literal(headquarters),
                sql.Literal(website),
                sql.Literal(established_date),
                sql.Literal(revenue),
                sql.Literal(num_employees)
            )
        )

    # join the values and generate the SQL statement
    sql_statement = sql.SQL("INSERT INTO base_airline (name, headquarters, website, established_date, revenue, num_employees) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
