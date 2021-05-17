def mulaiulang():
	mulai()
def mulai():
	print("PineapplePen v.1.0.1")
	print("Hanya bisa membuka file txt saja. untuk enter, gunakan '/n'")
	filepath = input("TEMPAT FILE : (ex : C:/User/Ihsan/sebuahteks.txt) ")
	if filepath in "/":
		file = open(filepath, "w")
		filebaca = open(filepath, "r")
	else:
		print("Tempat file tidak memiliki tanda '/'")
		mulaiulang()
def mulaiprogram():
	print(filebaca.read())
