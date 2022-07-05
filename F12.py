
def topup(user_role,user):
    #Validasi role user
    if user_role != "admin":
        print("Fungsi ini hanya bisa diakses oleh admin")
    else:
        username=input("Masukkan username: ")
        found=False
        for users in user:
            if username == users[1]:
                topup=int(input("Masukan saldo: "))
                saldo=int(users[5])
                if topup<0:
                    if topup*(-1)>saldo:
                        print("Masukan tidak valid.")
                    else:
                        saldo+=topup
                        users[5]=str(saldo)
                        print(f'''Top up berhasil. Saldo {username} berkurang menjadi {users[5]}.''')
                else:
                    saldo+=topup
                    users[5]=str(saldo)
                    print(f'''Top up berhasil. Saldo {username} bertambah menjadi {users[5]}.''')
                found=True
                break
        if found==False:
            print(f'''Username “{username}” tidak ditemukan.''')