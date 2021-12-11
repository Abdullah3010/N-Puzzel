from creator import Creator

#Create 8 puzzle
c = Creator(15)
x = c.initial_state()
g = c.goalState()
print(x)
print(g)

