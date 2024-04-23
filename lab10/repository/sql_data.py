# SQL

# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phonebook', 
    user='postgres', 
    password='OvyNx7$1'
    )

# Create a cursor to work with the database
cur = conn.cursor()


# Create a new table
cur.execute("""CREATE TABLE resident_data (
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

conn.commit()

# Create new students
cur.execute("""INSERT INTO resident_data (firstname, lastname, phone_number) VALUES 
            ('Ivanov', 'Ivan', '+77777777777'),
            ('Demetyenko', 'Vlad' , '+77011071177'),
            ('Pirozhkova', 'Dariya', '+77088887887'),
            ('Parker', 'Mark', '+77019874554');
""")

conn.commit()

# Get students
cur.execute('SELECT firstname, lastname, phone_number FROM resident_data')

print(cur.fetchall())
print(cur.fetchall())

cur.execute('SELECT firstname, lastname, phone_number FROM resident_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())


# Update students
cur.execute("""UPDATE resident_data
            SET firstname = 'Marina'
            WHERE phone_number = '+77088887887';
""")

conn.commit()
