from gameBoard import startGame


def showMainMenu():
    print("Press ENTER to Start Game")
    print("Press Q to Quit")

    gameChoice = input("")
    if gameChoice == "":
        startGame()
    elif gameChoice == "Q":
        print("Thanks for Playing")
