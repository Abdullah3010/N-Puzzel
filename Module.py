from queue import PriorityQueue as pq
from GUI import isValidMove, makeMove
from Board import Board

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Module:
    __Space = {}
    __Fronte = pq()
    __key = 0
    __Solution = []

    def creatSearchSpace(self, state, heuristicF, parent=-1, lastmove=None):
        if state == Board.getSolution():
            return self.__Solution
        self.__Space[self.__key] = [state, lastmove, parent]
        pkey = self.__key
        self.__key += 1
        #possiblestates is a list of [boardstate, lastmove]
        possiblestates = self.nextstate(state, lastmove)
        for pstate in possiblestates:
            heuristicvalue = heuristicF(pstate[0]) #pstate[0] represent boardstate
            self.__Fronte.put((heuristicvalue, state, pstate[1])) #pstate[1] represent lastmove
        NextState = self.__Fronte.get()
        self.__Solution.append(NextState[2]) #NextState[2] represent lastmove
        self.creatSearchSpace(NextState[1], heuristicF, pkey, NextState[2]) #NextState[1] represent boardstate NextState[2] represent lastmove

    def nextstate(self, board, lastMove):
        validMoves = [UP, DOWN, LEFT, RIGHT]
        nextstates = []
        # remove moves from the list as they are disqualified
        if lastMove == UP or not isValidMove(board, DOWN):
            validMoves.remove(DOWN)
        if lastMove == DOWN or not isValidMove(board, UP):
            validMoves.remove(UP)
        if lastMove == LEFT or not isValidMove(board, RIGHT):
            validMoves.remove(RIGHT)
        if lastMove == RIGHT or not isValidMove(board, LEFT):
            validMoves.remove(LEFT)
        for move in validMoves:
            nextstates.append([makeMove(board, move), move])
        return nextstates