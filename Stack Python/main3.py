from termcolor import colored
from collections import deque
from stacklib import stackAlgorithm
import os,sys
'''
Dalam contoh kasus pemrograman ini
garasi seorang pemilik mobil hanya
selebar 1 mobil, untuk memarkirkan
sejajar dan untuk mengeluarkan mobil
harus mengeluarkan mobil paling depan
agar mobil di belakangnya dapat keluar

Code: Python3
'''
def main():
    chance = 0
    keepAlive = 0
    out = deque()
    while keepAlive == 0:    
        os.system("clear")
        print(colored("="*60,"green"))
        print(colored("\t\tPROGRAM ALGORITMA STACK\n","blue"))
        print(colored("Pemilik\t: Stevano Titondea Prayoga Putra"))
        print(colored("NIM\t: A11.2019.11831"))
        print(colored("Code\t: Python3"))
        print(colored("="*60,"green"))
        print("Mobil anda sekarang di garasi adalah -->", sA.tampilkan_data())
        print("Mobil anda sekarang di luar garasi adalah --> ", out)
        print("1. Masukan mobil")
        print("2. keluarkan mobil")
        print("3. Masukan mobil ke garasi")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            if chance != 0:
                print(colored("Mobil anda sudah ada 3, mungkin sedang diluar?","yellow"))
                skip = str(input("enter to continue"))
                pass
            if chance == 0:
                for i in range(3):
                    sA.tambah_data(str(input("Merk mobil ke %s --> "%(i+1))))
                chance+=2
                continue
        if choose == "2":
            os.system("clear")
            if sA.panjang_data() == 0:
                print(colored("Digarasi sudah tidak ada mobil","yellow"))
                skip = input("enter to continue")
                pass
            else:
                for i in range(1):
                    out.append(sA.tampilkan_data()[sA.panjang_data()-1])
                    sA.hapus_data()
            continue
        if choose == "3":
            os.system("clear")
            print(out)
            mobil = str(input("-> Mobil yang ingin dimasukan-> "))
            i = 0
            while i < len(out):
                if mobil == out[i]:
                    sA.tambah_data(mobil)
                    del out[i]
                else:
                    pass
                i+=1
            continue
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    sA = stackAlgorithm()
    main()