import keyboard
import time
import os

map_layer1 = []
map_layer2 = []

x = 0
y = 0
xold = 0
yold = 0

w = 0
h = 0

mode = ""
version = "0.1"


def draw(map_layer1, map_layer2):
    frame_buffer = []
    line_buffer = []
    for y in range(0, h):
        for x in range(0, w):
            line_buffer.append(map_layer1[y][x])
            if map_layer2[y][x] != " ":
                line_buffer[x] = map_layer2[y][x]
        frame_buffer.append(line_buffer)
        line_buffer.clear()

    print(frame_buffer)

    line_buffer_str = ""
    for y in range(0, h):
        for x in range(0, w):
            print(y, x)
            line_buffer_str += frame_buffer[y][x]
        print(line_buffer_str)
        line_buffer_str = ""


def bind_pos(map_, x, y, xold, yold, map_layer2):
    try:
        map_layer2[y][x + 1] = "<"
    except:
        pass
    try:
        map_layer2[y][x - 1] = ">"
    except:
        pass
    try:
        map_layer2[yold][xold + 1] = " "
    except:
        pass
    try:
        map_layer2[yold][xold + 1] = " "
    except:
        pass
    return map_layer2


def detect_keypress(map_, x, y):
    if keyboard.is_pressed("w") and y != 0:
        if map_[y - 1][x] != "#":
            y -= 1
    if keyboard.is_pressed("a") and x != 0:
        if map_[y][x - 1] != "#":
            x -= 1
    if keyboard.is_pressed("s") and y != len(map_):
        if map_[y + 1][x] != "#":
            y += 1
    if keyboard.is_pressed("d") and x != len(map_[0]):
        if map_[y][x + 1] != "#":
            x += 1

    return [x, y]


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def initialize():
    print("Initializing Map_Editor Version", version)
    print("Need map data to initialize")
    # Inputting Map data (width, height)
    # w = int(input("Input Map Width : "))
    # h = int(input("Input Map Height : "))
    w = 120
    h = 25
    print("Map data has been inserted!")
    print("Generating empty map")

    # Generating empty map
    lunit = list()
    result = list()
    for x_ in range(0, w):
        lunit.append(" ")

    for y_ in range(0, h):
        result.append(lunit)

    print("Done!")
    print("Returning Values")

    # Returning Variables using list
    return [w, h, result]


if __name__ == "__main__":
    output = initialize()

    # Assign values outputted by the initialize function to the global variables
    w = output[0]
    h = output[1]
    map_layer1 = output[2]
    map_layer2 = output[2]

    # Starting app
    while True:
        output = detect_keypress(map_layer1, x, y)
        x = output[0]
        y = output[1]

        map_layer2 = bind_pos(map_layer1, x, y, xold, yold, map_layer2)

        draw(map_layer1, map_layer2)

        time.sleep(0.033)
        clear()
