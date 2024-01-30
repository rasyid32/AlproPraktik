import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="5230411121"
)

cursor = db.cursor()


def print_menu():
    print("\n1. Tampilkan Siswa")
    print("2. Tampilkan Guru")
    print("3. Keluar")


def print_students():
    cursor.execute("SELECT * FROM students")
    list_mahasiswa = cursor.fetchall()
    print("")
    for mahasiswa in list_mahasiswa:
        print(f"{mahasiswa[1]} - {mahasiswa[3]} Tahun - {mahasiswa[2]}")


def print_teachers():
    cursor.execute("SELECT * FROM teachers")
    list_guru = cursor.fetchall()
    print("")
    for guru in list_guru:
        print(f"{guru[1]} - {guru[2]}")


while True:
    print_menu()
    menu = input("Masukan pilihan menu [1-3] : ")
    if menu == "1":
        print_students()
    elif menu == "2":
        print_teachers()
    elif menu == "3":
        break
    else:
        print("\n=================")
        print("Pilihan Tidak Ada")
        print("=================")
