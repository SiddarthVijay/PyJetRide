def showMainMenu():
    print("Press ENTER to Start Game")
    print("Press Q to Quit")

    gameChoice = input("")
    if gameChoice == "":
        print("Going into game")
    elif gameChoice == "Q":
        print("Quitting out")
