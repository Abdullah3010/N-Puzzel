import numpy as np
import random
import math

class Creator:

    # N is the size of puzzle ex ({8,9 Puzzle},{15,16 Puzzle},{24,25 Puzzle})
    def __init__(self,N):
        self.N = int(math.sqrt(N+1))

    #Create random intial state for N-puzzle
    def initial_state(self):
        initState = np.zeros((self.N,self.N),dtype=int)
        a = []

        #create random array with distinct values in the range
        while(len(a) != self.N*self.N):
            n = random.randint(0,self.N*self.N-1)
            if not a.__contains__(n):
                a = a +[n]

        #copy the distinct array in matrix  
        index = 0
        for i in range(0,self.N):
            for j in range(0,self.N):
                initState[i][j] = a[index]
                index = index+1 
        return initState

    #Create goal state for N-puzzle
    def goalState(self):
        goal = np.zeros((self.N,self.N),dtype=int)
        index = 1
        for i in range(0,self.N):
            for j in range(0,self.N):
                goal[i][j] = index
                index = index+1
        goal[self.N-1][self.N-1] = 0
        return goal