import functions.functions as fc
import modules.ListGame as mygames

def search(UserID, parsed_owned, parsed_game, id, year):
    UserGame = mygames.listGame(UserID, parsed_owned, parsed_game)
    searched = []

    if id =='':
        if year == '':  #id kosong dan year kosong
            return UserGame
        else:   #id kosong dan year ada
            for game in UserGame:
                if game[3] == year:
                    fc.apen(searched, game)
    else:
        if year == '':  #id ada dan year kosong
            for game in UserGame:
                if game[0] == id:
                    fc.apen(searched, game)
        else:   #id dan year ada
            for game in UserGame: #keduanya harus sesuai
                if game[0] == id and game[3] == year:
                    fc.apen(searched, game)

    return searched
