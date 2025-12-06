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


conn.commit()
conn.close()

#[2:-3]