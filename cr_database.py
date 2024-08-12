import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    father_name TEXT,
    contact_no TEXT,
    email_address TEXT,
    date_of_birth TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
