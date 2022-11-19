# Importing Libraries
import os

# Importing Custom Modules
from archer import renderArcherColor
from defs import *
from huts import Hut
from walls import Wall
from townHall import TownHall
from king import King, renderKingColor, attackKing
from queen import Queen, renderQueenColor, attackQueen
from cannon import Cannon, attackCannon
from wizardTower import WT, attackWT
from building import renderBuildingColor
from barbarian import renderBarbarianColor, moveBarbarians, attackBarbarians, spawnBarbarian
from archer import renderArcherColor, moveArchers, attackArchers, spawnArcher
from balloon import renderBalloonColor, moveBalloons, attackBalloons, spawnBalloon

class Game:
    def __init__(self, level, maxBarbarians, maxArchers, maxBalloons, charType):
        # Initializing vars
        self.board = []
        self.state = True
        self.activeDefenseBuildings = []
        self.activeCannons = []
        self.activeBuildings = []
        self.activeWTs = []
        self.Barbarians = []
        self.Balloons = []
        self.Archers = []
        self.numActiveBuildings = 0
        self.maxBarbarians = maxBarbarians
        self.maxArchers = maxArchers
        self.maxBalloons = maxBalloons
        self.numActiveTroops = maxBalloons + maxArchers + maxBarbarians + 1
        self.numBarbariansSpawned = 0
        self.numBalloonsSpawned = 0
        self.numArchersSpawned = 0
        self.result = None
        self.currChar = "Barbarian"
        self.level = level
        self.MC_Type = charType
        self.MC = None

        # Calling init functions
        self.initBoard()
        TownHall.initTH(self)
        Hut.initHut(self)
        Cannon.initCannon(self)
        WT.initWT(self)
        Wall.initWall(self)

        if(charType == "1"):
            King.initKing(self)
        else:
            Queen.initQueen(self)


    def initBoard(self):
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                if(i == 0 and j == 0):
                    row.append(TOP_LEFT_CORNER)
                elif(i == 0 and j == COLS-1):
                    row.append(TOP_RIGHT_CORNER)
                elif(i == ROWS-1 and j == 0):
                    row.append(BOTTOM_LEFT_CORNER)
                elif(i == ROWS-1 and j == COLS-1):
                    row.append(BOTTOM_RIGHT_CORNER)
                elif(i == 0 or i == ROWS-1):
                    row.append(TOP_WALL)
                elif(j == 0 or j == COLS-1):
                    row.append(SIDE_WALL)
                else:
                    row.append(BG)
            row.append('\n')
            self.board.append(row)
    
    def printBoard(self):

        renderBuildingColor(self, self.activeBuildings)
        renderBarbarianColor(self, self.Barbarians)
        renderBalloonColor(self, self.Balloons)
        renderArcherColor(self, self.Archers)

        if(self.MC_Type == "1"):
            renderKingColor(self, self.MC)
        else:
            renderQueenColor(self, self.MC)

        print("LEVEL " + str(self.level))

        board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end='')
        
        if(self.MC_Type == "1"):
            numHearts = int((self.MC.health / MAX_KING_HEALTH) * 10)
            print("King Health: " + u'\u2665' * numHearts)
        else:
            numHearts = int((self.MC.health / MAX_QUEEN_HEALTH) * 10)
            print("Queen Health: " + u'\u2665' * numHearts)



    def checkGame(self):
        if(self.numActiveTroops <= 0):
            os.system('clear')
            print('YOU LOSE :(')
            exit(0)
        elif(self.numActiveBuildings <= 0):
            self.result = 'WIN'
            self.state = False

    def update(self):
        moveBarbarians(self)
        attackBarbarians(self)

        moveArchers(self)
        attackArchers(self)

        moveBalloons(self)
        attackBalloons(self)

        attackCannon(self)
        attackWT(self)

        self.checkGame()


def spawnCharacter(game, key):
    if(game.currChar == "Barbarian"):
        spawnBarbarian(game, key)
    elif(game.currChar == "Archer"):
        spawnArcher(game, key)
    elif(game.currChar == "Balloon"):
        spawnBalloon(game, key)

def attackMC(game, direction):
    if(game.MC_Type == "1"):
        attackKing(game)
    else:
        attackQueen(game, direction)

def moveMC(game, direction):
    if(game.MC_Type == "1"):
        King.move(game,direction)
    else:
        Queen.move(game,direction)


def saveGame(moves):
    file = open('../history/replay.txt', 'a')

    for move in moves:
        if(move == None):
            file.write("!")
        else:
            file.write(str(move))

    file.write('\n')
    file.close()