# Importing Default Libraries
from symtable import Symbol
from colorama import Back, Style

# Importing Custom Modules
from defs import *
from character import Character


class Balloon(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.position = [[xPos, yPos]]

    def getClosestBuilding(self, game):
        # Get the closest building from self
        closestBuilding = None
        closestDistance = None

        for building in game.activeDefenseBuildings:

            if(building.name == 'W'):
                continue

            distance = self.getDistance(building)
            if((closestDistance == None or distance < closestDistance) and building.isActive):
                closestBuilding = building
                closestDistance = distance

        if(closestBuilding != None):
            return closestBuilding
        
        for building in game.activeBuildings:

            if(building.name == 'W'):
                continue

            distance = self.getDistance(building)
            if(closestDistance == None or distance < closestDistance):
                closestBuilding = building
                closestDistance = distance
        
        return closestBuilding

    def move(self, game):
        closestBuilding = self.getClosestBuilding(game)
        
        # Move Balloon towards closest building
        if(self.xPos < closestBuilding.center[0]):
            game.board[self.xPos][self.yPos] = BG
            self.xPos += 1 * self.speed
            self.position = [[self.xPos, self.yPos]]
            game.board[self.xPos][self.yPos] = self.symbol
        if(self.xPos > closestBuilding.center[0]):
            game.board[self.xPos][self.yPos] = BG
            self.xPos -= 1 * self.speed
            self.position = [[self.xPos, self.yPos]]
            game.board[self.xPos][self.yPos] = self.symbol
        if(self.yPos < closestBuilding.center[1]):
            game.board[self.xPos][self.yPos] = BG
            self.yPos += 1 * self.speed
            self.position = [[self.xPos, self.yPos]]
            game.board[self.xPos][self.yPos] = self.symbol
        if(self.yPos > closestBuilding.center[1]):
            game.board[self.xPos][self.yPos] = BG
            self.yPos -= 1 * self.speed
            self.position = [[self.xPos, self.yPos]]
            game.board[self.xPos][self.yPos] = self.symbol

    def attack(self, game):

        # Get the closest building from self
        closestBuilding = self.getClosestBuilding(game)

        checkSides = [self.xPos+1, self.yPos] in closestBuilding.position or [self.xPos-1, self.yPos] in closestBuilding.position or [self.xPos, self.yPos+1] in closestBuilding.position or [self.xPos, self.yPos-1] in closestBuilding.position
        checkCorners = [self.xPos+1, self.yPos+1] in closestBuilding.position or [self.xPos+1, self.yPos-1] in closestBuilding.position or [self.xPos-1, self.yPos+1] in closestBuilding.position or [self.xPos-1, self.yPos-1] in closestBuilding.position

        # Check if barbarians next move is coinciding with building.symbol
        if(checkSides or checkCorners):
            # Attack building
            closestBuilding.health -= self.damage

            if(closestBuilding.health <= 0):
                # make position of building equal to BG

                for i in closestBuilding.position:
                    game.board[i[0]][i[1]] = BG

                closestBuilding.isActive = False
                closestBuilding.center = [100000, 100000]
                game.numActiveBuildings -= 1

            return

def spawnBalloon(game, locID):

    if(game.numBalloonsSpawned >= game.maxBalloons):
        return

    if(locID == 1):
        x = 1;
        y = 1;
    elif(locID == 2):
        x = ROWS-2;
        y = 1;
    elif(locID == 3):
        x = ROWS-2;
        y = COLS-2;
    
    numBalloons = len(game.Balloons)
    BalloonID = 'B' + str(numBalloons+1)

    balloon = Balloon(BalloonID, MAX_BALLOON_HEALTH, BALLOON_DAMAGE, BALLOON_SPEED, BALLOON_SYMBOL, x, y)
    game.Balloons.append(balloon)
    game.board[x][y] = balloon.symbol
    game.numBalloonsSpawned += 1

def renderBalloonColor(game, Balloons):
    for Balloon in Balloons:
        if Balloon.health <= 0:
            Balloon.symbol = BG
            for i in Balloon.position:
                game.board[i[0]][i[1]] = BG
        elif(Balloon.health <= 0.25 * MAX_BALLOON_HEALTH):
            Balloon.symbol = Back.RED + BALLOON_SYMBOL + Style.RESET_ALL
            for i in Balloon.position:
                game.board[i[0]][i[1]] = Balloon.symbol
        elif(Balloon.health <= 0.75 * MAX_BALLOON_HEALTH):
            Balloon.symbol = Back.YELLOW + BALLOON_SYMBOL + Style.RESET_ALL
            for i in Balloon.position:
                game.board[i[0]][i[1]] = Balloon.symbol
        else:
            Balloon.symbol = Back.GREEN + BALLOON_SYMBOL + Style.RESET_ALL
            for i in Balloon.position:
                game.board[i[0]][i[1]] = Balloon.symbol


def moveBalloons(game):
    for Balloon in game.Balloons:
        if(Balloon.isActive):
            Balloon.move(game)

def attackBalloons(game):
    for Balloon in game.Balloons:
        if(Balloon.isActive):
            Balloon.attack(game)