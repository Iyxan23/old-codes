# W = 100
# H = 55
# @author NurIhsan

import keyboard
import os
import time
import random

LPloc = [1, 1, 1, 1, {}, 0, "", False, {}]
filerekor = open("rekor.txt", "w")
problema = ""
hablah = int()
waktu = str()
dtkwaktu = int()
mntwaktu = int()
# ----- Start FPS Counter -----
FPS = int()
FPScount = int()
waktuDetikFPS = int()
wdfl = int()
# -----  End FPS Counter  -----
nmor = int()
posBom = list()
lenpb = int()
kalah = False
player = str()
posDuit = list()
Duit = int()
map = dict()
# -----------
PlocXold = 0
PlocYold = 0
# ------------
PlocY = 0
PlocX = 0


def drawMap(dataLoc, dataMap):
    dataHasil = str()

    for a in range(0, 25):
        for b in range(0, 120):
            dataHasil += map[a][b]
        print(dataHasil)
        dataHasil = ""


def bindPlayer(PlocX, PlocY, map, locYold, locXold, d, pl, kal, pb):
    map[PlocY][PlocX] = pl
    try:
        if map[PlocY+1][PlocX] == pl and map[PlocY-1][PlocX] == pl and map[PlocY][PlocX+1] == pl and map[PlocY][PlocX-1] == pl:
            kal = True
    except KeyError:
        pass
    d += 10

    return [PlocX, PlocY, locYold, locXold, map, d, pl, kal, pb]


def checkControl(PlocY, PlocX, locYold, locXold, m, pd, p, kl, pb, nm):
    duit = 0
    if keyboard.is_pressed("w"):
        if not PlocY == 0 and not m[PlocY-1][PlocX] == "#" and not m[PlocY-1][PlocX] == "▄" and not m[PlocY-1][PlocX] == "█":
            PlocY -= 1
            p = "█"
    if keyboard.is_pressed("s"):
        if not PlocY == 24 and not m[PlocY+1][PlocX] == "#" and not m[PlocY+1][PlocX] == "▄" and not m[PlocY+1][PlocX] == "█":
            PlocY += 1
            p = "█"
    if keyboard.is_pressed("a"):
        if not PlocX == 0 and not m[PlocY][PlocX-1] == "#" and not m[PlocY][PlocX-1] == "█" and not m[PlocY][PlocX-1] == "▄":  # •
            PlocX -= 1
            p = "▄"
    if keyboard.is_pressed("d"):
        if not PlocX == 120 and not m[PlocY][PlocX+1] == "#" and not m[PlocY][PlocX+1] == "█" and not m[PlocY][PlocX+1] == "▄":
            PlocX += 1
            p = "▄"
    if [PlocY, PlocX] in pd:
        pd.remove([PlocY, PlocX])
        duit += 5000
    else:
        duit = duit
    if [PlocY, PlocX] in pb:
        pb.remove([PlocY, PlocX])
    if keyboard.is_pressed("q"):
        exit()
    return [PlocX, PlocY, locYold, locXold, m, duit, p, kl, pb]


def initialization(kem, pb):
    c = int()
    pd = list()
    lunit = list()

    # initialization
    for a in range(0, 25):
        for b in range(0, 120):
            if random.randint(1, kem) == random.randint(1, kem):
                if random.randint(0, 55) == random.randint(0, 55):
                    lunit.append("¤")
                    pb.append([a, b])
                elif random.randint(1, kem + 5) == random.randint(1, kem + 5):
                    c += 1
                    lunit.append("$")
                    pd.append([a, b])
                else:
                    lunit.append("#")
            else:
                lunit.append(" ")
        map[a] = lunit
        lunit = []

    if len(pd) == 0:
        for a in range(0, random.randint(1, 20)):
            b = random.randint(0, 24)
            c = random.randint(0, 120)
            map[b][c] = "$"
            pd.append([b, c])

    map[0][0] = " "
    map[1][0] = " "
    map[0][1] = " "
    map[1][1] = " "

    return [pd, pb, len(pb)]


