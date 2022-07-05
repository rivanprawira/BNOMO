def banyak(li): 
    x = 0
    for i in li:
        x += 1
    return x


# Mengambil data dari game.csv
def search_game_at_store(arrG):
   id=input('Masukan ID Game: ')
   namaGame=input('Masukan Nama Game: ')
   harga=input('Masukan Harga: ')
   Kategori=input('Masukan Kategori Game: ')
   tahun=input('Masukan tahun Game: ')
   how=''
   y=1

   # Menentukan kondisi-kondisi pencarian game pada store
   # ID | NAMA  | Harga | Kategori | Tahun rilis | stok
   print("Daftar game pada toko yang memenuhi kriteria:")
   for i in range (1,banyak(arrG)):
      if arrG[i][0]==id and arrG[i][1]==namaGame and arrG[i][2]==harga and arrG[i][3]==Kategori and arrG[i][4]==tahun:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         break
      if arrG[i][0]==id and arrG[i][1]==namaGame and arrG[i][2]==harga and arrG[i][3]==Kategori:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         break
      if arrG[i][0]==id and arrG[i][1]==namaGame and arrG[i][2]==harga:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         break
      if arrG[i][0]==id and arrG[i][1]==namaGame:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         break
      if arrG[i][0]==id:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         break
      if arrG[i][4]==tahun:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         continue
      if arrG[i][3]==Kategori and arrG[i][4]==tahun:
         print(y,'.',namaGame[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         continue
      if arrG[i][2]==harga and arrG[i][3]==Kategori and arrG[i][4]==tahun:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         continue
      if arrG[i][1]==namaGame and arrG[i][2]==harga and arrG[i][3]==Kategori and arrG[i][4]==tahun:
         print(y,'.',arrG[i][0],'|',arrG[i][1],'|',arrG[i][2],'|',arrG[i][3],'|',arrG[i][4],'|',arrG[i][5])
         how='found'
         y+=0
         continue
   if not how=='found': # Jika tidak ada game yang memenuhi kriteria
      print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
   
