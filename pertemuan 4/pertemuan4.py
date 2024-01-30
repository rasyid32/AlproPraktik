# operator perbandingan
# sama dengan
data_1 = 10
data_2 = 10
samaDengan = data_1 == data_2
print(samaDengan)

# tidak sama dengan
data_1 = 10
data_2 = 10
print(data_1 != data_2)

# lebih dari
data_1 = 11
data_2 = 10
print(data_1 > data_2)
# lebih dari samadengan
data_1 = 10
data_2 = 10
print(data_1 >= data_2)
# kurang dari
data_1 = 10
data_2 = 11
print(data_1 < data_2)
# kurang dari samadengan
data_1 = 10
data_2 = 10
print(data_1 <= data_2)

nama = 10
nama_2 = 20
# tidak bisa
cek = nama is 10
# bisa
cek = nama is not nama_2
print(cek)

# AND
print(True and True)
# or
print(True or True)
print(True | True)
# not
print(not True)
# xor
print(True ^ True)

no_1 = 20
no_2 = 10
if no_1 == no_2:
    print("kondisi 1")
elif no_1 >= no_2:
    print("kondisi 2")

else:
    print("kecuali")
# Percabangan
data_1 = 20
data_2 = 10
if data_1 % 3 == 0:
    print("Kondisi 1")
else:
    print("Kecuali")

if data_1 >= data_2:
    print("Kondisi 1")
    if data_1 < data_2:
        print("Kondisi 2")
        if data_2 >= data_1:
            print("Kondisi 3")
        if data_1 >= data_2:
            print("Kondisi 4")
            if data_1 == data_1:
                print("Kondisi 5")
    else:
        print("Kondisi 6")
else:
    print("Kecuali")
