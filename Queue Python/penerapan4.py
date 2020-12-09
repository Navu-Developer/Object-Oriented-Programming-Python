from Queuelib import queueAlgorithm
from termcolor import colored
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
Code    : Python3
        > Gerbong Roller Costers FIFO
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
        for gerbong in qA.showData():
            print(gerbong, end='')
            print("~", end='')
        print("\n")
        print("1. masukan gerbong")
        print("2. sampai")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            banyak = int(input("berapa gerbong (1-8) --> "))
            for i in range(banyak):
                qA.append("gerbong (%s)"%(i+1))
        if choose == "2":
            os.system("clear")
            if qA.length() == 0:
                print("Belum ada gerbong yang jalan")
                skip = input()
            else:
                os.system("clear")
                print("Yang pertama sampai")
                i = 1
                while True:
                    if qA.length() == 0:
                        break
                    else:
                        print("ke-%s"%i,qA.showData()[0])
                        i+=1
                        qA.erase()
                skip = input()
            continue
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    qA = queueAlgorithm()
    main()