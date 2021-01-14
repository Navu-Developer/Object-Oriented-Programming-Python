from DLL import DoubleLinkedList
import os

def main():
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print("="*42)
        print("\tDouble Linked List (Stack)")
        print("\nNama\t:Stevano Titondea Prayoga Putra")
        print("Code\t:Python3.x")
        print("="*42)
        print("1. tambah data")
        print("2. hapus data")
        print("3. tampilkan data")
        print("4. isEmpty")
        print("5. len")
        print("6. exit")
        choose = str(input("--> "))
        if choose == "1":
            data = str(input("data --> "))
            dll.push(data)
        if choose == "2":
            if dll.isEmpty():
                print("data masih kosong")
                pass
            else:
                dll.pop()
                print("penghapusan data berhasil")
            skip = input()
        if choose == "3":
            print("data anda sekarang")
            print("--> ",dll.showData())
            skip = input()
        if choose == "4":
            if dll.isEmpty():
                print("data masih kosong --> ",dll.isEmpty())
            else:
                print("anda memiliki data --> ",dll.isEmpty())
            skip = input()
        if choose == "5":
            print("panjang data anda")
            print("--> ",dll.length())
            skip = input()
        if choose == "6":
            keepAlive-=1
if __name__ == "__main__":
    dll = DoubleLinkedList()
    main()