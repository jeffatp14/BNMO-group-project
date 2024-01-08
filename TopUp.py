def topup(parsed_user): #parameter berupa username dan saldo dari main.py
    username = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo: ")) 

    while username == '' or saldo == '':   #validasi
        print("Username atau saldo tidak boleh kosong. Silakan coba lagi")
        username = input("Masukkan username: ")
        saldo = int(input("Masukkan saldo: ")) 

    for user in parsed_user: #setiap baris pada matriks
        if user[1] == username:
            if int(user[5]) + saldo >= 0:    #kalau saldo akhir lebih dari atau sama dengan nol
                user[5] = str(int(user[5]) + saldo)
                if saldo > 0:
                    return "Top up berhasil. Saldo {} ".format(user[2]) + "bertambah menjadi {}.".format(user[5])   #jika berhasil
                else:
                    return "Top up berhasil. Saldo {} ".format(user[2]) + "berkurang menjadi {}.".format(user[5])
            else:
                return "Masukan tidak valid." #jika saldo akhir < 0

    return 'Username "{}" tidak ditemukan.'.format(username)    #jika tidak ditemukan



        