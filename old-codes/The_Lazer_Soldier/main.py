import os
import sys
import time
import keyboard
import random

# @author NurIhsan
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
posListrik = []
posCelah = []
posDinamitAmbil = []
posDinamit = []
dinamitInt = 0
lazerInt = 100
waktuMusuhBeraksi = 0
dbg_mode = False
dbg_enabled = False
# ----- Start FPS Counter -----
FPS = int()
FPScount = int()
waktuDetikFPS = int()
wdfl = int()
# -----  End FPS Counter  -----


def pickupChecker(posDinamitAmbil, PlocY, PlocX, dinamit, posListrik):
    for a in posDinamitAmbil:
        if [PlocY, PlocX] == a:
            dinamit += 1
            posDinamitAmbil.remove(a)

    return [posDinamitAmbil, dinamit, posListrik]


def musuhAktif(pM):   # AI Musuh v1
    posYangDilihatKanan = []
    posYangDilihatKiri = []
    posYangDilihatBawah = []
    posYangDilihatAtas = []
    for a in pM:
        posYangDilihatKanan = []
        posYangDilihatKiri = []
        posYangDilihatBawah = []
        posYangDilihatAtas = []

        # AI ------------------------

        # 1 |#OO#OOOO##|
        # 2 |#OOOOOO## |
        # 3 |  #OOM#  #|
        # 4 |   #OO# # |
        # 5 |### #O   #|
        # 
        
        try:
        # Scan Kanan
            for y in range(1, 4):  # Scan dari atas ke x musuh ( atas kanan )
                # Scan dari point ke kanan (atas ke bawah)
                for x in range(1, 6):
                    if map[a[0] - (3 - y)][a[1] + x] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] - (3 - y), a[1] + x])
        
            for y in range(1, 3):  # Scan dari xy-musuh ke y-2
                for x in range(1, 6):
                    if map[a[0] + y][a[1] + x] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] + y, a[1] + x])
        except:
            pass


        try:
            # Scan Kiri
            for y in range(1, 4):
                for x in range(1, 6):
                    if map[a[0] - (3 - y)][a[1] - x] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] - (3 - y), a[1] - x])
    
            for y in range(1, 3):
                for x in range(1, 6):
                    if map[a[0] + y][a[1] - x] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] + y, a[1] - x])
        except:
            pass

        try:
            # Scan Atas
            for x in range(1, 6):
                for y in range(1, 4):
                    if map[a[0] + y][a[1] - (5 - x)] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] + y, a[1] - (5 - x)])

            for x in range(1, 6):
                for y in range(1, 3):
                    if map[a[0] + y][a[1] + x] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] + y, a[1] + x])
        except:
            pass

        try:
            # Scan Bawah
            for x in range(1, 6):
                for y in range(1, 3):
                    if map[a[0] - y][a[1] - (5 - x)] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] - y, a[1] - (5 - x)])

            for x in range(1, 6):
                for y in range(1, 3):
                    if map[a[0] - y][a[1] + x] == "#" and random.randint(0,2) == random.randint(0,2):
                        break
                    else:
                        posYangDilihatAtas.append([a[0] - y, a[1] + x])
        except:
            pass

        # for y in range(0, 25):
        #     for x in range(0, 120):
        #         if map[y][x] == "O":
        #             map[y][x] = " "

        # Checking POS
        for pos in posYangDilihatKanan:
            #map[pos[0]][pos[1]] = "O"
            if not pos in posYangDilihatAtas or not pos in posYangDilihatBawah:
                posYangDilihatKanan.remove(pos)

        for pos in posYangDilihatKiri:
            #map[pos[0]][pos[1]] = "O"
            if not pos in posYangDilihatAtas or not pos in posYangDilihatBawah:
                posYangDilihatKiri.remove(pos)

        for pos in posYangDilihatAtas:
            #map[pos[0]][pos[1]] = "O"
            if not pos in posYangDilihatKanan or not pos in posYangDilihatKiri:
                posYangDilihatAtas.remove(pos)

        for pos in posYangDilihatBawah:
            #map[pos[0]][pos[1]] = "O"
            if not pos in posYangDilihatKanan or not pos in posYangDilihatKiri:
                posYangDilihatBawah.remove(pos)

        posSemua = posYangDilihatKanan + posYangDilihatBawah + posYangDilihatKiri + posYangDilihatAtas

        # Menentukan Arah
        for p in posSemua:
            if p[0] == PlocY and p[1] == PlocX:
                if p in posYangDilihatKanan:
                    a[1] += 1
                    break
                elif p in posYangDilihatKiri:
                    a[1] -= 1
                    break
                elif p in posYangDilihatAtas:
                    a[0] += 1
                    break
                elif p in posYangDilihatBawah:
                    a[0] -= 1
                    break
        if a[0] == a[2] and a[1] == a[3]:
            if random.randint(0, 5) == 2:
                if random.randint(0, 2) == 1 and (len(posYangDilihatKanan) + len(posYangDilihatKiri)) > (len(posYangDilihatAtas) + len(posYangDilihatBawah)):
                    # Kanan Kiri
                    if random.randint(0, 2) == 1 and len(posYangDilihatKanan) >= len(posYangDilihatKanan) and a[1] != 119 and map[a[0]][a[1]+1]!= "#":
                        a[1] += 1
                    else:
                        while True:
                            try:
                                b = random.randint(1, 4)  # Atas, Bawah, Kanan, Kiri
                                if b == 1:
                                    if not a[0] == 0:
                                        if map[a[0] - 1][a[1]] != "#":
                                            a[0] -= 1
                                            break
                                        else: break

                                elif b == 2:
                                    if not a[0] == 24:
                                        if map[a[0] + 1][a[1]] != "#":
                                            a[0] += 1
                                            break

                                elif b == 3:
                                    if not a[1] == 119:
                                        if map[a[0]][a[1] + 1] != "#":
                                            a[1] += 1
                                            break
                                        else: break

                                elif b == 4:
                                    if not a[1] == 0:
                                        if map[a[0]][a[1] - 1] != "#":
                                            a[1] -= 1
                                            break
                                        else: break
                            except:
                                pass
                            else:
                                break
                else:
                    if random.randint(0, 2) == 1 and len(posYangDilihatAtas) >= len(posYangDilihatBawah) and a[0] != 0 and map[a[0]-1][a[1]]!= "#":
                        a[1] -= 1
                    else:
                        while True:
                            try:
                                b = random.randint(1, 4)  # Atas, Bawah, Kanan, Kiri
                                if b == 1:
                                    if not a[0] == 0:
                                        if map[a[0] - 1][a[1]] != "#":
                                            a[0] -= 1
                                            break
                                        else: break

                                elif b == 2:
                                    if not a[0] == 24:
                                        if map[a[0] + 1][a[1]] != "#":
                                            a[0] += 1
                                            break

                                elif b == 3:
                                    if not a[1] == 119:
                                        if map[a[0]][a[1] + 1] != "#":
                                            a[1] += 1
                                            break
                                        else: break

                                elif b == 4:
                                    if not a[1] == 0:
                                        if map[a[0]][a[1] - 1] != "#":
                                            a[1] -= 1
                                            break
                                        else: break
                            except:
                                pass
                            else:
                                break

            else:  # Scr random, akan jadi random
                while True:
                    try:
                        b = random.randint(1, 4)  # Atas, Bawah, Kanan, Kiri
                        if b == 1:
                            if not a[0] == 0:
                                if map[a[0] - 1][a[1]] != "#":
                                    a[0] -= 1
                                    break
                                else: break

                        elif b == 2:
                            if not a[0] == 24 and a[0] != 0:
                                if map[a[0] + 1][a[1]] != "#":
                                    a[0] += 1
                                    break

                        elif b == 3:
                            if a[1] != 119 and a[1] != 0:
                                if map[a[0]][a[1] + 1] != "#":
                                    a[1] += 1
                                    break
                                else: break

                        elif b == 4:
                            if not a[1] == 0:
                                if map[a[0]][a[1] - 1] != "#":
                                    a[1] -= 1
                                    break
                                else: break
                    except:
                        pass
                    else:
                        break

        if a[0] <= 25 and a[1] <= 120:
            try:
                if map[a[0]][a[1]] == "o":
                    map[a[0]][a[1]] = " "
                    pM.remove(a)
            except:
                pass

        if a[0] != 24 and a[1] != 119:
            map[a[2]][a[3]] = " "

        if not a[0] >= 25:
            map[a[0]][a[1]] = " "
            map[a[0]][a[1]] = "M"
        a[2] = a[0]
        a[3] = a[1]

    return pM


