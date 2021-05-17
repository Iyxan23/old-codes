import os

view = list()
tokensHistory = list()
back = list()

def rn(start, stop):
    result = []
    value = start
    while True:
        if value == stop:
            # print(result)
            return result
        else:
            result.append(value)
            value += 1


def processcommands(cmd, vw, back):
    # using split()
    tokens = cmd.split()
    tokensHistory.append(tokens)
    # print("TOKENS: " + str(tokens))
    if len(tokens) != 0:

        if len(tokens) == 2:  # Berarti ad 1 Vector2
            vw[int(tokens[0])][int(tokens[1])] = " "

        elif len(tokens) == 4:  # Berarti ad 2 Vector2

            print("Carving from " + tokens[0] +","+ tokens[1] + " to " + tokens[2] +","+ tokens[3])
            # print("SYTART LOOp")
            # print(int(tokens[0]), int(tokens[1]), int(tokens[2]), int(tokens[3]))

            # print(range.count(range(int(tokens[0]), int(tokens[1]))))
            # print(range.count(range(int(tokens[2]), int(tokens[4]))))
            # for y in range(int(tokens[0]), int(tokens[1])):  # Y
            #     print("y")
            #     for x in range(int(tokens[2]), int(tokens[4])):  # X
            #         print("x")
            #         vw[y][x] = " "
            #         print(y, x)
            # print("Done!")

            for y in rn(int(tokens[0]), int(tokens[2])):  # Y
                # print("y")
                for x in rn(int(tokens[1]), int(tokens[3])):  # X
                    # print("x")
                    vw[y][x] = " "
                    print(y, x)
            print("Done!")

        elif tokens[0] == "z":
            vw = back

        elif tokens[0] == "dbg":
            print(vw)
            print(tokens)
            print(tokensHistory)

        elif tokens[0] == "rerun":
            os.system("python carver.py")
            exit(0)

        elif tokens[0] == "export":
            print("Exporting..")
            print(view)
            exit(0)

        else:
            print("== ERROR ==")
            print("something weird happened :v")
            print(" DID YOU PRESS SOMETHING??")
        back = vw
    return vw, back


def initialize(w, h):
    lunit = list()
    for y in range(0, h):
        for x in range(0, w):
            lunit.append("#")
        view.append(lunit)
        lunit = []


def draw():
    resString = ""
    yCoord = 0
    for y in view:
        for x in y:
            resString += x
        print(str(yCoord) + "\t" +  resString)
        yCoord += 1
        resString = ""


print("Starting Program..")

width = int(input("Width : "))
height = int(input("Height : "))

initialize(width, height)

print("Done!")
print("== Carver 1.0 Made By NurIhsan =====================")

# draw()

while True:
    try:
        draw()
        print("Type commands to carve..")
        command = input("=(CARVE)=> ")

        aa = processcommands(command, view, back)
        view = aa[0]
        back = aa[1]
    except Exception as e:
        print("\n==ERROR========================================")
        print(e)
        print("===============================================\n")
