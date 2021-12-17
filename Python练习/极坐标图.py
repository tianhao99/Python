# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:43:21 2021

@author: kingb
"""

import numpy as np
import matplotlib.pyplot as plt
N = 10
theta = np.linspace(0.0,2*np.pi,N,endpoint=False)
radii = 10*np.random.rand(N)
width = np.pi/2*np.random.rand(N)

ax = plt.subplot(111,projection='polar')#绘制区域111，一个区域
bars = ax.bar(theta,radii,width=width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/20.))
    bar.set_alpha(0.9)
plt.show()
