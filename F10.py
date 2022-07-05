from function  import length, printMatriks, lenColCSV       

#Fungsi search_my_game()
#Fungsi untuk mencari game yang dimiliki sesuai dengan game id dan/atau tahun yang dimasukkan

#Kamus Lokal
#game: Array Matriks berisi data file game.csv
#kepemilikan: Array Matriks berisi data file kepemilikan.csv
#user_role: String berisi info role user
#user_id: String berisi info id dari user

#10.1. Fungsi jumlahGame berfungsi untuk mencari jumlah game yang dimiliki user
#Input: Arr, matriks dari file kepemilikan.csv. 
#       usnID, ID dari user
#Output: Int berupa jumlah game yang dimiliki user dengan ID usnID
def jumlahGame(Arr, usnID):
    jumlah = 0
    for i in range(length(Arr)):
        if Arr[i][1] == usnID:
            jumlah += 1
        else:
            None
    return jumlah

#10.2 Fungsi inventory berfungsi untuk menghasilkan matriks dari game yang dimiliki user
#Input: ArrG, Array berupa matriks dari file game.csv
#       ArrK, Array berupa matriks dari file kepemilikan.csv
#       usnID, Int berupa user ID dari user
#Output: Array berupa matriks dari game yang dimiliki user
def inventory(ArrG, ArrK, usnID):
    inventoryGameID = ['' for i in range(jumlahGame(ArrK, usnID))]
    numGame = 0
    for i in range(length(ArrK)):
        if ArrK[i][1] == usnID:
            inventoryGameID[numGame] = ArrK[i][0]
            numGame += 1
        else:
            None
    inventory = [['' for i in range(lenColCSV(ArrG))] for i in range(jumlahGame(ArrK, usnID))]
   
    for i in range(length(ArrG)):
        for j in range(length(inventoryGameID)):
            if ArrG[i][0] == inventoryGameID[j]:
                inventory[j] = ArrG[i]
            else:
                None
    return inventory

#10.3 Fungsi countGamebyYear berfungsi untuk mencari banyaknya game di inventory yang memiliki tahun rilis "year"
#Input: arrI, Array berupa matriks dari Inventory User
#       year, tahun rilis yang ingin dicari
#Output: Int berupa banyaknya game di inventory yang memiliki tahun rilis "year"
def countGamebyYear(arrI, year):
    jumlah = 0
    for i in range(length(arrI)):
        if arrI[i][3] == year:
            jumlah += 1
        else:
            None
    return jumlah

#10.4 Fungsi searchByYear berfungsi untuk mencari game di inventory yang memiliki tahun rilis "year"
#Input: arrI, Array berupa matriks dari Inventory User
#       arrG, Array berupa matriks dari file game.csv
#       year, tahun rilis yang ingin dicari
#Output: Array berupa matriks yang berisi game di inventory yang memiliki tahun rilis "year"
def searchByYear(arrI, arrG, year):
    aftSearch = [['' for i in range(lenColCSV(arrG))] for i in range(countGamebyYear(arrI, year))]
    for i in range(length(arrG)):
        for j in range(length(aftSearch)):
            if arrG[i][3] == year:
                aftSearch[j] = arrG[i]
            else:
                None
    return aftSearch

#10.5 Fungsi countGamebyGameID berfungsi untuk mencari banyaknya game di inventory yang memiliki id "GID"
#Input: arrI, Array berupa matriks dari Inventory User
#       GID, Game ID yang ingin dicari
#Output: Int berupa banyaknya game di inventory yang memiliki id game "GID"
def countGamebyGameID(arrI, GID):
    jumlah = 0
    for i in range(length(arrI)):
        if arrI[i][0] == GID:
            jumlah += 1
        else:
            None
    return jumlah

#10.6 Fungsi searchByGameID berfungsi untuk mencari game di inventory yang memiliki id game "GID"
#Input: arrI, Array berupa matriks dari Inventory User
#       arrG, Array berupa matriks dari file game.csv
#       GID, Game ID yang ingin dicari
#Output: Array berupa matriks yang berisi game di inventory yang memiliki id game "GID"
def searchByGameID(arrI, arrG, GID):
    aftSearch = [['' for i in range(lenColCSV(arrG))] for i in range(countGamebyGameID(arrI, GID))]
    for i in range(length(arrG)):
        for j in range(length(aftSearch)):
            if arrG[i][0] == GID:
                aftSearch[j] = arrG[i]
            else:
                None
    return aftSearch


#Fungsi utama
def search_my_game(game, kepemilikan, user_role, user_id):      
    #Validasi role dari user
    if user_role != "user":
        print("Hanya user yang bisa melakukan fungsi ini.")
    else:
        #Membuat inventory dari game yang dimiliki user
        inventoryUser = inventory(game, kepemilikan,user_id)

        #Meminta input untuk nilai yang ingin dicari
        searchGameID = input("Masukkan ID Game: ")
        searchYear = input("Masukkan Tahun Rilis Game: ")
        
        #Pembagian kasus if else sesuai dengan input user
        if searchGameID == "" and searchYear == "":
            aftSearch = inventoryUser
        elif searchGameID != "" and searchYear == "":
            aftSearch = searchByGameID(inventoryUser, game, searchGameID)
        elif searchGameID == "" and searchYear != "":
            aftSearch = searchByYear(inventoryUser, game, searchYear)
        elif searchGameID != "" and searchYear != "":
            aftSearch = searchByYear(inventoryUser, game, searchYear)
            aftSearch = searchByGameID(aftSearch, game, searchGameID)
            
        print("Daftar game pada inventory yang memenuhi kriteria:")
        if length(aftSearch) > 0:
            printMatriks(aftSearch)
        else:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")