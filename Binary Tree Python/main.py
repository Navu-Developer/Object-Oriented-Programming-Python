from BinaryTreeV2 import BinaryTree
import os

def main():
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print("="*42)
        print("\tBINARY TREE V2")
        print("\tStruktur Data Seimbang")
        print("\nROOT --> ",t.rootData())
        print("="*42)
        print("1. tambah data")
        print("2. tampilkan data")
        print("3. hapus data")
        print("0. Exit")
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            print("="*42)
            print("PENAMBAHAN DATA TREE")
            print("="*42)
            print("1. Balance")
            print("2. Unbalance")
            choose1 = str(input("--> "))
            data = str(input("Data --> "))
            if bool(data) is False or bool(choose1) is False:
                print("Harus mengisi semua input")
                skip = input()
            else:
                if choose1 == "1":
                    t.insert(int(data))
                if choose1 == "2":
                    os.system("clear")
                    print("1. Left")
                    print("2. Right")
                    choose2 = str(input("--> "))
                    if choose2 == "1":
                        t.insertLeft(int(data))
                    elif choose2 == "2":
                        t.insertRight(int(data))
        elif choose == "2":
            os.system("clear")
            print("="*42)
            print("\tMODE")
            print("="*42)
            print("1. Tampilkan hanya data")
            print("2. Tampilkan alamat data")
            choose3 = str(input("--> "))
            if choose3 == "1":
                print("Data anda sekarang\n--> ",t.showData())
            elif choose3 == "2":
                print("Data anda sekarang\n--> ",t.showData())
                print("\nData beserta alamat\n")
                print(t.showDataAdd())
            skip = input()
        elif choose == "3":
            os.system("clear")
            print("1. Hapus semua")
            print("2. Hapus element (balanced data)")
            choose4 = str(input("--> "))
            if choose4 == "1":
                t.deleteAll()
            elif choose4 == "2":
                print("data sekarang -> ",t.showData())
                data = str(input("Data --> "))
                if bool(data) is False:
                    print("Tidak ada data dihapus")
                    skip = input()
                else:
                    t.deleteElement(int(data))
        elif choose == "999":
            if t.rootData() is None:
                main()
        elif choose == "0":
            keepAlive-=1
if __name__ == "__main__":
    t = BinaryTree()
    main()    
