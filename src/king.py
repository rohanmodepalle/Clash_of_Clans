# Importing Default Libraries
from colorama import Back, Style

# Importing Custom Modules
from defs import *
from character import Character

class King(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.position = [[xPos, yPos]]

    def initKing(game):
        king = King('King', MAX_KING_HEALTH, KING_DAMAGE, KING_SPEED, KING_SYMBOL, 1, COLS-2)
        game.board[king.xPos][king.yPos] = king.symbol
        game.MC = king

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


def renderKingColor(game, king):

    if(game.MC == None):
        return

    if king.health <= 0:
        king.symbol = BG
        for i in king.position:
            game.board[i[0]][i[1]] = BG
    elif(king.health <= 0.25 * MAX_KING_HEALTH):
        king.symbol = Back.RED + KING_SYMBOL + Style.RESET_ALL
        for i in king.position:
            game.board[i[0]][i[1]] = king.symbol
    elif(king.health <= 0.75 * MAX_KING_HEALTH):
        king.symbol = Back.YELLOW + KING_SYMBOL + Style.RESET_ALL
        for i in king.position:
            game.board[i[0]][i[1]] = king.symbol
    else:
        king.symbol = Back.GREEN + KING_SYMBOL + Style.RESET_ALL
        for i in king.position:
            game.board[i[0]][i[1]] = king.symbol


def attackKing(game):
    king = game.MC
    king.attack(game)