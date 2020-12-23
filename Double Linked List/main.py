from DLL import DoubleLinkedList
import os

def main():
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print("="*36)
        print("\tDOUBLE LINKED LIST")
        print("\nCode\t: Python3")
        print("="*36)
        print("1.)\ttambah data (depan)")
        print("2.)\ttambah data (belakang)")
        print("3.)\ttambah data (index)")
        print("4.)\ttampilkan data (semua)")
        print("5.)\tpanjang data")
        print("6.)\thapus data (index)")
        print("7.)\ttampilkan data (ganjil)")
        print("8.)\ttampilkan data (genap)")
        print("9.)\toperasi aritmatika (+ - x :)")
        print("0.)\texit")
        choose = str(input("--> "))
        if choose == "1":
            print("masukan nilai input")
            dll.prepend(str(input("data --> ")))
            continue
        if choose == "2":
            print("masukan nilai input")
            dll.append(str(input("data --> ")))
            continue
        if choose == "3":
            os.system("clear")
            print("data sekarang")
            print(dll.showData())
            index = str(input("index (0-%d)\t--> "%(dll.length())))
            data = str(input("data\t\t--> "))
            if bool(index) is False:
                print("index tidak bisa kosong")
                pass
            else:
                if int(index) > dll.length():
                    print("index lebih besar dari panjang data")
                    pass
                else:
                    dll.addElement(int(index), data)
            continue
        if choose == "4":
            print("data sekarang")
            print(dll.showData())
            skip = input()
        if choose == "5":
            print("panjang data sekarang --> ",dll.length())
            skip = input()
            continue
        if choose == "6":
            if dll.length() == 0:
                print("belum ada data")
                pass
            else:
                print("data sekarang")
                print(dll.showData())
                index = str(input("hapus index (0-%d) --> "%(dll.length()-1)))
                if bool(index) is False:
                    print("index tidak bisa kosong")
                    pass
                else:
                    if int(index)>dll.length()-1:
                        print("range index hanya (0-%d)"%(dll.length()-1))
                        pass
                    else:
                        os.system("clear")
                        print("\ndata berhasil di hapus")
                        print("data sebelumnya")
                        print(dll.showData())
                        dll.deleteAtIndex(int(index)-1)
                        print("data anda sekarang")
                        print(dll.showData())
            skip = input()
        if choose == "7":
            print("DATA GANJIL")
            dll.oddElement()
            skip = input()
        if choose == "8":
            print("DATA GENAP")
            dll.evenElement()
            skip = input()
        if choose == "9":
            os.system("clear")
            print("Jika tipe data String (teks) maka value=0")
            penugasan = ''
            print("ARITMATIKA LINKED LIST")
            print("Anda mempunyai data : ")
            print(dll.showData())
            print("1. penjumlahan")
            print("2. pengurangan")
            print("3. perkalian")
            print("4. pembagian")
            operasional = str(input("--> "))
            if operasional == "1":
                penugasan = "+"
            if operasional == "2":
                penugasan = "-"
            if operasional == "3":
                penugasan = "*"
            if operasional == "4":
                penugasan = "//"
            index1 = str(input("angka 1, index --> "))
            index2 = str(input("angka 2, index --> "))
            bo1 = bool(index1)
            bo2 = bool(index2)
            if (int(index1) or int(index2)) > dll.length()-1:
                print("index tidak ada")
                pass
            else:
                if int(operasional) > 4:
                    print("tidak ada asignment")
                    pass
                else:
                    if (bo1 and bo2) is False:
                        print("angka 1 atau 2 tidak bisa kosong")
                        pass
                    else: 
                        print("hasil : ",dll.aritmatika(penugasan, int(index1), int(index2)))
                    skip = input()
            continue
        if choose == "0":
            keepAlive-=1
if __name__ == "__main__":
    dll = DoubleLinkedList()
    main()
