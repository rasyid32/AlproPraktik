import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_pln",
    )
    return conn


def tambahPelanggan(data):
    sql = "INSERT INTO pelanggan VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, data)
    conn.commit()


def editPelanggan(data, id):
    sql = "UPDATE pelanggan SET nama_pelanggan=%s, tarif_daya=%s, tarif_watt=%s WHERE id=%s"
    edit = data + (id,)
    cursor.execute(sql, edit)
    conn.commit()


def hapusPelanggan(id):
    sql = "DELETE FROM pelanggan WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()


def cariPelanggan(id):
    sql = "SELECT * FROM pelanggan WHERE id=%s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    return result


def selectPelanggan():
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def printPelanggan(list_pelanggan):
    print(
        "\n{:<8} {:<20} {:<15} {:<10}".format("ID", "Nama", "Tarif Daya", "Tarif Watt")
    )
    print("-" * 63)
    for pelanggan in list_pelanggan:
        print(
            "{:<7} {:<20} {:<15} {:<10}".format(
                pelanggan[0], pelanggan[1], pelanggan[2], pelanggan[3]
            ),
        )
    print("-" * 63)


def tambahTagihan(data):
    sql = "INSERT INTO tagihan(pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun, status) VALUES(%s, %s, %s, %s, %s, 1)"
    cursor.execute(sql, data)
    conn.commit()
    return cursor.lastrowid


def printStruk(
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


def printMenu():
    print("----------------------")
    print("1. Data Pelanggan")
    print("2. Data Tagihan")
    print("3. Keluar")
    print("----------------------")


def printPelangganMenu():
    print("-----------------------")
    print("1. Tambah Pelanggan")
    print("2. Ubah Pelanggan")
    print("3. Hapus Pelanggan")
    print("4. Tampilkan Pelanggan")
    print("5. Kembali")
    print("-----------------------")


def printTagihanMenu():
    print("-----------------------")
    print("1. Tambah Tagihan")
    print("2. Keluar")
    print("-----------------------")


conn = get_connection()
cursor = conn.cursor()

while True:
    printMenu()
    menu = int(input("Masukan pilihan menu [1-3] : "))

    if menu == 1:
        while True:
            printPelangganMenu()
            menu = int(input("Masukan Pilihan menu [1-5] : "))
            if menu == 1:
                id = input("Masukan id pelanggan : ")

                if cariPelanggan(id) != None:
                    print("--------------------")
                    print("Pelanggan sudah ada")
                    print("--------------------")
                    continue

                nama = input("Masukan nama pelanggan : ")
                tarif_daya = input("Masukan tarif daya : ")
                tarif_watt = input("Masukan tarif watt : ")

                tambahPelanggan((id, nama, tarif_daya, tarif_watt))

                print("-------------------------------")
                print("Berhasil menambahkan pelanggan")
                print("-------------------------------")

            elif menu == 2:
                id = input("Masukan id pelanggan : ")

                if cariPelanggan(id) == None:
                    print("--------------------")
                    print("Pelanggan tidak ada")
                    print("--------------------")
                    continue

                nama = input("Masukan nama pelanggan : ")
                tarif_daya = input("Masukan tarif daya : ")
                tarif_watt = input("Masukan tarif watt : ")

                editPelanggan((nama, tarif_daya, tarif_watt), id)

                print("----------------------------")
                print("Berhasil mengubah pelanggan")
                print("----------------------------")

            elif menu == 3:
                id = input("Masukan id pelanggan : ")

                if cariPelanggan(id) == None:
                    print("--------------------")
                    print("Pelanggan tidak ada")
                    print("--------------------")
                    continue

                hapusPelanggan(id)

                print("-----------------------------")
                print("Berhasil menghapus pelanggan")
                print("-----------------------------")

            elif menu == 4:
                list_pelanggan = selectPelanggan()
                printPelanggan(list_pelanggan)
                enter = input("\nenter untuk melanjutkan")

            elif menu == 5:
                break

            else:
                print("-----------------")
                print("Menu Tidak Valid")
                print("-----------------")

    elif menu == 2:
        while True:
            printTagihanMenu()
            menu = int(input("Masukan pilihan menu [1-2] : "))

            if menu == 1:
                pelanggan_id = input("Masukan id pelanggan : ")
                pelanggan = cariPelanggan(pelanggan_id)

                if pelanggan == None:
                    print("--------------------")
                    print("Pelanggan tidak ada")
                    print("--------------------")
                    continue

                tanggal_bayar = input("Masukan tanggal bayar : ")
                beban_penggunaan = int(input("Masukan beban penggunaan : "))
                bulan_tahun = input("Masukan bulan tahun : ")
                tagihan = beban_penggunaan * pelanggan[3]

                resi = tambahTagihan(
                    (
                        pelanggan_id,
                        tanggal_bayar,
                        beban_penggunaan,
                        tagihan,
                        bulan_tahun,
                    )
                )

                printStruk(
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
                enter = input("Enter untuk melanjutkan")

            elif menu == 2:
                break

            else:
                print("--------------------")
                print("Pilihan Tidak Valid")
                print("--------------------")

    elif menu == 3:
        break

    else:
        print("--------------------")
        print("Pilihan Tidak Valid")
        print("--------------------")
