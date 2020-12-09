from linkedList import linkedList
from termcolor import colored
import os
'''
program dasar menggunakan 
class stack hanya untuk 
memastikan fungsi pada 
library berjalan dengan baik
'''
# untuk main display
def mainDisplay():
    mainloop = 0
    while mainloop < 1:
        os.system("clear")  
        print("="*23)
        print(" ", colored("PROGRAM LINKED LIST\n\nNama  : Stevano\nNim   : A11.2019.11831\nCode  : Python3","blue"))
        print("="*23)
        print("1.)   Append",colored("(tambah data dari belakang)","yellow"))
        print("2.)   Prepend",colored("(tambah data dari depan)","yellow"))
        print("3.)   Length",colored("(jumlah data)","yellow"))
        print("4.)   Search",colored("(cari data berdasarkan index)","yellow"))
        print("5.)   Show Data")
        print("6.)   Erase",colored("(Hapus berdasarkan index)","yellow"))
        print("7.)   Sort from Smallest Element")
        print("8.)   Even Data")
        print("9.)   Odd Data")
        print("10.)  Penerapan SLL",colored("Topic 7 Praktek Single Linked List 2","cyan"))
        print("0.)", colored("  Exit", 'red'))
        choose = str(input("masukan pilihan anda : "))
        if choose == "1":
            os.system("clear")
            rep = int(input("Berapa kali -> ")) # repetition
            i = 1
            while i != (rep + 1):
                dataInput = str(input("Data ke - {} : ".format(i)))
                SLL.append(dataInput)
                i+=1
            continue
        if choose == "2":
            os.system("clear")
            rep = int(input("Berapa kali (repeatation)-> "))
            i = 1
            while i != (rep + 1):
                dataInput = str(input("Data ke - {} : ".format(i)))
                SLL.prepend(dataInput)
                i+=1
            continue
        if choose == "3":
            os.system("clear")
            print("jumlah data sekarang adalah (Total Data) -> ",SLL.length())
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "4":
            os.system("clear")
            indexInput = int(input("Index yang ingin dicari (index search) : "))
            print("elemen yang ada di index {} adalah : ".format(indexInput))
            print(SLL.search(indexInput))
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "5":
            os.system("clear")
            print("Data anda sekarang adalah : ")
            SLL.display()
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "6":
            os.system("clear")
            print("Data anda sekarang adalah : ")
            SLL.display()
            inputData = int(input("index yang ingin di hapus : "))
            SLL.delete(inputData)
            print("index pada {} telah dihapus".format(inputData))
            print("data anda sekarang adalah : ")
            SLL.display()
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "7":
            os.system("clear")
            print("Linked List sekarang adalah :")
            SLL.display()
            print("Data disortir menjadi")
            print("-> ", end='')
            print(SLL.sort())
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "8":
            os.system("clear")
            print(colored("Linked List sekarang adalah :","yellow"))
            SLL.display()
            print(colored("Data genap dari linked ","yellow"))  
            print("->", end='')
            print(SLL.even())
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "9":
            os.system("clear")
            print(colored("Linked List sekarang adalah :","yellow"))
            SLL.display()
            print(colored("Data ganjil dari linked ","yellow"))
            print("->", end='')
            print(SLL.odd())
            back = str(input("0 untuk kembali -> "))
            if back == "0":
                continue
            else:
                break
        if choose == "10":
            os.system("clear")
            os.system("python3 pChange.py")
            continue
        if choose == "0":
            os.system("clear")
            mainloop+=2

if __name__ == "__main__":
    SLL = linkedList()
    mainDisplay()