# def nama():
#     print("nama saya rasyid")
#     print("saya adalah mahasiswa UTY")


# nama()


# def luas_segitiga():
#     alas = 10
#     tinggi = 5
#     luas = alas * tinggi
#     print("luas segitiga adalah ", luas)


# luas_segitiga()


# def luasPersegi():
#     sisi = 10
#     luas = sisi * sisi
#     return luas


# # print(luasPersegi())  # cara 1
# # tampung_luas = luasPersegi()  # cara 2
# # print(tampung_luas)
# # proses = tampung_luas + 200
# # print(proses)


# # def dataDiri():
# #     nama = "Rasyid"
# #     prodi = "informatika"
# #     angka = 10
# #     return nama, prodi, angka


# # tampungNama, tampungProdi, tampungAngka = dataDiri()
# # print(tampungNama)
# # print(tampungProdi)
# # print(tampungAngka)


# # def luasPersegi(sisi):
# #     luas = sisi * sisi
# #     print("luas persegi", luas)


# # input_sisi = int(input("masukkan sisi = "))
# # luasPersegi(input_sisi)


# # def persegiPanjang(tambahan, panjang=10, lebar=20):
# #     luas = panjang * lebar + tambahan
# #     print("luas persegi panjang adalah =", luas)


# # persegiPanjang(20, 40, 50)
# # persegiPanjang(20)
# # persegiPanjang(20, lebar=30)


# def luasPersegi(sisi):
#     luas = sisi * sisi
#     return luas


# inputSisi = int(input("masukkan sisi = "))
# tampung_luas = luasPersegi(inputSisi)
# print("luas persegi adalah =", tampung_luas)


# def perulangan(angka):
#     print("perulangan ke-", angka)
#     if angka == 0:
#         print("perulangan berhenti")
#     else:
#         perulangan(angka - 1)


# perulangan(10)


# def nama(mahasiswa):
#     global namaMahasiswa
#     namaMahasiswa = []
#     namaMahasiswa.append(mahasiswa)
#     print(namaMahasiswa)


# def tampil():
#     print("hasil tampil", namaMahasiswa)


# nama("rasyid")
# tampil()
data = []
while True:
    dataInput = int(input("masukkan angka"))
    data.append(dataInput)
    print(data)
    a = len(data)
    print(a)
