# Specifications for the checkers.py file:
# 1 point: The checkers.py file must import only the items from the numpy library required,
# using the “from” import construct.
import numpy as np
from numpy import random
# 1 point: This app must use two files, a main (called main.py) and
# a second one called checkers.py containing a function for generating a game board.
# 1 point: The checkers.py file must contain a function called build_board which takes a parameter
# representing the size of the board; e.g. if 3 is passed in, the function will generate a 3x3 board. The function will then use numpy to populate each cell of the board randomly with one of the following strings: ‘Empty’, ‘Red’, ‘Black’. The function will then return the newly created board.

def build_board(board_size):
    board=random.choice(['Empty','Red', 'Black'], size=(board_size,board_size))
    return board
# 1 point: The checkers.py file must contain a function called get_count which takes two parameters:
# A board and a string of either Empty, Red, or Black. It will return how many of that item exists in the board.
def get_count(board,bSquare):
    grid=(board==bSquare)
    return grid.sum()

# 1 point: The checkers.py file must check if it’s running as a main,
# and if so print out a message stating the file is not intended to be run as a main.

if __name__=="__main__":
    print("This file can't be run as a main file")
























