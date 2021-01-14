from DLL import DoubleLinkedList
import os

def main():
    while True:
        os.system("cls")
        print("="*42)
        print("\tDouble Linked List Circullar")
        print("\nNama\t:Stevano Titondea Prayoga Putra")
        print("Code\t:Python3.x")
        print("="*42)
        print("1. Tambah data")
        print("2. Hapus data")
        print("3. Cari Data")
        print("4. Tampilkan")
        print("5. Tampilkan terbalik")
        print("6. IsEmpty")
        print("7. Length data")
        print("0. exit")
        choose = str(input("--> "))
        if choose == "1":
            data = str(input("masukan data pertama --> "))
            if bool(data) == False:
                print("tidak menginput apapun")
                skip = input()
            else:
                dll.enqueue(data)
        if choose == "2":
            if dll.isEmpty() == True:
                print("Data Masih kosong")
            else:
                dll.dequeue()
                print("data berhasil di hapus")
            skip = input()
        if choose == "3":
            item = str(input("data yang ingin dicari -->  "))
            dll.search(item)
            skip = input()
        if choose == "4":
            print("List dengan arah kedepan > > : ")
            dll.showDataForward()
            skip = input()
        if choose == "5":
            print("List dengan arah kebelakang < < : ")
            dll.showDataBackward()
            skip = input()
        if choose == "6":
            print(dll.isEmpty()) 
            skip = input()
        if choose == "7":
            print("Jumlah data sekarang -->",dll.length())
            skip = input()
        if choose == "0":
            exit()

if __name__ == "__main__":
    dll = DoubleLinkedList()
    main()