def bindPlayer(x, y, xo, yo):
    map[yo][xo] = " "
    map[y][x] = "@"
    yo = y
    xo = x
    return [xo, yo]


def cekKontrol(PlocY, PlocX, kalah, lazerInt, dinamit, posDinamit):

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

    if not lazerInt <= 0:
        if keyboard.is_pressed("right") or keyboard.is_pressed("f"):
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

    if keyboard.is_pressed("e"):
        if not dinamit == 0 and not dinamit < 0:
            if map[PlocY - 1][PlocX] == " ":
                dinamit -= 1
                map[PlocY - 1][PlocX] = "o"
                posDinamit.append([PlocY - 1, PlocX])

            elif map[PlocY - 1][PlocX - 1] == " ":
                dinamit -= 1
                map[PlocY - 1][PlocX - 1] = "o"
                posDinamit.append([PlocY - 1, PlocX - 1])

            elif map[PlocY + 1][PlocX] == " ":
                dinamit -= 1
                map[PlocY + 1][PlocX] = "o"
                posDinamit.append([PlocY + 1, PlocX])

            elif map[PlocY + 1][PlocX + 1] == " ":
                dinamit -= 1
                map[PlocY + 1][PlocX + 1] = "o"
                posDinamit.append([PlocY + 1, PlocX + 1])

            elif map[PlocY][PlocX - 1] == " ":
                dinamit -= 1
                map[PlocY][PlocX - 1] = "o"
                posDinamit.append([PlocY, PlocX - 1])

            elif map[PlocY + 1][PlocX - 1] == " ":
                dinamit -= 1
                map[PlocY][PlocX] = "o"
                posDinamit.append([PlocY, PlocX])

            elif map[PlocY][PlocX + 1] == " ":
                dinamit -= 1
                map[PlocY][PlocX + 1] = "o"
                posDinamit.append([PlocY, PlocX + 1])

            elif map[PlocY - 1][PlocX + 1] == " ":
                dinamit -= 1
                map[PlocY - 1][PlocX + 1] = "o"
                posDinamit.append([PlocY - 1, PlocX + 1])
    
    for a in posListrik:
        
        if [PlocY, PlocX, PlocY, PlocX] == a:
            lazerInt += 10
            
            if lazerInt > 100:
                lazerInt = 100
            posListrik.remove(a)

    return [PlocY, PlocX, kalah, lazerInt, dinamit, posDinamit]


