import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Define student data
students = [
    ('Alice Johnson', 'Robert Johnson', '1234567890', 'alice.johnson@example.com', '2000-01-01'),
    ('Bob Smith', 'William Smith', '2345678901', 'bob.smith@example.com', '1999-02-02'),
    ('Charlie Brown', 'James Brown', '3456789012', 'charlie.brown@example.com', '1998-03-03'),
    ('Diana Prince', 'George Prince', '4567890123', 'diana.prince@example.com', '1997-04-04'),
    ('Eve Adams', 'Michael Adams', '5678901234', 'eve.adams@example.com', '1996-05-05')
]

# Insert data into the table
cursor.executemany('''
INSERT INTO students (name, father_name, contact_no, email_address, date_of_birth)
VALUES (?, ?, ?, ?, ?)
''', students)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Student details inserted successfully.")
