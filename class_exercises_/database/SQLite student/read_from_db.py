import sqlite3
conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

read_query = """
    SELECT * FROM students
    WHERE firstname = 'Jacqueline';"""

all_students = cursor.execute(read_query).fetchall()
print(all_students)

conn.commit()
conn.close()

#howdy