import os
import globals
import input

from buildCharacter import Mandalorian
from gameHandler import mandoHandler
from gameBoard import GameBoard


def endGame():
    print("Sorry, you lost")
    return 1


def gameLoop(board, mando):
    # Handling lives
    if mando.LIVES == 0:
        gameEnd = endGame()
    else:
        board.printBoard()
        gameEnd = 0

    return gameEnd


def startGame():
    # create instances of mando'a and initialize the score to zero and what not

    # Creating our character
    jango = Mandalorian()

    os.system('clear')
    boardInstance = GameBoard(jango)

    #for i in range(10):
    while(1):
        gameEnd = gameLoop(boardInstance, jango)
        char = input.get()
        if char == 'q':
            gameEnd += endGame()
        else:
            mandoHandler(boardInstance, jango, char)
        
        if gameEnd == 1:
            break

        # Run the LIVEs to 0 to check if it ends