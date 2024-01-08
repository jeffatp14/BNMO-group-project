# Module Login
# Berisi fungsi/prosedur untuk melakukan login akun (F03 - Login).

import functions.functions as fc
import modules.Register as rg

def findAttr(user, id, attrIdx) : 
# Mencari atribut tertentu dari matriks “user” berdasarkan “id” yang dimasukkan. Atribut yang dicari tersebut ditentukan oleh “attrIdx”. 
# “attrIdx” adalah indeks kolom dari atribut yang ingin dicari pada matriks “user” (attrIdx bernilai [0..5])
    return user[id-1][attrIdx]

# Fungsi Utama
def login(user) :
# Menyediakan fitur login dengan cara menyocokkan informasi yang dimasukkan (username dan password) saat fungsi dipanggil dengan matriks “user”. 
# Jika login berhasil, fungsi akan mengembalikan id dari pengguna yang login (> 0), jika tidak akan mengembalikan 0.
    # Masukan
    usn = input("Masukkan username: ")
    pw = input("Masukkan password: ")
    # Mengecek usn dan pw terhadap data pada matriks "user"
    if rg.findId(user,usn) > 0 : # Username ditemukan
        if findAttr(user, rg.findId(user,usn), 3) == pw : # attrIdx dari password adalah 3
            # Password sesuai, login berhasil
            print("Halo, {}! Selamat datang di Binomo.".format(findAttr(user, rg.findId(user,usn), 2))) # attrIdx dari nama adalah 2
        else : # Login gagal karena password tidak sesuai data pada matriks "user"
            print("Password salah.")
            return 0
    else : # Login gagal karena username tidak ditemukan (rg.findId(user,usn) == 0)
        print("Username salah atau tidak ditemukan.")
    return rg.findId(user,usn) # Jika login berhasil, rg.findId(user,usn) > 0, jika tidak rg.findId(user,usn) == 0.
