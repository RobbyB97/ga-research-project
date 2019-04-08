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
        self.complete = False
        self.env = Board(width=size, height=size)
        if chromosome:
            self.chromosome = chromosome
        else:
            self.chromosome = self.make_chromosome()
        return


    def try_chromosome(self):

        for gene in self.chromosome:
            self.env.place_queen(row=gene[0], column=gene[1])

        self.env.print_board()


    def make_chromosome(self):

        # Create chromosome for first gen GA
        chromosome = []
        for i in range(self.size):
            gene = [i, randint(0, self.size-1)]
            chromosome.append(gene)
        return chromosome