from Queuelib import queueAlgorithm
from termcolor import colored
import math
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
Code    : Python3
        > baris parkiran mobil di parkiran paling bawah kapal FIFO
'''
def main():
    kesempatan = 1
    keepAlive = 1
    while keepAlive == 1:
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("\tPROGRAM QUEUE","cyan"))
        print("Nama\t: Stevano Titondea Prayoga Putra")
        print("NIM\t: A11.2019.11831")
        print("Code\t: Python3")
        print(colored("="*40,"green"))
        print("1. masukan mobil")
        print("2. keluarkan")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            if kesempatan == 1:
                if qA.length() == 6:
                    print("maksimal 6 baris")
                    skip = input()
                    pass
                else:
                    os.system("clear")
                    banyak = int(input("banyak mobil -> "))
                    baris = math.ceil(banyak/3.0)
                    if baris > 6:
                        print("tidak cukup")
                        skip = input()
                        pass
                    else:
                        for i in range(baris):
                            i = qA.length()+1
                            qA.append("baris mobil ke-%d"%i)
                            print(qA.showData()[qA.length()-1],"masuk")
                        kesempatan-=1
                        print(colored("mobil sebanyak {} diparkir dalam {} baris".format(banyak, baris),"yellow"))
                        skip = input()
            else:
                print("Keluarkan semua mobil dulu")
                skip = input()
                pass
        if choose == "2":
            if kesempatan == 0:
                if qA.length() > 0:
                    i = 0
                    count = qA.length()
                    while i < count:
                        i+=1
                        print("baris ke-%d"%i,"keluar")
                        qA.erase()
                        skip = input()
                    kesempatan+=1
                    continue
            else:
                print("masukan lagi mobil")
            continue
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    qA = queueAlgorithm()
    main()
