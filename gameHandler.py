def mandoHandler(board, mando, char):
    '''Handles movement, firing of gun etc'''

    if char == "w":
        canMove = board.check(char)
        if canMove:
            mando.moveUp()
            board.update()
    elif char == "s":
        canMove = board.check(char)
        if canMove:
            mando.moveDown()
            board.update()
    elif char == "d":
        canMove = board.check(char)
        if canMove:
            mando.moveRight()
            board.update()
    elif char == "a":
        canMove = board.check(char)
        if canMove:
            mando.moveLeft()
            board.update()