from Queuelib import queueAlgorithm
from termcolor import colored
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
Code    : Python3
        > Penjualan dengan metode FIFO
'''
def main():
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("\tPROGRAM QUEUE","cyan"))
        print("Nama\t: Stevano Titondea Prayoga Putra")
        print("NIM\t: A11.2019.11831")
        print("Code\t: Python3")
        print(colored("="*40,"green"))
        print("Stok barang --> ",qA.showData())
        print("1. tambah persediaan")
        print("2. jual persediaan")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            nama = str(input("Nama barang : "))
            qA.append(nama)
            continue
        if choose == "2":
            if qA.length() == 0:
                print(colored("Tidak ada stok barang","yellow"))
                skip = input()
            else:
                qA.erase()
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    qA = queueAlgorithm()
    main()