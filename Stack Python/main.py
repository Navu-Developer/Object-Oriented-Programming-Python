from stacklib import stackAlgorithm
from termcolor import colored
import os,sys

def main():
    keepAlive = 0
    while keepAlive == 0:    
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("PROGRAM STACK CLASS DASAR\n","blue"))
        print(colored("Nama\t: Stevano Titondea Prayoga Putra"))
        print(colored("NIM\t: A11.2019.11831"))
        print(colored("Code\t: Python3"))
        print(colored("="*40,"green"))
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            count = int(input(colored("Jumlah input\n--> ")))
            i = 0
            os.system("clear")
            while i != count:
                i+=1
                data = str(input("Data ke %s --> " %i))
                sA.tambah_data(data)
            continue
        if choose == "2":
            os.system("clear")
            if sA.panjang_data() == 0:
                print(colored("[!] Data masih kosong.","red"))
                pass
            else:    
                sA.erase()
                print("[i] Data belakang telah dihapus.")
            skip = input()
            continue
        if choose == "3":
            os.system("clear")
            print("Data anda sekarang: ")
            print(sA.tampilkan_data())
            s = input()
            continue
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    sA = stackAlgorithm()
    main()