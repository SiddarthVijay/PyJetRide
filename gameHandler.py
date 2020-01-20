def mandoHandler(board, mando, char):
    '''Handles movement, firing of gun etc'''

    if char == "w":
        canMove = board.check(mando, char)
        if canMove:
            board.removeMando(mando)
            mando.moveUp()
            board.moveMando(mando)
    elif char == "s":
        canMove = board.check(mando, char)
        if canMove:
            board.removeMando(mando)
            mando.moveDown()
            board.moveMando(mando)
    elif char == "d":
        canMove = board.check(mando, char)
        if canMove:
            board.removeMando(mando)
            mando.moveRight()
            board.moveMando(mando)
        # Gravity
        canMove = board.check(mando, "s")
        if canMove:
            board.removeMando(mando)
            mando.moveDown()
            board.moveMando(mando)
    elif char == "a":
        canMove = board.check(mando, char)
        if canMove:
            board.removeMando(mando)
            mando.moveLeft()
            board.moveMando(mando)
        # Gravity
        canMove = board.check(mando, "s")
        if canMove:
            board.removeMando(mando)
            mando.moveDown()
            board.moveMando(mando)
    elif char == "":
        # Gravity
        canMove = board.check(mando, "s")
        if canMove:
            board.removeMando(mando)
            mando.moveDown()
            board.moveMando(mando)