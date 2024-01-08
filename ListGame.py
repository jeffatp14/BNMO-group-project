import functions.functions as fc    #import fungsi-fungsi yang ada di functions.py
def listGame(UserID, parsed_owned, parsed_game):    #mereturn game yang user punya
    UserGameID = []
    UserGames = []

    l = fc.leng(parsed_owned)
    l2 = fc.leng(parsed_game)

    for i in range(l):
        if int(parsed_owned[i][1]) == UserID:
            fc.apen(UserGameID, parsed_owned[i][0])

    for id in UserGameID:
        for i in range(l2):
            if id == parsed_game[i][0]:
                fc.apen(UserGames, parsed_game[i])

    return UserGames
            