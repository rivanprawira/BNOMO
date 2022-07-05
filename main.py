import argparse
import os
from re import X
import time
from B02 import kerangajaib
import function
import F02, F03, F04, F05, F06, F07, F08, F09, F10, F12, F13, F16, F17 , F11, F14, F15

#Program "BNMO"
#BNMO adalah sebuah robot game dengan sistem inventaris dan toko game. 
#Berikut adalah kode dari BNMO untuk mengatur dan menjalankan sistem 
#inventaris dan toko game dari BNMO sendiri

#Kamus Lokal
#user, game, riwayat, kepemilikan: Array berupa matriks data pada file csv
#user_id, user_username, user_nama, user_password, user_role, user_saldo: String yang berisi info dari user yang sedang menjalankan program
#login: Boolean apakah user sudah login atau belum

#Algoritma
#Deklarasi ArgParse
parser = argparse.ArgumentParser(description = "Argparse")
parser.add_argument('folder', type = str, help = 'Lokasi penyimpanan', default = '')
args = parser.parse_args()

F15.load()

#Pembukaan awal
print("\nSelamat datang di BNMO!\n")
time.sleep(1.5)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@//@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@//@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@//@@//@@@@@       @@      @@@          @@       @@@")      
print("@@@@@//@@@@@@  @@@  @@  @@   @@  @@  @@  @@  @@@  @@@")  
print("@@@@//@@@@@@@       @@  @@   @@  @@  @@  @@       @@@")   
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print("Silahkan masukkan perintah untuk menjalani program\nSilahkan login terlebih dahulu untuk mengakses program utama")
perintah = input(">>>")

#Memberi value ke variabel awal untuk menjalankan program
login = False
main = True

#Membuat beberapa variabel array sesuai dengan file csv yang ada
game = function.csvToArr(args.folder + "\\game.csv")
user = function.csvToArr(args.folder + "\\user.csv")
riwayat = function.csvToArr(args.folder + "\\riwayat.csv")
kepemilikan = function.csvToArr(args.folder + "\\kepemilikan.csv")

#Menambahkan variabel info user yang akan diubah ketika user login
user_id = ""
user_username = ""
user_nama = ""
user_password = ""
user_role = ""
user_saldo = 0

while not login:
    if perintah == "login":
        i = F03.Login(user)
        login = True
        user_id = i[0]
        user_username = i[1]
        user_nama = i[2]
        user_password = i[3]
        user_role = i[4]
        user_saldo = int(i[5])
        break
    elif perintah == "help":
        F14.help(user_role,login)
    else:
        print("Silahkan Login terlebih dahulu sebelum memasuki ke dalam program utama")
    perintah = input(">>>")   


print("Silahkan masukkan perintah yang diinginkan ")
while login and main:
    perintah = input(">>>")
    if perintah == 'register':
        user = F02.register(user, user_role)
    elif perintah == 'tambah_game':
        game = F04.tambah_game(game,user_role)
    elif perintah == 'ubah_game':
        F05.ubahgame(user_role, game)
    elif perintah == 'ubah_stok':
        F06.ubah_stok(user_role,game)
    elif perintah == 'list_game_toko':
        F07.list_game_toko(game)
    elif perintah == 'buy_game':
        [kepemilikan,i[5],riwayat] = F08.buy_game(user_role, game, kepemilikan, user_id, user_saldo,riwayat)
    elif perintah == 'list_game':
        F09.list_game(user_role, kepemilikan, user_id, game)
    elif perintah == 'search_my_game':
        F10.search_my_game(game, kepemilikan, user_role, user_id)           
    elif perintah == 'search_game_at_store':
        F11.search_game_at_store(game)
    elif perintah == 'topup':
        F12.topup(user_role, user)
    elif perintah == 'riwayat':
        F13.riwayatUser(riwayat, user_id, user_role)
    elif perintah == 'help':
        F14.help(user_role,login)
    elif perintah == 'save':
        F16.save(user, game, kepemilikan, riwayat)
    elif perintah == 'exit':
        F17.exit(user, game, kepemilikan, riwayat)
        main = False
    elif perintah == 'kerangajaib':
        kerangajaib()
    else:
        print("Perintah tidak tersedia. Silahkan masukkan perintah yang lain")