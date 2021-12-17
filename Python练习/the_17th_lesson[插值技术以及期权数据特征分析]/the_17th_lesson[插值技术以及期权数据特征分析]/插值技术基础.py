# -*- coding: utf-8 -*-
"""
本例子演示使用插值工具的使用方法
技术参考：
https://blog.csdn.net/qq_31347869/article/details/100916017
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splrep.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html
https://www.cnblogs.com/duye/p/8671820.html
"""
#%%
import numpy as np
import scipy.interpolate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'



def f(x):
    return np.sin(x) + 0.5 * x
x = np.linspace(-2 * np.pi, 2 * np.pi, 25)

#splrep 函数计算出 B-spline曲线的参数
#参数k为拟合度
ipo = spi.splrep(x, f(x), k=1)
#从ipo中获取对应的值
iy = spi.splev(x, ipo)
plt.figure()
plt.plot(x, f(x), 'b.', label='f(x)')
plt.plot(x, iy, 'r', label='interpolation')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')


#%%
# 将局部放大后看插值结果
plt.figure()
xd = np.linspace(1.0, 3.0, 50)
iyd = spi.splev(xd, ipo)
plt.plot(xd, f(xd), 'b.', label='f(x)')
plt.plot(xd, iyd, 'r', label='interpolation')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

#%%
#提高插值的拟合度后，重新拟合
plt.figure()
ipo = spi.splrep(x, f(x), k=3)
iyd = spi.splev(xd, ipo)
plt.plot(xd, f(xd), 'b.', label='f(x)')
plt.plot(xd, iyd, 'r', label='interpolation')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

#%%
#用于判断是否每个值都相等
np.allclose(f(xd), iyd)
#用于判断误差大小
np.sum((f(xd) - iyd) ** 2) / len(xd)
#%%

