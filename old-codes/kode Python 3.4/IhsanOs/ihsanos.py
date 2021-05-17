import IUCM
import PineapplePen
import ant_file_explorer
def mulaii():
	mulaik()
def mulaiui(nama):
	print("+--------------------------------------------+")
	print("|  Peringatan!!                 | - | [] | X |")
	print("+--------------------------------------------+")
	print("|Selamat Datang,", nama + "! Di IhsanOs!     |")
	print("+--------------------------------------------+")
	mulaik()
def mulaik():
	print("Berikut aplikasi yang dapat anda jalankan. cara menjalankanya : tulis nomor yang ada disebelah kiri nama aplikasi tsb.")
	print("1. IUCM(IhsanOs User Command Manager)")
	print("2. PineapplePen Pengedit Teks")
	print("3. Ant File Explorer(hanya untuk menjelajah file setelah Folder IhsanOs)")
	plihan = int(input("Saya pilih aplikasi nomor : "))
	if pilihan == 1:
		IUCM.mulai()
	elif pilihan == 2:
		PineapplePen.mulai()
	elif pilihan == 3:
		ant_file_explorer.mulai()
	else:
		print("Tidak ada pilihan yang menyerupai", pilihan)
