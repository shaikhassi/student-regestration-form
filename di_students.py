import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Fetch all student records
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Display student records
for row in rows:
    print(row)

# Close the connection
conn.close()
