import colorama
from random import seed, randint

class GameBoard:
    def __init__(self, mando, gameWidth=2000, gameHeight=50):
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.frameWidth = 200
        self.frameHeight = 50
        self.offset = 0

        self.gameBoardArr = [[[" "] for i in range(self.gameWidth)]
                             for j in range(self.gameHeight)]

        # Making the ground and sky
        self.groundSize = 3
        self.skySize = 1

        # Adding characters for sky
        for i in range(self.skySize):
            for j in range(self.gameWidth):
                self.gameBoardArr[i][j][0] = "t"

        # Adding the floor
        for i in range(self.groundSize):
            for j in range(self.gameWidth):
                self.gameBoardArr[-i-1][j][0] = "g"
        
        # Adding our mando
        for i in range(mando.position_y, mando.position_y + mando.bodyHeight):
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                self.gameBoardArr[-i-1-self.groundSize][j][0] = "m"

        seed(1)
        # Adding coins
        numberCoins = randint(250, 500)
        # Now actually adding these coins to gameboard
        for i in range(numberCoins):
            coinHeight = randint(self.groundSize+1, gameHeight-self.skySize)
            coinWidth = randint(0, gameWidth-1)
            if self.gameBoardArr[coinHeight][coinWidth][0] == " ":
                self.gameBoardArr[coinHeight][coinWidth][0] = "c"
        
        # Checking loop made for each loop, rn the loop is checking above mando for moving up
        j = mando.position_x + mando.bodyWidth
        for i in range(mando.position_y + self.groundSize, mando.position_y + mando.bodyHeight + self.groundSize):
            self.gameBoardArr[-i-1][j][0] = "k"


    def check(self, mando, char):
        # Right now Im just returning can or cannot move, but later I'll return what Im colliding with so that I can use for collision and shit
        if char == "w":
            i = mando.position_y + mando.bodyHeight
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                if self.gameBoardArr[-i-1-self.groundSize][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif self.gameBoardArr[-i-1-self.groundSize][j][0] != " ":
                    return 0
        elif char == "s":
            i = mando.position_y + 1
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                if self.gameBoardArr[-i-2][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif self.gameBoardArr[-i-2][j][0] != " ":
                    return 0
        elif char == "d":
            j = mando.position_x + mando.bodyWidth
            for i in range(mando.position_y + self.groundSize, mando.position_y + mando.bodyHeight + self.groundSize):
                if self.gameBoardArr[-i-1][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif self.gameBoardArr[-i-1][j][0] != " ":
                        return 0
        elif char == "a":
            # To check for the left end in the beginning
            if mando.position_x == self.offset:
                return 0
            j = mando.position_x - 1
            for i in range(mando.position_y + self.groundSize, mando.position_y + mando.bodyHeight + self.groundSize):
                if self.gameBoardArr[-i-1][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif self.gameBoardArr[-i-1][j][0] != " ":
                        return 0
        return 1

    def removeMando(self, mando):
        # remove the last line and add one line
        for i in range(mando.position_y, mando.position_y + mando.bodyHeight):
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                self.gameBoardArr[-i-1-self.groundSize][j][0] = " "

        return 1
    
    def moveMando(self, mando):
        # remove the last line and add one line
        for i in range(mando.position_y, mando.position_y + mando.bodyHeight):
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                self.gameBoardArr[-i-1-self.groundSize][j][0] = "m"
        print(mando.SCORE)

        return 1

    def updateFrame(self, mando):
        if (mando.position_x - mando.bodyWidth/2) >= ((self.frameWidth + self.offset)/2):
            self.offset += 1

    def printBoard(self):
        print("\033[0;0H]")
        for i in range(self.frameHeight):
            for j in range(self.offset, self.frameWidth + self.offset):
                print(self.gameBoardArr[i][j][0], end="")
            print()
        return

    def cprintBoard(self):
        print("\033[0;0H]")
        for i in range(self.frameHeight):
            for j in range(self.offset, self.frameWidth + self.offset):
                if self.gameBoardArr[i][j][0] == "g":
                    print(colorama.Back.GREEN + " ", end="")
                elif self.gameBoardArr[i][j][0] == "t":
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "m":
                    print(colorama.Back.YELLOW + " ", end="")
                elif self.gameBoardArr[i][j][0] == "k":
                    print("k", end="")
                else:
                    print(colorama.Back.BLUE + " ", end="")
            print()