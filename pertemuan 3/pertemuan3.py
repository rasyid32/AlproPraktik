# integer
tipe_integer = 20000
ubah_float = float(tipe_integer)
ubah_string = str(tipe_integer)
ubah_boolean = bool(tipe_integer)

# float
tipe_float = 20000.0
ubah_integer = int(tipe_float)
ubah_string = str(tipe_float)
ubah_boolean = bool(tipe_float)

# string
# string bisa diubah menjadi integer jika nilainya angka
# string bisa diubah menjadi float jika nilainya angka
# string bernilai false jika nilainya kosong, dan bernilai true jika ada nilainya
tipe_string_angka = "2000"
tipe_string_huruf = "Rasyid"
ubah_integer = int(tipe_string_angka)
ubah_float = float(tipe_string_angka)
ubah_boolean = bool(tipe_string_huruf)

# boolean
tipe_boolean = True
ubah_integer = int(tipe_boolean)
ubah_string = str(tipe_boolean)
ubah_boolean = bool(tipe_boolean)


# Operator
# penjumlahan
angka_1 = 20
angka_2 = 10
proses = angka_1 + angka_2
print(proses)

# pengurangan
angka_1 = 20
angka_2 = 10
proses = angka_1 - angka_2
print(proses)

# perkalian
angka_1 = 20
angka_2 = 10
proses = angka_1 * angka_2
print(proses)

# pembagian
angka_1 = 20
angka_2 = 10
proses = angka_1 / angka_2
print(proses)

# Modulus
modulus = 10 % 2
print(modulus)

# pangkat
pangkat = 10**2
print(pangkat)

# floor devision
floor_devision = 20 // 3
print(floor_devision)


inputUser = input("masukkan nama : ")

inputHarga = int(input("masukkan harga : "))
inputFloat = float(input("masukkan nilai float : "))
inputBoolean = bool(input("masukkan nilai boolean : "))

u_float = float(inputHarga)
print(u_float)
