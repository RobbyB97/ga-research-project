"""
    Author: Robby Bergers

    This class runs tests comparing the genetic algorithm to the random agent
"""



import logging
import os
import json
import time
from random import randint

from chessenv.board import Board
from galgorithm.ga import GA
from ra.ra import RA

log = logging.getLogger('GA_Project')

class GATest:


    def __init__(self, name='results'):

        # Attributes and flags
        self.name = name    # Name file to store results in
        self.ga_complete = False
        self.ga_attempts = 0
        self.final_ga_attempts = None
        return


    def current_time(self):
        return int(round(time.time() * 1000))


    def run_test(self):

        # Run GA
        self.ga_start_time = self.current_time()
        while not self.ga_complete:

            # First generation chromosomes
            first_gen = self.run_ga_test()
            if not first_gen:
                break
            first_fittest = self.fitness_function(batch=first_gen)

            # Splice and execute fittest 4 times (Second generation chromosomes)
            for i in range(4):
                test_chroms = self.splice(first_fittest)
                gen2 = self.run_ga_test(chromosomes=test_chroms)

            if not gen2:
                break
            else:
                second_fittest = self.fitness_function(batch=gen2)

            # Splice and execute fittest twice (Third generation chromosomes)
            for i in range(2):
                test_chroms = self.splice(second_fittest)
                self.run_ga_test(chromosomes=test_chroms)

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
                    self.final_ga_attempts = self.ga_attempts
                    self.ga_complete = True
                    return False
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
                    self.final_ga_attempts = self.ga_attempts
                    self.ga_complete = True
                    return
                else:
                    chromosome_list.append(x)

        # Return chromosome batch
        return chromosome_list


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

        # Return spliced chromosomes
        return spliced_chromosomes


    def fitness_function(self, batch, divisor=5):

        fittest = []        # List of fittest chromosomes

        # Give up on batch if it's too small
        if len(batch) <= 2:
            return False

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

            # Return fittest chromosomes
            return fittest


    def store_results(self):

        # Create dictionary with test data
        self.results = {}
        self.results['Name'] = self.name
        self.results['GA_Attempts'] = self.final_ga_attempts
        return
