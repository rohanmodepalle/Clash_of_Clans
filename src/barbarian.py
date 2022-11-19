# Importing Default Libraries
from colorama import Back, Style

# Importing Custom Modules
from defs import *
from character import Character

class Barbarian(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.position = [[xPos, yPos]]

    def move(self, game):
        closestBuilding = self.getClosestBuilding(game)

        # Move Barbarian towards closest building
        if(self.xPos < closestBuilding.center[0]):
            if(game.board[self.xPos+1*self.speed][self.yPos] == BG):
                game.board[self.xPos][self.yPos] = BG
                self.xPos += 1 * self.speed
                self.position = [[self.xPos, self.yPos]]
                game.board[self.xPos][self.yPos] = self.symbol
        if(self.xPos > closestBuilding.center[0]):
            if(game.board[self.xPos-1*self.speed][self.yPos] == BG):
                game.board[self.xPos][self.yPos] = BG
                self.xPos -= 1 * self.speed
                self.position = [[self.xPos, self.yPos]]
                game.board[self.xPos][self.yPos] = self.symbol
        if(self.yPos < closestBuilding.center[1]):
            if(game.board[self.xPos][self.yPos+1*self.speed] == BG):
                game.board[self.xPos][self.yPos] = BG
                self.yPos += 1 * self.speed
                self.position = [[self.xPos, self.yPos]]
                game.board[self.xPos][self.yPos] = self.symbol
        if(self.yPos > closestBuilding.center[1]):
            if(game.board[self.xPos][self.yPos-1*self.speed] == BG):
                game.board[self.xPos][self.yPos] = BG
                self.yPos -= 1 * self.speed
                self.position = [[self.xPos, self.yPos]]
                game.board[self.xPos][self.yPos] = self.symbol


def spawnBarbarian(game, locID):

    if(game.numBarbariansSpawned >= game.maxBarbarians):
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
    
    numBarbs = len(game.Barbarians)
    BarbID = 'B' + str(numBarbs+1)

    barb = Barbarian(BarbID, MAX_BARB_HEALTH, BARB_DAMAGE, BARB_SPEED, BARB_SYMBOL, x, y)
    game.Barbarians.append(barb)
    game.board[x][y] = barb.symbol
    game.numBarbariansSpawned += 1

def renderBarbarianColor(game, barbarians):
    for barb in barbarians:
        if barb.health <= 0:
            barb.symbol = BG
            for i in barb.position:
                game.board[i[0]][i[1]] = BG
        elif(barb.health <= 0.25 * MAX_BARB_HEALTH):
            barb.symbol = Back.RED + BARB_SYMBOL + Style.RESET_ALL
            for i in barb.position:
                game.board[i[0]][i[1]] = barb.symbol
        elif(barb.health <= 0.75 * MAX_BARB_HEALTH):
            barb.symbol = Back.YELLOW + BARB_SYMBOL + Style.RESET_ALL
            for i in barb.position:
                game.board[i[0]][i[1]] = barb.symbol
        else:
            barb.symbol = Back.GREEN + BARB_SYMBOL + Style.RESET_ALL
            for i in barb.position:
                game.board[i[0]][i[1]] = barb.symbol


def moveBarbarians(game):
    for barb in game.Barbarians:
        if(barb.isActive):
            barb.move(game)

def attackBarbarians(game):
    for barb in game.Barbarians:
        if(barb.isActive):
            barb.attack(game)