def faktorisasiprima(y):
    x = int(y)
    factorlist = []
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            factorlist.append(loop)
        else:
            loop += 1
    return factorlist


def fpb():
    nomor1 = input("Silahkan tulis nomor pertama ")
    nomor2 = input("Silahkan tulis nomor kedua ")
    print("Mencari FPB dari", nomor1, "dan", nomor2)
    fpb1 = faktorisasiprima(nomor1)
    fpb2 = faktorisasiprima(nomor2)
    while fpb2 == 0:
        if test2 == testt:

        testt += 1



def mulai():
    print("Pencari FPB dan KPK")
    pilih = input("Anda ingin mencari apa (FPB/KPK)? ")
    if pilih == "FPB":
        fpb()
    elif pilih == "KPK":
        kpk()
    else:
        print("Tolong tulis kembali... ada kesalahan...")
