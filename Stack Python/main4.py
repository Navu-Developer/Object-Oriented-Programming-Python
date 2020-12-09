from stacklib import stackAlgorithm
from termcolor import colored
from collections import deque
import os,sys
'''
Pada restoran, seorang pelayan
akan mengantarkan makanan dengan
urutan pembuka utama dan penutup
pemesan diprogram untuk memesan
penutup > utama > pembuka agar
dapat memenuhi algoritma LIFO

Code: Python3
'''
def main():
    menuPembuka = deque(['Salad Buah', 'Cocktail', 'Risoles'])
    menuUtama = deque(['Ayam Bakar', 'Ayam Madu', 'Ayam Goreng'])
    menuPenutup = deque(['Biskuit', 'Pai', 'Pudding'])
    chance = 0
    keepAlive = 0
    while keepAlive == 0:    
        os.system("clear")
        print(colored("="*60,"green"))
        print(colored("\t\tPROGRAM ALGORITMA STACK\n","blue"))
        print(colored("Pemilik\t: Stevano Titondea Prayoga Putra"))
        print(colored("NIM\t: A11.2019.11831"))
        print(colored("Code\t: Python3"))
        print(colored("="*60,"green"))
        print("\t\tMENU RUMAH MAKAN PAK VANO")
        print("Menu Pembuka\t\tMenu Utama\t\tMenu Penutup")
        print("Salad Buah\t\tAyam Bakar\t\tBiskuit")
        print("Cocktail\t\tAyam Madu\t\tPai")
        print("Risoles\t\t\tAyam Goreng\t\tPudding")
        print(colored("="*60,"green"))
        print("Pessanan anda: ",sA.tampilkan_data())
        print("1. Buat Pesanan")
        print("2. Antarkan Pesanan")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            if sA.panjang_data() == 3:
                print("Anda sudah memesan, tunggu sebentar")
                skip = input("enter to continue")
                pass
            else:
                tipePesanan = 3
                pesanan = 0
                if sA.panjang_data() == 1:
                    pesanan = 1
                if sA.panjang_data() == 2:
                    pesanan = 2
                while pesanan < tipePesanan:
                    os.system("clear")
                    print(colored("="*60,"green"))
                    print("\t\tMENU RUMAH MAKAN PAK VANO")
                    print("Menu Penutup\t\tMenu Utama\t\tMenu Pembuka")
                    print("Biskuit\t\t\tAyam Bakar\t\tSalad Buah")
                    print("Pai\t\t\tAyam Goreng\t\tCocktail")
                    print("Pudding\t\t\tAyam Madu\t\tRisoles")
                    print(colored("="*60,"green"))
                    print(sA.tampilkan_data())
                    pesan = str(input("pesanan ke %s--> "%(pesanan+1)))
                    for elemen in menuPenutup:
                        if pesanan == 0:
                            if pesan not in menuPenutup:
                                print("tidak ada dalam menu")
                                print(colored("tidak ada dalam menu","yellow"))
                                break
                            else:
                                sA.tambah_data(pesan)
                                pesanan+=1
                                break
                        if pesanan == 1:
                            if pesan not in menuUtama:
                                print(colored("tidak ada dalam menu","yellow"))
                                skip = input("enter to continue")
                                break
                            else:
                                sA.tambah_data(pesan)
                                pesanan+=1
                                break
                        if pesanan == 2:
                            if pesan not in menuPembuka:
                                print(colored("tidak ada dalam menu","yellow"))
                                skip = input("enter to continue")
                                break
                            else:
                                sA.tambah_data(pesan)
                                pesanan+=1
            continue
        if choose == "2":
            sA.hapus_data()            
            continue
        if choose == "0":
            keepAlive+=1
            os.system("clear")
if __name__ == "__main__":
    sA = stackAlgorithm()
    main()
    