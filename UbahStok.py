def ubah_stok(id,jumlah,parsed_game): #parameter berupa id dan jumlah dari main.py  
    for game in parsed_game: #setiap baris pada matriks
        if game[0]==id: 
            if jumlah>=0: #Kondisi penambahan stok
                game[5] = int(game[5])+jumlah
                return "Stok game {}".format(game[1]) + " berhasil ditambah. Stok sekarang: {}".format(game[5])
            elif jumlah<0: #Kondisi pengurangan stok
                if int(game[5])+jumlah>=0:
                    game[5] = int(game[5])+jumlah
                    return "Stok game {}".format(game[1]) + " berhasil dikurangi. Stok sekarang: {}".format(game[5])
                else: #jumlah yang mau dikurang harus lebih sedikit atau sama dengan stok, kalo engga gagal mengurangi stok
                    return "Stok game {}".format(game[1]) + "gagal dikurangi karena stok kurang. Stok sekarang: {}".format(game[5]) + " < {}".format((-jumlah))
                
    return "Tidak ada game dengan ID tersebut!" #id yang diinput harus sama,kalo engga langsung output hasil ini

