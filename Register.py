# Module Register
# Berisi fungsi/prosedur untuk melakukan registrasi akun (F02 - Register).

import functions.functions as fc

def findId(user, usn) :
# Mencari ID pada matriks “user” berdasarkan “usn” (username) yang dimasukkan. Jika username tersebut terdaftar pada matriks “user” fungsi mengembalikan ID milik usn tersebut (ID > 0), jika tidak maka akan mengembalikan 0.
    N = fc.leng(user) # N >= 1 karena untuk melakukan fungsi ini harus ada seorang Admin sehingga tidak ada kasus kosong.
    found = False 
    # Mengecek setiap username pada matriks “user”
    for i in range(N) :
        if usn == user[i][1] :
            found = True
            break
    if found :
        return i + 1 # Username ditemukan (terdaftar), mengembalikan ID milik username tersebut (ID mulai dari 1)
    else :
        return 0 # Username tidak ditemukan (tidak terdaftar)

# Fungsi Utama
def register(user) :
# Menambahkan akun ke dalam matriks “user” berdasarkan informasi yang dimasukkan saat fungsi dipanggil. Informasi berupa username harus valid, yaitu username hanya dapat mengandung alfabet (A-Z,a-z), underscore (_), strip (-), dan angka (0-9), serta username bersifat unik. 
# Mengembalikan matriks “user” yang terupdate.
    # Masukan pertama
    nama = input("Masukkan nama: ")
    usn = input("Masukkan username: ")
    pw = input("Masukkan password: ")
    # Validasi : nama, usn, pw tidak boleh kosong
    while nama == "" or usn == "" or pw == "" :
        print("Nama, Username, dan Password tidak boleh kosong.")
        nama = input("Masukkan nama: ")
        usn = input("Masukkan username: ")
        pw = input("Masukkan password: ")
    # Validasi : mengecek tiap karakter yang terkandung pada usn, apakah mengandung karakter terlarang, ditentukan oleh nilai Valid1
    Valid1 = True
    for i in range(fc.leng(usn)):
        # nilai ASCII angka : 48 s.d. 57, alfabet nonkapital : 97 s.d. 122, alfabet kapital : 65 s.d. 90, underscore : 95, strip : 45
        if not((ord(usn[i]) >= 48 and  ord(usn[i]) <= 57) or (ord(usn[i]) >= 65 and  ord(usn[i]) <= 90) or (ord(usn[i]) >= 97 and  ord(usn[i]) <= 122) or ord(usn[i]) == 95 or ord(usn[i]) == 45) :
            Valid1 = False
            break
    # Validasi : apakah usn sudah dipakai atau belum, ditentukan oleh nilai Valid2 (Valid2 == 0 berarti belum terpakai, Valid2 > 0 berarti sudah terpakai)
    Valid2 = findId(user, usn)
    # Pesan gagal/berhasil
    if not(Valid1) : # Register gagal karena username mengandung karakter terlarang
        print("Username {} mengandung karakter yang dilarang. Username hanya dapat mengandung alfabet (A-Z,a-z), underscore (_), strip (-), dan angka (0-9).".format(usn))
    elif Valid2 != 0 : # Register gagal karena username sudah terpakai
        print("Username {} sudah terpakai, silakan menggunakan username lain.".format(usn))
    else : # Register berhasil
        print("Username {} telah berhasil register ke dalam Binomo.".format(usn))
        # Meng-update matriks “user” dengan cara menyimpan informasi tadi dalam array newAcc terlebih dahulu
        newAcc = [str(fc.leng(user)+1), usn, nama, pw, "User", "0"] # Role yang bisa diregister hanya "User" dan saldo awal == 0 (belum melakukan top up) 
        fc.apen(user,newAcc)
    return user
