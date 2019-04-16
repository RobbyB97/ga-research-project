"""
    Author: Robby Bergers

    This is the main file for testing Genetic Algorithms.
"""

import logging
import os
import json
import time
from random import randint
import csv

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

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



def run_trials(trial_num=100, name='results'):

    # Create CSV file and write header
    os.chdir('results')
    with open('%s.csv' % name, 'w') as f:
        f.write('Trial,RA Attempts,GA Attempts,Num. of trials\n')

    # Run trial and get results
    first_trial = True
    for i in range(trial_num):
        x = GATest(name=str(i))
        x.run_test()

        # Append results to file
        with open('%s.csv' % name, 'a') as f:
            if first_trial:
                f.write('%s,%s,%s,%s\n' % (x.results['Name'], x.results['GA_Attempts'], x.results['RA_Attempts'], trial_num))
                first_trial = False
            else:
                f.write('%s,%s,%s\n' % (x.results['Name'], x.results['GA_Attempts'], x.results['RA_Attempts']))
    return


def json_to_csv(name='results'):

    # Create CSV file and write header
    os.chdir('results')
    with open('%s.csv' % name, 'w') as f:
        f.write('Trial,RA Attempts,GA Attempts,RA Average,GA Average,Num. of trials\n')

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
        trial_number = 1
        for object in json_objects:
            if set_averages:
                f.write('%s,%s,%s\n' % (trial_number, object['RA_Attempts'], object['GA_Attempts']))
            else:
                f.write('%s,%s,%s,%s,%s,%s\n' % (trial_number, object['RA_Attempts'], object['GA_Attempts'], averages['RA'], averages['GA'], averages['Trials']))
                set_averages = True
            trial_number += 1
    return


def get_ra_csv():

    # Import data
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir('trials')
    with open('results.csv', 'r') as f:
        reader = csv.reader(f)
        mydict= {rows[0]:rows[1] for rows in reader}

    # Write to file
    with open('random_agent.csv', 'w') as f:
        for element in mydict:
            try:
                x = int(element)
                f.write('%s,%s\n' % (element, mydict[element]))
            except:
                log.debug('Incompatible row')

    # Return to main directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    return


def get_trial_one_csv():

    # Import data
    with open('results.csv', 'r') as f:
        reader = csv.reader(f)
        mydict= {rows[0]:rows[2] for rows in reader}

    # Write to file
    with open('ga_trial_one.csv', 'w') as f:
        for element in mydict:
            try:
                x = int(element)
                f.write('%s,%s\n' % (element, mydict[element]))
            except:
                log.debug('Incompatible row')

    # Return to main directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    return


if __name__ == '__main__':
