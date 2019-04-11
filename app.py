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
    for i in range(trial_num):
        x = GATest(name=str(i))
        x.run_test()
        trials.append(x)
    return trials


def store_results(results):

    # Store data
    if not os.path.exists('results'):
        os.makedirs('results')
    os.chdir('results')
    for result in results:
        json_object = json.dumps(result.results, sort_keys=True, indent=4)
        with open('%s.json' % result.name, 'w+') as f:
            f.write(json_object)
    return


if __name__ == '__main__':
    data = run_trials(100)
    store_results(data)
