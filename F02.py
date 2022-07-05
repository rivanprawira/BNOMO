from function  import length, append

#Fungsi register
#Berguna untuk mendaftarkan user baru

#Kamus Lokal
#user: Array matriks dari isi file user.csv
#user_role: String, yang berisi info role dari user

#Fungsi utama
def register(user, user_role):        
        #Validasi role user
        if user_role != "admin":
            print("Fungsi ini hanya bisa diakses oleh admin")
        else:
            #Meminta input data user baru
            newUserName = input("Masukkan nama: ")
            newUserUsername = input("Masukkan username: ")
            newUserPassword = input("Masukkan password: ")
            
            #Validasi username apakah hanya mengandung a-z, A-Z, 0-9, "_", "-"
            charBanned = False
            for i in newUserUsername:
                if 65 <= ord(i) <= 90 or 48 <= ord(i) <= 57 or 97 <= ord(i) <= 122 or ord(i) == 95 or ord(i) == 45:
                    None
                else:
                    charBanned = True 

            #Pembagian kasus if else untuk apakah username sudah sesuai syarat
            if charBanned:
                print("Username hanya boleh mengandung alfabet 'a-z', 'A-Z',underscore '_', strip '-', dan angka 0-9.")
            else:
                #Membuat array yang berisi username yang sudah tersedia
                usernameExist = ['' for i in range(length(user) - 1)]
                for i in range(length(user) - 1):
                    usernameExist[i] = user[i+1][1]

                #Validasi apakah username baru sudah ada atau tidak
                usnExist = False
                for i in usernameExist:
                    if newUserUsername == i:
                        usnExist = True
                    else:
                        None
                
                #Pembagian kasus if else sesuai dengan hasil validasi
                if not usnExist:
                    newUser = [str(length(user)), newUserUsername, newUserName, newUserPassword, "user", "0"]
                    user = append(user, newUser)
                    print("Username", newUserUsername, 'telah berhasil register ke dalam "Binomo"')
                    return user
                else:
                    print("Username", newUserUsername, 'sudah terpakai, silahkan menggunakan username lain') 