############################
# Copyright IhsanGames     #
# Author        : Ihsan    #
# Created when  : Unknown  #
# Created using : Python 3 #
############################

import os
import time
import keyboard
import random

# Menginiliasasi (XD) Variabel yg dibutuhkan

map = dict()
problema = str()
PlocX = int()
PlocY = int()
PlocYold = int()
PlocXold = int()
kalah = bool()
tujuanPosTembak = [0, 0]
posMusuh = []
lazerInt = 100
# ----- Start FPS Counter -----
FPS = int()
FPScount = int()
waktuDetikFPS = int()
wdfl = int()
# -----  End FPS Counter  -----


def musuhAktif(pM):   # Musuh pergerakannya dibuat Random.., Malez buat AI
    for a in pM:
        while True:
            b = random.randint(1, 4)  # Atas, Bawah, Kanan, Kiri
            if b == 1:
                if a[0] != 0:
                    if map[a[0] - 1][a[1]] != "#":
                        a[0] -= 1
                        break
                    else: break
            elif b == 2:
                if a[0] != 24:
                    if map[a[0] + 1][a[1]] != "#":
                        a[0] += 1
                        break
            elif b == 3:
                if a[1] != 119:
                    if map[a[0]][a[1] + 1] != "#":
                        a[1] += 1
                        break
                    else: break
            elif b == 4:
                if a[1] != 0:
                    if map[a[0]][a[1] - 1] != "#":
                        a[1] -= 1
                        break
                    else: break

        map[a[2]][a[3]] = " "
        map[a[0]][a[1]] = "M"
        a[2] = a[0]
        a[3] = a[1]


def bindPlayer(x, y, xo, yo):
    map[yo][xo] = " "
    map[y][x] = "@"
    yo = y
    xo = x
    return [xo, yo]


def cekKontrol(PlocY, PlocX, kalah, lazerInt):

    # Pergerakan Player

    if keyboard.is_pressed("w"):
        if not PlocY == 0:
            if map[PlocY-1][PlocX] != "#":
                PlocY -= 1
            elif map[PlocY-1][PlocX] == "M":
                kalah = True
    elif keyboard.is_pressed("s"):
        if not PlocY == 24:
            if map[PlocY+1][PlocX] != "#":
                PlocY += 1
            elif map[PlocY+1][PlocX] == "M":
                kalah = True
    elif keyboard.is_pressed("d"):
        if not PlocX == 119:
            if map[PlocY][PlocX+1] != "#":
                PlocX += 1
            elif map[PlocY][PlocX+1] == "M":
                kalah = True
    elif keyboard.is_pressed("a"):
        if not PlocX == 0:
            if map[PlocY][PlocX-1] != "#":
                PlocX -= 1
            elif map[PlocY][PlocX-1] == "M":
                kalah = True

    # Tembakan

    if keyboard.is_pressed("right"):
        for a in range(PlocX + 1, 119):
            if a == 119:
                tujuanPosTembak[0] = 119
                tujuanPosTembak[1] = PlocY
                break
            if map[PlocY][a] == "#":
                tujuanPosTembak[0] = a
                tujuanPosTembak[1] = PlocY
                break
            elif map[PlocY][a] == "M":
                posMusuh.remove([PlocY, a, PlocY, a])
                map[PlocY][a] = " "
                tujuanPosTembak[0] = a - 1
                tujuanPosTembak[1] = PlocY
                break
        for a in range(PlocX + 1, tujuanPosTembak[0]):
            map[PlocY][a] = "─"
        lazerInt -= 1

    elif keyboard.is_pressed("left"):
        c = list()
        for b in range(0, PlocX):
            c.append(b)
        c = list(reversed(c))
        for a in c:
            if map[PlocY][a] == "#":
                tujuanPosTembak[0] = a + 1
                tujuanPosTembak[1] = PlocY
                break
            elif map[PlocY][a] == "M":
                posMusuh.remove([PlocY, a, PlocY, a])
                map[PlocY][a] = " "
                tujuanPosTembak[0] = a + 1
                tujuanPosTembak[1] = PlocY
                break
        for a in range(tujuanPosTembak[0], PlocX):
            map[PlocY][a] = "─"
        lazerInt -= 1

    elif keyboard.is_pressed("up"):
        c = list()
        for b in range(0, PlocY):
            c.append(b)
        c = list(reversed(c))
        for a in c:
            if map[a][PlocX] == "#":
                tujuanPosTembak[0] = PlocX
                tujuanPosTembak[1] = a + 1
                break
            elif map[a][PlocX] == "M":
                posMusuh.remove([a, PlocX, a, PlocX])
                map[a][PlocX] = " "
                tujuanPosTembak[0] = PlocX
                tujuanPosTembak[1] = a + 1
                break
        for a in range(tujuanPosTembak[1], PlocY):
            map[a][PlocX] = "│"
        lazerInt -= 1

    elif keyboard.is_pressed("down"):
        for a in range(PlocY + 1, 119):
            if a == 25:
                tujuanPosTembak[0] = PlocX
                tujuanPosTembak[1] = 25
                break
            if map[a][PlocX] == "#":
                tujuanPosTembak[0] = PlocX
                tujuanPosTembak[1] = a
                break
            elif map[a][PlocX] == "M":
                posMusuh.remove([a, PlocX, a, PlocX])
                map[a][PlocX] = " "
                tujuanPosTembak[0] = PlocX
                tujuanPosTembak[1] = a - 1
                break
        for a in range(PlocY + 1, tujuanPosTembak[1]):
            map[a][PlocX] = "│"
        lazerInt -= 1

    return [PlocY, PlocX, kalah, lazerInt]


