def mandoHandler(board, mando, char):
    '''Handles movement, firing of gun etc'''

    if char == "w":
        canMove = board.check(mando, char)
        if canMove:
            mando.moveUp()
            board.moveMando(mando, char)
    elif char == "s":
        canMove = board.check(mando, char)
        if canMove:
            mando.moveDown()
            board.moveMando(mando, char)
    elif char == "d":
        canMove = board.check(mando, char)
        if canMove:
            mando.moveRight()
            board.moveMando(mando, char)
    elif char == "a":
        canMove = board.check(mando, char)
        if canMove:
            mando.moveLeft()
            board.moveMando(mando, char)