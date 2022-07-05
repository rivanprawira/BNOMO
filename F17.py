import F16

#Fungsi exit()
#Fungsi untuk memberhentikan while loop sehingga program terhenti.

#Fungsi utama


def exit(user, game, kepemilikan, riwayat):
    #Meminta input saving option untuk user
    savingopt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    #Pembagian kasus if else sesuai dengan jawaban user
    inputCond = False
    while not inputCond:
        if savingopt == "y" or savingopt == "Y":
            F16.save(user, game, kepemilikan, riwayat)
            print("------------Program Selesai dan Sudah disave------------")
            inputCond = True
        elif savingopt == "n" or savingopt == "N":
            print("------------Program Selesai------------")
            inputCond = True
        else:
            savingopt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")