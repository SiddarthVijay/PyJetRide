from buildCharacter import bullet

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
    elif char == " ":
        c = board.shieldChecker(mando)
        
        if c == 1:
            mando.shieldToggle = 1
    elif char == "b":
        newBullet = bullet(mando.position_x + mando.bodyWidth, -mando.position_y + 1 - board.groundSize - mando.bodyHeight)
        board.bulletArray.append(newBullet)