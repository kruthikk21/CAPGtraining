import mysql.connector

# Establish connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

# Check connection
if con.is_connected():
    print("Connected to MySQL Server")

cursor = con.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("Database created successfully (if not exists)")

# Use the database
cursor.execute("USE mydatabase")

# Create table if it doesn't exist
cursor.execute(
    """CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        grade VARCHAR(20)
    )"""
)
print("Table created successfully (if not exists)")

# Insert data
sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
values = ("Alice", 20, "A")
cursor.execute(sql, values)
con.commit()  # Save changes
print("Data inserted successfully")

# Fetch all records
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
print("Student Records:")
for row in result:
    print(row)

# Update data
cursor.execute("UPDATE students SET grade = 'B' WHERE name = 'Alice'")
con.commit()
print("Data updated successfully")

cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
print("Student Records:")
for row in result:
    print(row)

# Close cursor and connection
cursor.close()
con.close()
print("Connection closed")
