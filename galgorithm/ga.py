"""

"""

import logging
import os
from chessenv.board import Board
from random import randint

log = logging.getLogger('GA_Project')



class GA:


    def __init__(self, chromosome=None, size=8):

        # Set attributes
        self.size = size
        self.env = Board(width=size, height=size)
        if chromosome:
            self.chromosome = chromosome
        else:
            self.make_chromosome()
        return


    # Create chromosome for first gen GA
    def make_chromosome(self):

        chromosome = []
        for i in range(self.size):
            gene = [i, randint(0, self.size-1)]
            chromosome.append(gene)
