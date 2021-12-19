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

    def Hamming(self, board):
        heuristic=0
        for x in range(self.__BoardSize):
            for y in range(self.__BoardSize):
                if board[y][x] and self.__GoalBoard[y][x] != board[y][x]:
                    heuristic += 1
        return heuristic

    def Euclidean(self, board):
        heuristic = 0
        for x1 in range(self.__BoardSize):
            for y1 in range(self.__BoardSize):
                found = False

                for x2 in range(self.__BoardSize):
                    for y2 in range(self.__BoardSize):
                        if self.__GoalBoard[x1][y1] == board[x2][y2]:
                            found = True
                            dx = int(m.fabs(x2 - x1))
                            dy = int(m.fabs(y2 - y1))
                            heuristic += int(m.floor(m.sqrt(dx*dx + dy*dy)))
                            break
                    if found:
                        break
        return heuristic

    def Manhattan(self, board):
        heuristic = 0
        board = np.array(board)
        goal = np.array(self.__GoalBoard)
        for x in range(self.__BoardSize):
            for y in range(self.__BoardSize):
                if board[y][x] and goal[y][x] != board[y][x]:
                    row, col = np.where(goal == board[y][x])
                    heuristic += abs(row[0] - x) + abs(col[0] - y)
        return heuristic

    def __count_conflicts(self,candidate_row, solved_row, ans=0):
        counts = [0 for x in range(self.__BoardSize)]
        for i, tile_1 in enumerate(candidate_row):
            if tile_1 in solved_row and tile_1 != 0:
                for j, tile_2 in enumerate(candidate_row):
                    if tile_2 in solved_row and tile_2 != 0:
                        if tile_1 != tile_2:
                            if (solved_row.index(tile_1) > solved_row.index(tile_2)) and i < j:
                                counts[i] += 1
                            if (solved_row.index(tile_1) < solved_row.index(tile_2)) and i > j:
                                counts[i] += 1
        if max(counts) == 0:
            return ans * 2
        else:
            i = counts.index(max(counts))
            candidate_row[i] = -1
            ans += 1
            return self.__count_conflicts(candidate_row, solved_row, ans)


    def linear_conflicts(self, board):
        board = np.array(board).flatten()
        goal = np.array(self.__GoalBoard).flatten()
        res = self.manhattan(board)
        candidate_rows = [[] for y in range(self.__BoardSize)]
        candidate_columns = [[] for x in range(self.__BoardSize)]
        solved_rows = [[] for y in range(self.__BoardSize)]
        solved_columns = [[] for x in range(self.__BoardSize)]
        for y in range(self.__BoardSize):
            for x in range(self.__BoardSize):
                idx = (y * self.__BoardSize) + x
                candidate_rows[y].append(board[idx])
                candidate_columns[x].append(board[idx])
                solved_rows[y].append(goal[idx])
                solved_columns[x].append(goal[idx])
        for i in range(self.__BoardSize):
            res += self.__count_conflicts(candidate_rows[i], solved_rows[i], self.__BoardSize)
        for i in range(self.__BoardSize):
            res += self.__count_conflicts(candidate_columns[i],solved_columns[i], self.__BoardSize)
        return res

    def Permutation(self, board):
        heuristic=0
        board=np.array(board)
        board=np.transpose(board).flatten()
        for x in range(len(board)-1):
            for y in range(x+1,len(board)):
                if board[x] and board[y] and board[x] > board[y]:
                    heuristic += 1
    
        if board[len(board)-1]:
            heuristic +=1
        return  heuristic
