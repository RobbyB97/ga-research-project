"""
    Author: Robby Bergers

    This is the main file for testing Genetic Algorithms.
"""

import logging
import os
from chessenv.board import Board
from galgorithm.ga import GA
import time

# Set logger
log = logging.getLogger('GA_Project')
log.setLevel(logging.INFO)
handlerpath = os.path.dirname(os.path.realpath(__file__)) + '/app.log'
handler = logging.FileHandler(handlerpath)
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)
log.info('Running file ~/main/app.py:')



def current_time():
    return int(round(time.time() * 1000))


def ga_test():

    info = {}       # Dictionary containing all GA testing data

    # First generation
    info['firstgen'] = {}
    log.info('Running first generation of chromosomes...')
    info['firstgen']['start_time'] = current_time()
    info['firstgen']['algorithms'] = execGA()
    info['firstgen']['fittest'] = fitness_one(batch=info['firstgen']['algorithms'])

    newChrom = recombine(info['firstgen']['fittest'])

    # Second generation
    info['secondgen'] = {}
    log.info('Running second generations of chromosomes...')
    return

""" Create, execute and return set of chromosomes """
def execGA(num=100, chromosome=None):

    batch = []
    solve = False       # Flag for whether or not solution is found

    # Execute chromosome on chess environment
    for i in range(num):
        if chromosome:
            x = GA(chromosome)
        else:
            x = GA()

        # Check whether or not current chromosome achieves goal state
        solve = x.try_chromosome()
        batch.append(x)
    return batch


""" Randomly Scramble and return list of chromosomes """
def recombine(ga):

    chromosomes = []        # List of recombined chromosomes to be returned
    galen = len(ga)
    return chromosomes


""" First fitness function, returns list of fittest chromosomes """
def fitness_one(batch, divisor=5):

    fittest = []        # List of fittest chromosomes

    # Get number of chromosomes to return
    crop = len(batch)/5
    for i in range(int(crop)):
        fitness = 100
        possible = []

        # Find set number of fittest chromosomes from initial list
        for object in batch:
            if object.env.conflicts < fitness:
                fitness = object.env.conflicts
                possible.append(object)

        # Convert fittest chromosome to flat list
        possible.sort(key=lambda x: x.env.conflicts, reverse=False)
        batch.pop(batch.index(possible[0]))
        log.info('Fitness: %s conflicts' % possible[0].env.conflicts)
        chrom = []  # Chromosome to be appended to fittest list
        for gene in possible[0].chromosome:
            for num in gene:
                chrom.append(num)
        fittest.append(chrom)
    return fittest


if __name__ == '__main__':
