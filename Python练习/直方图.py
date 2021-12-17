# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:17:22 2021

@author: kingb
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu,sigma = 100,20     #均值和标准差
a = np.random.normal(mu,sigma,size=100)

plt.hist(a,30,density=True,histtype='stepfilled',facecolor='r',alpha=0.75)
plt.title('Histrogram')

plt.show()