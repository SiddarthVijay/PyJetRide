import os
import globals
from gameBoard import GameBoard


def endGame():
    print("Sorry, you lost")
    return 1


def gameLoop(board):
    # Handling lives
    if globals.LIVES == 0:
        gameEnd = endGame()
    else:
        board.printBoard()
        gameEnd = 0

    return gameEnd


def startGame():
    # create instances of mando'a and initialize the score to zero and what not

    os.system('clear')
    boardInstance = GameBoard()

    # Start the game loop
    globals.LIVES = 3
    globals.SCORE = 0

    while(1):
        gameEnd = gameLoop(boardInstance)
        # if gameEnd == 1:
            # break
        break

        # Run the LIVEs to 0 to check if it ends
