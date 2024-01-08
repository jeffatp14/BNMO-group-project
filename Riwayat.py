import functions.functions as fc

def cetak_riwayat(array):
    if fc.leng(array)!=0:
        for i in array:
            for j in range(5):
                if j != 4 and j !=3:
                    print(i[j], end=" | ")
                elif j==3:
                    pass
                else:
                    print(i[j])
    else:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.")
def riwayat_user(UserID,parsed_riwayat):
    arrRiwayat=[]
    for i in (parsed_riwayat):
        if int(i[3])==UserID:
            arrRiwayat+=[i]
    return arrRiwayat