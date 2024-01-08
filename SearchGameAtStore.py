import functions.functions as fc

def ada(text):
    if text != '':
        return True 
    return False

def tru(list):
    for item in list:
        if item == False:
            return False 
    return True

def search_at_store(parsed_game, gameid, gamename, gamegenre, gameyear, gameprice):
    searched = []
    params = [gameid, gamename, gamegenre, gameyear, gameprice]
    indexes = []

    for i in range(5):
        if ada(params[i]):
            fc.apen(indexes, i)

    tf = []
    for game in parsed_game:
        for index in indexes:
            if params[index] == game[index]:
                fc.apen(tf, True) 
            else:
                fc.apen(tf, False)
        if tru(tf):
            fc.apen(searched, game)
        tf = []

    return searched
