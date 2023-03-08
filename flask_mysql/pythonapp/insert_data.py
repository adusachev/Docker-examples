
import mysql.connector
import csv

# connect database
connection = mysql.connector.connect(
    user="myuser",
    password="mypass",
    host="mysql", 
    port="3306", 
    database="db"
)
print('Database connected \n')


# read csv data
new_values = []
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        val = (row[0], row[1])
        new_values.append(val)

# insert data to our table
cursor = connection.cursor()
sql = "INSERT INTO people_table(name, age) VALUES (%s, %s)"
cursor.executemany(sql, new_values)
connection.commit()
print(cursor.rowcount, "rows were inserted from data.csv \n")

# data output to stdout
cursor.execute('Select * FROM people_table')
people = cursor.fetchall()
connection.close()
print('Inserted data:')
print(people)
