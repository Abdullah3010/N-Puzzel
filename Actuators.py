import math
import copy

class Actuators:

    def get_zero_index(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not board[i][j]:
                    x=i
                    y=j
        return x,y

    
    def move_up(self,board):
        emtpy_tile_index=self.get_zero_index(board)
        x=emtpy_tile_index[0]
        y=emtpy_tile_index[1]       
        check_bottom= (x == len(board)-1)

        if(not check_bottom):   # empty tile is not on the bottom
            board[x][y]=board[x+1][y]
            board[x+1][y]=None
            possible=True
        else:
            possible=False

        return possible, board

    
    
    def move_down(self,board):
        emtpy_tile_index=self.get_zero_index(board)
        x=emtpy_tile_index[0]
        y=emtpy_tile_index[1]    
        check_top = (x==0)

        if (not check_top):  # empty tile is not on the top
            board[x][y]=board[x-1][y]
            board[x-1][y]=None
            possible = True
        else:
            possible = False

        return possible, board

      
     

    def move_right(self,board):
        emtpy_tile_index=self.get_zero_index(board)
        x=emtpy_tile_index[0]
        y=emtpy_tile_index[1]    
        check_left = (y==0)

        if (not check_left):  # empty tile is not on the leftmost
           board[x][y]=board[x][y-1]
           board[x][y-1]=None
           possible = True
        else:
           possible = False

        return possible, board



    def move_left(self,board):
        emtpy_tile_index=self.get_zero_index(board)
        x=emtpy_tile_index[0]
        y=emtpy_tile_index[1]    
        check_right = (y== len(board)-1)

        if (not check_right):  #empty tile is not on the righmost
            board[x][y]=board[x][y+1]
            board[x][y+1]=None
            possible = True
        else:
            possible = False

        return possible, board

