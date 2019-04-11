"""
    Author: Robby Bergers

    This is the main file for testing Genetic Algorithms.
"""

import logging
import os
import json
import time
from random import randint

from chessenv.board import Board
from galgorithm.ga import GA
from ra.ra import RA

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

        # Attributes and flags
        self.name = name    # Name file to store results in
        self.ga_complete = False
        self.ra_complete = False
        self.ga_attempts = 0
        self.ra_attempts = 0
        return


    def current_time(self):
        return int(round(time.time() * 1000))


    def run_test(self):

        # Run tests
        self.ga_start_time = self.current_time()
        while not self.ga_complete:
            self.run_ga_test()
        self.ga_total_time = self.ga_end_time - self.ga_start_time

        self.ra_start_time = self.current_time()
        while not self.ra_complete:
            self.run_ra_test()
        self.ra_total_time = self.ra_end_time - self.ra_start_time

        # Return results
        self.store_results()
        return


    def run_ga_test(self, size=8, chromosomes=None):

        chromosome_list = []

        # If this is first-gen
        if not chromosomes:
            self.ga_first_gen = True

            # Create first batch of chromosomes
            for i in range(100):
                x = GA(size=size)
                self.ga_attempts += 1
                x.try_chromosome()

                # Check if goal state found
                if x.complete:
                    self.ga_end_time = self.current_time()
                    log.info('GA Solution found after %s attempts' % str(self.ga_attempts))
                    self.ga_complete = True
                    return
                else:
                    chromosome_list.append(x)

        else:
            self.ga_first_gen = False

            # Run each chromosome
            for chromosome in chromosomes:
                x = GA(size=size, chromosome=chromosome)
                self.ga_attempts += 1
                x.try_chromosome()

                # Check if goal state found
                if x.complete:
                    self.ga_end_time = x.end_time
                    log.info('GA Solution found after %s attempts' % str(self.ga_attempts))
                    self.ga_complete = True
                    return
                else:
                    chromosome_list.append(x)

        # Get fittest chromosomes
        return self.fitness_function(batch=chromosome_list)


    def splice(self, chromosomes):

        unspliced_chromosomes = []
        spliced_chromosomes = []

        # Convert list of chromosomes to embedded lists
        for chromosome in chromosomes:
            new_chromosome = []
            for i in range(0, len(chromosome), 2):
                new_chromosome.append(chromosome[i:i+2])
            unspliced_chromosomes.append(new_chromosome)

        # Splice chromosomes
        for i in range(int(len(unspliced_chromosomes)/2)):

            # Pick two chromosomes at random
            pick_one = randint(0, len(unspliced_chromosomes)-1)
            chromosome_one = unspliced_chromosomes[pick_one]
            unspliced_chromosomes.pop(pick_one)
            pick_two = randint(0, len(unspliced_chromosomes)-1)
            chromosome_two = unspliced_chromosomes[pick_two]
            unspliced_chromosomes.pop(pick_two)

            # Create fragments
            upper_left = []
            upper_right = []
            lower_left = []
            lower_right = []
            cutting_point = randint(1, len(chromosome_one)-1)
            for gene in chromosome_one:
                if chromosome_one.index(gene) < cutting_point:
                    upper_left.append(gene)
                else:
                    lower_right.append(gene)

            for gene in chromosome_two:
                if chromosome_two.index(gene) < cutting_point:
                    lower_left.append(gene)
                else:
                    upper_right.append(gene)

            # Create spliced chromosomes and append to spliced list
            spliced_one = []
            spliced_two = []
            for gene in upper_left:
                spliced_one.append(gene)
            for gene in upper_right:
                spliced_one.append(gene)
            for gene in lower_left:
                spliced_two.append(gene)
            for gene in lower_right:
                spliced_two.append(gene)

            spliced_chromosomes.append(spliced_one)
            spliced_chromosomes.append(spliced_two)
        return self.run_ga_test(chromosomes=spliced_chromosomes)


    def run_ra_test(self, size=8):

        # Run instance of random agent
        self.ra_attempts += 1
        x = RA()
        x.run()

        # Check if goal state found
        if x.complete:
            self.ra_end_time = self.current_time()
            log.info('RA Solution found after %s attempts' % str(self.ra_attempts))
            self.ra_complete = True
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

        # Create dictionary with test data
        self.results = {}
        self.results['Name'] = self.name
        self.results['GA_Attempts'] = self.ga_attempts
        self.results['RA_Attempts'] = self.ra_attempts
        self.results['GA_Total_Time'] = self.ga_total_time
        self.results['RA_Total_Time'] = self.ra_total_time
        return



if __name__ == '__main__':

    trials = []

    # Run trials
    for i in range(10):
        x = GATest(name=str(i))
        x.run_test()
        trials.append(x)

    # Store data
    if not os.path.exists('results'):
        os.makedirs('results')
    os.chdir('results')
    for trial in trials:
        json_object = json.dumps(trial.results, sort_keys=True, indent=4)
        with open('%s.json' % trial.name, 'w+') as f:
            f.write(json_object)
