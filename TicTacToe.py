# Module TicTacToe
# Berisi fungsi-fungsi untuk memainkan game tic-tac-toe (B03 - Game Tic-Tac-Toe).

def printMat(M) :
# I.S. matriks M terdefinisi, berukuran 3 x 3 (matriks M dianggap sebagai "Papan TicTacToe")
# F.S. matriks M ter-print secara rapi
    print("Status Papan")
    # Menampilkan setiap elemen matriks M
    for i in range(3) :
        for j in range(3) :
            print(M[i][j], end = "")
        print()
    print()

def cekMenang(M,xo) :
# Mengecek apakah pemain dengan simbol "xo" ("xo" bernilai "X" atau "O", sesuai giliran pemain) memenangkan permainan TicTacToe atau tidak. Kemenangan terjadi jika simbol "xo" berurutan 3 kali secara diagonal, horizontal, atau vertikal.
# M adalah matriks berukuran 3 x 3 yang menjadi papan TicTacToe. Fungsi akan mengembalikan nilai True jika pemain "xo" menang, False jika tidak/belum menang (tidak menang != kalah).
    if (M[0][0] == xo and M[1][1] == xo and M[2][2] == xo) or (M[2][0] == xo and M[1][1] == xo and M[0][2] == xo) : # Cek kemenangan diagonal
        printMat(M)
        print("Pemain {} menang.".format(xo))
        return True # "xo" menang secara diagonal
    for i in range(3) :
        if (M[i][0] == xo and M[i][1] == xo and M[i][2] == xo) or (M[0][i] == xo and M[1][i] == xo and M[2][i] == xo) : # Cek kemenangan horizontal atau vertikal
            printMat(M)
            print("Pemain {} menang.".format(xo))
            return True # "xo" menang secara horizontal atau vertikal
    return False # Tidak ditemukan simbol "xo" berurutan 3 kali baik secara horizontal, vertikal, maupun diagonal

def cekKosong(M) :
# Mengecek apakah matriks M (berukuran 3 x 3, sebagai papan TicTacToe) masih memiliki bagian yang kosong (belum diisi simbol). Bagian yang kosong ditandai dengan pagar (#).
# Jika masih ada bagian yang kosong, fungsi mengembalikan nilai True. Jika matriks sudah penuh, mengembalikan nilai False.
    for i in range(3) :
        for j in range(3) :
            if M[i][j] == "#" :
                return True # Masih ada bagian kosong
    return False # Matriks M sudah penuh

def inputMat(M,xo) :
# Mengisi simbol "xo" ("xo" bernilai "X" atau "O", sesuai giliran pemain) pada matriks M (berukuran 3 x 3, sebagai papan TicTacToe) sesuai informasi lokasi (X dan Y) yang dimasukkan pengguna.
# Masukan lokasi tersebut harus divalidasi (lokasi tersebut ada dan lokasi yang ingin diisi simbol "xo" masih kosong) hingga didapat masukan yang valid.
# Mengembalikan matriks M yang sudah terisi dengan simbol "xo" pada lokasi yang valid.
    # Masukan pertama
    print("Giliran pemain {}".format(xo))
    X = int(input("X: "))
    Y = int(input("Y: "))
    # Validasi : nilai X dan Y harus valid (X, Y bernilai antara [1..3])
    while not (X >= 1 and X <= 3 and Y >= 1 and Y <= 3) :
        print("Kotak tidak valid.\n")
        print("Giliran pemain {}".format(xo))
        X = int(input("X: "))
        Y = int(input("Y: "))
    # Validasi : lokasi terpilih dengan posisi (X,Y) harus kosong (validasi ini dipisah dengan validasi sebelumnya untuk mencegah error karena nilai X atau Y di luar daerah definisi indeks matriks)
    while M[Y-1][X-1] != "#" :
        print("Kotak sudah terisi. Silakan pilih kotak lain.\n")
        print("Giliran pemain {}".format(xo))
        X = int(input("X: "))
        Y = int(input("Y: "))
    # Lokasi yang terpilih sudah valid, maka di situ akan terisi dengan simbol "xo"
    M[Y-1][X-1] = xo
    return M

# Prosedur Utama
def ticTacToe():
# Menyediakan permainan TicTacToe
# I.S. Parameter tidak ada (variabel yang dibutuhkan disediakan prosedur ini sendiri).
# F.S. Permainan TicTacToe selesai dimainkan, dengan kondisi salah satu pemain menang atau seri.
    M = [['#' for i in range(3)] for j in range(3)] # M berukuran 3 x 3, sebagai papan TicTacToe
    win = False
    count = 1 # count menunjukkan giliran pemain. Jika count bernilai ganjil, saat itu adalah giliran pemain "X", sedangkan jika count bernilai genap, saat itu adalah giliran pemain "O"
    # Panduan
    print("Selamat datang di game Tic Tac Toe! Selamat bermain.")
    print("Legenda:")
    print("# Kosong")
    print("X Pemain 1")
    print("O Pemain 2\n")
    # Permainan bergilir antara pemain "X" dan "O" selama belum ada pemenang dan masih ada bagian papan yang kosong
    while win == False and cekKosong(M) :
        printMat(M) 
        if count % 2 != 0 : # count bernilai ganjil, giliran pemain "X"
            M = inputMat(M,"X")
            print()
            if cekMenang(M,"X") :
                win = True
                break
        else : # count bernilai genap, giliran pemain "O"
            M = inputMat(M,"O")
            print()
            if cekMenang(M,"O") :
                win = True
                break
        count += 1
    # Jika belum ada pemenang tetapi papan sudah penuh, permainan seri.
    if win == False and cekKosong(M) == False :
        printMat(M)
        print("Permainan seri.")
