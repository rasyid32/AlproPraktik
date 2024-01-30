import mysql.connector
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np


def connectionDatabase():
    connector = mysql.connector.connect(
        host="localhost", user="root", password="", database="kimia_farma"
    )
    if connector.is_connected:
        print("Database terkoneksi")
        return connector
    else:
        print("Database gagal terkoneksi")
        return False


def insertData(id_karyawan, nama_karyawan):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "INSERT INTO karyawan (id_karyawan, nama_karyawan) VALUES (%s, %s)"
        data = (id_karyawan, nama_karyawan)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambah")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def insertLembur(januari, februari, maret, id):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "UPDATE karyawan SET januari=%s,februari=%s, maret=%s, waktu_input=%s  WHERE id_karyawan=%s"
        now = dt.datetime.now()
        waktu_input = now.strftime("%d-%m-%Y %H:%M")
        data = (januari, februari, maret, waktu_input, id)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambah pada ", waktu_input)
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def updateData(nama_karyawan, id_karyawan):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "UPDATE karyawan SET nama_karyawan = %s WHERE id_karyawan = %s"
        data = (nama_karyawan, id_karyawan)
        cursor.execute(sql, data)
        conn.commit()
        print("data telah diubah")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def deleteData(id_karyawan):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "DELETE FROM karyawan WHERE id_karyawan = %s"
        data = (id_karyawan,)
        cursor.execute(sql, data)
        conn.commit()
        print("data telah dihapus")
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
        sql = "SELECT id_karyawan, nama_karyawan, januari, februari, maret, waktu_input FROM karyawan WHERE id_karyawan = %s"
        search = (inputUser,)
        cursor.execute(sql, search)
        result = cursor.fetchone()
        if result:
            print("\n=====Data Karyawan=====")
            print(f"ID   : {result[0]}")
            print(f"Nama : {result[1]}")
            print(f"Jumlah Jam Lembur:")
            print(f"1. January {result[2]} kali lembur")
            print(f"1. February {result[3]} kali lembur")
            print(f"3. Maret {result[4]} kali lembur")
            print(f"Data diinputkan pada: {result[5]}")

        else:
            print("data tidak ditemukan")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def tampilVisual(inputUser):
    try:
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "SELECT id_karyawan, nama_karyawan, januari, februari, maret FROM karyawan WHERE id_karyawan = %s"
        search = (inputUser,)
        cursor.execute(sql, search)
        result = cursor.fetchone()
        if result:
            x = np.array(selectBulan())
            y = np.array([result[2], result[3], result[4]])
            plt.bar(x, y)
            plt.show()
        else:
            print("data tidak ditemukan")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def selectBulan():
    conn = connectionDatabase()
    cursor = conn.cursor()
    sql = "SELECT januari, februari, maret FROM bulan"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def menu():
    print("1. Input data karyawan")
    print("2. Input jumlah lembur")
    print("3. Edit data karyawan")
    print("4. Hapus data karyawan")
    print("5. Lihat data karyawan")
    print("6. Tampilkan visual data karyawan")
    print("7. Keluar")


while True:
    usernamee = input("username : ")
    passwordd = input("password : ")
    if usernamee == "admin" and passwordd == "admin123":
        while True:
            menu()
            input_menu = int(input("Pilih [1-7] : "))
            if input_menu == 1:
                input_id = input("Masukkan ID: ")
                input_nama = input("Masukkan nama karyawan: ")
                insertData(input_id, input_nama)
            elif input_menu == 2:
                input_id = input("masukkan id: ")
                input_jan = input("Masukkan lembur Januari: ")
                input_feb = input("Masukkan lembur Februari: ")
                input_mar = input("Masukkan lembur Maret: ")
                insertLembur(input_jan, input_feb, input_mar, input_id)
            elif input_menu == 3:
                input_id = input("Masukkan ID yg akan diedit: ")
                input_nama = input("Masukkan nama yg akan diganti: ")
                updateData(input_nama, input_id)
            elif input_menu == 4:
                input_id = input("masukkan ID yg akan dihapus :")
                deleteData(input_id)
            elif input_menu == 5:
                input_id = input("masukkan id : ")
                selectData(input_id)
            elif input_menu == 6:
                input_id = input("masukkan id : ")
                tampilVisual(input_id)
            elif input_menu == 7:
                break
            else:
                break
    else:
        print("username atau password salah")
