'''
+-----------------------------------------------------------------------------------------------------------------------+
|	``````````		```````````	|		``````			|\		/|			+-----------+			|```````````````	|
|	|		|		|			|		|	 |			| \	   / |			|			|			|			   |	|
|	|  [-]	|		|	[[]]	|		|	 |			|  \  /	 |			|	[````]	|			|	|```````````	|
|	|		|		|	________|		|	 |			\	\/	 /			|	[	 ]	|			|	|``````````|	|
|	|	|	|		|	|				|	 |		     \		/			|	[	 ]	|			|___________   |	|
|	|	|	|		|	|				|	 |			  \	   /			|	[____]	|			|----------|   |	|
|	|___|___|		|___|				|____|			   /	\			|			|			|______________|	|
|														  /______\			+-----------+								|
+-----------------------------------------------------------------------------------------------------------------------+
'''

# Kalo banner yg diatas nggak rapi, buka pake Code editor jangan pake IDLE....
# APIXOS BY IHSAN
# COPYRIGHT KOMIXAPIX

import os
import permainan
import tpao
import manajer_aplikasi


def apixos():
    osname = "ApixOs"
    publisher = "NurIhsan AlGhifari"
    created = "Thursday, 5 - April 2018"
    NB = "Hope you enjoy it! :)        (Made In Indonesian)         "


def pemasukkanperintah():
    perintah = input(">")
    pusataucm(perintah)


def pusataucm(kode):
    kode = kode.lower()
    kode1 = kode.split()
    if kode1[0] == "tulis":
        if kode == "tulis":
            pemasukkanperintah()
        print(kode1[1])
        pemasukkanperintah()
    else:
        if kode1[0] == "apakah":
            if kode == "apakah":
                pemasukkanperintah()
            kondisi1 = kode1[1]
            pembandingankondisi = kode1[2]
            kondisi2 = kode1[3]
            if pembandingankondisi == "serupadengan":
                bul = kondisi1 == kondisi2
                if bul:
                    print("Iya")
                    pemasukkanperintah()
                else:
                    print("Nggak")
                    pemasukkanperintah()
            elif pembandingankondisi == "tidakserupadengan":
                bul = kondisi1 != kondisi2
                if bul:
                    print("Iya")
                    pemasukkanperintah()
                else:
                    print("Nggak")
                    pemasukkanperintah()
            elif pembandingankondisi == "lebihbesardari":
                bul = kondisi1 > kondisi2
                if bul:
                    print("Iya")
                    pemasukkanperintah()
                else:
                    print("Nggak")
                    pemasukkanperintah()
            elif pembandingankondisi == "lebihkecildari":
                bul = kondisi1 < kondisi2
                if bul:
                    print("Iya")
                    pemasukkanperintah()
                else:
                    print("Nggak")
                    pemasukkanperintah()
            else:
                print("Pembandingan konidsi pada statment 'apakah' tidak memiliki maksud.")
                pemasukkanperintah()
        else:
            if kode1[0] == "matematika":
                if kode == "matematika":
                    pemasukkanperintah()
                angka1 = int(kode1[1])
                angka2 = int(kode1[3])
                operatormat = kode1[2]
                if operatormat == "+":
                    print(angka1 + angka2)
                    pemasukkanperintah()
                elif operatormat == "-":
                    print(angka1 - angka2)
                    pemasukkanperintah()
                elif operatormat == "*" or operatormat == "x" or operatormat == "X":
                    print(angka1 * angka2)
                    pemasukkanperintah()
                elif operatormat == ":" or operatormat == "bagi":
                    print(angka1 / angka2)
                else:
                    print("Perintah matematika tidak menyamai operator +, -, x, :")
                    pemasukkanperintah()
            else:
                if kode1[0] == "buka":
                    if kode == "buka":
                        pemasukkanperintah()
                    if kode1[1] == "japp":
                        print("Jumlah Aplikasi :", tpao.japp)
                    elif kode1[1] == "manajer":
                        tpao.mulaimanajer()
                        pemasukkanperintah()
                    elif kode1[1] == "app1":
                        manajer_aplikasi.app1()
                    elif kode1[1] == "app2":
                        manajer_aplikasi.app2()
                    elif kode1[1] == "app3":
                        manajer_aplikasi.app3()
                    elif kode1[1] == "app4":
                        manajer_aplikasi.app4()
                    elif kode1[1] == "app5":
                        manajer_aplikasi.app5()
                    elif kode1[1] == "app6":
                        manajer_aplikasi.app6()
                    elif kode1[1] == "app7":
                        manajer_aplikasi.app7()
                    elif kode1[1] == "app8":
                        manajer_aplikasi.app8()
                    elif kode1[1] == "app9":
                        manajer_aplikasi.app9()
                    elif kode1[1] == "app10":
                        manajer_aplikasi.app10()
                    else:
                        print("PERINTAH GAGAL...")
                        pemasukkanperintah()
                elif kode == "keluar":
                    print("Apakah anda benar benar ingin keluar dari ApixOs?")
                    print("Tulis 'ya' atau 'tidak'.")
                    qwertyuiop = input("KELUAR>")
                    if qwertyuiop == "tidak":
                        pemasukkanperintah()
                    else:
                        pass
                elif kode1[0] == "bersihkan":
                    if kode == "bersihkan":
                        os.system("cls")
                        pemasukkanperintah()
                    elif kode1[1] == "tetap":
                        halamanutama()
                    else:
                        os.system("cls")
                        pemasukkanperintah()
                elif kode1[0] == "permainan":
                    if kode == "permainan":
                        pemasukkanperintah()
                    if kode1[1] == "tebak":
                        if kode1[2] == "nomor":
                            permainan.tebak_nomor()
                            pemasukkanperintah()
                        else:
                            print("Ada kesalahan saat menjalankan paket 'permainan'")
                            pemasukkanperintah()
                    elif kode1[1] == "DEBUG":
                        print("RAHASIA WEEEEEEE.......")
                        pemasukkanperintah()
                    else:
                        print("Tidak ada permainan yang bernama '", kode1[1], "' di ApixOs.")
                else:
                    print("Tidak ada paket '" + kode1[
                        0] + "' Didalam ApixOs atau anda salah tulis atau anda tidak menulis mode dengan benar.")
                    pemasukkanperintah()


