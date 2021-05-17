import random
import time
import os

# @author NurIhsan

val = random.randint(20, 150)
money = 100
start = 0
lastnum = 0
st = ""
spaces = ""
rg = int()

# Company Names
companyNames = ["Orange", 'Cuputer', "Coolter", "Grape", "Door", "Floor", "Cool", "Sense", "Habbit", "Ready", "Computer",
        "Lunix", "Faster", "Fast", "Tiger", "Elephant", "Atara", "Super", "Group", "Gray", "Red", "White", "Green", "Yellow",
        "Wow", "Cobra", "King", "Queen", "Kingdom", "Village", "Forest", "Tree", "Bush", "Dirt", "Stone", "Diamond", "Gold",
        "Expensive", "Hard", "Ez", "Light", "LightSpeed", "Years", "Moon", "Sun", "Mercury", "Venus", "Uranus", "Marz",
        "Probe", "Cable", "Port", "Server", "Website", "Counts"]


def makeCompanyName():
    result = str()
    for a in range(0, random.randint(1,2)):
        result += " " + companyNames[random.randint(0, len(companyNames))]
    return result


comName = makeCompanyName()


def process(cmd):
    cmds = cmd.split()
    if len(cmds) != 0:
        if cmds[0] == "next":
            comName = makeCompanyName()
            return comName
        elif cmds[0] == "buy":
            return int(cmds[1])
        elif cmds[0] == "sell":
            return -int(cmds[1])


while True:
    print("Your Money : " + str(money))
    print(comName + " : " + str(val))
    try:
        buy = process(input("Actions > "))
        noring = buy + 1
    except:
        comName = buy
        val = random.randint(20, 150)
    else:
        
        rg = int(input("Please Enter a waiting session number : "))
        os.system("clear")
        money -= buy
        start = val
        print("How Much You Buys : " + str(buy))
        print("Starts At : " + str(start))
        print("Target : " + str(val + buy + 10) + "\n")
        st = "-"
        for a in range(0, rg):
            lastnum = val
            val += random.randint(-10, 10)

            spaces = " " * (lastnum - start)

            print(val, spaces, st)

            if lastnum > val: st = "<"
            elif lastnum < val: st = ">"
            else: st = "-"

            time.sleep(random.randint(1, 10) / 10)
        earnings = (val - start) - buy # + int((val - start) * (buy / (val - start)))
        print("Earnings : " + str(earnings))
        money += earnings
        print("Your Balance : " + str(money))
        input()
    finally:
        os.system("clear")
