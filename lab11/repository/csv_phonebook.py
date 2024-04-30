import psycopg2
import csv
conn = psycopg2.connect(
    host='localhost', 
    dbname='phonebook', 
    user='postgres', 
    password='OvyNx7$1'
)

def phone_book_proccess():
    print("1 - CSV file; 2 - Console")
    variant = int(input("Write variant to write data into table: "))

    filename = 'phonebook.csv'
    if variant == 1:
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                firstname, lastname, phone_number = row

                cur.execute("""INSERT INTO resident_data (firstname, lastname, phone_number) VALUES
                                (%s, %s, %s) ON CONFLICT (phone_number) DO NOTHING""", (firstname, lastname, phone_number))

                conn.commit()
        print("Data inserted successfully from CSV.")
    if variant == 2:
        print("1 - Add into phone book; 2 - Update; 3 - Query data; 4 - Delete from phonebook; 5 - Paginate; 6 - Get record by pattern")
        variant = int(input("Write variant to write data into table: "))
        if variant == 1:
            insert_console()
        if variant == 2:
            update_info()
        if variant == 3:
            query_data()
        if variant == 4:
            delete_data()
        if variant == 5:
            get_paginated_records()
        if variant == 6:
            get_record_by_patern()

def insert_console():
    i = 0
    qnt = int(input("How many person would like to write: "))
    if qnt < 0:
        print("Wrong quantity")
        insert_console()
    else:    
        while i < qnt:
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            phone_number = input("Enter phone number: ")
            cur.execute("""INSERT INTO resident_data (firstname, lastname, phone_number) VALUES
                                (%s, %s, %s) ON CONFLICT (phone_number) DO NOTHING""", (firstname, lastname, phone_number))
            i+=1
            conn.commit()
        print("Data inserted successfully from console")
    
def update_info():
    phone_number = input("Enter phone_number that desirable to change: ")
    new_firstname = input("Enter new firstname: ")
    new_phone_number = input("Enter new phone number: ")
    cur.execute("""UPDATE resident_data
                SET firstname = %s, phone_number = %s
                WHERE phone_number = %s""", (new_firstname, new_phone_number, phone_number))
    conn.commit()
    print("Data updated successfully")
    
def query_data():
    print("1 - Filter all; 2 - Filter by option")
    variant_q = int(input("Write option to filter: "))
    if variant_q == 1:
        cur.execute("SELECT * FROM resident_data")
        rows = cur.fetchall()
        if rows:
            print("Query results:")
            for row in rows:
                print(row)
    elif variant_q == 2:
        print("Write option: First name, Last name, Phone number")
        filter_by = input("Write option to filter: ")
        cur.execute("SELECT * FROM resident_data WHERE firstname = %s OR lastname = %s OR phone_number = %s",
                    (filter_by, filter_by, filter_by))
        rows = cur.fetchall()
        if rows:
            print("Query results:")
            for row in rows:
                print(row)
        else:
            print("No results found.")
    else:
        print("Wrong variant")
        query_data()

def delete_data():
    delete_ = input("Write first name, last name or phone number to delete (Pick only one): ")
    cur.callproc('delete_data_by_name_or_phone',(delete_))
    conn.commit()
    print("Data deleted successfully.")

def get_record_by_patern():
    pattern = input("Write firstname, lastname or phone number: ")
    cur.execute("SELECT * FROM resident_data WHERE firstname LIKE %s OR lastname LIKE %s OR phone_number LIKE %s",
                (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    records = cur.fetchall()
    print("Records matching pattern: ")
    for record in records:
        print(record)

def get_paginated_records():
    limit_val = int(input("Enter limit value: "))
    offset_val = int(input("Enter offset value: "))
    cur.callproc('get_paginated_records', (limit_val, offset_val))
    records = cur.fetchall()
    if records:
        print("Paginated records:")
        for record in records:
            print(record)
    else:
        print("No records found.")

cur = conn.cursor()

print("Would you like create new Phone Book?")
var = input("Y/N:")

if var == "Y" or var == "y":

    cur.execute('DROP TABLE resident_data;')

    conn.commit()

    cur.execute("""CREATE TABLE resident_data (
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                phone_number VARCHAR(20) PRIMARY KEY
    )
    """)

    conn.commit()

    phone_book_proccess()
if var == "N" or var == "n":
    phone_book_proccess()
else:
    print("Wrong option")