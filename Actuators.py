import math
import copy

class Actuators:


    def move_up(self,arr):
        row_size=int(math.sqrt(len(arr) + 1))
        emtpy_tile_index = arr.index(0)
        result = copy.deepcopy(arr)
        
        if(not (emtpy_tile_index >= (len(arr) - row_size))):  # empty tile is not on the bottom
             underlying_tile_index = emtpy_tile_index + row_size
             underlying_tile = arr[underlying_tile_index]
             result[emtpy_tile_index] = underlying_tile
             result[underlying_tile_index] = 0
             possible = True

        else:
             possible = False

        return possible, result
        
      
            
    def move_down(self,arr):
        row_size=int(math.sqrt(len(arr) + 1))
        emtpy_tile_index = arr.index(0)
        result = copy.deepcopy(arr)

        if (not (emtpy_tile_index < row_size)):  # empty tile is not on the top
            above_tile_index = emtpy_tile_index - row_size
            underlying_tile = arr[above_tile_index]
            result[emtpy_tile_index] = underlying_tile
            result[above_tile_index] = 0
            possible = True
        else:
            possible = False

        return possible, result



    def move_left(self,arr):
        row_size=int(math.sqrt(len(arr) + 1))
        emtpy_tile_index = arr.index(0)
        result = copy.deepcopy(arr)

        if (not(emtpy_tile_index % row_size == row_size - 1)):  #empty tile is not on the righmost
            right_tile_index = emtpy_tile_index + 1
            right_tile = arr[right_tile_index]
            result[emtpy_tile_index] = right_tile
            result[right_tile_index] = 0
            possible = True
        else:
            possible = False

        return possible, result


   
    def move_right(self,arr):
        row_size=int(math.sqrt(len(arr) + 1))
        emtpy_tile_index = arr.index(0)
        result = copy.deepcopy(arr)

        if (not(emtpy_tile_index %  row_size == 0)):  # empty tile is not on the leftmost
           right_tile_index= emtpy_tile_index - 1
           right_tile = arr[right_tile_index]
           result[emtpy_tile_index] = right_tile
           result[right_tile_index] = 0
           possible = True
        else:
           possible = False

        return possible, result







    # def is_possible(self,direction,arr):

    #     row_size=int(math.sqrt(len(arr) + 1))
    #     index_of_emtpy_tile = arr.index(0)

    #     if direction=="up":
    #         return (index_of_emtpy_tile >= (len(arr) - row_size))
    #     if direction=="down":
    #         return (index_of_emtpy_tile < row_size)
    #     if direction=="right":
    #         return (index_of_emtpy_tile % row_size == 0)
    #     if direction=="left":
    #         return (index_of_emtpy_tile % row_size == row_size - 1)
    


    # for i in range(len(arr)):
    #     for j in range(len(arr[0])):
    #         if arr[i][j]==0:
    #             x=i
    #             y=j
    



    