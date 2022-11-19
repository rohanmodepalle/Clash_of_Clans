# Importing Default Libraries
from colorama import Back, Style

# Importing Custom Modules
from defs import *
from character import Character

class Queen(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.position = [[xPos, yPos]]

    def initQueen(game):
        queen = Queen('queen', MAX_QUEEN_HEALTH, QUEEN_DAMAGE, QUEEN_SPEED, QUEEN_SYMBOL, 1, COLS-2)
        game.board[queen.xPos][queen.yPos] = queen.symbol
        game.MC = queen

    def move(game, direction):
        # Check if object exists in the direction
        if(direction == 'w'):
            if(game.board[game.MC.xPos-2][game.MC.yPos] != BG):
                return False
        elif(direction == 's'):
            if(game.board[game.MC.xPos+2][game.MC.yPos] != BG):
                return False
        elif(direction == 'a'):
            if(game.board[game.MC.xPos][game.MC.yPos-2] != BG):
                return False
        elif(direction == 'd'):
            if(game.board[game.MC.xPos][game.MC.yPos+2] != BG):
                return False    

        # Move the object
        if(direction == 'w'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.xPos -= 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol
        elif(direction == 's'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.xPos += 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol
        elif(direction == 'a'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.yPos -= 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol
        elif(direction == 'd'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.yPos += 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol


    def getAttackCoordinates(self, direction):

        coordinates = []

        if(direction == 'w'):
            coordinates.append(max(self.position[0][0] - 8, 2))
            coordinates.append(self.position[0][1])
        elif(direction == 'a'):
            coordinates.append(self.position[0][0])
            coordinates.append(max(self.position[0][1] - 8, 2))
        elif(direction == 's'):
            coordinates.append(min(self.position[0][0] + 8, ROWS-2))
            coordinates.append(self.position[0][1])
        else:
            coordinates.append(self.position[0][0])
            coordinates.append(min(self.position[0][1] + 8, COLS-2))

        return coordinates

    def attack(self, game, direction):

        attackCoordinates = self.getAttackCoordinates(direction)
        print(self.position)
        print(attackCoordinates)

        buildings = []

        # Get all buildings in 5x5 grid around attack coordinates
        for i in range(attackCoordinates[0]-2, attackCoordinates[0]+3):
            for j in range(attackCoordinates[1]-2, attackCoordinates[1]+3):
                for building in game.activeBuildings:
                    for k in building.position:
                        if(k[0] == i and k[1] == j):
                            if(building not in buildings and building.isActive and building.name != 'W'):
                                buildings.append(building)
                            break

        if(len(buildings) == 0):
            # Check if wall is on the way to building
            if(game.board[self.xPos+1][self.yPos] == WALL_SYMBOL):
                self.attackWall(game, self.xPos+1, self.yPos)
            elif(game.board[self.xPos-1][self.yPos] == WALL_SYMBOL):
                self.attackWall(game, self.xPos-1, self.yPos) 
            elif(game.board[self.xPos][self.yPos+1] == WALL_SYMBOL):
                self.attackWall(game, self.xPos, self.yPos+1)
            elif(game.board[self.xPos][self.yPos-1] == WALL_SYMBOL):
                self.attackWall(game, self.xPos, self.yPos-1)  
            
            print("empty")
            return


        for i in buildings:
            print(i.name)


        # attack all buildings
        for building in buildings:

            building.health -= self.damage
            if(building.health <= 0):
                
                for i in building.position:
                    game.board[i[0]][i[1]] = BG
                
                building.isActive = False
                building.center = [100000, 100000]
                game.numActiveBuildings -= 1

def renderQueenColor(game, queen):

    if(game.MC == None):
        return

    if queen.health <= 0:
        queen.symbol = BG
        for i in queen.position:
            game.board[i[0]][i[1]] = BG
    elif(queen.health <= 0.25 * MAX_QUEEN_HEALTH):
        queen.symbol = Back.RED + QUEEN_SYMBOL + Style.RESET_ALL
        for i in queen.position:
            game.board[i[0]][i[1]] = queen.symbol
    elif(queen.health <= 0.75 * MAX_QUEEN_HEALTH):
        queen.symbol = Back.YELLOW + QUEEN_SYMBOL + Style.RESET_ALL
        for i in queen.position:
            game.board[i[0]][i[1]] = queen.symbol
    else:
        queen.symbol = Back.GREEN + QUEEN_SYMBOL + Style.RESET_ALL
        for i in queen.position:
            game.board[i[0]][i[1]] = queen.symbol


def attackQueen(game, direction):
    queen = game.MC
    queen.attack(game, direction)