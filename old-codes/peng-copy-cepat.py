import os

def main():
    os.system("title Pengcopy cepat by Ihsan!")
    print("Peng-Copy Cepat by Ihsan!")
    path = input("Tulis path(file) : ")
    f = open(path, "r")
    path2 = input("Tulis path tempat copy : ")
    nama = input("Tulis nama file yang setelah dicopy : ")
    f2 = open(path2+nama, "w")
    print("Copying....")
    print("")
    print(f.read())
    a = f.read()
    f2.write(a)
    print("")
    print("Completed!")
    f.close()
    f2.close()

if __name__ == "__main__":
    main()
    os.system("pause")