def halamanutama(k="kk"):
    if k == "g":
        print("ApixOs v.1.0 Free source code!...")
        print("Anda memiliki", tpao.japp, "Aplikasi")
        print("AUCM (ApixOs User Command Manager v.1.0)")
        perintah = input(">")
        pusataucm(perintah)
    else:
        os.system('cls')
        print("ApixOs v.1.0 Free source code!...")
        print("Anda memiliki", tpao.japp, "Aplikasi")
        print("AUCM (ApixOs User Command Manager v.1.0)")
        perintah = input(">")
        pusataucm(perintah)
    print(
        "Klo lo liat ini ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRR"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def pilihuser():
    print("ApixOs 1.0")
    print("User yang ada di ApixOs")
    print("Ihsan")
    print("Guest (Tamu)")
    pilihan = input("Pilih User : ")
    if pilihan == "Ihsan":
        print("Memasuki User Ihsan....................")
        passwr = input("Tulis pasword user tersebut : ")
        os.system('cls')
        if passwr == "ihsanganteng":
            print("Selamat Datang Kembali, Ihsan Di ApixOs")
            input("Tekan enter untuk melanjutkan..")
            halamanutama()
        else:
            print("Password salah. Memasuki User Guest.............................")
            halamanutama("g")
    elif pilihan == "Guest":
        print("Memasuki User Guest....................................................................................")
        halamanutama()


pilihuser()

'''EROR!! & Koming Suun!!!!!!!!!!!!
def ulangibuatakun(ja):
	buatakun(ja)

 #ERROR
def buatakun(jumlahakun):
	print("ApixOs v.1.0")
	print("Buat Akun")
	namausr = input("Tulis nama user yang ingin ditambahkan : ")
	print("User yang akan ditabahkan :", namausr)
	passw = input("Password user tersebut? ")
	print("Menyimpan passowrd.......................................................................................................................")
	passw2 = input("Mohon ditulis ulang password tersebut? ")
	if passw2 == passw:
		filepassword = open("8724hwsb624su3274bt1287h7s32748s898j89fy732hd832h835lohhisyw8q7h8sy83629hs7h8idfhdscjfcjh6497hs88s8wej9hek3en384u8374127281377ws8hgwehfindwh8387juyx3973786739lps08876gs7hufkak.txt", "w")
		if jumlahakun >= "1":
			filepassword.write(passw2)
			jumlahakun = jumlahakun + 1
		else:
			filepassword.write("\n"+passw2)
			jumlahakun = jumlahakun + 1
		filetst = open("8724hwsb624su3274bt1287h7s32748s898j89fy732hd832h835lohhisyw8q7h8sy83629hs7h8idfhdscjfcjh6497hs88s8wej9hek3en384u8374127281377ws8hgwehfindwh8387juyx3973786739lps08876gs7hufkak.txt", "r")
		bukapass = filetest.read(jumlahakun)
		if bukapass == passw2:
			print("Pembuatan Akun Berhasil!. klik enter untuk kembali ke Halaman Utama")
			lol = input(">>>")
			halamanutama()
	else:
		print("Password anda berbeda")
		ulangibuatakun(jumlahakun)

fileakun = open("filejumlahakunapixos.txt", "r")
jumlahuser = fileakun.read()
jumlahuser = jumlahuser
if jumlahuser == "":
		jumlahuser = "0"
		buatakun(jumlahuser)
else:
	halamanutama()
'''
