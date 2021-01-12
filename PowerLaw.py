# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:20:04 2021
Power Law
@author: Roy
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto
#scale
x_m = 1
#list of values of shape parameters 
alpha = [0.5, 1.16, 3] 
samples = np.linspace(start=0, stop=7, num=1000)
for a in alpha:
    output = np.array([pareto.pdf(x=samples, b=a, loc=0, scale=x_m)])
    plt.plot(samples, output.T, label='alpha {0}' .format(a))
plt.xlabel('samples', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.title('Probability Density function', fontsize=15)
plt.grid(b=True, color='grey', alpha=0.3, linestyle='--', linewidth=1)
plt.rcParams["figure.figsize"] = [8, 5]
plt.legend(loc='best')
plt.xlim([1.01, 7])