from function import *
# FUNGSI MENAMBAH GAME

#KAMUS
# game = [id,nama,kategori,tahun_rilis,harga,stok]

#ALGORITMA
def tambah_game(game,user_role):
    # Validasi role user
    if user_role != 'admin':
        print('Fungsi ini hanya bisa diakses oleh admin')
    else:
        # game = [id,nama,kategori,tahun_rilis,harga,stok]
        Valid = False

        # Membuat loop selama inputan belum benar
        while not Valid:
            nama = input('Masukkan nama game: ')
            kategori = input('Masukkan kategori: ')
            tahun_rilis = input('Masukkan tahun rilis: ')
            harga = input('Masukkan harga: ')
            stok = input('Masukkan stok awal: ')
            print()
            if(nama == '') or (kategori == '') or (tahun_rilis == '') or (harga == '') or (stok == ''):  # Terisi semua
                print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
            else:
                i = length(game) # Menunjukkan banyak data pada file game
                if i//100 == 0:
                    if i//10 == 0:
                        angka = '00' + str(i)
                    else:
                        angka = '0' + str(i)
                else:
                    angka = i

                game = game + [[f'GAME{angka}', nama, kategori, tahun_rilis, harga, stok]]
                print('Selamat! Berhasil menambahkan game', nama)
                Valid = True
    return game