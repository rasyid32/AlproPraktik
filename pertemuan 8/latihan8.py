namaMahasiswa = []


def menu():
    print("1. Input nama dan NIM mahasiswa")
    print("2. Cari Mahasiswa")
    print("3. hapus mahasiswa berdasarkan NIM")
    print("4. Edit nama mahasiswa berdasarkan NIM")
    print("5. Exit")


def mahasiswa(nama, nim):
    data = {"nama": nama, "nim": nim}
    namaMahasiswa.append(data)


def cari_mahasiswa(nim):
    if i["nim"] == cari:
        print("Nama : ", i["nama"])
        print("Nim : ", i["nim"])


def edit(nim):
    for i in namaMahasiswa:
        if i["nim"] == nim:
            i["nama"] = nama_baru


def hapus(nim):
    global namaMahasiswa
    newNamaMahasiswa = []
    for i in namaMahasiswa:
        if nim != i["nim"]:
            newNamaMahasiswa.append(i)

    list_lama = len(namaMahasiswa)
    namaMahasiswa = newNamaMahasiswa
    if list_lama == len(newNamaMahasiswa):
        print("Mahasiswa tidak ditemukan")
    else:
        print("mahasiswa sudah dihapus")


while True:
    menu()
    input_menu = int(input("pilih [1-5] :"))
    if input_menu == 1:
        input_nama = input("masukkan nama:")
        input_nim = input("masukkan nim:")
        mahasiswa(input_nama, input_nim)
    elif input_menu == 2:
        cari = input("cari nim mahasiswa :")
        for i in namaMahasiswa:
            cari_mahasiswa(cari)
    elif input_menu == 3:
        hapus_mahasiswa = input("masukkan nim mahasiswa yg akan dihapus :")
        hapus(hapus_mahasiswa)

    elif input_menu == 4:
        nim = input("masukkan nim: ")
        nama_baru = input("masukkan nama baru: ")
        edit(nim)
        # for i in namaMahasiswa:
        #     if i["nim"] == nim:
        #         i["nama"] = nama_baru
    else:
        print("pilihan tidak ada")
        break
