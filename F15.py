import argparse
import os

#Deklarasi ArgParse
parser = argparse.ArgumentParser(description = "Argparse")
parser.add_argument('folder', type = str, help = 'Lokasi penyimpanan', default = '')
args = parser.parse_args()

def load():
        if not os.path.exists(args.folder):
            print('Folder "' + str(args.folder) + '" tidak ditemukan.')
            exit()
        else:
            None


        

