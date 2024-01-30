while True:
    print("1. lihat nilai")
    print("2. Exit")
    inputMenu = input("Masukkan [1-2] :")
    if inputMenu == "1":
        nilai = int(input("masukkan nilai: "))
        if nilai > 100:
            print("nilai harus dibawah 100")
            continue
        elif nilai >= 81:
            print("A")
        elif nilai >= 61:
            print("B")
        elif nilai >= 41:
            print("C")
        elif nilai >= 21:
            print("D")
        elif nilai >= 0:
            print("E")
        else:
            print("nilai harus diatas 0")
            continue
    elif inputMenu == "2":
        print("program selesai")
        break
