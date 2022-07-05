from function import *
# FUNGSI MEMBELI GAME

# KAMUS

# ALGORITMA
def buy_game(user_role,game,kepemilikan,user_id,user_saldo,riwayat):
    # Validasi role dari user
    if user_role != 'user':
        print('Hanya user yang bisa melakukan fungsi ini.')
    else:
        # game = [id,nama,kategori,tahun rilis,harga,stok]
        # kepemilikan = [game_id,user_id]
        valid = True

        id_game = input('Masukkan ID Game: ')
        print()

        # Mengecek apakah sudah memiliki game tersebut atau tidak
        for cek in kepemilikan[1:]:
            if id_game == cek[0] and user_id == cek[1]:
                print('Anda sudah memiliki Game tersebut!')
                valid = False

        # Jika belom akan dicek id game
        if valid:
            for cek in game[1:]:
                if cek[0] == id_game:
                    # Cek saldo apakah memnuhi
                    if user_saldo >= int(cek[4]):
                        # Cek stok apakah memenuhi
                        if int(cek[5]) > 0:
                            print(f'Game "{cek[1]}" berhasil dibeli!')
                            cek[5] = int(cek[5]) - 1
                            cek[5] = str(cek[5])
                            user_saldo = user_saldo - int(cek[4])
                            user_saldo = str(user_saldo)
                            kepemilikan = kepemilikan + [[id_game, user_id]]
                            # pengubahan file riwayat
                            riwayat = riwayat + [[cek[0], cek[1], cek[4], user_id, '2022']]
                            valid = False

                        else:
                            print('stok Game tersebut sedang habis!')
                            valid = False
                    else:
                        print('Saldo Anda tidak cukup untuk membeli Game tersebut!')
                        valid = False
        # jika tidak ada id game
        # Asumsi id game bisa salah
        if valid:
            print('Masukan id game salah!!')
    return kepemilikan,user_saldo,riwayat