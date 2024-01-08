import functions.functions as fc
def sorting(parsed_game, index, ad):
    front = 0
    
    if ad == "+":
        for i in range(fc.leng(parsed_game)):
            for j in range(front, fc.leng(parsed_game)):
                
                if int(parsed_game[i][index]) > int(parsed_game[j][index]):
                    parsed_game[i],parsed_game[j]=parsed_game[j],parsed_game[i]
                    
            front += 1
    elif ad == "-":
        for i in range(fc.leng(parsed_game)):
            for j in range(front, fc.leng(parsed_game)):
                
                if int(parsed_game[i][index]) < int(parsed_game[j][index]):
                    parsed_game[i],parsed_game[j]=parsed_game[j],parsed_game[i]
                    
            front += 1
    return parsed_game


def printing(parsed_game):
    
    for i in parsed_game:
        for j in range(fc.leng(i)):
            if j != (fc.leng(i)-1):
                print(i[j], end=" | ")
            else:
                print(i[j])


def list_game_toko(parsed_game, command):
    new_game_data = []
    for i in range(fc.leng(parsed_game)):
        new_game_data+=[parsed_game[i]]
    if command == '':
        printing(new_game_data)
        return ""
    else:
        try:
            a_or_d = command[5]
            command = command[0]+command[1]+command[2]+command[3]+command[4]
        
            if (command == "Tahun" or command == "tahun") and (a_or_d == "+" or a_or_d == "-"):
                idx = 3
                printing(sorting(new_game_data, idx, a_or_d))
                return ""
            elif (command == "Harga" or command == "harga") and (a_or_d == "+" or a_or_d == "-"):
                idx = 4
                printing(sorting(new_game_data, idx, a_or_d))
                return ""
            else:
                return "Input tidak valid"
        except IndexError:
            return "Masukan Tidak Valid"