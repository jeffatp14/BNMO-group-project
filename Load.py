import os
import functions.functions as fc
global user
global game
global kepemilikan
global riwayat

def Validasi_load(files) : #validasi apakah filenya ada
    if os.path.exists(files) :
        return True
    else :
        return False

def load (files,tipe) : #menerima data file dan tipe file, lalu memanggil fungsi yang sesuai dengan tipe dan mengembalikannya
    if tipe == "user" :
        return load_user(files)
    elif tipe == "game" :
        return load_game(files)
    elif tipe == "kepemilikan" :
        return load_kepemilikan(files)
    elif tipe == "riwayat" :
        return load_riwayat(files)
    else :
        print ("Tipe salah")
    
def load_user (files) : #memproses file user
    if Validasi_load(files) :
        data1 = open(files)
        raw_user = data1.readlines()
        user = fc.parser(raw_user, 6) #user matrix
        return user
    else :
         print (f"Folder “{files}” tidak ditemukan.")

def load_kepemilikan (files) :#memproses file kepemilikan
    if Validasi_load(files) :
        data2 = open(files)
        raw_kepemilikan = data2.readlines()
        kepemilikan = fc.parser(raw_kepemilikan, 2) #kepemilikan matrix
        return kepemilikan
    else :
         print (f"Folder “{files}” tidak ditemukan.")
def load_game (files) : #memproses file game
    if Validasi_load(files) :
        data3 = open(files)
        raw_game = data3.readlines()
        game = fc.parser(raw_game, 6)   #game matrix
        return game
    else :
         print (f"Folder “{files}” tidak ditemukan.")
def load_riwayat (files) : #memproses file riwayat
    if Validasi_load(files) :
        data4 = open(files)
        raw_riwayat = data4.readlines()
        riwayat = fc.parser(raw_riwayat, 5) #riwayat matrix
        return riwayat
    else :
         print (f"Folder “{files}” tidak ditemukan.")
