import os
import sys
import math 
import time 
import argparse
import datetime

import modules.SearchMyGame as CariGim
import modules.TopUp as topup
import modules.ListGame as mygames
import modules.SearchGameAtStore as CariGimToko
import functions.functions as fc
import modules.UbahStok as Ubah_Stok
import modules.BuyGame as buygame
import modules.MengubahGamePadaTokoGame as ubahgame
import modules.MenambahGameKeTokoGame as tambahgame
import modules.ListingGame as list_game_toko
import modules.Riwayat as rwyt
import modules.Register as register
import modules.Login as login 
import modules.Login as login 
import modules.TicTacToe as tic
import modules.KerangAjaib as kerangajaib
import modules.Help as Help
import modules.Save as Save
import modules.Load as Load
import modules.Exit as Exit

#all parsed file -> matrix[attr][row]
user= Load.load(r'database/user.csv',"user")
game = Load.load(r'database/game.csv',"game")
kepemilikan = Load.load(r'database/kepemilikan.csv',"kepemilikan")
riwayat = Load.load(r'database/riwayat.csv',"riwayat")

################################################################

pilihan = fc.awalan()
while pilihan!=1 :
    if pilihan == 2 :
        Help.help()
        pilihan = fc.awalan ()
    elif pilihan == 1 :
        pass
    else :
        print ("Pilihan anda salah")
        pilihan = fc.awalan()

print("Silakan login.")
UserID = login.login(user)
while UserID == 0 :
    print("Anda harus login terlebih dahulu sebelum menggunakan Binomo.")
    UserID = login.login(user)

print("Silakan masukkan perintah.")
comm = input()
isAdmin = fc.isAdmin(UserID, user) 

while comm != 'Exit':    
    if comm == 'lihat_game_dimiliki':
        if isAdmin:
            print("Hanya User yang dapat menggunakan perintah ini.")
        else:
            if mygames.listGame(UserID, kepemilikan, game) == []:   #kalau ga punya game
                print("Maaf, Anda belum mempunyai game apapun, silakan beli terlebih dahulu.")
            else:
                print("Daftar game: ")  #kalau punya game
                fc.tableList(mygames.listGame(UserID, kepemilikan, game), 5)

    elif comm == 'cari_game_dimiliki':     #klo ini gua rapihin alias taro di modul ada bug jalan 2 kali
        if isAdmin:
            print("Hanya User yang dapat menggunakan perintah ini.")
        else:
            id = input("Masukkan ID Game: ")
            year = input("Masukkan Tahun Rilis Game: ")

            if id =='' and year =='':   #kalau ga masukin apa-apa menampilkan semua game yang user punya
                fc.tableList(mygames.listGame(UserID, kepemilikan, game), 5)
            elif CariGim.search(UserID, kepemilikan, game, id, year) == []: #ga ada game yang dimiliki yang sesuai dengan pencarian
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
            else:
                fc.tableList(CariGim.search(UserID, kepemilikan, game, id, year), 5)    #ada yang sesuai

    elif comm == 'topup_saldo':
        if isAdmin:
            print(topup.topup(user))
        else:   #kalau user nakal coba coba
            print("Hanya Admin yang dapat menggunakan perintah ini.")

    elif comm == 'cari_game_toko':     #klo ini gua rapihin alias taro di modul ada bug jalan 2 kali
        gameid = input("Masukkan ID Game: ")
        gamename = input("Masukkan Nama Game: ")
        gamegenre = input("Masukkan Kategori Game: ")
        gameyear = input("Masukkan Tahun Rilis Game: ")
        gameprice = input("Masukkan Harga Game: ")
        
        if gameid == gamename == gameprice == gamegenre == gameyear == '':  #klo kosong, nampilin semua game yang ada di toko
            print("Daftar game pada toko yang memenuhi kriteria: ")
            fc.tableList(game, 5)
        elif CariGimToko.search_at_store(game, gameid, gamename, gamegenre, gameyear, gameprice) == []:  #ga ada yang sesuai pencarian
            print("Tidak ada game yang memenuhi kriteria pada toko")
        else:
            print("Daftar game pada toko yang memenuhi kriteria: ") #ada yang sesuai
            fc.tableList(CariGimToko.search_at_store(game, gameid, gamename, gamegenre, gameyear, gameprice), 5)

    elif comm == 'Ubah_Stok':
        if isAdmin:
            id=input("Masukkan ID Game: ")
            jumlah=int(input("Masukkan jumlah: "))

            print(Ubah_Stok.ubah_stok(id, jumlah, game))
        else:
            print("Hanya Admin yang dapat menggunakan perintah ini.")
    
    elif comm == "ubah_game" :
        if isAdmin :
            game = ubahgame.ubah_game(game)
        else :
            print("Hanya Admin yang dapat menggunakan perintah ini.")
        # fc.tableList(game, 6) #jangan jadiin komen klo mau buat debugging
        
    elif comm == 'tambah_game':
        if isAdmin :
            game = tambahgame.tambah_game(game)
        else :
            print("Hanya Admin yang dapat menggunakan perintah ini.")

    elif comm == 'buy_game':
        id=input("Masukkan ID Game: ")

        print(buygame.buygame(UserID,id,riwayat,user,game,kepemilikan))

    elif comm == "list_game_toko":
        command=input("Skema sorting : ")
        print(list_game_toko.list_game_toko(game,command))
    
    elif comm == "reg":
        if isAdmin :
            user = register.register(user)
        else :
            print("Hanya Admin yang dapat menggunakan perintah ini.")
    
    elif comm == 'riwayat':
        rwyt.cetak_riwayat(rwyt.riwayat_user(UserID,riwayat))
  
    elif comm == "Help" :
        if isAdmin :
            Help.help_admin()
        else :
            Help.help_user()
  
    elif comm == "Save" :
        Save.save(user,game,kepemilikan,riwayat)
    
    elif comm == "tictactoe":
        tic.ticTacToe() 
    
    elif comm == "kerangajaib":
        kerangajaib.kerangAjaib()
    
    print("Silakan masukkan perintah selanjutnya.")
    comm = input()

Exit.exit(user,game,kepemilikan,riwayat)
