import sqlite3
import random
from faker import Faker

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

paramterised_insert_query = """
    INSERT INTO students (firstname, lastname, age, gender)
    VALUES (?, ?, ?, ?);
"""
fake = Faker('en_GB')

student_data = []
for _ in range(100):
    gender = random.choice(['Male', 'Female'])
    if gender == 'Female':
        firstname = fake.first_name_female()
        lastname = (fake.last_name_female())[0]
    else:
        firstname = fake.first_name_male()
        lastname = (fake.last_name_female())[0]
    age = random.randint(11, 18)
    student_data.append([firstname, lastname, age, gender])

cursor.executemany(paramterised_insert_query, student_data)
conn.commit()
conn.close()

#howdy





