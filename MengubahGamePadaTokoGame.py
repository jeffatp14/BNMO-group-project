# Module MengubahGamePadaTokoGame
# Berisi fungsi/prosedur untuk mengubah game pada toko game (F05 - Mengubah Game Pada Toko Game).

import functions.functions as fc
import modules.MenambahGameKeTokoGame as tambahgame

def findGameId(gID,game) :
# Mencari nomor game ID pada matriks “game” berdasarkan “gID” (game ID) yang dimasukkan. Jika game ID tersebut terdaftar pada matriks “game”, 
# fungsi mengembalikan game ID tanpa "GAME", jika tidak ada, mengembalikan 0. gID ber-type string, dapat langsung dianggap sebagai array of character.
    N = fc.leng(game) # Jika N = 0, maka akan menghasilkan kasus kosong, tetapi return fungsi tetap benar karena jika N = 0 artinya tidak ada game yang dapat diubah (game tidak ditemukan).
    found = False
    # Mengecek setiap game ID pada matriks “game”
    for i in range(N) :
        if gID == game[i][0] :
            found = True
            break
    if found : # game ID ditemukan
        return 100 * int(gID[4]) + 10 * int(gID[5]) + int(gID[6]) # Format dari gID yang valid adalah “GAMEXXX” dengan XXX adalah angka yang menunjukkan urutan game pada matriks “game”, XXX > 001
    else :
        return 0 # game ID tidak ditemukan

# Fungsi Utama
def ubah_game(game) :
# Mengubah permainan pada matriks “game” sesuai dengan informasi yang dimasukkan pada saat fungsi dipanggil. Informasi yang divalidasi adalah tahun dan harga 
# (jika memasukkan salah satu informasi tersebut, harus berupa angka). Mengembalikan matriks “game” yang sudah terupdate.
    # Masukan pertama
    ID = input("Masukkan ID game: ") 
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    # Validasi hingga didapat masukan yang valid : game ID ditemukan, dan jika memasukkan data harga atau tahun, data tersebut harus berupa susunan angka-angka
    while not(findGameId(ID,game) > 0 and (tambahgame.isNumber(tahun) or tahun == "") and (tambahgame.isNumber(harga) or harga == "")) :
        print("Masukkan ID yang valid, atau jika ingin mengubah tahun dan/atau harga, masukkan tahun dan/atau harga yang valid.")
        ID = input("Masukkan ID game: ") 
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
    # Menampilkan pesan keberhasilan
    print("Informasi game berhasil diubah.")
    # Seluruh masukan telah valid, menyimpan data masukan dalam array temp
    temp = [ID, nama, kategori, tahun, harga]
    # Mengubah data game dengan game ID "ID" pada matriks user sesuai masukan, jika masukan == "" maka dilewati (data tidak diubah)
    for i in range(1,fc.leng(temp)) :
        if temp[i] != "" :
            game[findGameId(ID,game)-1][i] = temp[i]
    return game
