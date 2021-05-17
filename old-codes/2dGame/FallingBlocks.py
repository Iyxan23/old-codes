import keyboard
import os
import time

def bindPlayer()

def cekKontrol(X, Y, map):
    
    # Pergerakan Player
    if keyboard.is_pressed("a"):  # Kekiri
        if X != 0 and map[Y][X - 1] != "#":
            X -= 1
    
    elif keyboard.is_pressed("d"):
        if X != 119 and map[Y][X + 1] != "#":
            X += 1

    return [X, Y]

def main():
    cls()
    pilih = [">", " ", " "]
    pilihan = 0
    diff = int()
    time.sleep(1)
    while True:
        header("Select Difficulties")

        print(" " + pilih[0] + " Eazy")
        print(" " + pilih[1] + " Medium")
        print(" " + pilih[2] + " Hard")

        if keyboard.is_pressed("up"):
            if pilihan == 0:
                pilihan = 2
            else:
                pilihan -= 1

        elif keyboard.is_pressed("down"):
            if pilihan == 2:
                pilihan = 0
            else:
                pilihan += 1

        elif keyboard.is_pressed("enter"):
            diff = pilihan + 1
            cls()
            time.sleep(1)
            break
        
        pilih[0] = " "
        pilih[1] = " "
        pilih[2] = " "

        pilih[pilihan] = ">"

        time.sleep(0.1)
        cls()

    # GAME!!
    map = dict()
    PlocX = 0
    PlocY = 0

    # Initialize

    lunit = []
    for y in range(0, 29):
        for x in range(0, 119):
            lunit.append(" ")
        map[y] = lunit
        lunit = []

    for a in range(0, 119):
        lunit.append("#")
    map[29] = lunit
    lunit = []    

    while True:
        header()

        data = cekKontrol(PlocX, PlocY, map)
        PlocX = data[0]
        PlocY = data[1]

        map = bindPlayer()

        #spawnblocks()
        
        #gravity()

        #draw()

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def header(teks=""):
    print("")
    print("Falling Blocks".center(120))
    print("By Ihsan".center(120))
    print("\t" + teks)
    print("_"*120)
    print("")


if __name__ == "__main__":
    # Main Menu
    pilih = 1
    pilihan = [">", " ", " "]
    upnum = 0
    while True:
        header("Main Menu")
        
        print(" " + pilihan[0] + " Play The Game")
        print(" " + pilihan[1] + " Scoreboards")
        print(" " + pilihan[2] + " Exit")

        if keyboard.is_pressed("up"):
            if pilih == 1:
                pilih = 3
            else:
                pilih -= 1
   
        elif keyboard.is_pressed("down"):
            if pilih == 3:
                pilih = 1
            else:
                pilih += 1

        elif keyboard.is_pressed("enter"):
            if pilih == 1:
                main()
                time.sleep(1)
            elif pilih == 2:
                scoreboards()
                time.sleep(1)
            elif pilih == 3:
                cls()
                time.sleep(1)
                exit(0)

        pilihan[0] = " "
        pilihan[1] = " "
        pilihan[2] = " "
        pilihan[pilih-1] = ">"

        print("\n"*11)

        time.sleep(0.103)
        cls()
