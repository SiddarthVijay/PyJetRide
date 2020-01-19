import colorama


class GameBoard:
    def __init__(self, mando, gameWidth=2000, gameHeight=50):
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.frameWidth = 200
        self.frameHeight = 50
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


    def check(self, char):
        # Right now Im just returning can or cannot move, but later I'll return what Im colliding with so that I can use for collision and shit
        if char == "w":
            #checking


    def printBoard(self):
        print("\033[0;0H]")
        for i in range(self.frameHeight):
            for j in range(self.frameWidth):
                if self.gameBoardArr[i][j][0] == "g":
                    print(colorama.Back.GREEN + " ", end="")
                elif self.gameBoardArr[i][j][0] == "t":
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "m":
                    print(colorama.Back.YELLOW + " ", end="")
                else:
                    print(colorama.Back.BLUE + " ", end="")
            print()
