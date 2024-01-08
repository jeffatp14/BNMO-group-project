import os;import functions.functions as fc
import time
global user
global game
global riwayat
global kepemilikan

def convert_data(data): #mengubah data menjadi string
    string_data = ""
    a=0
    for array_data in data:
        array_data_string = [str(var_data) for var_data in array_data] #mengubah masing-masing data menjadi string
        for x in array_data_string: #mengeluarkan data string dari array menjadi string
            if a>0 :
                string_data+=';'+x 
            else :
                string_data +=x
            a+=1
        string_data += '\n'
        a=0
    return string_data

def Validasi_save(files) : #validasi apakah filenya ada
    if os.path.exists(files) :
        return True
    else :
        return False

def save(user,game,kepemilikan,riwayat) :
    namafolder = str(input("Masukkan nama folder penyimpanan: "))
    while namafolder=='':
        print ("Nama Folder yang diinput kosong.Tolong masukan ulang nama folder") #jika namafolder kosong, maka akan terus diulang sampai namafolder tidak kosong
        namafolder = str(input("Masukkan nama folder penyimpanan: "))
    print("Saving..")
    time.sleep(3) #memberikan jeda 3 detik
    if Validasi_save(namafolder): #Validasi apakah namafolder sudah ada atau belum. 
        open_user = open(f"{namafolder}"+"/user.csv", "w") #namafolder sudah ada, langsung menulis data pada file masing - masing
        open_user.write (convert_data(user))
        open_game = open(f"{namafolder}"+"/game.csv", "w")
        open_game.write(convert_data(game))
        open_kepemilikan = open(f"{namafolder}"+"/kepemilikan.csv", "w")
        open_kepemilikan.write (convert_data(kepemilikan))
        open_riwayat = open(f"{namafolder}"+"/riwayat.csv", "w")
        open_riwayat.write(convert_data(riwayat))
    else : #namafolder belum ada
        os.makedirs(namafolder) #membuat folder baru 
        open_user = open(f"{namafolder}"+"/user.csv", "w") #menulis data pada file masing - masing
        open_user.write (convert_data(user))
        open_game = open(f"{namafolder}"+"/game.csv", "w")
        open_game.write(convert_data(game))
        open_kepemilikan = open(f"{namafolder}"+"/kepemilikan.csv", "w")
        open_kepemilikan.write (convert_data(kepemilikan))
        open_riwayat = open(f"{namafolder}"+"/riwayat.csv", "w")
        open_riwayat.write(convert_data(riwayat))
    print("Data telah disimpan pada folder ",namafolder, " !")
    return


