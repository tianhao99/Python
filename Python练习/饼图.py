# -*- coding: utf-8 -*-
"""
Created on Sat May 22 08:37:41 2021

@author: kingb
"""

import matplotlib.pyplot as plt
labels = 'dogs','pigs','horse','fish'
sizes = [15,20,60,5]
explode = [0,0,0.1,0]

plt.pie(sizes,explode = explode,labels=labels,autopct='%1.1f%%',
        shadow=True,startangle=90)
plt.axis('equal')
plt.show()