import random

jb = random.randint(1, 10)
tries = 1

coba = 5

def mulaaigemku(cba):
    cba = cba - 1
    print("Anda memiliki", coba, "Kesempatan Lagi....")
    if cba == 0:
        print("maaf, kesempatan anda habis... jawaban yang sebenarnya adalah", jb)
    mulai_gem(cba)

def mulai_gem(cba):
    print("Aku memikirkan salah satu nomor dari 1 sampai 10... bisakah kamu menebaknya?")
    jawaban = int(input("Jawabanku adalah : "))
    if jawaban == jb:
        print("Benar!!")
    else:
        print("maaf, jawaban anda salah...")
        mulaaigemku(cba)

print("Hai, Selamat datang di gem Pikirkan nomornya! (by Ihsan)")
nama = str(input("Siapa namamu? "))
print("Halo,", nama + "!")
yno = str(input("apakah kamu(" + nama +") Ingin Memainkan gem ini?[Y/T]"))
if yno == "Y":
    mulai_gem(5)
elif yno == "y":
    mulai_gem(5)
elif yno == "T":
    print("ohh.. yaudah kalo gitu")
elif yno == "t":
    print("ohh.. yaudah kalo gitu")
else:
    print("error")
