import ihsanos1
import logging
import ihsanos
logging.basicConfig(filename="IhsanOs.log", level=logging.DEBUG)
osname = "IhsanOs"
versi = "0.1.1"
fl = open("login.txt", "r")
lojin= fl.read()
logging.debug("Ngecek Login")
#Ngecek klo dah login apa blm..
lojintestt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if not lojin in lojintestt:
	#Buat akun
	logging.info("User lg buat akun")
	print("Hai, Selamat datang di IhsanOs!. disini anda dapat menikmati sistem operasi berkode python yang ber UI text!. Selamat mencoba!")
	hshjdhuherug = input("Tekan Enter untuk melanjutkan")
	print("Sebelum anda masuk ke IhsanOs, anda harus membuat akun anda dulu...")
	nama = input("Nama User: ")
	def passs():
		password = input("Password anda: ")
		passs()
	if not password in 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
		print("Maaf.. password anda harus menggunakan nomor. setidaknya hanya satu")
		passs()
	passwul = input("Masukkan ulang password anda: ")
	if passwul == password:
		datalogin = password
		f = open("login.txt", "w")
		f.write(datalogin)
		f.close()
fl.close()
def loginlagi():
	logincuy()
def logincuy():
	print("User yang ada di IhsanOs :", nama)
	loginn = input("Pilih User : ")
	if loginn == nama:
		file = open("login.txt", "r")
		paq = file.read()
		qw = input("Masukkan Password anda : ")
		if not qw == paq:
			print("Password anda salah.")
			ihsanos1.loginnnn()
		ihsanos.mulaiui(nama, osname, versi)
	else:
		print("Tidak ada user yang bernama", loginn)
		loginlagi()
print(osname, "v", versi)
print(osname, "Login")
logincuy()
'''#Logging test....
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
'''
