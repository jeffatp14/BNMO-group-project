# Module Kerang Ajaib
# Berisi fungsi/prosedur untuk bermain Kerang Ajaib (B02 - Magic Conch Shell).

import time

def lcg(a,b,x0,m) :
# Menghasilkan bilangan acak semu yang merupakan hasil dari (a * x0 + b) mod m (linear congruential generator).
    return (a * x0 + b) % m

# Prosedur Utama
def kerangAjaib():
# Kerang yang mampu menjawab pertanyaan yang diberikan pengguna secara acak.
# I.S. Parameter tidak ada (variabel yang dibutuhkan disediakan prosedur ini sendiri).
# F.S. Pertanyaan yang diberikan pengguna dijawab oleh kerang ajaib secara random.
    print("Selamat datang di kerang ajaib!")
    question = input("Apa pertanyaanmu? ") # Hanya masukan, tidak memengaruhi jawaban kerang
    # Mengambil nilai-nilai untuk menjadi parameter fungsi lcg dari waktu lokal pengguna
    nowTime = time.strftime("%H:%M:%S") # Fungsi time.strftime mengubah tuple waktu (defaultnya adalah waktu lokal) menjadi string sesuai format yang diberikan di argumen
    hour = int(nowTime[0] + nowTime[1])
    minute = int(nowTime[3] + nowTime[4])
    second = int(nowTime[6] + nowTime[7]) + 1 # Ditambah 1 untuk mencegah munculnya pembagian oleh 0 atau "mod 0"
    timeInSeconds = int(time.time()) # Fungsi time.time mengembalikan waktu dalam detik sejak “epoch”
    # Pemberian jawaban oleh kerang, ada 13 jawaban
    answer = lcg(hour,minute,timeInSeconds,second) % 13
    if answer == 0 :
        print("Ya.")
    elif answer == 1 :
        print("Tidak.")
    elif answer == 2 :
        print("Bisa jadi.")
    elif answer == 3 :
        print("Mungkin.")
    elif answer == 4 :
        print("Tentunya.")
    elif answer == 5 :
        print("Ga mungkin lah. Jangan ngada-ngada.")
    elif answer == 6 :
        print("Kerang gatau :(.")
    elif answer == 7 :
        print("Sayang banget tapi Kerang dilarang ngasihtau kamu.")
    elif answer == 8 :
        print("Rahasia XD.")
    elif answer == 9 :
        print("Kerang lagi gak mood jawab :/")
    elif answer == 10 :
        print("Menurut kamu?! >:(")
    elif answer == 11 :
        print("Pikir sendiri, masa gitu aja nanya Kerang :<")
    else : # answer == 12
        print("Hmm. Kerang no comment deh...")
