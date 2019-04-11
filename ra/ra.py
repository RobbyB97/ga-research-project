"""
    Author: Robby Bergers

    This class runs a random agent to solve the toy problem
"""

import logging
import os
import time
from random import randint

from chessenv.board import Board

log = logging.getLogger('GA_Project')



class RA:


    def __init__(self, size=8):

        # Set attributes
        self.complete = False
        self.size = size
        self.env = Board(width=size, height=size)
        return


    def current_time(self):
        return int(round(time.time() * 1000))


    def run(self):

        # Place queens randomly
        self.solution = []
        for i in range(self.size):
            col = randint(0, self.size-1)
            self.env.place_queen(row=i, column=col)
            self.solution.append([i, col])

        # Store completion data if goal state achieved
        if not self.env.conflicts:
            log.info('RA Found solution: %s' % self.solution)
            self.complete = True
            self.end_time = self.current_time()
            self.env.print_board()
