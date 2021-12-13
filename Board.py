class Board:
    def __init__(self, N):
        self.BoardSize = N

    def setBOARDERSIZE(self, N):
        self.BoardSize = N

    def getBOARDERSIZE(self):
        return self.BoardSize

    def getBoard(self, BOARDSIZE):
        # Return a board data structure with tiles in the solved state.
        # For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function
        # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
        counter = 1
        board = []
        for x in range(BOARDSIZE):
            column = []
            for y in range(BOARDSIZE):
                column.append(counter)
                counter += BOARDSIZE
            board.append(column)
            counter -= BOARDSIZE * (BOARDSIZE - 1) + BOARDSIZE - 1

        board[BOARDSIZE - 1][BOARDSIZE - 1] = None
        return board