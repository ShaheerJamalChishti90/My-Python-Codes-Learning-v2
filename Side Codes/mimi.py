import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

# Insert query
query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s);"
values = ("value1", "value2")

cursor.execute(query, values)
connection.commit()

print(cursor.rowcount, "record inserted.")

# Close the connection
cursor.close()
connection.close()
