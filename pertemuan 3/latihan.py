# luas segitiga
alas = float(input("masukkan alas segitiga : "))
tinggi = float(input("masukkan tinggi segitiga : "))
luas_segitiga = float(alas * tinggi / 2)
print("luas segitiga adalah ", luas_segitiga)

# luas lingkaran
r = int(input("masukkan jari jari lingkaran : "))
phi = 22 / 7
luas_lingkaran = int(phi * r * r)
print("luas lingkaran adalah ", luas_lingkaran)

# luas trapesium
sisi_a = int(input("masukkan sisi a : "))
sisi_b = int(input("masukkan sisi b : "))
tinggi = int(input("masukkan tinggi : "))
luas_trapesium = ((sisi_a + sisi_b) / 2) * tinggi
print("luas trapesium adalah ", int(luas_trapesium))

# keliling persegi panjang
panjang = float(input("masukkan panjang : "))
lebar = float(input("masukkan lebar : "))
keliling = float(2 * (panjang + lebar))
print("keliling persegi panjang adalah ", keliling)
