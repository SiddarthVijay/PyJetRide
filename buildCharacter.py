class Mandalorian:
    def __init__(self):
        self.body = [[' ', '_', '_', '_', ' '],
                     [' ', '|', '+', '|', ' '],
                     [' ', '-', '-', '-', ' '],
                     ['/', '|', ' ', '|', '\\'],
                     [' ', '-', '-', '-', ' '],
                     [' ', '/', ' ', '\\', ' ']]
        self.position_x = 0
        self.position_y = 0
        self.bodyHeight = 6
        self.bodyWidth = 5

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
    def __init__(self):
        self.form1 = [['-', '-']]
        self.form2 = [['-'], ['-']]
        self.form3 = [['-'],[' ', '-']]
        self.form4 = [[' ', '-'], ['-']]

mando = Mandalorian()
mando.print()
