import sqlite3
import random
from datetime import datetime, timedelta

# Connect to SQLite
connection = sqlite3.connect("Facilities.db")

# Create a cursor object to insert records and create tables
cursor = connection.cursor()

# Create the table if not exists
table_info = """
CREATE TABLE IF NOT EXISTS FACILITY (
    FAC_ID INTEGER PRIMARY KEY,
    FAC_NAME VARCHAR(100),
    STAFF_NAME VARCHAR(50),
    STAFF_ID INTEGER,
    FAC_TYPE VARCHAR(50),
    FAC_STATUS VARCHAR(50),
    FAC_ADDRESS VARCHAR(200),
    FAC_CITY VARCHAR(50),
    FAC_AVAIL_BEDS INTEGER,
    FAC_START_DATE DATE,
    FAC_EXIT_DATE DATE
);
"""
cursor.execute(table_info)

# Sample hospital names
hospital_names = [
    'Cedars-Sinai Medical Center',
    'UCLA Medical Center',
    'Stanford Health Care',
    'California Pacific Medical Center',
    'Sharp Memorial Hospital',
    'Scripps Mercy Hospital',
    'Huntington Hospital'
]

# Generate sample data for insertion
faculty_data = []

for i in range(2001, 4001):  # Generate 2000 records
    fac_id = i
    fac_name = random.choice(hospital_names)
    staff_name = random.choice(['Robert.jr', 'Jack sparrow', 'John cena', 'Jack daniels'])
    staff_id = random.randint(1000, 7000)  # Corrected range
    fac_type = random.choice(['GGH', 'SHG', 'GH'])
    fac_status = random.choice(['Active', 'Inactive'])
    fac_address = f"{random.randint(1, 1000)} {random.choice(['Main St', 'Elm St', 'Oak St','mosc st','dhada st'])}"
    fac_city = random.choice(['New York', 'Los Angeles','Stanford','San Francisco','Newport Beach'])
    fac_avail_beds = random.randint(10, 100)
    fac_start_date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
    fac_exit_date = (datetime.now() + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
    faculty_data.append((fac_id, fac_name, staff_name, staff_id, fac_type, fac_status, fac_address, fac_city, fac_avail_beds, fac_start_date, fac_exit_date))

# Insert sample data
cursor.executemany("INSERT INTO FACILITY VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", faculty_data)

# Display the inserted records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM FACILITY ")
for row in data:
    print(row)

# Commit your changes to the database
connection.commit()
connection.close()