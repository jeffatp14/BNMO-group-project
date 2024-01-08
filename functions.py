def seplit(csv):                            #padanan split. separatornya harus ;, mau diganti juga bisa
    temp = ''
    ans = []
    for row in csv:
        for char in row:
            if char != ';' and char != '\n':
                temp+=char 
            else:
                ans+=[temp]
                temp = ''

    return ans

def leng(List):                             #padanan len()
    len = 0
    for item in List:
        len+=1
    return len

def apen(list, item):                       #padanan append()
    list+=[item]
    return list

def parser(read_csv, count_attr):           #buat ubah csv yang udah direadline() jadi matriks[attribut][length] 
    list = seplit(read_csv)
    attr = list[:(count_attr-1)]
    l = leng(list)

    parse = []
    temp = []
    i = count_attr
    while i < l:
        for header in attr:
            if i == l:
                break
            temp+=[list[i]]
            if leng(temp) == count_attr:
                parse+=[temp]
                temp = []
            i+=1

    return parse

def tableList(list, count_attr):    #membuat tabel dari list 
    nomor = 1
    for item in list:
        for i in range(count_attr):
            if i == count_attr-1:
                print(item[i])
            elif i == 0:
                print(str(nomor) + '. ' + item[i], end=' | ')
            elif i == 1:
                print(item[i], end='')
                for j in range(30-leng(item[i])):
                    print(" ", end='')
                print(' | ', end='')
            elif i == 2:
                print(item[i], end='')
                for j in range(15-leng(item[i])):
                    print(" ", end='')
                print(' | ', end='')
            elif i == 4:
                print(item[i], end='')
                for j in range(15-leng(item[i])):
                    print(" ", end='')
                print(' | ', end='')
            else:
                print(item[i], end=' | ')
        
        nomor+=1

def isAdmin(UserID, parsed_user):
    for user in parsed_user:
        if user[0] == str(UserID) and user[4] == "Admin":
            return True 
    return False

def cipher(text):   #modified bifid cipher
    base = [["m", "1", "k", "a", "c", "h"],["4", "n", "f", "e", "b", "r"],["i", "g", "w", "3", "j", "0"],["s", "t", "o", "l", "p", "5"],["2", "u", "y", "z", "x", "d"], ["8", "q", "7", "9", "v", "6"]]
    row = []
    col = []
    ciphered = ""
    for item in text:
        for i in range (6):
            for j in range (6):
                if base[i][j] == item:
                    apen(row, i)
                    apen(col, j)
    
    l = leng(row)

    reversed_col = []
    for i in range(l-1, -1, -1):
        apen(reversed_col, col[i])

    row_col = row + reversed_col

    l2 = leng(row_col)
    for i in range(0, l2-1, 2):
        tempj = row_col[i]
        tempk = row_col[i+1]
        
        ciphered += base[tempj][tempk]  

    return ciphered

def uncipher(text):
    base = [["m", "1", "k", "a", "c", "h"],["4", "n", "f", "e", "b", "r"],["i", "g", "w", "3", "j", "0"],["s", "t", "o", "l", "p", "5"],["2", "u", "y", "z", "x", "d"], ["8", "q", "7", "9", "v", "6"]]
    row = []
    col = []
    unciphered = ""
    for item in text:
        for i in range (6):
            for j in range (6):
                if base[i][j] == item:
                    apen(row, i)
                    apen(col, j)

    l = leng(text)
    row1 = []
    for i in range(l):
        if leng(row1) == l:
            break
        apen(row1, row[i])
        apen(row1, col[i])

    col1 = []
    for i in range(l-1, -1, -1):
        if leng(col1) == l:
            break 
        apen(col1, col[i])
        apen(col1, row[i])

    for i in range(l):
        unciphered += base[row1[i]][col1[i]]

    return unciphered

def awalan () :
    print("Selamat datang di Binomo! Silakan pilih fitur berikut :")
    print ("1. Login")
    print ("2. Help")
    pilihan = int(input("Masukkan pilihan Anda (1/2) : "))
    return pilihan