def draw():
    # Nge print seluruh isi dict map
    strtes = str()
    
    for a in range(0, 24):
        
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
    
    for a in range(1, 23):
        lunit.append("#")
        
        for b in range(0, 120):
            
            try:
                if random.randint(1, kem - int(kem/2)) == random.randint(1, kem - int(kem/2)) and map[a][b-1] == "#":
                    lunit.append("#")
                
                elif random.randint(1, kem + int(kem / 4)) == random.randint(1, kem + int(kem / 4)) and map[a-1][b] == "#":
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

    for a in range(0, 120):
        ltest.append("#")
    map[23] = ltest

    for c in range(0, random.randint(20, 300)):
        if random.randint(1, kem) == random.randint(1, kem):
            a = random.randint(0, 23)
            b = random.randint(0, 119)
            map[a][b] = "M"
            posMusuh.append([a, b, a, b])  # Y, X, Yold, Xold

    if len(posMusuh) == 0:
        for c in range(0, random.randint(kem-int(kem/2), kem+5)):
            a = random.randint(0, 23)
            b = random.randint(0, 119)
            map[a][b] = "M"
            posMusuh.append([a, b, a, b])  # Y, X, Yold, Xold
    
    for ghj in range(0, random.randint(0, 100)):
        if random.randint(1, kem + 5) == random.randint(1, kem + 5):
            random1 = random.randint(0, 24)
            random2 = random.randint(0, 119)
            map[random1][random2] = "I"
            posListrik.append([random1, random2, random1, random2])  # Y, X, Yold, Xold

    # Penaruh DINAMIT AMBIL
    for a in range(5, 30): # DINAMIT itu agk langka
        if random.randint(1, kem) == random.randint(1, kem):
            random1 = random.randint(0, 24)
            random2 = random.randint(0, 119)
            map[random1][random2] = "■"
            posDinamitAmbil.append([random1, random2])
            # Display dinamit setelah di taruh : ǒ


