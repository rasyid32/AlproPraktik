import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    db="test",
)

cursor = conn.cursor()


def login(username, password) -> bool:
    sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()

    if result == None:
        return False
    else:
        return True


def print_menu_guest():
    print("1. Login")
    print("2. Keluar")


def print_menu_user():
    pass


while True:
    print_menu_guest()
    menu = input("Masukan pilihan menu [1-2]: ")

    if menu == "1":
        username = input("Masukan username : ")
        password = input("Masukan password : ")

        if login(username, password) == True:
            while True:
                print_menu_user()
                # menu sajdksajdlkaskd;
        else:
            print("Login Gagal")

    elif menu == "2":
        break
    else:
        print("Pilihan Tidak Ada")
