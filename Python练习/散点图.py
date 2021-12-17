# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:54:32 2021

@author: kingb
"""

import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()#绘制区域默认111，一个区域
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')#randn正态分布生成横纵轴100个点，同时扩大十倍
ax.set_title('Simple Scatter')

plt.show()