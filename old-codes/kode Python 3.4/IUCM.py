#Terminal IhsanOs

import boot

def ulang():
	mat()

def perintahutama():
	h = input(nama+"@IhsanOs =>>")
	proses(h)

def mat():
	math = input(nama+"@IUCM|IhsanOs?mat =>>")
	if math == "keluar": perintahutama()
	else:
		hitung = math.split()
		angka1 = hitung[0]
		op = hitung[1]
		angka2 = hitung[2]
		if op == "+":
			print(angka1 + angka2)
		elif op == "-":
			print(angka1 - angka2)
		elif op == "*" or "x" or "X":
			print(angka1 * angka2)
		elif op == ":":
			print(angka1 / angka2)
		else:
			print("Operator matematika tidak ditemukan.")
			ulang()

def proses(printah):
	if perintah in "~":
		if perintah == "tolong~":
			print(ihsanos1.tlong())
		if perintah == "mat~":
			print("Mode mat-ematika .Tulis 'keluar' untuk keluar dari mode Mat-ematika")
			mat()

	else:
		printa = printah.split()
		prnt = printa[0]
		if prnt == "^":
			pass
		else: print("Kesalahan,  Perintah anda tidak diawali dengan '^'")
                        

def mulai():
	print("Selamat datang di IUCM (IhsanOs User Command Manager)v.0.1.2 [Copyright KomixApix 2018 - 2020 By Ihsan] di Ihsan Os versi", versi + ". Tulis 'tolong~' di command untuk bertanya perintah yang ada di TIOs. Setiap perintah harus diawali dengan '^ ' [menggunakan spasi] dan setiap perintah harus menggunakan spasi")
	print("	|		|     |		/`````		|\  /|	  /\ 	")
	print("	|		|     |		|     		| \/ |		")
	print("	|		\_____/		\_____		|    |		")
	h = input(boot.nama+"@IhsanOs =>>")
	proses(h)

#Memulai UI
mulai()
