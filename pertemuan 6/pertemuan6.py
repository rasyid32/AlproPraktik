# # list
# dataList = [10, 20, 30]
# print(dataList)

# # dictionary
# dataDictionary = {"nama": "Rasyid", "list": [10, 20, 30]}
# # tuple
# dataTuple = (1, 2, 3)
# print(dataTuple)

# # set
# dataSet = {1, 2, 3}
# print(dataSet)

# index dimulai dari 0
# panjang dimulai dari 1
# positif 0  1  2  3  4  5  6
# negatif -7 -6 -5 -4 -3 -2 -1
# data = [10, 20, 30, 40, 50, 60, 70]
# cara mengambil data
# tidak bisa mengambil diluar index
# print(data[6])
# print(data[-4])

# slicing
# 20 - 50
# print(data[1:5])
# # 20 sampai habis ke kanan
# print(data[1:])
# # 60 sampai habis ke kiri
# print(data[:-2])

# manipulasi data
# data = [40, 10, 20, 100, 25, 50]
# mengganti nilai
# data[2] = "rasyid"
# data[1:3] = "eee", "wok"


# # menambahkan nilai sesuai index(insert)
# data.insert(1, "RR")
# data.insert(10, "kok")
# # append = menambahkan nilai di index terakhir
# data.append("rasyid")
# data.append("oy")
# # print(data)

# # menghapus berdasrkan nilainya
# # data.remove(40)
# # print(data)

# # # menghapus dengan delete berdasarkan index
# del data[-1]
# print(data)

# # menghapus dengan pop
# # menghapus dari yg paling terakhir
# # akan eror jika nilai yg dihapus habis
# data.pop()
# print(data)

# menggabungkan
data1 = [10, 50, 30, 20, 70]
data2 = ["rasyid", "bara"]
data1.extend(data2)
print(data1)

# # mengurutkan
# data1 = [10, 50, 30, 20, 70]
# data2 = ["rasyid", "bara"]
# data1.sort()
# print(data1)

# data1 = [10, 50, 30, 20, 70]
# data1.sort()
# data1.reverse()
# print(data1)

# data2.sort()
# print(data2)

# # mengetahui panjang list
# data1 = [10, 50, 30, 20, 70]
# panjanglist = len(data1)
# print(panjanglist)

data = []
while True:
    print("========================")
    print("=======menu karyawan=======")
    print("1. input karyawan")
    print("2. cari karyawan")
    print("3. tampil karyawan")
    print("4. exit")
    inputMenu = int(input("masukkan menu [1-3] :"))
    if inputMenu == 1:
        inputNama = input("masukkan nama :")
        data.append(inputNama)
    elif inputMenu == 2:
        cariKaryawan = input("masukkan karyawan :")
        for i in data:
            print("cek input karyawan ", cariKaryawan)
            if i == cariKaryawan:
                print("karyawan", i, "ada")
                break
        else:
            print("karyawan", cariKaryawan, "tidak ada")
            break

    elif inputMenu == 3:
        for i in data:
            print(i)
