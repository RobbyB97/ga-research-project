"""
    Author: Robby Bergers

    This is the main file for testing Genetic Algorithms.
"""

import logging
import os
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



def execGA(num=100):

    batch = []
    for i in range(num):
        x = GA()
        x.try_chromosome()
        batch.append(x)
    return batch

def fitness_one(batch, divisor=5):

    fittest = []
    crop = len(batch)/5
    for i in range(int(crop)):
        fitness = 100
        possible = []
        for object in batch:
            if object.env.conflicts < fitness:
                fitness = object.env.conflicts
                possible.append(object)
        possible.sort(key=lambda x: x.env.conflicts, reverse=True)
        fittest.append(possible[0])
    return fittest

if __name__ == '__main__':

    # Storage
    info = {}
    info['firstgen'] = {}
    info['firstgen']['algorithms'] = execGA()
    info['firstgen']['fittest'] = fitness_one(batch=info['firstgen']['algorithms'])

    print(len(info['firstgen']['fittest']))
