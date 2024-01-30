import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="cobadata"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM mahasiswa")
hasil = cursor.fetchall()
print(hasil)
