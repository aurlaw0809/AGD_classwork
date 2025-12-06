import sqlite3

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

#write SQL command to create a student table
create_students_table = '''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
    );'''

#execute the command
cursor.execute(create_students_table)
conn.close()