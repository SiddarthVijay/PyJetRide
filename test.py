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
