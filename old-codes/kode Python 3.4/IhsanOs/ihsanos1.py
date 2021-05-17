def ulanglogin():
	loginnnn()
	
def loginnnn():
	file = open("login.txt", "r")
	paq = file.read()
	qw = input("Masukkan Password anda : ")
	if not qw == paq:
		print(" Maaf,Password anda salah.")
		ulanglogin()

