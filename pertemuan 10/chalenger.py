import matplotlib.pyplot as plt
import numpy as np

data_mahasiswa = [
    {
        "NIM": "1",
        "Nama": "Rasyid",
        "matkul": {"Matematika": 100, "Inggris": 90, "Alpro": 80},
    },
    {
        "NIM": "2",
        "Nama": "gading",
        "matkul": {"Matematika": 90, "Inggris": 70, "Alpro": 100},
    },
    {
        "NIM": "3",
        "Nama": "alfin",
        "matkul": {"Matematika": 50, "Inggris": 50, "Alpro": 50},
    },
    {
        "NIM": "4",
        "Nama": "rapli",
        "matkul": {"Matematika": 70, "Inggris": 60, "Alpro": 60},
    },
    {
        "NIM": "5",
        "Nama": "hari",
        "matkul": {"Matematika": 30, "Inggris": 75, "Alpro": 40},
    },
]


def menu():
    print("1. Cari Mahasiswa")
    print("2. keluar")


while True:
    menu()
    input_menu = int(input("masukkan pilihan[1-2]: "))
    if input_menu == 1:
        input_nim = input("masukkan nim :")
        hasil = None
        for mahasiswa in data_mahasiswa:
            if mahasiswa["NIM"] == input_nim:
                hasil = mahasiswa

        if hasil == None:
            print("Mahasiswa tidak ditemukan")
            continue

        data_pie = np.array(
            [
                hasil["matkul"]["Matematika"],
                hasil["matkul"]["Inggris"],
                hasil["matkul"]["Alpro"],
            ]
        )
        labels = ["Matematika", "Inggris", "Alpro"]
        plt.pie(data_pie, labels=labels, autopct="%1.0f%%")
        plt.show()
    elif menu == "2":
        break
    else:
        print("Pilihan Tidak Valid")
