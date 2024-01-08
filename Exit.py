import modules.Save as Save
global user
global game
global kepemilikan
global riwayat
def exit(user,game,kepemilikan,riwayat) :
    a_exit = 0
    while a_exit == 0 : #jika input salah, maka akan diulang sampai input benar
        jawaban_exit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") #menanyakan pengguna apakah mau save/ga
        if jawaban_exit == "Y" or jawaban_exit == "y" or jawaban_exit == "N" or jawaban_exit == "n" :
            a_exit = 1 
            if jawaban_exit == "Y" or jawaban_exit == "y" : #bila pengguna ingin save
                Save.save(user,game,kepemilikan,riwayat) 
        else : 
            a_exit = 0
