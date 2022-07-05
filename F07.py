from function  import printMatriks, length

#Fungsi list_game_toko
#Fungsi ini untuk menampilkan game di toko sesuai dengan skema pengurutan yang dimasukkan

#Kamus Lokal
#game: Array matriks berisi data dari file game.csv

#7.1. Fungsi sortAsc berfungsi untuk menyortir array sesuai dengan kolom "col" secara ascending(dari kecil ke besar)
#Input: li, Array berupa matriks dari suatu file csv
#       col, Int berupa indeks kolom yang akan disortir(indeks python mulai dari 0)
#Output: Array berupa matriks berisi game yang sudah disortir secara ascending pada kolom "col"
#Output:
def sortAsc(li, col):
    for i in range(1,length(li)):
        for j in range(i + 1, length(li)):
            if int(li[i][col]) > int(li[j][col]):
                li[i], li[j] = li[j], li[i]
    return li

#7.2. Fungsi sortDesc berfungsi untuk menyortir array sesuai dengan kolom "col" secara descending(dari besar ke kecil)
#Input: li, Array berupa matriks dari suatu file csv
#       col, Int berupa indeks kolom yang akan disortir(indeks python mulai dari 0)
#Output: Array berupa matriks berisi game yang sudah disortir secara descending pada kolom "col"
def sortDesc(li, col):
    for i in range(1,length(li)):
        for j in range(i + 1, length(li)):
            if int(li[i][col]) < int(li[j][col]):
                li[i], li[j] = li[j], li[i]     
    return li

#Fungsi utama
def list_game_toko(game):
        #Meminta input untuk skema sorting yang ada
        skemaSort = input("Skema sorting: ")

        #Pembagian kasus if else sesuai input user
        if skemaSort == "tahun-":
            aftsort = sortDesc(game, 3)
            printMatriks(aftsort)
        elif skemaSort == "tahun+":
            aftsort = sortAsc(game, 3)
            printMatriks(aftsort)
        elif skemaSort == "harga-":
            aftsort = sortDesc(game, 4)
            printMatriks(aftsort)
        elif skemaSort == "harga+":
            aftsort = sortAsc(game, 4)
            printMatriks(aftsort)
        elif skemaSort == '':
            printMatriks(game)
        else:
            print("Skema sorting tidak valid")