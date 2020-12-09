from stacklib import stackAlgorithm
from termcolor import colored
import os,sys
'''
Pemasangan bagian motor
biasanya dimulai pada
bagian dalam dan jika
ingin membongkar harus
melepas bagian terluar
pada motor.
'''
def main():
    tetapJalan = 0
    sparePart = ['rangka', 'mesin', 'body']
    while tetapJalan == 0:    
        os.system("clear")
        print(colored("="*40,"green"))
        print(colored("\tPROGRAM ALGORITMA STACK\n","blue"))
        print(colored("Implementasi pemasangan & pembongkaran motor\n","cyan"))
        print(colored("Mekanik\t: Stevano Titondea Prayoga Putra"))
        print(colored("NIM\t: A11.2019.11831"))
        print(colored("Code\t: Python3"))
        print(colored("="*40,"green"))
        Proses = ""
        if sA.panjang_data() == 0:
            Proses = "Belum Mengerjakan sama sekali"
        if sA.panjang_data() == 1:
            Proses = "Baru memasang rangka, perlu memasang mesin selanjutnya"
        if sA.panjang_data() == 2:
            Proses = "Anda perlu memasang body untuk menyelesaikan motor"
        if sA.panjang_data() == 3:
            Proses = "Motor telah jadi"
        print(colored(Proses,"yellow"))
        print("1. Kerjakan motor")
        print("2. Bongkar motor")
        print(colored("0. Exit","red"))
        choose = str(input("--> "))
        if choose == "1":
            os.system("clear")
            if sA.panjang_data() == 3:
                print("Anda telah menyelesaikan motor")
                lanjut = input("enter to continue")
                pass
            else:
                panduan = 3
                i = 0
                if sA.panjang_data() == 1:
                    i = 1
                if sA.panjang_data() == 2:
                    i = 2
                while i != panduan:
                    i+=1
                    os.system("clear")
                    print(colored("Panduan:\n1. rangka\n2. mesin\n3. body\n","yellow"))
                    print("kerjaan: ",sA.tampilkan_data(),"<-- lanjutkan sesuai panduan")
                    print("pasang bagian ke %s"%i)
                    do = str(input("--> "))
                    sA.tambah_data(do)
                    if i == 1:
                        if sA.tampilkan_data()[0] != sparePart[0]:
                            print(colored("Gagal memasang bagian (bagian: tidak sesui panduan)","red"))
                            lanjut = input("enter to continue")
                            sA.hapus_data()
                            break
                        else:
                            pass
                    if i == 2:
                        if sA.tampilkan_data()[1] != sparePart[1]:
                            print(colored("Gagal memasang bagian (bagian: tidak sesui panduan)","red"))
                            lanjut = input("enter to continue")
                            sA.hapus_data()
                            break
                        else:
                            pass
                    if i == 3:
                        if sA.tampilkan_data()[2] != sparePart[2]:
                            print(colored("Gagal memasang bagian (bagian: tidak sesui panduan)","red"))
                            lanjut = input("enter to continue")
                            sA.hapus_data()
                            break
                        else:
                            pass
        if choose == "2":
            os.system("clear")
            if sA.panjang_data() != 3:
                print(colored("\nBelum ada motor yang jadi\nSelesaikan terlebih dahulu perakitan","yellow"))
                lanjut = input("enter to continue")
                pass
            else:
                print("kerjaan anda sekarang telah selesai\nbagian terpasang:")
                bag1 = str(sA.tampilkan_data()[0])
                bag2 = str(sA.tampilkan_data()[1])
                bag3 = str(sA.tampilkan_data()[2])
                print("1.",bag1)
                print("2.",bag2)
                print("3.",bag3)
                perulangan = 0
                while perulangan != 3:
                    i = 3
                    if sA.panjang_data() == 2:
                        i = 2
                    if sA.panjang_data() == 1:
                        i = 1
                    while i != 0:
                        os.system("clear")
                        print(sA.tampilkan_data())
                        copotBagian = str(input("Bagian yang dicopot --> "))
                        if i == 3:
                            if copotBagian == "body":
                                print("bagian ke",format(i),bag3,"Berhasil di copot")
                                sA.hapus_data()
                                lanjut = input("enter to continue")
                                perulangan+=1
                            else:
                                print(colored(("Harus melepaskan",bag3,"untuk menyelesaikan pembongkaran"),"red"))
                                lanjut = input("enter to continue")
                                break
                        if i == 2:
                            if copotBagian == "mesin":
                                print("bagian ke",format(i),bag2,"Berhasil di copot")
                                sA.hapus_data()
                                lanjut = input("enter to continue")
                                perulangan+=1
                            else:
                                print(colored(("Harus melepaskan",bag2,"untuk menyelesaikan pembongkaran"),"red"))
                                lanjut = input("enter to continue")
                                break
                        if i == 1:
                            if copotBagian == "rangka":
                                print("bagian ke",format(i),bag1,"Berhasil di copot")
                                sA.hapus_data()
                                lanjut = input("enter to continue")
                                perulangan+=1
                            else:
                                print(colored(("Harus melepaskan",bag1,"untuk menyelesaikan pembongkaran"),"red"))
                                lanjut = input("enter to continue")
                                break
                        i-=1
        if choose == "0":
            tetapJalan+=1
            os.system("clear")
if __name__ == "__main__":
    sA = stackAlgorithm()
    main()