from creator import Creator
from Actuators import Actuators

#Create 8 puzzle
# c = Creator(15)
# x = c.initial_state()
# g = c.goalState()
# print(x)
# print(g)

board=[[1,2,3],
       [4,0,5],
       [6,7,8]]

A=Actuators()

res=A.move_up(board)
print(board)
res2=A.move_up(res[1])
print(res2)
res3=A.move_down(res2[1])
print(res3)
res4=A.move_right(res3[1])
print(res4)
res5=A.move_left(res4[1])
print(res5)