def draw():
    # Nge print seluruh isi dict map
    strtes = str()
    for a in range(0, 25):
        for b in range(0, 120):
            strtes += map[a][b]
        print(strtes)
        strtes = ""


def initialization(kem):
    # Nge buat Peta dengan parameter nilai kemungkinan yang sudah dimasukkan pada awal dibuka
    ltest = list()
    for a in range(0, 120):
        ltest.append("#")
    map[0] = ltest
    ltest = list()
    ltest.append("#")
    for a in range(0, 120):
        if random.randint(0, kem) == random.randint(0, kem):
            ltest.append("#")
        else:
            ltest.append(" ")
    map[1] = ltest
    lunit = []
    for a in range(1, 25):
        lunit.append("#")
        for b in range(0, 120):
            try:
                if random.randint(1, kem - int(kem / 2)) == random.randint(1, kem - int(kem / 2)) and map[a][b-1] == "#":
                    lunit.append("#")
                elif random.randint(1, kem + int(kem / 3)) == random.randint(1, kem + int(kem / 3)) and map[a-1][b] == "#":
                    lunit.append("#")
                else:
                    lunit.append(" ")
            except KeyError:
                if random.randint(1, kem - int(kem / 2)) != random.randint(1, kem - int(kem / 2)):
                    lunit.append("#")
                else:
                    lunit.append(" ")
            except IndexError:
                lunit.append(" ")
        lunit.append("#")
        map[a] = lunit
        lunit = []
    for c in range(0, random.randint(2, 5)):
        a = random.randint(0, 24)
        b = random.randint(0, 119)
        map[a][b] = "M"
        posMusuh.append([a, b, a, b])  # Y, X, Yold, Xold

    map[0][0] = " "
    map[1][0] = " "
    map[1][1] = " "
    map[0][1] = " "


if __name__ == "__main__":
    os.system("cls")
    print("\n\n\n")
    print(" [i] Kemungkinan temboknya Random atau tidak? [i]")
    kemungkinan = input("Random atau tidak? [y/t] ")
    if kemungkinan == "y":
        initialization(random.randint(5, 50))
    elif kemungkinan == "t":
        print(" [i] min. 2, maks. 70 (Masukkan Nomor) [i]")
        try:
            kemungkinan = int(input("Masukkan kemungkinan Tembok = "))
        except ValueError:
            exit()
        else:
            initialization(kemungkinan)
    waktuDetikFPS = int(time.perf_counter())
    while True:

        print("\n                                                   The Lazer Soldier\n" +
              "                                                     --By Ihsan--         | " +
              str(FPS) + " FPS |")
        print("X: " + str(PlocX) + " ,Y: " + str(PlocY))
        print("_" * 120)

        lbj = cekKontrol(PlocY, PlocX, kalah, lazerInt)  # Ngecek klo player nge-klik WASD dll..

        PlocY = lbj[0]
        PlocX = lbj[1]
        kalah = lbj[2]
        lazerInt = lbj[3]

        if keyboard.is_pressed("q"):
            os.system("cls")
            exit()

        musuhAktif(posMusuh) # Buat Musuh bisa bergerak (scr random)

        a = bindPlayer(PlocX, PlocY, PlocXold, PlocYold)  # Ngeposisikan Player ke tempat yang sudah di
        PlocXold = a[0]                                   # atur pada function cekKontrol()
        PlocYold = a[1]

        draw() # Draw Map

        print("\nSisa Listrik = " + str(lazerInt) + "%")

        for a in range(0, 25):                           # Ngehapus lazer biar nggak ada jejaknya ;)
            for b in range(0, 120):
                if map[a][b] == "─" or map[a][b] == "│":
                    map[a][b] = " "

        time.sleep(0.08)  # diberi delay agar beraturan

        # Sistem buat ngecek klo player kalah

        if kalah:
            break
        if len(posMusuh) == 0:
            break
        if [PlocY, PlocX, PlocY, PlocX] in posMusuh:
            kalah = True
            problema = "Kena Musuh"
            break
        if lazerInt == 0:
            kalah = True
            problema = "Kehabisan Listrik"
            break

        os.system("cls")

        waktuDetikFPS = int(time.perf_counter())   # Menghitung berapa Frame per Detik (FPS)
        if waktuDetikFPS == wdfl + 1:              # Udah kena delay, jadi.. bukan FPS asli..
            wdfl = waktuDetikFPS
            FPS = FPScount
            FPScount = 0
        else:
            FPScount += 1

    os.system("cls")
    print("")
    if kalah:
        print("                                                   Anda Kalah                " + problema + "\n")
    else:
        print('                                                  Anda Menang')
    print("_" * 120)
    print("\n Tekan Enter untuk Keluar")
    input()
    os.system("cls")
