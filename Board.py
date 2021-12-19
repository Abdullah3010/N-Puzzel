import numpy as np
import math as m
from queue import PriorityQueue as pq

class Board:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    __Solution = []
    __Forantier = pq()
    __GoalBoard = []

    def __init__(self, N):
        self.__BoardSize = N
        self.__MovCounter = 0

    def setBOARDERSIZE(self, N):
        self.__BoardSize = N

    def getBOARDERSIZE(self):
        return self.__BoardSize

    def getTILESIZE(self):
        return int(250/self.__BoardSize)

    def getMovCounter(self):
        return self.__MovCounter

    def incMovCounter(self):
        self.__MovCounter += 1
        
    def resetMovCounter(self):
        self.__MovCounter = 0

    def getBoard(self):
        # Return a board data structure with tiles in the solved state.
        # For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function
        # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
        
        self.__MovCounter = 0
        counter = 1
        board = []

        for x in range(self.__BoardSize):
            column = []
            for y in range(self.__BoardSize):
                column.append(counter)
                counter += self.__BoardSize
            board.append(column)
            counter -= self.__BoardSize * (self.__BoardSize - 1) + self.__BoardSize - 1

        board[self.__BoardSize - 1][self.__BoardSize - 1] = None
        self.__GoalBoard = board
        return board

    def Solve(self, H,board):
        cost = H(board)
        self.__Forantier.put((cost,board))
               

        

    def getSolution(self):
        return self.__Solution


