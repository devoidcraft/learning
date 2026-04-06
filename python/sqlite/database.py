import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Insert data (correct way)
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("aditya", 80))

conn.commit()
conn.close()

print("Database & table created successfully 🚀")