if __name__ == "__main__":
    os.system("cls")
    print("\n\n\n")
    print(" [i] Kemungkinan temboknya Random atau tidak? [i]")
    kemungkinan = input("Random atau tidak? [y/t] ")
    if kemungkinan == "y":
        lbj = initialization(random.randint(5, 50), posBom)
        posDuit = lbj[0]
        posBom = lbj[1]
        lenpb = lbj[2]
        lbj.clear()
    elif kemungkinan == "t":
        print(" [i] 1 = 100%, maks. 50 (Masukkan Nomor) [i]")
        try:
            kemungkinan = int(input("Masukkan kemungkinan Tembok = "))
        except ValueError:
            exit()
        else:
            lbj = initialization(kemungkinan, posBom)
            posDuit = lbj[0]
            posBom = lbj[1]
            lenpb = lbj[2]
            lbj.clear()
    waktuDetikFPS = int(time.perf_counter())
    wdfl = int(time.perf_counter())
    for a in range(1, len(posDuit) + 1):
        dtkwaktu += 10
        if dtkwaktu == 60:
            dtkwaktu = 0
            mntwaktu += 1

    while True:
        kp = " "
        if hablah == 2:
            hablah = 0
            kp = "•"
        LPloc = checkControl(PlocY, PlocX, PlocYold, PlocXold, map, posDuit, player, kalah, posBom, nmor) # Ngecek klo player nge-release key.. trs diatur posisi player

        PlocX = LPloc[0]
        PlocY = LPloc[1]
        PlocYold = LPloc[2]
        PLocXold = LPloc[3]
        map = LPloc[4]
        Duit += LPloc[5]
        player = LPloc[6]
        kalah = LPloc[7]
        posBom = LPloc[8]

        if not len(posBom) == lenpb:
            kalah = True
            problema = "Kena Bom.."
            break

        LPloc = bindPlayer(LPloc[0], LPloc[1], LPloc[4], LPloc[2], LPloc[3], LPloc[5], LPloc[6], kalah, posBom)    # Dialokasikan lokasi player di variabel map

        map = LPloc[4]    # Setelah di bind.. map berubah dan dimasukkan ke LPloc.. stelah itu map yg ada di LPloc dipindah ke variabel map itu sendiri
        LPloc.remove(LPloc[4])

        PlocX = LPloc[0]
        PlocY = LPloc[1]
        PlocYold = LPloc[2]
        PLocXold = LPloc[3]
        LPloc[4] -= 10
        Duit += LPloc[4]
        player = LPloc[5]
        kalah = LPloc[6]
        posBom = LPloc[7]

        print("\n"+kp + "                                                      Snake Money\n" +
              "                                                     --By Ihsan--         | " +
              str(FPS) + " FPS |")
        print("                                                                          | Waktu Tersisa = " +
              waktu + " |")
        print("_" * 120)

        drawMap(LPloc, map)
        print("_" * 120)
        print("Duit = Rp " + str(Duit) + "\t\t\t\t\t\t\t Ada " + str(len(posDuit)) + " duit tersisa")
        print("Kontrol = WASD Untuk Bergerak, q untuk keluar")
        print("Ikon = \"#\" = Tembok , \"$\" = Uang 10.000, \"o\" = Bom , \"•\" = Berkedip saat tidak lag")
        if len(posDuit) == 0:
            kalah = False
            break
        if kalah:
            break
        time.sleep(0.09)
        os.system("cls")

        waktuDetikFPS = int(time.perf_counter())
        if waktuDetikFPS == wdfl + 1:

            if dtkwaktu == 0:
                mntwaktu -= 1
                dtkwaktu = 59
            else:
                dtkwaktu -= 1
            if dtkwaktu == 0 and mntwaktu == 0:
                kalah = True
                problema = "Waktu habis.."
                break

            wdfl = waktuDetikFPS
            FPS = FPScount
            FPScount = 0
        else:
            FPScount += 1

        # Waktu
        kk = str()
        if len(str(dtkwaktu)) == 1:
            kk = "0" + str(dtkwaktu)
        else:
            kk = str(dtkwaktu)
        waktu = str(mntwaktu) + ":" + kk

        hablah += 1
    # while rampung!
    file = open("rekor.txt", "r")
    os.system("cls")
    print("")
    if not kalah:
        print("                                                      Anda Menang!")
    else:
        print("                                                      Anda Kalah..                          " + problema)
    print("_" * 120)
    print("\nHasil Uang anda = Rp" + str(Duit))
    if not kalah:
        print("\nRekor = " + file.readline(len(file.readlines())))
    input("\nTekan Enter Untuk Keluar ")
    os.system("cls")
