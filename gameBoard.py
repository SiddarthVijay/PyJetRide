import os


class GameBoard:
    def __init__(self, gameWidth, gameHeight):
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.frameWidth = 100
        self.frameHeight = 70
        self.gameBoardArr = [[[" "] for i in range(gameWidth)]
                             for j in range(gameHeight)]

    def printBoard(self):
        # print(self.gameBoardArr)
        for gameBoardArrRow in self.gameBoardArr:
            for gameBoardArrCell in gameBoardArrRow:
                print(gameBoardArrCell[0], end='')
            print()


def startGame():
    # create instances of mando'a and initialize the score to zero and what not

    os.system('clear')
    boardInstance = GameBoard(2000, 7)
    boardInstance.printBoard()
