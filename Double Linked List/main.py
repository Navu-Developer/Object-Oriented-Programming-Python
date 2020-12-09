from DLL import DoubleLinkedList
import os

def main():
    keepAlive = 1
    dll.append(2)
    dll.append(3)
    dll.append(5)
    dll.append(10)
    dll.append(4)
    dll.append(1)
    while keepAlive == 1:
        os.system("clear")
        print("="*36)
        print("\tDOUBLE LINKED LIST")
        print("="*36)
        print("1. tambah data depan")
        print("2. tambah data belakang")
        print("3. tambah data pada index pilihan")
        print("4. tampilkan data")
        print("5. panjang data")
        print("6. hapus data berdasarkan index")
        print("7. tampilkan data ganjil")
        print("8. tampilkan data genap")
        print("9. operasi aritmatika")
        print("0. exit")
        choose = str(input("--> "))
        if choose == "1":
            dll.prepend(str(input("data --> ")))
            continue
        if choose == "2":
            dll.append(str(input("data --> ")))
            continue
        if choose == "3":
            os.system("clear")
            index = int(input("index --> "))
            data = str(input("data --> "))
            dll.addElement(index, data)
            skip = input()
            continue
        if choose == "4":
            print(dll.showData())
            skip = input()
        if choose == "5":
            print("panjang data sekarang --> ",dll.length())
            skip = input()
            continue
        if choose == "6":
            print("data sekarang")
            print(dll.showData())
            index = int(input("hapus index (0-%d) --> "%(dll.length()-1)))
            if index>dll.length():
                print("range index hanya (0-%d)"%(dll.length()-1))
                pass
            else:
                dll.deleteAtIndex(index-1)
                print("\ndata berhasil di hapus")
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
                penugasan = ":"
            index1 = int(input("angka 1, index --> "))
            index2 = int(input("angka 2, index --> "))
            print("hasil : ",dll.aritmatika(penugasan, index1, index2))
            skip = input()
            continue
        if choose == "0":
            keepAlive-=1
if __name__ == "__main__":
    dll = DoubleLinkedList()
    main()