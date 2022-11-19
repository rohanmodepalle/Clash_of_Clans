# Importing Custome Modules
from defs import *
from building import Building

class TownHall(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)
        self.position = []
        self.center = []
        self.maxHealth = MAX_TOWN_HALL_HEALTH

    def initTH(game):
        game.numActiveBuildings += 1

        TH = TownHall('TH', MAX_TOWN_HALL_HEALTH, TOWN_HALL_SYMBOL)
        game.activeBuildings.append(TH)

        centerX = ROWS//2
        centerY = COLS//2
        coord = []
        for i in range(centerX-2, centerX+2):
            point = [i]
            for j in range(centerY-2, centerY+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = TH.symbol
            
        TH.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        TH.center = [avgX, avgY]
