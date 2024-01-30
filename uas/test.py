import mysql.connector


def buat_koneksi():
    koneksi = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zaki",
    )
    return koneksi


def print_menu():
    print("\n1. Management Pelanggan")
    print("2. Management Tagihan")
    print("3. Keluar")


def print_menu_pelanggan():
    print("\n1. Tambah Pelanggan")
    print("2. Ubah Pelanggan")
    print("3. Hapus Pelanggan")
    print("4. Tampilkan Pelanggan")
    print("5. Kembali")


def print_menu_tagihan():
    print("\n1. Tambah Tagihan")
    print("2. Keluar")


def tambah_pelanggan(data):
    sql = "INSERT INTO pelanggan VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, data)
    koneksi.commit()


def ubah_pelanggan(data, id):
    sql = "UPDATE pelanggan SET nama_pelanggan=%s, tarif_daya=%s, tarif_watt=%s WHERE id=%s"
    cursor.execute(sql, data + (id,))
    koneksi.commit()


def hapus_pelanggan(id):
    sql = "DELETE FROM pelanggan WHERE id=%s"
    cursor.execute(sql, (id,))
    koneksi.commit()


def cari_pelanggan(id):
    sql = "SELECT * FROM pelanggan WHERE id=%s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    return result


def semua_pelanggan():
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def print_pelanggan(list_pelanggan):
    print("{:<7} {:<30} {:<12} {:<6}".format("ID", "Nama", "Tarif Daya", "Tarif Watt"))
    print("-" * 63)
    for pelanggan in list_pelanggan:
        print(
            "{:<7} {:<30} {:<12} {:<6}".format(
                pelanggan[0], pelanggan[1], pelanggan[2], pelanggan[3]
            ),
        )


def tambah_tagihan(data):
    sql = "INSERT INTO tagihan(pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun, status) VALUES(%s, %s, %s, %s, %s, 1)"
    cursor.execute(sql, data)
    koneksi.commit()
    return cursor.lastrowid


def print_struk(
    tanggal, resi, pelanggan_id, nama, tarif, daya, beban, tagihan, bulan_tahun
):
    print(f"Tanggal  : {tanggal}")
    print(f"No. Resi : {resi}")

    print("\n          STRUK PEMBAYARAN TAGIHAN LISTRIK          ")
    print("====================================================")
    print(f"ID Pelanggan   : {pelanggan_id}")
    print(f"Nama           : {nama}")
    print(f"Tarif/Daya     : {tarif}/{daya}")
    print(f"Beban          : {beban}")
    print(f"Rp Tagihan PLN : {tagihan}")
    print(f"BL/TH          : {bulan_tahun}")


koneksi = buat_koneksi()
cursor = koneksi.cursor()

while True:
    print_menu()
    menu = input("Masukan pilihan menu [1-3] : ")

    if menu == "1":
        while True:
            print_menu_pelanggan()
            menu = input("Masukan Pilihan menu [1-5] : ")
            if menu == "1":
                id = input("Masukan id pelanggan : ")

                if cari_pelanggan(id) != None:
                    print("\n===================")
                    print("Pelanggan sudah ada")
                    print("===================")
                    continue

                nama = input("Masukan nama pelanggan : ")
                tarif_daya = input(
                    "Masukan tarif daya pelanggan [Contoh: R1M/900VA] : "
                )
                tarif_watt = input("Masukan tarif watt pelanggan [Contoh: 1500]: ")

                tambah_pelanggan((id, nama, tarif_daya, tarif_watt))

                print("\n==============================")
                print("Berhasil menambahkan pelanggan")
                print("==============================")

            elif menu == "2":
                id = input("Masukan id pelanggan : ")

                if cari_pelanggan(id) == None:
                    print("\n===================")
                    print("Pelanggan tidak ada")
                    print("===================")
                    continue

                nama = input("Masukan nama pelanggan : ")
                tarif_daya = input(
                    "Masukan tarif daya pelanggan [Contoh: R1M/900VA] : "
                )
                tarif_watt = input("Masukan tarif watt pelanggan [Contoh: 1500]: ")

                ubah_pelanggan((nama, tarif_daya, tarif_watt), id)

                print("\n==============================")
                print("Berhasil mengubah pelanggan")
                print("==============================")

            elif menu == "3":
                id = input("Masukan id pelanggan : ")

                if cari_pelanggan(id) == None:
                    print("\n===================")
                    print("Pelanggan tidak ada")
                    print("===================")
                    continue

                hapus_pelanggan(id)

                print("\n============================")
                print("Berhasil menghapus pelanggan")
                print("============================")

            elif menu == "4":
                list_pelanggan = semua_pelanggan()
                print_pelanggan(list_pelanggan)
                enter = input("Enter untuk melanjutkan")

            elif menu == "5":
                break

            else:
                print("\n================")
                print("Menu Tidak Valid")
                print("================")

    elif menu == "2":
        while True:
            print_menu_tagihan()
            menu = input("Masukan pilihan menu [1-2] : ")

            if menu == "1":
                pelanggan_id = input("Masukan id pelanggan : ")
                pelanggan = cari_pelanggan(pelanggan_id)

                if pelanggan == None:
                    print("\n===================")
                    print("Pelanggan tidak ada")
                    print("===================")
                    continue

                tanggal_bayar = input("Masukan tanggal bayar [Contoh: 2024-01-16] : ")
                beban_penggunaan = int(
                    input("Masukan beban penggunaan [Contoh: 100, max: 128]: ")
                )
                bulan_tahun = input("Masukan bulan tahun [Contoh: JAN/2024] : ")
                tagihan = beban_penggunaan * pelanggan[3]

                resi = tambah_tagihan(
                    (
                        pelanggan_id,
                        tanggal_bayar,
                        beban_penggunaan,
                        tagihan,
                        bulan_tahun,
                    )
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
                enter = input("Enter untuk melanjutkan")

            elif menu == "2":
                break

            else:
                print("\n================")
                print("Menu Tidak Valid")
                print("================")

    elif menu == "3":
        break

    else:
        print("\n================")
        print("Menu Tidak Valid")
        print("================")
