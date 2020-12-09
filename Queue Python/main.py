from Queuelib import queueAlgorithm
from termcolor import colored
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
Code    : Python3
'''
def main():
    keepAlive = 0
    while keepAlive == 0:
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("\tPROGRAM QUEUE","cyan"))
        print("Nama\t: Stevano Titondea Prayoga Putra")
        print("NIM\t: A11.2019.11831")
        print("Code\t: Python3")
        print(colored("="*40,"green"))
        print(colored("Data anda sekarang: ","red"))
        print(colored(qA.showData(),"cyan"))
        print("1. Tambah data",colored("(tambah belakang)","yellow"))
        print("2. Hapus data",colored("(hapus depan)","yellow"))
        print("3. Ganjil")
        print("4. Genap")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            print("Berapa banyak ingin menambahkan data?")
            count = int(input("--> "))
            i = 0
            os.system("clear")
            while i != count:
                i+=1
                data = str(input("data %s : "%i))
                qA.append(data)
            continue
        if choose == "2":
            os.system("clear")
            if qA.length() >= 1:
                qA.erase()
                print(colored("[i] Data telah kosong","red"))
            else:
                print(colored("[!] Belum ada data dalam antrian","red"))
                skip = input()
                pass
            skip = input()
            continue
        if choose == "3":
            os.system("clear")
            print(colored("Data ganjil adalah","green"))
            print(qA.odd())
            skip = input()
            continue
        if choose == "4":
            os.system("clear")
            print(colored("Data genap adalah","green"))
            print(qA.even())
            skip = input()
            continue
        if choose == "0":
            keepAlive+=1
if __name__ == "__main__":
    qA = queueAlgorithm()
    main()