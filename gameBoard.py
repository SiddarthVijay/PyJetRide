import colorama
import itertools
import sys

from printMessages import printLifeLost, printGameOver

from buildCharacter import beamBarrier
from random import seed, randint

class GameBoard:
    def __init__(self, mando, gameWidth=500, gameHeight=50):
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.frameWidth = 200
        self.frameHeight = 50
        self.offset = 0
        self.frameSpeed = 1

        self.gameClock = 0
        self.currentShieldONTime = 0
        self.currentShieldCoolDownTime = 0

        self.gameBoardArr = [[[" "] for i in range(self.gameWidth)]
                             for j in range(self.gameHeight)]

        # Making the ground and sky
        self.groundSize = 3
        self.skySize = 1

        # Bullet array
        self.bulletArray = []

        self.bossLocation = 10

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

        # Adding a boss
        for i in range(10, 30):
            for j in range(gameWidth-30, gameWidth-20):
                self.gameBoardArr[-i-1-self.groundSize][j][0] = "-"

        seed(1)
        # Adding coins
        numberCoins = randint(250, 500)
        # Now actually adding these coins to gameboard
        for i in range(numberCoins):
            coinHeight = randint(self.groundSize+1, gameHeight-self.skySize)
            coinWidth = randint(0, gameWidth-100)
            if self.gameBoardArr[coinHeight][coinWidth][0] == " ":
                self.gameBoardArr[coinHeight][coinWidth][0] = "c"

        # Adding th espeed powerup
        speedHeight = randint(self.groundSize+1, gameHeight-self.skySize)
        coinWidth = randint(10, 20)
        if self.gameBoardArr[coinHeight][coinWidth][0] == " ":
            self.gameBoardArr[coinHeight][coinWidth][0] = "S"

        # Adding the beams
        numberBeams = randint(75, 100)
        # Now actually adding the beams to gameboard
        for i in range(numberBeams):
            beamY = randint(self.groundSize+1, gameHeight-self.skySize)
            beamX = randint(0, gameWidth-100)
            beam = beamBarrier(beamX, beamY)

            if beam.formChoice == 1:
                try:
                    j = beam.position_x
                    for i in range(beam.position_y + self.groundSize, beam.position_y + beam.vSize + self.groundSize):
                        if self.gameBoardArr[-i-1][j][0] in "c ":
                            self.gameBoardArr[-i-1][j][0] = "-" + str(i)
                except:
                    pass
            elif beam.formChoice == 2:
                try:
                    i = beam.position_y
                    for j in range(beam.position_x, beam.position_x + beam.hSize):
                        if self.gameBoardArr[-i-1][j][0] in "c ":
                            self.gameBoardArr[-i-1][j][0] = "="
                except:
                    pass
            elif beam.formChoice == 3:
                for i, j in zip(range(beam.position_y + self.groundSize, beam.position_y + beam.crossSize + self.groundSize), range(beam.position_x, beam.position_x + beam.crossSize)):
                    try:
                        if self.gameBoardArr[-i-1][j][0] in "c ":
                            self.gameBoardArr[-i-1][j][0] = "-" + str(i)
                    except:
                        pass
            elif beam.formChoice == 4:
                for i, j in zip(range(beam.position_y + self.groundSize, beam.position_y + beam.crossSize + self.groundSize), range(beam.position_x + beam.crossSize, beam.position_x, -1)):
                    try:
                        if self.gameBoardArr[-i-1][j][0] in "c ":
                            self.gameBoardArr[-i-1][j][0] = "-" + str(i)
                    except:
                        pass


    def removeBarrier(self, barrier):
        for i in range(self.gameHeight):
            for j in range(self.gameWidth):
                if self.gameBoardArr[i][j][0] is barrier:
                    self.gameBoardArr[i][j][0] = " "

    def updateClock(self):
        self.gameClock += 1
    
    def shieldChecker(self, mando):
        if mando.shieldToggle == 1:
            return 0
        elif mando.shieldToggle == 0:
            if self.currentShieldCoolDownTime <= 0:
                return 1

    def check(self, mando, char):
        # Right now Im just returning can or cannot move, but later I'll return what Im colliding with so that I can use for collision and shit
        if char == "w":
            i = mando.position_y + mando.bodyHeight
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                try:
                    length = len(self.gameBoardArr[-i-1-self.groundSize][j][0])
                except:
                    length = 0
                if self.gameBoardArr[-i-1-self.groundSize][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif length > 1:
                    if mando.shieldToggle == 0:
                        mando.LIVES -= 1
                        printLifeLost()
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                    elif mando.shieldToggle == 1:
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                if self.gameBoardArr[-i-1-self.groundSize][j][0] == "S":
                    mando.mandoSpeed += 3
                    self.frameSpeed += 3
                    return 1
                elif self.gameBoardArr[-i-1-self.groundSize][j][0] != " ":
                    return 0
        elif char == "s":
            i = mando.position_y + 1
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                try:
                    length = len(self.gameBoardArr[-i-2][j][0])
                except:
                    length = 0
                if self.gameBoardArr[-i-2][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif length > 1:
                    if mando.shieldToggle == 0:
                        mando.LIVES -= 1
                        printLifeLost()
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                    elif mando.shieldToggle == 1:
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                elif self.gameBoardArr[-i-2][j][0] != " ":
                    return 0
        elif char == "d":
            if (mando.position_x - self.offset + mando.bodyWidth) > (self.frameWidth-1):
                return 0
            j = mando.position_x + mando.bodyWidth
            for i in range(mando.position_y + self.groundSize, mando.position_y + mando.bodyHeight + self.groundSize):
                try:
                    length = len(self.gameBoardArr[-i-1][j][0])
                except:
                    length = 0
                if self.gameBoardArr[-i-1][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif length > 1:
                    if mando.shieldToggle == 0:
                        mando.LIVES -= 1
                        printLifeLost()
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                    elif mando.shieldToggle == 1:
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                elif self.gameBoardArr[-i-1][j][0] != " ":
                        return 0
        elif char == "a":
            # To check for the left end in the beginning
            if mando.position_x == self.offset:
                return 0
            j = mando.position_x - 1
            for i in range(mando.position_y + self.groundSize, mando.position_y + mando.bodyHeight + self.groundSize):
                try:
                    length = len(self.gameBoardArr[-i-1][j][0])
                except:
                    length = 0
                if self.gameBoardArr[-i-1][j][0] == "c":
                    mando.SCORE += 1
                    return 1
                elif length > 1:
                    if mando.shieldToggle == 0:
                        mando.LIVES -= 1
                        printLifeLost()
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                    elif mando.shieldToggle == 1:
                        self.removeBarrier(self.gameBoardArr[-i-1-self.groundSize][j][0])
                        return 1
                elif self.gameBoardArr[-i-1][j][0] != " ":
                        return 0
        return 1

    def removeMando(self, mando):
        # remove the entire character
        for i in range(mando.position_y, mando.position_y + mando.bodyHeight):
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                self.gameBoardArr[-i-1-self.groundSize][j][0] = " "

        return 1
    
    def moveMando(self, mando):
        # remove the last line and add one line
        for i in range(mando.position_y, mando.position_y + mando.bodyHeight):
            for j in range(mando.position_x, mando.position_x + mando.bodyWidth):
                self.gameBoardArr[-i-1-self.groundSize][j][0] = "m"
        print("SCORE: " + str(mando.SCORE))
        print("LIVES: " + str(mando.LIVES))

        return 1

    def updateFrame(self, mando):
        if self.offset + self.frameWidth < self.gameWidth - 5:
            if self.gameClock % 3 == 2:
                if mando.position_x == self.offset:
                    canMove = self.check(mando, 'd')
                    if canMove:
                        self.removeMando(mando)
                        mando.moveRight()
                        self.moveMando(mando)
                        self.offset += self.frameSpeed
                else:
                    self.offset += self.frameSpeed

    def removeBullet(self, bullet):
        self.gameBoardArr[bullet.position_y][bullet.position_x][0] = " "
    
    def checkBullet(self, bullet, mando):
        try:
            if self.gameBoardArr[bullet.position_y][bullet.position_x+1][0] == " ":
                return 1
            elif "=" in self.gameBoardArr[bullet.position_y][bullet.position_x+1][0]:
                self.gameBoardArr[bullet.position_y][bullet.position_x+1][0] = " "
                self.gameBoardArr[bullet.position_y][bullet.position_x][0] = " "
                self.bulletArray.remove(bullet)
                return 0
            elif "-" in self.gameBoardArr[bullet.position_y][bullet.position_x+1][0]:
                self.gameBoardArr[bullet.position_y][bullet.position_x+1][0] = " "
                self.gameBoardArr[bullet.position_y][bullet.position_x][0] = " "
                self.bulletArray.remove(bullet)
                return 0
            elif self.gameBoardArr[bullet.position_y][bullet.position_x+1][0] == "c":
                mando.SCORE += 1
                self.gameBoardArr[bullet.position_y][bullet.position_x][0] = " "
                return 1
        except:
            self.gameBoardArr[bullet.position_y][bullet.position_x][0] = " "
            self.bulletArray.remove(bullet)
            return 0
            pass

    def cprintBoard(self, mando):
        print("\033[0;0H]")
        for i in range(self.frameHeight):
            for j in range(self.offset, self.frameWidth + self.offset):
                print(self.gameBoardArr[i][j][0], end="")
            print()
        if mando.LIVES <= 0:
            printGameOver()
            sys.exit
        return

    def printBoard(self, mando):
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
                    if mando.shieldToggle == 0:
                        if mando.body[bodyCounter] == " ":
                            print(colorama.Back.BLUE + " ", end="")
                        else:
                            print(colorama.Back.BLUE + colorama.Fore.BLACK + mando.body[bodyCounter], end="")
                        bodyCounter += 1
                    elif mando.shieldToggle == 1:
                        if mando.body[bodyCounter] == " ":
                            print(colorama.Back.GREEN + " ", end="")
                        else:
                            print(colorama.Back.GREEN + colorama.Fore.BLACK + mando.body[bodyCounter], end="")
                        bodyCounter += 1
                elif self.gameBoardArr[i][j][0] == "k":
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "c":
                    print(colorama.Back.BLUE + colorama.Fore.YELLOW + "O", end="")
                elif self.gameBoardArr[i][j][0] == "S":
                    print(colorama.Back.RED + colorama.Fore.YELLOW + "S", end="")
                elif "-" in self.gameBoardArr[i][j][0]:
                    print(colorama.Back.RED + " ", end="")
                elif self.gameBoardArr[i][j][0] == "=":
                    print(colorama.Back.GREEN + " ", end="")
                elif self.gameBoardArr[i][j][0] == "b":
                    print(colorama.Back.BLUE + colorama.Fore.YELLOW + "b", end="")
                else:
                    print(colorama.Back.BLUE + " ", end="")
            print()
        
        if mando.shieldToggle == 0:
            if self.currentShieldCoolDownTime > 0:
                self.currentShieldCoolDownTime -= 1
        elif mando.shieldToggle == 1:
            if self.currentShieldONTime > 100:
                mando.shieldToggle = 0
                self.currentShieldONTime = 0
                self.currentShieldCoolDownTime = 60
            else:
                self.currentShieldONTime += 1

        for bullet in self.bulletArray:
            check = self.checkBullet(bullet, mando)
            if check == 1:
                self.removeBullet(bullet)
                bullet.moveBullet()
                self.gameBoardArr[bullet.position_y][bullet.position_x][0] = "b"
        
        if self.gameClock%2 == 0:
            try:
                for i in range(self.bossLocation, self.bossLocation+10):
                    for j in range(self.gameWidth-30, self.gameWidth-20):
                        self.gameBoardArr[-i-1-self.groundSize][j][0] = " "
                for i in range(mando.position_y, mando.position_y+10):
                    for j in range(self.gameWidth-30, self.gameWidth-20):
                        self.gameBoardArr[-i-1-self.groundSize][j][0] = "-"
            except:
                pass

        if mando.LIVES <= 0:
            printGameOver()
            sys.exit