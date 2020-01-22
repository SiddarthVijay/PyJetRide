import random

class Mandalorian:
    def __init__(self):
        self.body = [' ', '_', '_', '_', ' ', ' ', '|', '+', '|', ' ', ' ', '-', '-', '-', ' ', '/', '|', ' ', '|', '\\', ' ', '-', '-', '-', ' ', ' ', '/', ' ', '\\', ' ']
        self.position_x = 0
        self.position_y = 0
        self.bodyHeight = 6
        self.bodyWidth = 5

        self.LIVES = 3
        self.SCORE = 0

        self.isShield = 0

    def moveUp(self):
        self.position_y += 1
        print("moved up")
    def moveDown(self):
        self.position_y -= 1
        print("moved down")
    def moveRight(self):
        self.position_x += 1
        print("moved right")
    def moveLeft(self):
        self.position_x -= 1
        print("moved left")
    
    def print(self):
        for i in self.body:
            for j in i:
                print(j, end='')
            print()


class beamBarrier:
    def __init__(self, x, y):
        self.form1 = [['-', '-', '-', '-']]
        self.form2 = [['-'], ['-'], ['-'], ['-']]
        self.form3 = [['-'],[' ', '-'], [' ', ' ', '-'], [' ', ' ', ' ', '-']]
        self.form4 = [[' ', ' ', ' ', '-'], [' ', ' ', '-'], [' ', '-'], ['-']]

        self.formChoice = random.randint(1, 4)

        self.size = 6

        self.position_x = x
        self.position_y = y

# mando = Mandalorian()
# mando.print()
