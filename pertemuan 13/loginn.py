admin = [{"username": "admin", "password": "admin123"}]


def login(username, password):
    for masuk in admin:
        if masuk["username"] == username and masuk["password"] == password:
            return True
    return False


while True:
    username = input("masukan username : ")
    password = input("masukan password : ")
    if login(username, password) == True:
        while True:
            menu()
            inputMenu = int(input("masukan menu yang di pilih"))
            if inputMenu == 1:
                nama = input("masukan nama crush: ")
                identitas = input("masukan identitas : ")
                menambahkanKaryawan(nama, identitas)
            elif inputMenu == 2:
                januari = input("masukan jam lembur januari : ")
                februari = input("masukan jam lembur bulan februari : ")
                maret = input("masukan jam lembur bulan maret : ")
                identitas = input("masukan id : ")
                jamLembur(identitas, januari, februari, maret)
            elif inputMenu == 3:
                identitas = input("masukan id : ")
                nama = input("masukan nama : ")
                editKaryawan(identitas, nama)
            elif inputMenu == 4:
                identitas = input("masukan id : ")
                hapusCrush(identitas)
            elif inputMenu == 5:
                identitas = input("masukan id : ")
                lihatKaryawan(identitas)
            elif inputMenu == 6:
                identitas = input("input id : ")
                visual(identitas)
            elif inputMenu == 7:
                print("keluar data base")
                break
    else:
        print("username atau password salah")
