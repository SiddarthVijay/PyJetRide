import os
import input

def printLifeLost():
    os.system('clear')
    print("YOU LOST A LIFE")
    for row in range(6):
        for col in range(7):
            if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8:
                print('*',end="")
            else:
                print(" ",end=" ")
        print()
    print("Press SPACE to continue")

    while(1):
        char = input.get()
        if char == " ":
            return

def printGameOver():
    os.system('clear')
    print("GAME OVER")
    for row in range(6):
        for col in range(7):
            if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8:
                print('*',end="")
            else:
                print(" ",end=" ")
        print()
    print("Press SPACE to END GAME")

    while(1):
        char = input.get()
        if char == " ":
            return