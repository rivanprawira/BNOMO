import argparse
import os
import time
from function import *

#Deklarasi ArgParse
parser = argparse.ArgumentParser(description = "Argparse")
parser.add_argument('folder', type = str, help = 'Lokasi penyimpanan', default = '')
args = parser.parse_args()


#Function save
def save(user,game,kepemilikan,riwayat):
    folder = input("Masukkan nama folder penyimpanan: ") #program meminta input folder
    if not os.path.exists(folder): #mengecek eksistensi folder
        resp = input(f"Directory {folder} tidak ada, perlu buat directory?(Y/N) or (y/n)\n".format(folder))
        if resp == "Y" or resp == "y":
            os.makedirs(folder)
            args.folder = folder
        else: # resp=="N" or resp == "n"
            print("Mohon maaf, save gagal.")         
            return
    print()
    print("Menyimpan...")
    time.sleep(2)
    with open(args.folder + "\\user.csv", "w+") as f: #membuka file csv user
        for line in user:
                for x in [line]:  #kategori data user ada sebanyak 6 
                    data=join(x,";")    #melakukan perubahan/penyimpanan 
                    f.write(data)
                    f.write("\n")
    with open(args.folder + "\\game.csv", "w+") as f: #membuka file csv game
            for line in game:
                for x in [line]:  #kategori data game ada sebanyak 6 
                    data=join(x,";")
                    f.write(data)
                    f.write("\n")    
    with open(args.folder + "\\riwayat.csv", "w+") as f: #membuka file csv riwayat
            for line in riwayat:
                for x in [line]:  #kategori data riwayat ada sebanyak 5
                    data=join(x,";")
                    f.write(data)
                    f.write("\n")
    with open(args.folder + "\\kepemilikan.csv", "w+") as f: #membuka file csv kepemilikan
            for line in kepemilikan:
                for x in [line]:  #kategori data kepemilikan ada sebanyak 2
                    data=join(x,";")
                    f.write(data)
                    f.write("\n")
    print("Data berhasil disimpan.")     