import datetime
import functions.functions as fc

def punya_game(user_id,parsed_kepemilikan,id_game):
    punya=False
   
    for kepemilikan in parsed_kepemilikan:
        if user_id==int(kepemilikan[1]) and id_game==kepemilikan[0]:
            punya=True

            break
        else:
            pass
    return punya

def buygame(UserID,id_game,parsed_riwayat,parsed_user,parsed_game,parsed_kepemilikan):
    harga=""
    indeks=0
    
    for i in range(fc.leng(parsed_game)):
        if parsed_game[i][0]==id_game:
            harga=int(parsed_game[i][4])
            indeks=i
            if int(parsed_game[i][5])>0:
                stok_ada=True
            else:
                stok_ada=False
            break
        
    for user in parsed_user:
        if int(user[0])==UserID:
            if stok_ada and int(user[5])>=harga and (not punya_game(UserID,parsed_kepemilikan,id_game)):
                saldo_akhir=int(user[5])-harga
                user[5]=str(saldo_akhir)
                stok_akhir=int(parsed_game[indeks][5])-1
                parsed_game[indeks][5]=str(stok_akhir)
                riwayat=[id_game, parsed_game[indeks][1], harga, UserID, str(datetime.date.today().year)]
                parsed_riwayat+=[riwayat]
                parsed_kepemilikan+=[[id_game,UserID]]
                return "Game {} ".format(parsed_game[indeks][1]) +  "berhasil dibeli!"
            elif punya_game(UserID,parsed_kepemilikan,id_game):
                return "Anda sudah memiliki Game tersebut!"
            elif not stok_ada:
                return "Stok Game tersebut sedang habis"
            else: #saldo akhir < 0
                return "Saldo anda tidak cukup untuk membeli Game tersebut!"
