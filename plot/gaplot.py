

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


class GAPlotter:


    def __init__(self, datapath):
        self.datapath = datapath
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
