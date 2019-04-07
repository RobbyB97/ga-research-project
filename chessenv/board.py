"""


"""

import logging
import os

log = logging.getLogger('GA_Project')



class Board:


    def __init__(self, width=8, height=8):

        # Attributes
        self.board = []     # Board matrix [0 = empty, 1 = possible queen path, 2 = queen]
        self.queens = []    # Locations of queens on matrix

        # Create row
        row = []
        for i in range(width):
            row.append(0)

        # Create empty board
        for i in range(height):
            self.board.append(row)
        return


    def print_board(self):
        message = 'Current board status: \n'
        for row in self.board:
            message = message + str(row) + '\n'
        log.info(message)
        return


    def place_queen(self, row, column):
        return
