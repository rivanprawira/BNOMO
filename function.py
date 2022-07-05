#Function yang digunakan di main program
#Function umum yang digunakan di berbagai spesifikasi fungsi

#1. Fungsi length yang berfungsi untuk menghitung banyaknya suatu data dalam array atau banyaknya huruf dalam suatu string
#Input: a, Array/String
#Output: Int berupa panjang array/string
def length(a):
    len = 0
    for i in a:
        len += 1
    return len 

#2. Fungsi lenColCSV berfungsi untuk menghitung kolom dalam file csv
#Input: Arr, Array berupa baris dari isi file csv
#Output: Int berupa banyak kolom di dalam isi file csv tersebut
def lenColCSV(Arr):
    col = 1
    for i in Arr[0]:
        if i == ";":
            col += 1
    return col

#3. Fungsi csvToArr yang berfungsi mengubah file csv menjadi matriks di dalam file python
#Input: txt, string berupa nama dari file csv
#Output: Array berupa matriks dari isi csv
def csvToArr(txt):
    with open(txt, "r") as f:
        arrTemp = f.readlines()
        arr = [['' for i in range(lenColCSV(arrTemp))] for j in range(length(arrTemp))]
        numLine = 0
        col = 0
        for line in arrTemp:
            varTemp = ""
            for i in line:
                if i != ';':
                    varTemp += i
                else:   
                    arr[numLine][col] = varTemp
                    varTemp = ""
                    col += 1
                if col == lenColCSV(arrTemp) - 1:
                    varTemp1 = ''
                    for i in range(length(varTemp) - 1):
                        varTemp1 += varTemp[i]
                    arr[numLine][col] = varTemp1            
            numLine += 1
            col = 0
        return arr

#4. fungsi append berguna untuk menambahkan anggota array x pada ujung akhir array Arr
#Input: Arr, Array
#       x, sesuai dengan datatypes anggota array
#Output: Array dengan tambahan anggota x
def append(Arr, x):
    arrTemp = ['' for i in range(length(Arr) + 1)]
    for i in range(length(Arr) + 1):
        if i != length(Arr):
            arrTemp[i] = Arr[i]
        else:
            arrTemp[i] = x
    return arrTemp

#5. fungsi printMatriks berguna untuk menuliskan matriks pada output dengan rapih
#Input: Arr, berupa matriks
#Output: Menuliskan Arr dalam bentuk tabel pada output
def printMatriks(Arr):
    num = 1
    for i in Arr:
        print(f"{num}. {space(i[0],get_max_length(Arr, 0))} | {space(i[1],get_max_length(Arr, 1))} | {space(i[2],get_max_length(Arr, 2))} | {space(i[3],get_max_length(Arr, 3))} | {i[4]}")
        num += 1

#6. fungsi space berguna untuk menuliskan output dengan rapih kebawah
#Input : Str, berupa string dan n, berupa integer batas maksimal kata
#Output: Menuliskan Str dengan panjang yang sama dengan output lain
def space(Str, n):
    if length(Str) > n:
        Str
    else:
        Str = Str + str(' '*(n-length(Str)))
    return Str

#7. fungsi get_max_length berguna untuk mendapatkan nilai panjang string terbesar di kolom suatu matriks
#Input: arr, berupa array dalam bentuk matriks
#       idx, berupa index kolom yang ingin dicari
#Output:Int, berupa panjang string terpanjang di kolom tersebut
def get_max_length(arr, idx):
    arrTemp = ['' for i in range(length(arr))]
    for i in range(length(arr)):
        arrTemp[i] = arr[i][idx]
    
    x = -9999
    for i in range(length(arrTemp)):
        if length(arrTemp[i]) > x:
            x = length(arrTemp[i])
    return x

#8. Fungsi join yang digunakan untuk melakukan perluasan pada array dengan memisahkan tiap elemen dengan ";"
#Input: array, berupa array yang tersedia
#       char, berupa karakter untuk memisahkan elemen array
#Output:array, hasil penggabungan
def join(array, char=";"):
    word = ""
    for i in range (length(array)):
        word += array[i]
        if i != (length(array)-1): 
            word += char
    return word


