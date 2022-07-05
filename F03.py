from function import *
#Fungsi Login

#KAMUS

#ALGORITMA
def Login(user):
    Valid = False
    #Program memastikan sudah login
    while not Valid:
        print('='*25)
        print('\t LOGIN')
        print('Masukkan username:', end=' ')
        uname = input()
        print('Masukkan password:', end=' ')
        passw = input()
        print()
        for i in user[1:]:
            # i sudah menjadi array dengan urutan
            if (uname == i[1]) and (passw == i[3]):
                Valid = True
                break
        if (Valid):
            print('Halo ' + i[2] + '! Selamat datang di Menu Utama “BNMO”.')
        else:
            print('Password atau username salah atau tidak ditemukan')
    return i
