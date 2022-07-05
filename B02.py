import time

def kerangajaib():
        t = time.time()   # time passed since epoch (January 1,1970, 00:00:00)
        q = input("Apa pertanyaanmu? ")
        num =  1+int(str(t-int(t))[2:])%5     #memanfaatkan time(), menggunakan modulo untuk memperoleh angka acak 1-5

        if num == 1:
            print("Tidak.")
        elif num == 2:
            print("Ya.") 
        elif num == 3:
            print("Jangan!")
        elif num == 4:
            print("Itu berat, biar aku saja.")
        elif num == 5:
            print("Mustahil.")