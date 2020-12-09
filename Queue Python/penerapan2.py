from Queuelib import queueAlgorithm
from termcolor import colored
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
Code    : Python3
        > Perhitungan jumlah mobil yang lewat di tol FIFO
'''
def main():
    count = []
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("\tPROGRAM QUEUE","cyan"))
        print("Nama\t: Stevano Titondea Prayoga Putra")
        print("NIM\t: A11.2019.11831")
        print("Code\t: Python3")
        print(colored("="*40,"green"))
        for item in qA.showData():
            print(item, end='')
            print(" << ", end='')
        print("\n")
        print("1. Mobil datang")
        print("2. Buka palang")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            i = len(count)
            count.append("*")
            qA.append("mobil ke-%d"%(i+1))
            continue
        if choose == "2":
            if qA.length() == 0:
                print(colored("belum ada mobil lagi","yellow"))
                skip = input()
            else:
                qA.erase()
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    qA = queueAlgorithm()
    main()