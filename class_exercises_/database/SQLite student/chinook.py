import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

#gather data on cutomers and put in list
customers = []
query = '''SELECT FirstName, LastName, Address FROM customers;'''

cursor.execute(query)
customer = cursor.fetchall()
for item in customer:
    customers.append(item)

#gather tracks available on protected ACC audio file and put in list
tracks = []
query2 = '''SELECT * FROM tracks
            WHERE MediaTypeID = 2;'''

cursor.execute(query2)
track = cursor.fetchall()
for item in track:
    tracks.append(item)

#creates a list of cities and the number of customers in the city, shows in order
cities = []
cities_total = []
seen = set()
query3 = '''SELECT City FROM customers;'''

cursor.execute(query3)
city = cursor.fetchall()
for item in city:
    cities.append(item[0].strip().title())

for item in cities:
    if item not in seen:
        seen.add(item)


cities_total = [[city, cities.count(city)] for city in seen]
cities_total = sorted(cities_total, key=lambda x: x[1], reverse=True)

#inserts media into media_types table
"""
query4 = '''INSERT INTO media_types (MediaTypeID, Name)
            VALUES (6, "Windows Media Audio"),
            (7, "FLAC audio file");'''
cursor.execute(query4)
"""
#the quotations are there so i don't run it multiple times and create duplicates

#creates a list of the employees reporting to Nancy Edwards , her ID is 2

query5 = '''SELECT LastName, FirstName FROM employees
            WHERE ReportsTo = 2;'''

cursor.execute(query5)
reportsto = cursor.fetchall()


conn.commit()
conn.close()
