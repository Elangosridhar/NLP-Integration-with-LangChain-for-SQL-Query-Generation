import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

# Now you can execute SQL queries using the cursor object
# For example, you can fetch all records from the FACILITY table
cursor.execute("SELECT * FROM FACILITY")
data = cursor.fetchall()
for row in data:
    print(row)

# Don't forget to close the connection when done
connection.close()
