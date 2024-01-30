import mysql.connector


def connection_database():
    connector = mysql.connector.connect(
        host="localhost", user="root", password="", database="rasyid_uas_alpro"
    )
    if connector.is_connected:
        return connector
    else:
        print("Database gagal terkoneksi")
        return False


def insert_pelanggan(id, nama_pelanggan, tarif_daya, tarif_watt):
    try:
        conn = connection_database()
        cursor = conn.cursor()
        sql = "INSERT INTO pelanggan (id, nama_pelanggan, tarif_daya, tarif_watt) VALUES (%s, %s, %s, %s)"
        data = (id, nama_pelanggan, tarif_daya, tarif_watt)
        cursor.execute(sql, data)
        conn.commit()
        print("-" * 20)
        print("Data berhasil ditambah")
        print("-" * 20)
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def update_pelanggan(nama_pelanggan, tarif_daya, tarif_watt, id):
    try:
        conn = connection_database()
        cursor = conn.cursor()
        sql = "UPDATE pelanggan SET nama_pelanggan = %s, tarif_daya = %s , tarif_watt= %s WHERE id = %s"
        data = (nama_pelanggan, tarif_daya, tarif_watt, id)
        cursor.execute(sql, data)
        conn.commit()
        print("-" * 20)
        print("data telah diubah")
        print("-" * 20)
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def delete_pelanggan(id):
    try:
        conn = connection_database()
        cursor = conn.cursor()
        sql = "DELETE FROM pelanggan WHERE id = %s"
        data = (id,)
        cursor.execute(sql, data)
        conn.commit()
        print("-" * 20)
        print("data telah dihapus")
        print("-" * 20)
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def select_pelanggan():
    try:
        conn = connection_database()
        cursor = conn.cursor()
        sql = "SELECT * FROM pelanggan"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def print_pelanggan(daftar_pelanggan):
    print(
        "\n{:<8} {:<20} {:<15} {:<10}".format("ID", "Nama", "Tarif Daya", "Tarif Watt")
    )
    print("-" * 60)
    for pelanggan in daftar_pelanggan:
        print(
            "{:<7} {:<20} {:<15} {:<10}".format(
                pelanggan[0], pelanggan[1], pelanggan[2], pelanggan[3]
            ),
        )
    print("-" * 60)


def cari_pelanggan(id):
    conn = connection_database()
    cursor = conn.cursor()
    sql = "SELECT * FROM pelanggan WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    result = cursor.fetchone()
    return result


def insert_tagihan(pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun):
    try:
        conn = connection_database()
        cursor = conn.cursor()
        sql = "INSERT INTO tagihan(pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun, status) VALUES(%s, %s, %s, %s, %s, 1)"
        data = (
            pelanggan_id,
            tanggal_bayar,
            beban_penggunaan,
            tagihan,
            bulan_tahun,
        )
        cursor.execute(sql, data)
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()


def print_struk(
    tanggal, resi, pelanggan_id, nama, tarif, daya, beban, tagihan, bulan_tahun
):
    print("")
    print("")
    print(f"Tanggal  : {tanggal}")
    print(f"No. Resi : {resi}")

    print("\n          STRUK PEMBAYARAN TAGIHAN LISTRIK          ")
    print("=======================================================")
    print(f"ID Pelanggan   : {pelanggan_id}")
    print(f"Nama           : {nama}")
    print(f"Tarif/Daya     : {tarif}/{daya}")
    print(f"Beban          : {beban}")
    print(f"Rp Tagihan PLN : {tagihan}")
    print(f"BL/TH          : {bulan_tahun}")
    print("=======================================================")


def print_menu():
    print("----------------------")
    print("1. Data Pelanggan")
    print("2. Data Tagihan")
    print("3. Keluar")
    print("----------------------")


def print_pelanggan_menu():
    print("-----------------------")
    print("1. Tambah Pelanggan")
    print("2. Ubah Pelanggan")
    print("3. Hapus Pelanggan")
    print("4. Tampilkan Pelanggan")
    print("5. Kembali")
    print("-----------------------")


def print_tagihan_menu():
    print("-----------------------")
    print("1. Tambah Tagihan")
    print("2. Keluar")
    print("-----------------------")


while True:
    print_menu()
    input_menu = int(input("Pilih Menu [1-3] : "))
    if input_menu == 1:
        while True:
            print_pelanggan_menu()
            input_menu = int(input("Pilih menu [1-5] : "))
            if input_menu == 1:
                input_id = input("Masukkan id pelanggan : ")
                input_nama = input("Masukkan nama pelanggan : ")
                input_daya = input("Masukkan tarif daya : ")
                input_watt = input("Masukkan tarif watt : ")
                insert_pelanggan(input_id, input_nama, input_daya, input_watt)
            elif input_menu == 2:
                input_id = input("Masukkan id pelanggan : ")
                input_nama = input("Masukkan nama pelanggan : ")
                input_daya = input("Masukkan tarif daya : ")
                input_watt = input("Masukkan tarif watt : ")
                update_pelanggan(input_nama, input_daya, input_watt, input_id)
            elif input_menu == 3:
                input_id = input("Masukkan id pelanggan : ")
                delete_pelanggan(input_id)
            elif input_menu == 4:
                daftar_pelanggan = select_pelanggan()
                print_pelanggan(daftar_pelanggan)
            elif input_menu == 5:
                break
            else:
                print("-" * 20)
                print("Pilihan tidak valid")
                print("-" * 20)

    elif input_menu == 2:
        while True:
            print_tagihan_menu()
            input_menu = int(input("Pilih menu [1-2] : "))
            if input_menu == 1:
                pelanggan_id = input("Masukkan id pelanggan : ")
                pelanggan = cari_pelanggan(pelanggan_id)
                tanggal_bayar = input("Masukan tanggal bayar : ")
                beban_penggunaan = int(input("Masukan beban penggunaan : "))
                bulan_tahun = input("Masukan bulan tahun : ")
                tagihan = beban_penggunaan * pelanggan[3]
                resi = insert_tagihan(
                    pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun
                )
                print_struk(
                    tanggal_bayar,
                    resi,
                    pelanggan_id,
                    pelanggan[1],
                    pelanggan[2],
                    pelanggan[3],
                    beban_penggunaan,
                    tagihan,
                    bulan_tahun,
                )
            elif input_menu == 2:
                break
            else:
                print("-" * 20)
                print("Pilihan tidak valid")
                print("-" * 20)
    elif input_menu == 3:
        break
    else:
        print("-" * 20)
        print("Pilihan tidak valid")
        print("-" * 20)
