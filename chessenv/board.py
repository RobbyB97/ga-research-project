"""


"""

import logging
import os

log = logging.getLogger('GA_Project')



class Board:


    def __init__(self, width=8, height=8):

        # Attributes
        self.board = []     # Board matrix
        # [0 = empty 1 = possible queen path, 2 = queen, 3 = queen in path]
        self.width = width
        self.height = height
        self.queens = []    # Locations of queens on matrix
        self.conflicts = 0      # Number of queens placed in path of other queen

        # Create row
        for i in range(height):
            row = []
            for i in range(width):
                row.append(0)
            self.board.append(row)
        return


    def print_board(self):

        if self.conflicts:
            conflicts = 'This board has %s conflicts\n' % self.conflicts
        else:
            conflicts = 'This board has no conflicts\n'

        board = ''
        for row in self.board:
            board = board + str(row) + '\n'
            
        log.info('Current board status: \n %s%s\n\n\n' % (conflicts, board))
        return


    """ Place queen on board matrix, check if queen crosses other queen path """
    def place_queen(self, row, column):

        # Set vertical path
        for rows in self.board:
            if rows[column] == 2:
                self.conflicts += 1
            else:
                rows[column] = 1

        # Set horizontal path
        for i in range(self.width):
            if self.board[row][i] == 2:
                self.conflicts += 1
            else:
                self.board[row][i] = 1

        path = []

        # Set upper-left diagonal path
        startrow = row
        startcol = column
        while startrow != 0 and startcol != 0:
            startrow -= 1
            startcol -= 1
            path.append([startrow, startcol])

        # Set upper-right diagonal path
        startrow = row
        startcol = column
        while startrow != 0 and startcol < self.width - 1:
            startrow -= 1
            startcol += 1
            path.append([startrow, startcol])

        # Set lower-right diagonal path
        startrow = row
        startcol = column
        while startrow < self.height - 1 and startcol < self.width - 1:
            startrow += 1
            startcol += 1
            path.append([startrow, startcol])

        # Set lower-left diagonal path
        startrow = row
        startcol = column
        while startrow < self.height - 1 and startcol != 0:
            startrow += 1
            startcol -= 1
            path.append([startrow, startcol])

        # Write diagonal paths to matrix
        for paths in path:
            x = paths[0]
            y = paths[1]
            if self.board[x][y] == 2:
                self.conflicts += 1
            else:
                self.board[x][y] = 1

        # Place queen
        self.board[row][column] = 2
        return
