import keyboard
import os
import time
import json


# Map dimensions = X Y
#                = 1000


PlocX = 500
PlocY = 0


def header():
    print("\n                                                   The Lazer Soldier\n" +
          "                                                     --By Ihsan--         | " +
          str("ll") + " FPS |")
    print("X: " + str(PlocX) + " ,Y: " + str(PlocY))
    print("_" * 120)


def play(data):
    print("Data Loaded")
    os.system("cls")

    while True:
        header()


if __name__ == "__main__":
    os.system("titile 2D Game Adventurer | Made By Ihsan")
    # file = open("data_2dgameadv.json", "+")
    # data = json.JSONEncoder().encode(file.read)
    #
    # JSON Data structure
    # {
    #   "game":{
    #       [
    #           {
    #               "name":"--name--"
    #           }
    #       ]
    #   }
    # }

    data = {}
    gamedata = {}
    number = 1

    while True:
        print("   2D Game Adventurer")
        print("  Made by Ihsan\n")
        print(" 1. Continue saved game")
        print(" 2. New Game")
        print(" 3. Exit\n")

        inp = input("Choose: ")
        os.system("cls")

        if inp == 1:
            if len(data["game"]) != 0:
                while True:
                    for a in data["game"]:
                        print(str(number) + a["name"])
                    inp = input("Choose: ")
                    if not (int(inp) - 1) > len(data["game"]):
                        print("Loading Data...")
                        play(data["game"])
                        break

    # file.close()
