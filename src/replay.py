# Importing Libraries
import os
import time

# Importing Custom Modules
from defs import *
from utils import Game, saveGame, spawnCharacter, attackMC, moveMC
from spells import castSpell

file = open('../history/replay.txt', 'r')
file = file.read()
file = file.split('\n')
numReplays = len(file) - 1

print("You have played " + str(numReplays) + " games.")
while(1):
    reqReplay = int(input("Enter the number of the replay you want to view(Latest game => 1 and 0 to quit): "))
    
    if(reqReplay == 0):
        break

    while(reqReplay <= 0 or reqReplay > numReplays):
        reqReplay = int(input("Please enter a valid input: "))

    replayStr = file[numReplays - reqReplay]
    index = 0

    while(1):
        print("Please select your Character(1 or 2):")
        print("1. Barbarian King")
        print("2. Archer Queen")


        inp = replayStr[index]
        index+=1

        while(inp not in ["1", "2"]):
            print("Please enter a valid input(1 or 2)")
            inp = replayStr[index]
            index+=1

        for level in [1, 2, 3]:

            game = Game(level, MAX_BARBARIANS, MAX_ARCHERS, MAX_BALLOONS, inp)

            while(game.state):
                # Printing Board 
                os.system('clear')
                game.printBoard()

                key = replayStr[index]
                index+=1

                # Handling Input
                if key == 'q':
                    game.state = False
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
                time.sleep(0.1)


            if(game.level < 2):
                print("LEVEL UP!")
                MAX_BARBARIANS += 2
                MAX_ARCHERS += 2
                MAX_BALLOONS += 1

        os.system('clear')
        print('YOU WIN :)')
        exit(0)