if __name__ == "__main__":
    # DEBUG MODE CHECKER
    try:
        if sys.argv[1] == "dbg_mode":
            dbg_mode = True
            lazerInt = int(sys.argv[2])
            dinamitInt = int(sys.argv[3])
    except:
        pass
    
    # TODO : BUAT DINAMIT

    if os.name != "nt": os.system("clear")
    else: os.system("cls")

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

        # Print Bar
        print("\n                                                   The Lazer Soldier\n" +
              "                                                     --By Ihsan--         | " +
              str(FPS) + " FPS |")
        print("X: " + str(PlocX) + " ,Y: " + str(PlocY))
        print("_" * 120)

        lbj = cekKontrol(PlocY, PlocX, kalah, lazerInt, dinamitInt, posDinamit)  # Ngecek klo player nge-klik WASD dll..

        PlocY = lbj[0]  # Memasukkan var hasil return func cekKontrol ke variabel penting
        PlocX = lbj[1]
        kalah = lbj[2]
        lazerInt = lbj[3]
        dinamitInt = lbj[4]
        posDinamit = lbj[5]

        # Sistem biar bisa keluar
        # Biasanya digunakan saat game nge-bug, atau keluar kesalahan.
        if keyboard.is_pressed("q"):
            os.system("cls")
            exit()

        posMusuh = musuhAktif(posMusuh) # Buat Musuh bisa bergerak (scr random)

        a = bindPlayer(PlocX, PlocY, PlocXold, PlocYold)  # Ngeposisikan Player ke tempat yang sudah di
        PlocXold = a[0]                                   # atur pada function cekKontrol()
        PlocYold = a[1]

        draw() # Draw Map


        # Print Sisa listrik dari Int LazerInt          Dan nge-print jumlah dinamit yang dipunya
        print("\nSisa Listrik = " + str(lazerInt) + "%" + " | Dinamit = " + str(dinamitInt))

        for a in range(0, 25):                           # Ngehapus lazer biar nggak ada jejaknya ;)
            for b in range(0, 120):
                if map[a][b] == "─" or map[a][b] == "│":
                    map[a][b] = " "

        # time.sleep(0.08)  # diberi delay agar beraturan

        # Sistem buat ngecek klo player kalah

        if kalah:
            break
        
        if len(posMusuh) == 0:
            break
        
        if [PlocY, PlocX, PlocY, PlocX] in posMusuh:
            kalah = True
            problema = "Kena Musuh"
            break

        if (lazerInt == 0 and len(posListrik) == 0) or (lazerInt < 0 and len(posListrik) == 0):
            kalah = True
            problema = "Kehabisan Listrik"
            break

        # Pickup Checker
        data = pickupChecker(posDinamitAmbil, PlocY, PlocX, dinamitInt, posListrik)
        posDinamitAmbil = data[0]
        dinamitInt = data[1]

        # nge-print ulang pickup item yg di tindihin musuh atau lazer
        for a in posListrik:
            if not map[a[0]][a[1]] == "M" or map[a[0]][a[1]] == "─" or map[a[0]][a[1]] == "│":
                map[a[0]][a[1]] = "I"

        for a in posDinamitAmbil:
            if not map[a[0]][a[1]] == "M" or map[a[0]][a[1]] == "│" or map[a[0]][a[1]] == "─":
                map[a[0]][a[1]] = "■"

        for a in posDinamit:
            if not map[a[0]][a[1]] == "│" or map[a[0]][a[1]] == "─" or map[a[0]][a[1]] == "─":
                map[a[0]][a[1]] = "o"
            
        time.sleep(0.085)

        if os.name != "nt": os.system("clear")
        else: os.system("cls")

        waktuDetikFPS = int(time.time())   # Menghitung berapa Frame per Detik (FPS)
        if waktuDetikFPS == wdfl + 1:              # Udah kena delay, jadi.. bukan FPS asli..
            wdfl = waktuDetikFPS
            FPS = FPScount
            FPScount = 0
        else:
            FPScount += 1


        # Developer debug things
        if dbg_mode:
            if dbg_enabled:
                print("posMusuh: "+ str(posMusuh) + "\nposDinamit: " + str(posDinamit) + "\nposDinamitAmbil: " + str(posDinamitAmbil) + "\nposListrik: " + str(posListrik))

            if keyboard.is_pressed("x"):
                dbg_enabled = True
            elif keyboard.is_pressed("z"):
                dbg_enabled = False
    if os.name != "nt": os.system("clear")
    else: os.system("cls")

    print("")
    if kalah:
        print("                                                   Anda Kalah                " + problema + "\n")
    else:
        print('                                                  Anda Menang')
    print("_" * 120)
    print("\n Tekan Enter untuk Keluar")
    input()

    if os.name != "nt": os.system("clear")
    else: os.system("cls")
