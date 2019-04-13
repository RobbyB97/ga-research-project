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

    # Return to root directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    return


def json_to_csv(name='results'):

    # Create CSV file and write header
    os.chdir('results')
    with open('%s.csv' % name, 'w') as f:
        f.write('RA Attempts,GA Attempts,RA Average,GA Average,Num. of trials\n')

    # Dictionary to store data for averages
    averages = {}
    averages['GA'] = 0
    averages['RA'] = 0
    averages['Trials'] = 0

    # Get all json objects
    json_objects = []
    for file in os.listdir(os.getcwd()):
        if '.json' in file:
            with open(file, 'r') as f:
                 json_object = json.loads(f.read())
            json_objects.append(json_object)

    # Calculate averages
    for object in json_objects:
        averages['GA'] += object['GA_Attempts']
        averages['RA'] += object['RA_Attempts']
        averages['Trials'] += 1
    averages['GA'] /= averages['Trials']
    averages['GA'] = int(averages['GA'])
    averages['RA'] /= averages['Trials']
    averages['RA'] = int(averages['RA'])


    # Add data to csv
    with open('%s.csv' % name, 'a') as f:
        set_averages = False
        for object in json_objects:
            if set_averages:
                f.write('%s,%s\n' % (object['RA_Attempts'], object['GA_Attempts']))
            else:
                f.write('%s,%s,%s,%s,%s\n' % (object['RA_Attempts'], object['GA_Attempts'], averages['RA'], averages['GA'], averages['Trials']))
                set_averages = True
    return

if __name__ == '__main__':
    json_to_csv()
