# Importing Custom Modules
from defs import *
from building import Building

class Wall(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)
        self.position = []
        self.maxHealth = MAX_WALL_HEALTH

    def initWall(game):

        x = ROWS//2
        y = COLS//2
        for i in range(x-3, x+3):
            for j in range(y-3, y+2):
                if(i == x-3 or i == x+2 or j == y-3 or j == y+1):
                    wall = Wall('W', MAX_WALL_HEALTH, WALL_SYMBOL)
                    wall.position.append([i, j])
                    game.activeBuildings.append(wall)
                    game.board[i][j] = WALL_SYMBOL

