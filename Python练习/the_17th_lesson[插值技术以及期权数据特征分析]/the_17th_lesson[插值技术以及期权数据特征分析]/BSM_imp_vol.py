#%%
# Black-Scholes-Merton (1973) European Call & Put Valuation
#
import math
from scipy.optimize import fsolve
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import quad
import mpl_toolkits.mplot3d.axes3d as p3
mpl.rcParams['font.family'] = 'serif'

#
# Helper Functions
#
def dN(x):
    ''' Probability density function of standard normal random variable x. '''
    return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)


def N(d):
    ''' Cumulative density function of standard normal random variable x. '''
    return quad(lambda x: dN(x), -20, d, limit=50)[0]


def d1f(St, K, t, r, sigma):
    ''' Black-Scholes-Merton d1 function.
        Parameters see e.g. BSM_call_value function. '''
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
          * t) / (sigma * math.sqrt(t))
    return d1

#
# Valuation Functions
#
def BSM_call_value(St, K,t, r, sigma):
    ''' Calculates Black-Scholes-Merton European call option value.

    Parameters
    ==========
    St : float
        stock/index level at time t
    K : float
        strike price
    t : float
        年化的到期时间     
    r : float
        constant, risk-less short rate
    sigma : float
        volatility

    Returns
    =======
    call_value : float
        European call present value at t
    '''
    d1 = d1f(St, K, t, r, sigma)
    d2 = d1 - sigma * math.sqrt(t)
    call_value = St * N(d1) - math.exp(-r * (t)) * K * N(d2)
    return call_value


def BSM_put_value(St, K, t, r, sigma):
    ''' Calculates Black-Scholes-Merton European put option value.

    Parameters
    ==========
    St : float
        stock/index level at time t
    K : float
        strike price
    t : float
        valuation date
    T : float
        年化的到期时间
    r : float
        constant, risk-less short rate
    sigma : float
        volatility

    Returns
    =======
    put_value : float
        European put present value at t
    '''
    put_value = BSM_call_value(St, K, t, r, sigma) \
        - St + math.exp(-r * t) * K
    return put_value


#
# get implied volatility Functions
#
def get_imp_vol(S, K, t, r,p,otype='call',sigma_est=0.2):
    '''  Return implied volatility given option price.
    Parameters
    ==========
    S : 标的价格
    K : 执行价格
    T : 年化的到期时间
    r : 无风险利率
    p : 期权价格
    otype : 期权类型， either 'call' or 'put', 默认为'call'
    sigma_est:初始的波动率
    '''
    def difference(sigma):
        if( otype == 'call' ):
            optionValue = BSM_call_value(S, K, t, r, sigma);
        else:
            optionValue = BSM_put_value(S, K, t, r, sigma);
            
        return optionValue - p ;

    iv = fsolve(difference, sigma_est)[0];
    return iv;


    
    
# ######################################################################
# # 下面是周宏成添加演示的例子，用于向东财的研究生讲解期权波动率的基本性质
# ###########################################################################    
S0 = 7514.46  
T = np.array((21., 49., 140., 231., 322.)) / 365.  # call option maturities
r = [0.0124, 0.0132, 0.015, 0.019, 0.0214]  # approx. short rates

# May 2011
K = np.array((7000, 7050, 7100, 7150, 7200, 7250, 7300, 7350, 7400, 7450,
          7500, 7550, 7600, 7650, 7700, 7750, 7800, 7850, 7900, 7950, 8000))
C1 = np.array((530.8, 482.9, 435.2, 388.5, 342.5, 297.8, 254.8, 213.7, 175.4,
          140.2, 108.7, 81.6, 59, 41.2, 27.9, 18.5, 12.1, 7.9, 5.1, 3.4, 2.3))

# June 2011
C2 = np.array((568.9, 524.5, 481.1, 438.7, 397.3, 357.5, 318.9, 281.9, 247, 214,
          183.3, 155.1, 129.3, 106.3, 86.1, 68.8, 54.1, 42, 32.2, 24.5, 18.4))

# Sep 2011
C3 = np.array((697.1, 657.9, 619.5, 581.8, 544.9, 509.1, 474.2, 440, 407.2, 375.4,
          344.8, 315.3, 287.5, 260.6, 235.5, 211.5, 189, 168, 148.8, 130.7,
          114.2))

# Dec 2011
C4 = np.array((811.5, 774.4, 737.9, 702.1, 666.9, 632.3, 598.5, 565.6, 533.5,
          502.1, 471.6, 442.1, 413.2, 385.6, 359, 333.2, 308.4, 284.9, 262.4,
          240.9, 220.4))

# Mar 2012
C5 = np.array((921.3, 885.4, 849.8, 814.7, 780.1, 746.6, 713.4, 680.8, 648.9,
          617.7, 587.1, 557.4, 528.6, 500.2, 472.6, 446, 419.9, 395, 370.4,
          347.1, 324.6))

# #%%

#
# BSM Implied Volatilities
#
imv1 = []
imv2 = []
imv3 = []
imv4 = []
imv5 = []
for j in range(len(K)):
    imv1.append(get_imp_vol(S0, K[j], T[0], r[0], C1[j],'call', 0.2))
    imv2.append(get_imp_vol(S0, K[j], T[1], r[1], C2[j],'call', 0.2))
    imv3.append(get_imp_vol(S0, K[j], T[2], r[2], C3[j],'call', 0.2))
    imv4.append(get_imp_vol(S0, K[j], T[3], r[3], C4[j],'call', 0.2))
    imv5.append(get_imp_vol(S0, K[j], T[4], r[4], C5[j],'call', 0.2))

imv1 = np.array(imv1)
imv2 = np.array(imv2)
imv3 = np.array(imv3)
imv4 = np.array(imv4)
imv5 = np.array(imv5)
imv = np.array((imv1, imv2, imv3, imv4, imv5))

#
# Graphical Output
#
## 2d Output
plt.figure()
plt.plot(K, imv[0] * 100, 'ro')
plt.plot(K, imv[1] * 100, 'gx')
plt.plot(K, imv[2] * 100, 'bv')
plt.plot(K, imv[3] * 100, 'yD')
plt.plot(K, imv[4] * 100, 'mh')
plt.grid(True)
plt.xlabel('Strike')
plt.ylabel('Implied Volatility')
plt.show()
#%%

## 3d Output
k, t = np.meshgrid(K, T)
fig = plt.figure()
plot = p3.Axes3D(fig)
plot.plot_wireframe(k, t, imv)
plot.set_xlabel('K')
plot.set_ylabel('T')
plot.set_zlabel('Implied Volatility')