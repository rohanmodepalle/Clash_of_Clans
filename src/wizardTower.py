# Importing Default Libraries
import math
from barbarian import Barbarian

# Importing Custome Modules
from defs import *
from building import Building


class WT(Building):
    def __init__(self, name, health, symbol, range, damage):
        super().__init__(name, health, symbol)
        self.range = range
        self.damage = damage
        self.maxHealth = MAX_WT_HEALTH

        self.position = []
        self.center = []
        self.target = None
        
    def addWT(self, game, x, y):
        coord = []
        for i in range(x, x+2):
            point = [i]
            for j in range(y-1, y+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = self.symbol

        self.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        self.center = [avgX, avgY]

    def initWT(game):

        if(game.level == 1):

            game.numActiveBuildings += 2
            WT1 = WT('W1', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)
            WT2 = WT('W2', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)

            game.activeBuildings.append(WT1)
            game.activeBuildings.append(WT2)

            game.activeWTs.append(WT1)
            game.activeWTs.append(WT2)

            game.activeDefenseBuildings.append(WT1)
            game.activeDefenseBuildings.append(WT2)

            x = ROWS // 4
            y = COLS // 5

            x1 = x*2
            y1 = y*3-2
            WT1.addWT(game, x1, y1)

            x2 = x*2
            y2 = y*2+1
            WT2.addWT(game, x2, y2)

        elif(game.level == 2):
            
            game.numActiveBuildings += 3
            WT1 = WT('W1', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)
            WT2 = WT('W2', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)
            WT3 = WT('W3', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)

            game.activeBuildings.append(WT1)
            game.activeBuildings.append(WT2)
            game.activeBuildings.append(WT3)

            game.activeWTs.append(WT1)
            game.activeWTs.append(WT2)
            game.activeWTs.append(WT3)

            game.activeDefenseBuildings.append(WT1)
            game.activeDefenseBuildings.append(WT2)
            game.activeDefenseBuildings.append(WT3)

            x = ROWS // 5
            y = COLS // 5

            x1 = x*2
            y1 = y*2+1
            WT1.addWT(game, x1, y1)

            x2 = x*2
            y2 = y*2+5
            WT2.addWT(game, x2, y2)

            x3 = x*2
            y3 = y*3-2
            WT3.addWT(game, x3, y3)

        elif(game.level == 3):

            game.numActiveBuildings += 4
            WT1 = WT('W1', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)
            WT2 = WT('W2', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)
            WT3 = WT('W3', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)
            WT4 = WT('W4', MAX_WT_HEALTH, WT_SYMBOL, WT_RANGE, WT_DAMAGE)

            game.activeBuildings.append(WT1)
            game.activeBuildings.append(WT2)
            game.activeBuildings.append(WT3)
            game.activeBuildings.append(WT4)

            game.activeWTs.append(WT1)
            game.activeWTs.append(WT2)
            game.activeWTs.append(WT3)
            game.activeWTs.append(WT4)

            game.activeDefenseBuildings.append(WT1)
            game.activeDefenseBuildings.append(WT2)
            game.activeDefenseBuildings.append(WT3)
            game.activeDefenseBuildings.append(WT4)

            x = ROWS // 5
            y = COLS // 5

            x1 = x*2
            y1 = y*2+1
            WT1.addWT(game, x1, y1)

            x2 = x*2
            y2 = y*2+5
            WT2.addWT(game, x2, y2)

            x3 = x*2
            y3 = y*3-2
            WT3.addWT(game, x3, y3)

            x4 = (ROWS // 4) * 2
            y4 = y*2+1
            WT4.addWT(game, x4, y4)



    def getDistance(self, character):
        x1 = self.center[0]
        y1 = self.center[1]
        x2 = character.xPos
        y2 = character.yPos

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        return distance

    def getTarget(self, game):
        # Get closest barbarian or king from self
        closestTarget = None
        closestDistance = None
        activeCharacters = game.Barbarians + [game.MC] + game.Archers + game.Balloons
        for character in activeCharacters:
            distance = self.getDistance(character)
            if((closestDistance == None or distance < closestDistance) and distance <= self.range and character.isActive):
                closestTarget = character
                closestDistance = distance
        
        return closestTarget

    def attack(self, game):
        if(self.target == None):
            self.target = self.getTarget(game)

        # Get all troops in a 3x3 grid around self.target
        targets = []
        targets.append(self.target)
        if(self.target != None):
            if(self.target.symbol == BALLOON_SYMBOL):
                for balloon in game.Balloons:
                    if(balloon.isActive and balloon != self.target):
                        xDistance = abs(balloon.xPos - self.target.xPos)
                        yDistance = abs(balloon.yPos - self.target.yPos)
                        if(xDistance <= 1 and yDistance <= 1):
                            targets.append(balloon)
            else:
                for barbarian in game.Barbarians:
                    if(barbarian.isActive and barbarian != self.target):
                        xDistance = abs(barbarian.xPos - self.target.xPos)
                        yDistance = abs(barbarian.yPos - self.target.yPos)
                        if(xDistance <= 1 and yDistance <= 1):
                            targets.append(barbarian)
                for archer in game.Archers:
                    if(archer.isActive and archer != self.target):
                        xDistance = abs(archer.xPos - self.target.xPos)
                        yDistance = abs(archer.yPos - self.target.yPos)
                        if(xDistance <= 1 and yDistance <= 1):
                            targets.append(archer)
                
                if(game.MC.isActive and game.MC != self.target):
                    xDistance = abs(game.MC.xPos - self.target.xPos)
                    yDistance = abs(game.MC.yPos - self.target.yPos)
                    if(xDistance <= 1 and yDistance <= 1):
                        targets.append(game.MC)

        # Attack all targets
        for target in targets:
            if(target != None and target.isActive and self.getDistance(target) <= self.range):
                target.health -= self.damage

                if(target.health <= 0):
                    if(target in game.Barbarians or target in game.Archers or target in game.Balloons):
                        target.isActive = False
                        game.numActiveTroops -= 1
                    else:
                        game.MC.isActive = False
                        game.numActiveTroops -= 1

                    self.target = None

def attackWT(game):
    for WT in game.activeWTs:
        if(WT.isActive):
            WT.attack(game)

