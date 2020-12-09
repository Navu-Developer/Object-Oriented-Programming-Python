from nodeLib import Node
from linkedList import linkedList
from termcolor import colored
import os
'''
Nama    : Stevano Titondea Prayoga Putra
NIM     : A11.2019.11831
'''
# untuk main display
def mainDisplay():
    SLL.append(35)
    SLL.append(34)
    SLL.append(37)
    SLL.append(38)
    SLL.append(32)
    SLL.append(36)
    SLL.append(33)
    mainloop = 0
    while mainloop < 1:
        os.system("clear")  
        print("="*53)
        print(" ", colored("PROGRAM LINKED LIST\n\nNama  : Stevano\nNim   : A11.2019.11831\nCode  : Python3","blue"))
        print("="*53)
        print("ANDA SEBAGAI TELLER MEMPUNYAI CLIENT NASABAH DENGAN NOMOR ANTRIAN:")
        print(colored(SLL.getDataAsList(),"green"))
        print("Nomor antrian terkecil adalah yang pertama selesai dan keluar kantor bank")
        print("="*53)
        print("1.)   Append",colored("(Bisa secara acak/ Tidak harus urut)","yellow"))
        print("2.)   Call",colored("(Memanggil nomor antrian terkecil)","yellow"))
        print("3.)  ",colored("Exit","red"))
        choose = str(input("masukan pilihan anda : "))
        if choose == "1":
            os.system('clear')
            print("Berapa antrian")
            rep = int(input("->"))
            for i in range(rep):
                num = int(input("Nomor antrian (acak saja) : "))
                SLL.append(int(num))
            continue
        if choose == "2":
            os.system('clear')
            print("Nomor antrian ke teller : ")
            minIndex = (SLL.getSmallestIndex()-1)
            SLL.delete(minIndex)
            s = input("enter to continue")
            continue
        if choose == "3":
            mainloop+=2
if __name__ == "__main__":
    SLL = linkedList()
    mainDisplay()