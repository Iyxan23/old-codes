import random
import app1
import app2
import app3
import app4
import app5
import app6
import app7
import app8
import app9
import app10

aplikasi = 0
h = random.randint(1, 100)
k = random.randint(58, 98765)
j = random.randint(567, 45678)
l = h * k
o = l * h * j
random = o * l * h * j + 456798765


def pasang(nama):
    a = open("aplikasi.txt", "r+")
    p = open(nama, "r+")
    q = open("app1.py", "r+")
    w = open("app2.py", "r+")
    h = open("app3.py", "r+")
    l = open("app4.py", "r+")
    d = open("app5.py", "r+")
    g = open("app6.py", "r+")
    r = open("app7.py", "r+")
    n = open("app8.py", "r+")
    v = open("app9.py", "r+")
    z = open("app10.py", "r+")
    if a.read() in "satu":
        a.write("dua")
        w.write(p.read())
        aplikasi = 2
    elif a.read() in "dua":
        a.write("tiga")
        aplikasi = 3
        h.write(p.read())
    elif a.read() in "tiga":
        a.write("empat")
        l.write(p.read())
        aplikasi = 4
    elif a.read() in "empat":
        a.write("lima")
        d.write(p.read())
        aplikasi = 5
    elif a.read() in "lima":
        a.write("enam")
        aplikasi = 6
        g.write(p.read())
    elif a.read() in "enam":
        a.write("tuju")
        aplikasi = 7
        r.write(p.read())
    elif a.read() in "tuju":
        a.write("delapan")
        n.write(p.read())
        aplikasi = 8
    elif a.read() in "delapan":
        a.write("sembilan")
        v.write(p.read())
        aplikasi = 9
    elif a.read() in "sembilan":
        a.write("sepuluh")
        z.write(p.read())
        aplikasi = 10
    elif a.read() in "sepuluh":
        print(
            "Jumlah aplikasi anda telah mencapai 10. Jumlah aplikasi ini adalah jumlah aplikasi maksimum yang bisa ditampung ApixOS")
    else:
        a.write("satu")
        q.write(p.read())
        aplikasi = 1
    a.close()
    p.close()
    q.close()
    w.close()
    h.close()
    l.close()
    d.close()
    g.close()
    r.close()
    n.close()
    v.close()
    z.close()
    print("Penginstalan aplikasi bernama '" + nama + "' Berhasil!")
    dfghjhg = input("Tekan enter untuk melanjutkan")


def mulai():
    print("MANAJER APLIKASI ApixOS")
    print("Nama file tersebut HARUS BEREKSTENSI .py!!!!! dan memiliki function mulai() untuk memulai aplikasi.")
    print("Total maksimal aplikasi yang ditampung ApixOs Adalah 10 aplikasi. Untuk membatalkan menginstal aplikasi... "
          "ketik 'keluar'.")
    print("Ini dia command MA..........")
    nkk = input("Manajer_Aplikasi> ")
    ma = nkk.split()
    if ma[0] == "pasang":
        nmafile = ma[1]
        fi = open(nmafile, "r")
        print("Menginstall.......")
        print("Membaca Aplikasi........")
        print(fi.read())
        if fi.read() in "mulai()":
            print("<==================INSTALL==================>")
            print("SerialCode =", random)
            pasang(nmafile)
            fi.close()
        else:
            print(nmafile, "Tidak memiliki function 'mulai()' !!")
            fi.close()
    elif ma[0] == "keluar":
        pass


def app1():
    app1.mulai()


def app2():
    app2.mulai()


def app3():
    app3.mulai()


def app4():
    app4.mulai()


def app5():
    app5.mulai()


def app4():
    app4.mulai()


def app5():
    app5.mulai()


def app6():
    app6.mulai()


def app7():
    app7.mulai()


def app8():
    app8.mulai()


def app9():
    app9.mulai()


def app10():
    app10.mulai()
