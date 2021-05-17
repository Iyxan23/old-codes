import os, time, keyboard, json


def MainMenu(data):
    print("\n                                                   The Youtuber Game")
    print("                                                   -=Made By Ihsan=-\n\n")
    print("                   -Pilih Permainan yang sudah disave-\n")
    b = 0
    for a in data["levels"]:
        b += 1
        print("       " + str(b) + ". " + a["namaLevel"])

    while True:
        try:
            pilih = int(input("Masukkan Nomor : "))
        except ValueError:
            pass
        else:
            break
    if not pilih > b:
        return pilih - 1
    else:
        quit()


if __name__ == "__main__":
    os.system('title The Youtuber - Made By Ihsan')
    os.system('mode con: cols=120 lines=35')
    with open("data.json", "r") as f:
        data = json.load(f)
        f.close()
    print(data)
    nom = MainMenu(data)
    print("Klik Enter Untuk memuat level : " + data["levels"][nom]["namaLevel"])
    input()
    os.system("cls")

input()
