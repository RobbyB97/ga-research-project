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
        self.datapath = datapath
        sns.set(color_codes=True)
        return


    def load_file(self, filename):
        os.chdir(self.datapath)

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
