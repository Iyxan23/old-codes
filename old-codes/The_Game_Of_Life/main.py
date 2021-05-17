import random

# W = 100
# H = 30
# Pixel = 3000

view = dict()


class live:
    icon = "#"
    locX = int()
    locY = int()

    def setlocY(self, locY):
        self.locY = locY

    def setlocX(self, locX):
        self.locX = locX

    def getNeighbour(self):
        ng = int()
        if view[self.locY][self.locX+1] == live or \
                view[self.locY][self.locX-1] == live or \
                view[self.locY+1][self.locX] == live or \
                view[self.locY-1][self.locX] == live or \
                view[self.locY+1][self.locX+1] == live or \
                view[self.locY-1][self.locX-1] == live or \
                view[self.locY-1][self.locX+1] == live or \
                view[self.locY+1][self.locX-1] == live:
            ng += 1


if __name__ =="__main__":
    # Buat Map
    c = str()
    unit = list()
    for a in range(0, 30):
        for b in range(0, 100):
            c += " "
        unit.append(c)
        c = ""