import random
def mulaitb(jab):
    mulait(jab)
def mulait(jaw):
    print("Aku memikirkan sebuah nomor, apakah kamu bisa menebaknya?")
    jaban = int(input("Jawabanku adalah : "))
    if jaban == jaw:
        print("BENAR!!!!, Anda bisa menebaknya!!")
    elif jaban > jaw:
        print("Jawaban anda lebih besar dari jawaban yang asilnya!!")
        mulaitb(jaw)
    elif jaban < jaw:
        print("Jawaban anda lebih kecil dari jawaban yang aslinya!!")
        mulaitb(jaw)
    else:
        print("SYSTEM ERROR")
def mulaitebaknomor():
    print("Silahkan pilih level..")
    level = int(input("Aku pilih level : "))
    if level == 1:
        jb = random.randint(1, 10)
        print("Anda memilih level 1")
        mulait(jb)
    elif level == 2:
        jb = random.randint(1, 50)
        print("Anda memilih level 2")
        mulait(jb)
    elif level == 3:
        jb = random.randint(1, 100)
        print("Anda memilih level 3")
        mulait(jb)
    else:
        pass
def tebak_nomor():
    print("Selamat datang di tebak Nomornya!, apakah anda yakin ingin memainkan game ini?")
    print("Tulis ya atau Tidak.")
    ya = input("(ya/tidak)==>>")
    if ya == "ya":
        print("Okey!")
        mulaitebaknomor()
    elif ya == "tidak":
        print("Ok, baiklah")
    else:
        print("Statment GAGAL...")