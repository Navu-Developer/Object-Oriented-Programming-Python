from stacklib import stackAlgorithm
from termcolor import colored
from collections import deque
import os,sys
'''
Tempat Peluru atau magazine
biasanya akan diisi ulang dengan
cara mengisinya dari atas hingga
ke bawah peluru yang pertama dimasukan
akan menjadi peluru yang paling bawah
pada magazine dan menjadi yang pertama
keluar dari magazine adalah peluru yang
terakhir.

Code: Python3
'''
def main():
    keepAlive = 0
    while keepAlive == 0:    
        os.system("clear")
        print(colored("="*60,"green"))
        print(colored("\t\tPROGRAM ALGORITMA STACK\n","blue"))
        print(colored("Pemilik\t: Stevano Titondea Prayoga Putra"))
        print(colored("NIM\t: A11.2019.11831"))
        print(colored("Code\t: Python3"))
        print(colored("="*60,"green"))
        print("1. Isi ulang tempat peluru (magazine)")
        print("2. Cek Peluru")
        print("3. Tembakan peluru")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            print("Berapa banyak peluru yang ingin ditambahkan")
            count = int(input("--> "))
            if count>15:
                print(colored("Maksimal peluru 15","yellow"))
                skip = input("enter to continue")
                pass
            else:
                i = 0
                while i < count:
                    i+=1
                    sA.tambah_data("peluru %s"%i)
            continue
        if choose == "2":
            os.system("clear")
            for elements in sA.tampilkan_data():
                print(elements)
            skip = input("enter to continue")
            continue
        if choose == "3":
            os.system("clear")
            for i in range(sA.panjang_data()):
                os.system("clear")
                print(sA.tampilkan_data()[sA.panjang_data()-1])
                skip = input("tekan enter untuk tembak, 0 untuk berhenti -> ")
                if skip == "0":
                    break
                else:
                    sA.hapus_data()
                    continue
            continue
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    sA = stackAlgorithm()
    main()