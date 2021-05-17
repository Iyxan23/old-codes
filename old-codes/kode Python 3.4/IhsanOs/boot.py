import ihsanos1
import logging
import ihsanos
def loginlagi(ma):
	logincuy(ma)
def logincuy(nma):
	print("User yang ada di IhsanOs :", nma)
	loginn = input("Pilih User : ")
	if loginn == nma:
		file = open("login.txt", "r")
		paq = file.read()
		qw = input("Masukkan Password anda : ")
		if not qw == paq:
			print("Password anda salah.")
			ihsanos1.loginnnn()
		ihsanos.mulaiui(nma)
	else:
		print("Tidak ada user yang bernama", loginn)
		loginlagi(nma)
def passs():
	pww = input("Password anda: ")
	return pww
def cekpass(password):
        lojinnnnnnnnnnnnnnnn = "a"
        if not password in lojinnnnnnnnnnnnnnnn:
                print("Maaf.. password anda harus mengandung huruf 'a'. contoh : q766r48yu27883rf0a") #WHAT????????
                passs()
        passwul = input("Masukkan ulang password anda: ")
        if passwul == password:
                datalogin = password
                f = open("login.txt", "w")
                f.write(datalogin)
                f.close()
logging.basicConfig(filename="IhsanOs.log", level=logging.DEBUG)
osname = "IhsanOs"
versi = "0.1.1"
fl = open("login.txt", "r")
lojin = fl.read()
logging.debug("Ngecek Login")
#Ngecek klo dah login apa blm..
lojintestt = "a"
if not lojin in lojintestt:
	#Buat akun
	logging.info("User lg buat akun")
	print("Hai, Selamat datang di IhsanOs!. disini anda dapat menikmati sistem operasi berkode python yang ber UI text!. Selamat mencoba!")
	hshjdhuherug = input("Tekan Enter untuk melanjutkan")
	print("Sebelum anda masuk ke IhsanOs, anda harus membuat akun anda dulu...")
	nama = input("Nama User: ")
	passd = passs()
	cekpass(passd)
else:
        print(osname, "v", versi)
        print(osname, "Login")
        logincuy(nama)
'''#Logging test....
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
'''
