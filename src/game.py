# Importing Libraries
import os

# Importing Custom Modules
from input import input_to, Get
from defs import *
from utils import Game, saveGame, spawnCharacter, attackMC, moveMC
from spells import castSpell

# Initializing Game
moves = []
direction = ""
 
print("Please select your Character(1 or 2):")
print("1. Barbarian King")
print("2. Archer Queen")
inp = input("")
 
while(inp not in ["1", "2"]):
    print("Please enter a valid input(1 or 2)")
    inp = input("")
    

for level in [1, 2, 3]:
    game = Game(level, MAX_BARBARIANS, MAX_ARCHERS, MAX_BALLOONS, inp)

    while(game.state):
        # Printing Board 
        os.system('clear')
        game.printBoard()

        # Getting Input
        get = Get()
        key = input_to(get)
        moves.append(key)

        # Handling Input
        if key == 'q':
            exit(0)
        elif key in ['1', '2', '3']:
            spawnCharacter(game, int(key))
        elif key in ['w', 'a', 's', 'd']:
            moveMC(game, key)
            direction = key
        elif key in ['r', 'h']:
            castSpell(game, key)
        elif key == ' ':
            attackMC(game, direction)
        elif key == 'b':
            game.currChar = "Barbarian"
        elif key == 'n':
            game.currChar = "Archer"
        elif key == 'm':
            game.currChar = "Balloon"
        
        game.update()

    if(game.level < 2):
        print("LEVEL UP!")
        MAX_BARBARIANS += 2
        MAX_ARCHERS += 2
        MAX_BALLOONS += 1


saveGame(moves)

os.system('clear')
print('YOU WIN :)')