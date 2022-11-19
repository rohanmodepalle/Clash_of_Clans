# Importing Default Libraries
from colorama import Back, Style
from barbarian import Barbarian

# Importing Custom Modules
from defs import *
from character import Character


class Archer(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.position = [[xPos, yPos]]  

    def move(self, game):
        closestBuilding = self.getClosestBuilding(game)

        if(self.getDistance(closestBuilding) < ARCHER_RANGE):
            return

        # Move Archer towards closest building
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

    def attack(self, game):

        # Get the closest building from self
        closestBuilding = self.getClosestBuilding(game)

        # Check if barbarians next move is coinciding with building.symbol
        if(self.getDistance(closestBuilding) <= ARCHER_RANGE):

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


        # Check if wall is on the way to building
        if(game.board[self.xPos+1][self.yPos] == WALL_SYMBOL):
            self.attackWall(game, self.xPos+1, self.yPos)
        elif(game.board[self.xPos-1][self.yPos] == WALL_SYMBOL):
            self.attackWall(game, self.xPos-1, self.yPos) 
        elif(game.board[self.xPos][self.yPos+1] == WALL_SYMBOL):
            self.attackWall(game, self.xPos, self.yPos+1)
        elif(game.board[self.xPos][self.yPos-1] == WALL_SYMBOL):
            self.attackWall(game, self.xPos, self.yPos-1)  

def spawnArcher(game, locID):

    if(game.numArchersSpawned >= game.maxArchers):
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
    
    numarchers = len(game.Archers)
    archerID = 'A' + str(numarchers+1)

    archer = Archer(archerID, MAX_ARCHER_HEALTH, ARCHER_DAMAGE, ARCHER_SPEED, ARCHER_SYMBOL, x, y)
    game.Archers.append(archer)
    game.board[x][y] = archer.symbol
    game.numArchersSpawned += 1

def renderArcherColor(game, Archers):
    for archer in Archers:
        if archer.health <= 0:
            archer.symbol = BG
            for i in archer.position:
                game.board[i[0]][i[1]] = BG
        elif(archer.health <= 0.25 * MAX_ARCHER_HEALTH):
            archer.symbol = Back.RED + ARCHER_SYMBOL + Style.RESET_ALL
            for i in archer.position:
                game.board[i[0]][i[1]] = archer.symbol
        elif(archer.health <= 0.75 * MAX_ARCHER_HEALTH):
            archer.symbol = Back.YELLOW + ARCHER_SYMBOL + Style.RESET_ALL
            for i in archer.position:
                game.board[i[0]][i[1]] = archer.symbol
        else:
            archer.symbol = Back.GREEN + ARCHER_SYMBOL + Style.RESET_ALL
            for i in archer.position:
                game.board[i[0]][i[1]] = archer.symbol


def moveArchers(game):
    for archer in game.Archers:
        if(archer.isActive):
            archer.move(game)

def attackArchers(game):
    for archer in game.Archers:
        if(archer.isActive):
            archer.attack(game)