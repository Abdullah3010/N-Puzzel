# from creator import Creator
# from Actuators import Actuators
# import numpy as np
# from Board import Board
# from GUI import makeMove
#Create 8 puzzle
# c = Creator(8)
# x = c.initial_state()
# print(x)
# print(g)
# A=Actuators()


# a = Board(3)
# x = a.getBoard()
# c = [[1,4,7],[2,6,5],[3,None,8]]
# x = np.array(x)
# c = np.array(c)
# print(x)
# print(c)
# row , col = np.where(x == 6)
# print(row[0])
# print(col[0])
# print('-----------------')
# res=A.move_up(c)
# print(res[1])
# print('-----------------')
# res2=A.move_up(res[1])
# print(res2[1])
# print('-----------------')
# res3=A.move_down(res2[1])
# print(res3[1])
# print('-----------------')
# res4=A.move_right(res3[1])
# print(res4[1])
# print('-----------------')
# res5=A.move_left(res4[1])
# print(res5[1])

# print(a.Permutation(c))
# print(c)
# print(makeMove(c,'up'))

# s = {}
#
#
# for i in range(5):
#     s[i] = [i+1]
#     print(s)
#
# from GUI import GUI
#
# def main():
#     GUI()
#
# if __name__ == '__main__':
#     main()

SearchSpace = {0: [[[1, 4, 7], [2, None, 8], [3, 5, 6]], 3, None, -1], 1: [[[1, 4, 7], [2, 8, None], [3, 5, 6]], 3, 'up', 0], 2: [[[1, 4, 7], [None, 2, 8], [3, 5, 6]], 3, 'down', 0], 3: [[[1, 4, 7], [2, 5, 8], [3, None, 6]], 3, 'left', 0], 4: [[[1, None, 7], [2, 4, 8], [3, 5, 6]], 3, 'right', 0], 5: [[[1, 4, 7], [2, 5, 8], [3, 6, None]], 2, 'up', 3], 6: [[[1, 4, 7], [2, 5, 8], [None, 3, 6]], 2, 'down', 3]}

def getSolution():  # space is searchspace map of keys : [0:state, 1:heuristec value, 2:lastmove, 3:parentState key]
    solution = list()
    laststate = SearchSpace.popitem()
    key = laststate[1][3]
    solution.append(laststate[1][2])
    print(key)
    print(solution)
    while True:
        if (SearchSpace.get(key))[3] == -1:
            print(solution)
            return solution
        solution.append(SearchSpace.get(key)[2])
        print(solution)
        key = SearchSpace.get(key)[3]
        print(key)
        print('*'*30)

getSolution()