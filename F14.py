def help(role,login): # Definisi fungsi role pengguna
    if not login :
        role = input("Masukkan role pengguna : ")
    if role == "Admin" or role == "admin": # Apabila role pengguna adalah sebagai admin
        print("======== HELP ========")
        print("1. register - Untuk mendaftarkan pengguna baru dengan memasukkan nama, username, dan password")
        print("2. login - Untuk masuk ke dalam aplikasi dengan memasukkan username dan password")
        print("3. tambah_game - Untuk menambah game pada toko game")
        print("4. ubah_game - Untuk mengubah game pada toko game")
        print("5. ubah_stok - Untuk mengubah stok game di toko")
        print("6. list_game_toko - Untuk melihat game-game yang ada di toko")
        print("7. search_game_at_store - Untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("8. topup - Untuk menambahkan saldo kepada User")
        print("9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
        print("10. help - memberikan panduan penggunaan sistem")
        print("11. exit - keluar dari program")

    elif role == "User" or role == "user": # Apabila role pengguna adalah sebagai user
        print(" ======== HELP ========")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("3. beli_game - Untuk membeli game yang terdapat di toko")
        print("4. list_game - Untuk melihat list game yang dimiliki")
        print("5. search_my_game - Untuk mencari game yang dimiliki dari ID dan Tahun Rilis")
        print("6. search_game_at_store - Untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("7. riwayat - Untuk melihat riwayat pembelian game")
        print("8. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
        print("9. help - memberikan panduan penggunaan sistem")
        print("10. exit - keluar dari program")
