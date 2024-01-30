import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="5230411122"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM guru")
hasil = cursor.fetchall()

for i in hasil:
    print(i)

cursor = connection.cursor()
cursor.execute("SELECT * FROM siswa")
hasil = cursor.fetchall()
for i in hasil:
    print(i)
