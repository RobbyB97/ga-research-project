"""
    Author: Robby Bergers

    This file is responsible for loading and displaying data
    gathered by the GA tests
"""

import os
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
        return


    def plot_file(self, filename, column=None):

        # Plot graph
        if column:
            x = pd.DataFrame.hist(data=self.data[filename], column=column, bins=20)
        else:
            x = pd.DataFrame.hist(data=self.data[filename], bins=20)

        self.plots.append(x)
        return


    def get_mean(self, filename, column):

        divisor = len(self.data[filename][column])
        total = 0
        for element in self.data[filename][column]:
            total += element

        avg = total/divisor
        return avg


    def show_data(self):
        plt.figure()
        plt.show()
        return
