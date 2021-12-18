from creator import Creator
from Actuators import Actuators
import numpy as np
from Board import Board

#Create 8 puzzle
c = Creator(8)
x = c.initial_state()
# print(x)
# print(g)
# A=Actuators()
# res=A.move_up(arr)
# print(res)
# res2=A.move_up(res[1])
# print(res2)
# res3=A.move_down(res2[1])
# print(res3)
# res4=A.move_right(res3[1])
# print(res4)
# res5=A.move_left(res4[1])
# print(res5)

a = Board(3)
x = a.getBoard()
c = [[1,None,8],[3,6,2],[7,4,1]]
x = np.array(x)
c = np.array(c)
print(x)
print(c)
row , col = np.where(x == 6)
print(row[0])
print(col[0])
print(a.Hamming(c))