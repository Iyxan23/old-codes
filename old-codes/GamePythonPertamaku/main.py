import os, keyboard, random, time

view = dict()
WIDTH = 120
HEIGHT = 25
LokPY = 0
LokPX = 0


def bindPlayer(vw):
    vw[LokPY][LokPX] = "@"  # Menaruh Posisi Player
    return vw


def cekKontrol(LokPY, LokPX):  # Menggunakan module keyboard
    if keyboard.is_pressed("w"):
        if not LokPY == 0 and not view[LokPY-1][LokPX] == "#":
            LokPY -= 1
            print("W")
    elif keyboard.is_pressed("s"):
        if not LokPY == 24 and not view[LokPY+1][LokPX] == "#":
            LokPY += 1
            print("s")
    elif keyboard.is_pressed("a"):
        if not LokPX == 0 and not view[LokPY][LokPX-1] == "#":  # •
            LokPX -= 1
            print("a")
    elif keyboard.is_pressed("d"):
        if not LokPX == 119 and not view[LokPY][LokPX+1] == "#":
            LokPX += 1
            print("D")
    print([LokPX, LokPY])
    return [LokPX, LokPY]  # Mengenmbalikan data yg sudah diubah


def draw():
    s = str()
    for a in range(0, HEIGHT):
        for b in range(0, WIDTH):
            s += view[a][b]
        print(s)
        s = ""


def initialize():
    # untuk membuat world yg random..
    lunit = list()
    for a in range(0, HEIGHT):
        for b in range(0, WIDTH):
            if random.randint(0, 15) == random.randint(0, 15):  # Random untuk membuat tembok
                lunit.append("#")
            else:
                lunit.append(" ")
        # Selesai loop For yang b.
        view[a] = lunit
        lunit = []
    # View nya udah jadi..


if __name__ == "__main__":
    os.system("title Game Cari Uang")  # MISALNYA xD
    initialize()
    while True:
        data = cekKontrol(LokPX, LokPX)  # Data yang berbentuk list
        print(data)
        LokPX = data[0]
        LokPY = data[1]
        print([LokPY, LokPX])
        view = bindPlayer(view)

        draw()
        time.sleep(0.1)  # Dikasih delay biar tdk gila
        os.system("cls")
