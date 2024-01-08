def help() : 
    role = input("Masukkan role Anda (Admin/User) : ") #meminta role dari pengguna
    if role == "Admin" :
        return help_admin() #menampilkan panduan penggunaan sistem yang dapat diakses oleh Admin
    elif role == "User" :
        return help_user() #menampilkan panduan penggunaan sistem yang dapat diakses oleh User
    else :
        return "Role salah" #input role salah
    

def help_admin() :
    print ("""
============ HELP ============
1. reg - Untuk melakukan registrasi user baru
2. login - Untuk melakukan login ke dalam sistem
3. tambah_game - Untuk menambah game yang dijual pada toko
4. ubah_game - Untuk mengubah data game yang dijual pada toko
5. Ubah_Stok - Untuk mengubah stok game yang dijual pada toko
6. list_game_toko - Untuk melihat list game yang dijual pada toko
7. cari_game_toko - Untuk mencari game yang dijual pada toko
8. topup_saldo - Untuk menambahkan saldo pada user 
9. Help - Untuk memberikan panduan penggunaan sistem
10. Save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
11. Exit - Untuk keluar dari aplikasi
""")

def help_user() :
        print ("""
============ HELP ============
1. login - Untuk melakukan login ke dalam sistem
2. list_game_toko - Untuk melihat list game yang dijual pada toko
3. buy_game - Untuk membeli game
4. lihat_game_dimiliki - Untuk melihat daftar game yang dimiliki oleh pengguna
5. cari_game_dimiliki - Untuk mencari game yang dimiliki oleh pengguna
6. cari_game_toko - Untuk mencari game yang dijual pada toko
7. riwayat - Untuk melihat riwayat pembelian game yang dilakukan oleh pengguna
8. Help - Untuk memberikan panduan penggunaan sistem
9. Save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
10. Exit - Untuk keluar dari aplikasi
""")
