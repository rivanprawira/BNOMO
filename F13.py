from function import *

def riwayatUser(riwayat, user_id, user_role):
    if user_role == "user":
        riwayatUser = []
        for i in riwayat:
            if i[3] == user_id:
                riwayatUser = append(riwayatUser, i)
        
        for i in range(length(riwayatUser)):
            riwayatUser[i] = riwayatUser[i][:5]
        
        if length(riwayatUser) > 0:
            print("Daftar game:")
            num = 1
            for i in riwayatUser:
                print(f"{num}. {space(i[0],get_max_length(riwayatUser, 0))} | {space(i[1],get_max_length(riwayatUser, 1))} | {space(i[2],get_max_length(riwayatUser, 2))} | {space(i[4],get_max_length(riwayatUser, 3))} |")
                num += 1
        else:
            print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        print("Hanya user yang bisa melakukan fungsi ini.")
      