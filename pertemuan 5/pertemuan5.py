# string
# nama = "rasyid prayogo"
# for i in nama:
#     print(i)


# integer
# for i in range(2, 10, 3):
#     print(i)

# list
# umur = [10, 50, 20, 30, 40, 50]

# # while
# i = 20
# while i >= 12:
#     print(i)
#     i = i - 1


# while i < 20:
#     i += 1
#     print(i)

# nama = "rasyid"
# data = [10, 20, 30, 40]

# i = 0
# while i < len(data):
#     print(data[i])
#     i = i + 1

data = [10, 20, 5, 30, 40, 50]

for i in data:
    print(i)
    if i == 5:
        print("kondisi 1")
        continue
    if i > 25:
        print("kondisi 2")
        break
    print("bawah")
print("batas akhir")

while True:
    print("Toko jaya")
    print("1. Luas")
    print("2. Exit")
    inputMenu = input("masukkan [1-2] :")
    if inputMenu == "1":
        inputSisi = int(input("masukkan sisi"))
        luas = inputSisi**2
        print("luasnya adalah : ", luas)
    elif inputMenu == "2":
        print("program selesai")
        break
