# Importing Default Libraries
from inspect import ClosureVars
import math

# Importing Custom Modules
from defs import *

class Character:
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.symbol = symbol
        self.xPos = xPos
        self.yPos = yPos
        self.isActive = True

    def getDistance(self, building):
        return math.sqrt((self.xPos - building.center[0])**2 + (self.yPos - building.center[1])**2)

    def getClosestBuilding(self, game):
        # Get the closest building from self
        closestBuilding = None
        closestDistance = None
        for building in game.activeBuildings:

            if(building.name == 'W'):
                continue

            distance = self.getDistance(building)
            if(closestDistance == None or distance < closestDistance):
                closestBuilding = building
                closestDistance = distance
        
        return closestBuilding

    def attackWall(self, game, xPos, yPos):
        # Find wall with xpos and ypos
        for building in game.activeBuildings:
            if(building.name == 'W'):
                if(building.position == [[xPos, yPos]]):
                    building.health -= self.damage
                    if(building.health <= 0):
                        building.isActive = False
                        building.center = [100000, 100000]
                    return

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


        # Check if wall is on the way to building
        if(game.board[self.xPos+1][self.yPos] == WALL_SYMBOL):
            self.attackWall(game, self.xPos+1, self.yPos)
        elif(game.board[self.xPos-1][self.yPos] == WALL_SYMBOL):
            self.attackWall(game, self.xPos-1, self.yPos) 
        elif(game.board[self.xPos][self.yPos+1] == WALL_SYMBOL):
            self.attackWall(game, self.xPos, self.yPos+1)
        elif(game.board[self.xPos][self.yPos-1] == WALL_SYMBOL):
            self.attackWall(game, self.xPos, self.yPos-1)



