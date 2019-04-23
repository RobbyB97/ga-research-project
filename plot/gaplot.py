"""
    Author: Robby Bergers

    This file is responsible for loading and displaying data
    gathered by the GA tests
"""

import logging

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

log = logging.getLogger('GA_Project')

class GAPlotter:


    def __init__(self, datapath):

        # Configure packages and variables
        self.datapath = datapath
        self.data = {}  # Dictionary for storing data
        self.plots = []     # List of plotted graphs
        sns.set(color_codes=True)
        return


    def load_file(self, filename, column=None):

        # Read file into data dictionary
        os.chdir(self.datapath)
        self.data[filename] = pd.read_csv('%s.csv' % filename)

        # Plot graph
        if column:
            self.plots.append(pd.DataFrame.hist(data=self.data[filename], column=column))
        else:
            self.plots.append(pd.DataFrame.hist(data=self.data[filename]))
        return


    def show_data(self):
        plt.show()
        return
"""
os.chdir('trials')
sns.set(color_codes=True)
os.chdir('trials')
ran = pd.read_csv('random_agent.csv')
print(ran.keys())
y = pd.DataFrame.hist(data=ran, column='Attempts')
plt.show()
"""
