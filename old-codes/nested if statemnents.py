#Nested if statments
#By Ihsan
#Kelas 5D, 24

print("Hai... siapa namamu?")
nama = input("Namaku adalah : ")
print("ohhh.. selamat datang ",nama )
kabar = input("Apa kabarmu? ")
if kabar == "baik":
    print("aku juga baik baik saja kok")
    kelas = int(input("btw kamu kelas brpa ya? "))
    if kelas < 5:
        print("Ohh kamu adik kelas ku :)")
    elif kelas > 5:
        namapangg = nama
        print("Halo mas", namapangg)
    else:
        print("kelas kamu sama kayak aku lhoo...")
elif kabar == "tidak":
    print("Ohh maaf ya mengganggu kamu")
else:
    print("maaf kabar anda tidak diketahui")
