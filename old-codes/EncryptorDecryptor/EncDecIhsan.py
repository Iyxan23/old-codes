import sys

# Encryptor dan Decryptor..... 2 in 1 XD

lis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
    , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '#', '$', '%', '&', "'", '('
    , ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}'
    , '~', '"']

error = bool()
c = int()


def main():
    print("\n===============================================\n")
    ls = sys.argv
    if "-m" in sys.argv:
        print(" [!] Pastikan seluruh huruf/ angka yang anda masukkan tercantum dalam kode manual ini.. [!] ")
        l = input("\n Manual encrypt/decrypt code = ")
        lis = []
        for a in l:
            lis.append(a)
        lis.append(" ")

    try:
        file = open(ls[1], "r")
        print(" Nama File = " + ls[1])

    except IndexError:
        k = ed(input("\n Masukkan Kalimat untuk di Encrypt / Decrypt = "))
        print("\n Hasil = " + k)

    except FileNotFoundError:
        print(" Error File Tidak Ditemukan = " + ls[1])

    else:
        isi = file.read()
        print(" Isi File = " + isi)
        k = ed(isi)
        print(" Hasil = " + k)
        klarifikasi = input(" Save ke File? [y/t] ")
        if klarifikasi == "y":
            fi = open(ls[1], "w")
            fi.write(k)
            fi.close()
        elif klarifikasi == "t":
            pass
        else:
            pass
        file.close()
    finally:
        print("\n===============================================\n")
        exit()


def ed(text):
    hasil = str()
    c = int()
    h = int()

    for a in text:
        for b in lis:
            c += 1
            if a == b:
                hasil += lis[-c]
                break
            h += 1
        c = 0
    return hasil


if __name__ == "__main__":
    main()
