# Module MenambahGameKeTokoGame
# Berisi fungsi/prosedur untuk menambah game ke toko game (F04 - Menambah Game Ke Toko Game).

import functions.functions as fc

def isNumber(str) :
# Mengecek apakah string yang dimasukkan merupakan susunan angka-angka (type string dapat dianggap langsung sebagai array of character).
    isStrNumber = True
    if fc.leng(str) == 0 : # str == "" (string kosong)
        isStrNumber = False
    else : # str != ""
        # Mengecek apakah tiap karakter penyusun str adalah angka, nilai ASCII angka : 48 s.d. 57
        for i in range(fc.leng(str)) :
            if not(ord(str[i]) >= 48 and ord(str[i]) <= 57) :
                isStrNumber = False
    return isStrNumber

# Fungsi Utama
def tambah_game(game) :
# Menambah permainan pada matriks “game” sesuai dengan informasi yang dimasukkan saat fungsi dipanggil. Informasi yang dimasukkan divalidasi hingga didapat masukan yang valid 
# (bukan masukan kosong dan untuk informasi tahun, harga, dan stok berupa susunan angka-angka).
    # Masukan pertama
    nama = input("Masukkan nama game: ") 
    kategori = input("Masukkan kategori: ")
    tahun = input("Masukkan tahun rilis: ") 
    harga = input("Masukkan harga: ")
    stok = input("Masukkan stok awal: ")
    # Validasi hingga didapat data valid : tidak ada informasi yang terlewat, serta informasi tahun, harga, dan stok harus berupa susunan angka.
    while nama == "" or kategori == "" or tahun == "" or harga == "" or stok == "" or not(isNumber(tahun) and isNumber(harga) and isNumber(stok)) : 
        print("Mohon masukkan semua informasi yang valid mengenai game agar dapat disimpan BNMO.")
        nama = input("Masukkan nama game: ") 
        kategori = input("Masukkan kategori: ")
        tahun = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok = input("Masukkan stok awal: ")
    # Menampilkan pesan keberhasilan
    print("Selamat, game {} berhasil ditambahkan!".format(nama))
    # Masukan sudah valid, membuat string game id
    nomorId = str(fc.leng(game) + 1)
    # Format dari game ID adalah “GAMEXXX” dengan XXX adalah angka-angka yang menunjukkan urutan game pada matriks “game”
    if fc.leng(nomorId) == 1 :
        gameId = "GAME00" + nomorId
    elif fc.leng(nomorId) == 2 :
        gameId = "GAME0" + nomorId
    else : # fc.leng(nomor) == 3 
        gameId = "GAME" + nomorId
    # Meng-update matriks “game” dengan menyimpan informasi dalam array gameBaru terlebih dahulu
    gameBaru = [gameId, nama, kategori, tahun, harga, stok]
    fc.apen(game, gameBaru)
    return game 
