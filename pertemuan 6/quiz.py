data = []
while True:
    print("========================")
    print("=======menu karyawan=======")
    print("1. input karyawan")
    print("2. lihat gaji")
    print("3. keluar")
    inputMenu = int(input("masukkan menu [1-3] :"))
    if inputMenu == 1:
        inputNama = input("masukkan nama karyawan :")
        data.append(inputNama)
    elif inputMenu == 2:
        cariKaryawan = input("masukkan karyawan :")
        for i in data:
            if i == cariKaryawan:
                inputJam = int(input("masukkan jam kerja :"))
                gaji = 50000 * inputJam
                print("====Pilih jabatan======")
                print("1. Manager")
                print("2. Programmer")
                print("3. akuntan")
                print("4. karyawan biasa")
                inputJabatan = int(input("Masukkan jabatan :"))
                print("========================")
                if inputJabatan == 1:
                    gajiTunjangan = 50 / 100 * gaji
                    print("nama : ", i)
                    print("Gaji pokok : ", gaji)
                    print("Gaji tunjangan : ", gajiTunjangan)
                    print("Gaji total : ", gaji + gajiTunjangan)
                    break
                elif inputJabatan == 2:
                    gajiTunjangan = 30 / 100 * gaji
                    print("nama : ", i)
                    print("Gaji pokok : ", gaji)
                    print("Gaji tunjangan : ", gajiTunjangan)
                    print("Gaji total : ", gaji + gajiTunjangan)
                    break
                elif inputJabatan == 3:
                    gajiTunjangan = 20 / 100 * gaji
                    print("nama : ", i)
                    print("Gaji pokok : ", gaji)
                    print("Gaji tunjangan : ", gajiTunjangan)
                    print("Gaji total : ", gaji + gajiTunjangan)
                    break
                elif inputJabatan == 4:
                    gajiTunjangan = 5 / 100 * gaji
                    print("nama : ", i)
                    print("Gaji pokok : ", gaji)
                    print("Gaji tunjangan : ", gajiTunjangan)
                    print("Gaji total : ", gaji + gajiTunjangan)
                    break
    elif inputMenu == 3:
        break
