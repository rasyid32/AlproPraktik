import mysql.connector
import matplotlib.pyplot as plt


def connectionDatabase():
    connector = mysql.connector.connect(
        host="localhost", user="root", password="", database="uty"
    )
    if connector.is_connected:
        print("Database terkoneksi")
        return connector
    else:
        print("Database gagal terkoneksi")
        return False


def insertData(nim, nama, mtk, ipa, agama):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "INSERT INTO nilai (nim, nama, mtk, ipa, agama) VALUES (%s, %s, %s,%s,%s)"
        data = (nim, nama, mtk, ipa, agama)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambah")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def selectData(inputUser):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "SELECT agama, mtk, ipa FROM nilai WHERE nim = %s"
        search = (inputUser,)
        cursor.execute(sql, search)
        result = cursor.fetchall()
        if result:
            print("data ditemukan")
            for i in result:
                matkul = ("agama", "mtk", "ipa")
                hasil = i
                plt.bar(matkul, hasil)
                plt.show()
        else:
            print("data tidak ditemukan")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def updateData(nama, mtk, agama, ipa, nim):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = (
            "UPDATE nilai SET nama = %s, mtk = %s , agama= %s , ipa = %s WHERE nim = %s"
        )
        data = (nama, mtk, agama, ipa, nim)
        cursor.execute(sql, data)
        conn.commit()
        print("data telah diubah")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def deleteData(nim):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "DELETE FROM nilai WHERE nim = %s"
        data = (nim,)
        cursor.execute(sql, data)
        conn.commit()
        print("data telah dihapus")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def menu():
    print("1. Tampilkan visual")
    print("2. input data")
    print("3. edit data")
    print("4. hapus data")


while True:
    menu()
    input_menu = int(input("pilih [1-4] : "))
    if input_menu == 1:
        input_nim = input("masukkan nim : ")
        selectData(input_nim)
    elif input_menu == 2:
        input_nim = input("masukkan nim : ")
        input_nama = input("masukkan nama : ")
        input_mtk = input("masukkan nilai mtk : ")
        input_ipa = input("masukkan nilai ipa : ")
        input_agama = input("masukkan nilai agama : ")
        insertData(input_nim, input_nama, input_mtk, input_ipa, input_agama)
    elif input_menu == 3:
        input_nim = input("masukkan nim yg akan diganti : ")
        input_nama = input("masukkan nama : ")
        input_mtk = input("masukkan nilai mtk : ")
        input_agama = input("masukkan nilai agama : ")
        input_ipa = input("masukkan nilai ipa : ")

        updateData(input_nama, input_mtk, input_agama, input_ipa, input_nim)
    elif input_menu == 4:
        input_nim = input("masukkan nim yg akan dihapus :")
        deleteData(input_nim)
    else:
        break
