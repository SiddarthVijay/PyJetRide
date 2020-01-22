import colorama
import itertools
from buildCharacter import beamBarrier
from random import seed, randint

class GameBoard:
    def __init__(self, mando, gameWidth=2000, gameHeight=50):
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.frameWidth = 200
        self.frameHeight = 50
        self.offset = 0

        self.gameClock = 0

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

        # Adding the beams
        numberBeams = randint(50, 100)
        # Now actually adding the beams to gameboard
        for i in range(numberBeams):
            beamY = randint(self.groundSize+1, gameHeight-self.skySize)
            beamX = randint(0, gameWidth-1)
            beam = beamBarrier(beamX, beamY)

            if beam.formChoice == 1:
                try:
                    j = beam.position_x
                    for i in range(beam.position_y + self.groundSize, beam.position_y + beam.vSize + self.groundSize):            
                        self.gameBoardArr[-i-1][j][0] = "-"
                except:
                    pass
            elif beam.formChoice == 2:
                try:
                    i = beam.position_y
                    for j in range(beam.position_x, beam.position_x + beam.hSize):
                        self.gameBoardArr[-i-1][j][0] = "-"
                except:
                    pass
            elif beam.formChoice == 3:
                try:
                    for i, j in zip(range(beam.position_y + self.groundSize, beam.position_y + beam.crossSize + self.groundSize), range(beam.position_x, beam.position_x + beam.size)):
                        self.gameBoardArr[-i-1][j][0] = "-"
                except:
                    pass
            elif beam.formChoice == 4:
                try:
                    for i, j in zip(range(beam.position_y + self.groundSize, beam.position_y + beam.crossSize + self.groundSize), range(beam.position_x + beam.size, beam.position_x, -1)):
                        self.gameBoardArr[-i-1][j][0] = "-"
                except:
                    pass

        
        # Checking loop made for each loop, rn the loop is checking above mando for moving up
        #j = mando.position_x + mando.bodyWidth
        #for i in range(mando.position_y + self.groundSize, mando.position_y + mando.bodyHeight + self.groundSize):
        #    self.gameBoardArr[-i-1][j][0] = "k"
        
        # Checking loop for building beams
        # Vertical beams - done
        #beam = beamBarrier(8, 6)
        #j = beam.position_x
        #for i in range(beam.position_y + self.groundSize, beam.position_y + beam.size + self.groundSize):            
        #    self.gameBoardArr[-i-1][j][0] = "-"

        # Horizontal beams - done
        #beam = beamBarrier(15, 8)
        #i = beam.position_y
        #for j in range(beam.position_x, beam.position_x + beam.size):
        #    self.gameBoardArr[-i-1][j][0] = "-"
        
        # left to right beam - done
        #beam = beamBarrier(25, 8)
        #for i, j in zip(range(beam.position_y + self.groundSize, beam.position_y + beam.size + self.groundSize), range(beam.position_x, beam.position_x + beam.size)):
        #        self.gameBoardArr[-i-1][j][0] = "-"

        # right to left beam - done
        #beam = beamBarrier(35, 8)
        #for i, j in zip(range(beam.position_y + self.groundSize, beam.position_y + beam.size + self.groundSize), range(beam.position_x + beam.size, beam.position_x, -1)):
        #        self.gameBoardArr[-i-1][j][0] = "-"

    def updateClock(self):
        self.gameClock += 1

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
            if (mando.position_x - self.offset + mando.bodyWidth) > (self.frameWidth-1):
                return 0
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
        if self.offset + self.frameWidth < self.gameWidth:
            if self.gameClock % 3 == 2:
                if mando.position_x == self.offset:
                    canMove = self.check(mando, 'd')
                    if canMove:
                        self.removeMando(mando)
                        mando.moveRight()
                        self.moveMando(mando)
                        self.offset += 1
                else:
                    self.offset += 1

    def printBoard(self, mando):
        print("\033[0;0H]")
        for i in range(self.frameHeight):
            for j in range(self.offset, self.frameWidth + self.offset):
                print(self.gameBoardArr[i][j][0], end="")
            print()
        return

    def cprintBoard(self, mando):
        print("\033[0;0H]")
        bodyCounter = 0
        for i in range(self.frameHeight):
            for j in range(self.offset-1, self.frameWidth+self.offset+1):
                if (j == self.frameWidth + self.offset) or (j == self.offset - 1):
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "g":
                    print(colorama.Back.GREEN + " ", end="")
                elif self.gameBoardArr[i][j][0] == "t":
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "m":
                    if mando.body[bodyCounter] == " ":
                        print(colorama.Back.BLUE + " ", end="")
                    else:
                        print(colorama.Back.BLUE + colorama.Fore.BLACK + mando.body[bodyCounter], end="")
                    bodyCounter += 1
                elif self.gameBoardArr[i][j][0] == "k":
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "c":
                    print(colorama.Back.BLUE + colorama.Fore.YELLOW + "C", end="")
                else:
                    print(colorama.Back.BLUE + " ", end="")
            print()