from function import *
#Fungsi Mengubah Stok Game

#KAMUS

#ALGORITMA

def ubah_stok(user_role,game):
    if user_role != 'admin':
        print("Fungsi ini hanya bisa diakses oleh admin")
    else:
        # game = [id,nama,kategori,tahun_rilis,harga,stok]
        Valid = 0

        id_game = input('Masukkan ID game: ')
        for cek in game[1:]:
            if id_game == cek[0]:  # Menyamakan id_game input dengan id dari file game
                ubah_stok = int(input('Masukkan jumlah: '))
                cek[5] = int(cek[5]) + ubah_stok
                if cek[5] >= 0:
                    Valid = -1
                    cek[5] = str(cek[5])
                    break
                else:
                    Valid = 1
                    cek[5] = cek[5] - ubah_stok
                    cek[5] = str(cek[5])
                    break

        if Valid == 0:
            print()
            print('Tidak ada game dengan ID tersebut!')
        elif Valid == -1:
            if ubah_stok >= 0:
                print()
                print('Stok game', cek[1], 'berhasil ditambah. Stok sekarang:', cek[5])
            else:
                print()
                print('Stok game', cek[1], 'berhasil dikurangi. Stok sekarang:', cek[5])
        elif Valid == 1:
            print()
            print('Stok game', cek[1], 'gagal dikurangi karena stok kurang. Stok sekarang:', cek[5], f'(< {ubah_stok*-1})')
