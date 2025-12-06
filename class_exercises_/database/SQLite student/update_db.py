import sqlite3

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

update_query = """
    UPDATE students
    SET firstname = 'Zebra'
    WHERE firstname = 'Debra';
    """

cursor.execute(update_query)
conn.commit()
conn.close()