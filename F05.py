def ubahgame(user_role,game):
    #Validasi role user
    if user_role != "admin":
        print("Fungsi ini hanya bisa diakses oleh admin")
    else:
        idgame=input("Masukkan ID game: ")
        nama=input("Masukkan nama game: ")
        kategori=input("Masukkan kategori: ")
        tahun_rilis=input("Masukkan tahun rilis: ")
        harga=input("Masukkan harga: ")
        for games in game:
            if idgame==games[0]:
                if nama != "":
                    games[1]= nama
                if kategori != "":
                    games[2]= kategori
                if tahun_rilis != "":
                    games[3]= tahun_rilis
                if harga != "" :
                    games[4]= harga
