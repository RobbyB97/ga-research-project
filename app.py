"""
    Author: Robby Bergers

    This is the main file for testing Genetic Algorithms.
"""

import logging
import os
import json
import time

from chessenv.board import Board
from galgorithm.ga import GA

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



class GATest:


    def __init__(self, name='results'):

        self.attempts = 0   # Keep track of number of solve attempts
        self.name = name    # Name file to store results in
        self.ga_complete = False
        self.ra_complete = False
        self.ga_attempts = 0
        self.ra_attemps = 0
        return


    def current_time(self):
        return int(round(time.time() * 1000))


    def run_test(self):

        # Run tests
        while not self.ga_complete:
            self.run_ga_test()
            if not self.ga_complete:
                log.info('GA thread did not yield goal state. Restarting...')

        self.run_ra_test()

        # Return results
        self.store_results()
        return


    def run_ga_test(self, size=8, chromosomes=None):

        chromosome_list = []

        # If this is first-gen
        if not chromosomes:

            # Create first batch of chromosomes
            for i in range(100):
                x = GA(size=size)
                self.ga_attempts += 1
                x.try_chromosome()

                # Check if goal state found
                if x.complete:
                    self.ga_complete = True
                    return
                else:
                    chromosome_list.append(x)

        else:

            # Run each chromosome
            for chromosome in chromosomes:
                x = GA(size=size, chromosome=chromosome)
                self.ga_attempts += 1
                x.try_chromosome()

                # Check if goal state found
                if x.complete:
                    log.info('GA Solution found after %s attempts' % str(self.ga_attempts))
                    self.ga_complete = True
                    return
                else:
                    chromosome_list.append(x)

        # Get fittest chromosomes
        return self.fitness_function(batch=chromosome_list)


    def splice(self, chromosomes):

        chromosome_list = []        # Spliced chromosomes to be returned

        # Convert list of chromosomes to embedded lists
        for chromosome in chromosomes:
            new_chromosome = []
            for i in range(0, len(chromosome), 2):
                new_chromosome.append(chromosome[i:i+2])

            chromosome_list.append(new_chromosome)

        log.info('%s genes to be spliced' % len(chromosome_list))

        return self.run_ga_test(chromosomes=chromosome_list)


    def run_ra_test(self, size=8):
        return


    def fitness_function(self, batch, divisor=5):

        fittest = []        # List of fittest chromosomes

        # Give up on batch if it's too small
        if len(batch) <= 10:
            return

        else:

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
                chrom = []  # Chromosome to be appended to fittest list
                for gene in possible[0].chromosome:
                    for num in gene:
                        chrom.append(num)
                fittest.append(chrom)
            return self.splice(chromosomes=fittest)


    def store_results(self):
        with open('%s.txt' % self.name, 'w+') as f:
            f.write('%s RESULTS:' % self.name)
            f.write('--------------------------------')
            f.write('GA Attempts before goal state: %s' % self.ga_attempts)
        return



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

    trial_one = GATest(name='trial_one')
    trial_one.run_test()
