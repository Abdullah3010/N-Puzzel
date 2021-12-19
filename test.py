from creator import Creator
from Actuators import Actuators
import numpy as np
from Board import Board
from GUI import makeMove
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

s = {}


for i in range(5):
    s[i] = [i+1]
    print(s)