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
from test.gatest import GATest

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



def run_trials(trial_num=10):

    trials = []

    # Run trials
    for i in range(11,13):
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


if __name__ == '__main__':
