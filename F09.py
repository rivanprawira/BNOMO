from function import *

def list_game(user_role,kepemilikan,user_id,game): 
    #Validasi role user
    if user_role != "user":
        print("Fungsi ini hanya bisa diakses oleh user")
    else:
        list_game=[] #akan diisi game yang dimiliki
        for data in kepemilikan:
            if user_id==data[length(data)-1]:
                list_game+=data
        if list_game==[] :  # tidak memiliki game
            print("Maaf, kamu belum membeli game. Ketik perintah \033[1m buy_game \033[0m untuk beli game.")
        else:
            num=1 #penomoran daftar game
            print("Daftar game:")
            for data2 in game:    
                for game in list_game:
                    if game==data2[0]:
                        print(f"{num}. {data2[0]}  | {space(data2[1],30)} | {space(data2[2],12)} | {data2[3]} | {data2[4]}")
                        num+=1