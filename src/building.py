# Importing Default Libraries
from colorama import Back, Style

# Import Custom Modules
from defs import *

class Building:
    def __init__(self, name, health, symbol):
        self.name = name
        self.health = health
        self.symbol = symbol
        self.isActive = True

def renderBuildingColor(game, activeBuildings):
    renderBuildings(game, activeBuildings)

def renderBuildings(game, activeBuildings):

    for building in activeBuildings:
        if(building.symbol != WALL_SYMBOL):
            if building.health <= 0:
                building.symbol = BG
                for i in building.position:
                    game.board[i[0]][i[1]] = BG
            elif(building.health <= 0.25 * building.maxHealth):
                for i in building.position:
                    game.board[i[0]][i[1]] = Back.RED + building.symbol + Style.RESET_ALL
            elif(building.health <= 0.75 * building.maxHealth):
                for i in building.position:
                    game.board[i[0]][i[1]] = Back.YELLOW + building.symbol + Style.RESET_ALL
            else:
                for i in building.position:
                    game.board[i[0]][i[1]] = Back.GREEN + building.symbol + Style.RESET_ALL
        else:
            if building.health <= 0:
                for i in building.position:
                    game.board[i[0]][i[1]] = BG
            else:
                for i in building.position:
                    game.board[i[0]][i[1]] = building.symbol