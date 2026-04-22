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
my_students = [
    ("abhi", 70),
    ("madhu", 21),
    ("me", 98),
    ("ram", 5000),
    ("hemsworth", 57),
]


# cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("aditya", 80))
# VALUES (?, ?) so input taken as data not code'

cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", my_students)


# query the database
cursor.execute("SELECT*FROM students")
# cursor.fetchone()
# cursor.fetchmany(3)
iteams = cursor.fetchall()
for iteam in iteams:
    print(iteam)


cursor.execute("SELECT*FROM students WHERE age<50")
print(cursor.fetchall())

conn.commit()
conn.close()

print("Database & table created successfully 🚀")
