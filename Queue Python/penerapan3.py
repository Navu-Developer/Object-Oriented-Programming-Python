from Queuelib import queueAlgorithm
from termcolor import colored
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
Code    : Python3
        > Flying Fox FIFO
'''
def main():
    sampeDibawah = []
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("\tPROGRAM QUEUE","cyan"))
        print("Nama\t: Stevano Titondea Prayoga Putra")
        print("NIM\t: A11.2019.11831")
        print("Code\t: Python3")
        print(colored("="*40,"green"))
        for orang in qA.showData():
            print(orang, end='')
            print(" <-- ", end='')
        print("\n")
        print("1. tambah orang")
        print("2. yang sampai duluan?")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            sampeDibawah.append("sampe")
            i = len(sampeDibawah)
            qA.append("orang %d"%i)
        if choose == "2":
            if qA.length() == 0:
                print(colored("Tidak ada orang di atas lagi","yellow"))
                skip = input()
            else:
                print(qA.showData()[0],"Sampai dibawah")
                skip = input()
                qA.erase()
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    qA = queueAlgorithm()
    main()