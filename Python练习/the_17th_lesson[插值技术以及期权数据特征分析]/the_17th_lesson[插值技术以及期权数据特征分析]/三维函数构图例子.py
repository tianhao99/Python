# -*- coding: utf-8 -*-
"""
参考：
https://matplotlib.org/users/pyplot_tutorial.html

"""

#%%
import numpy as np
import matplotlib as mpl
from pylab import plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn')
import statsmodels.api as sm
mpl.rcParams['font.family'] = 'serif'


##############################################################
#1.三维函数构图例子
###############################################################
def fm(p):
    x, y = p
    return np.sin(x) + 0.25 * x + np.sqrt(y) + 0.05 * y ** 2

x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)


# generates 2-d grids out of the 1-d arrays
Z = fm((X, Y))

fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=mpl.cm.coolwarm,
        linewidth=0.5, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
fig.colorbar(surf, shrink=0.5, aspect=5)

#%%