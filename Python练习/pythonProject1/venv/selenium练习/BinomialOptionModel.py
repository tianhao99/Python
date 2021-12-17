###############################################################
# Cox-Ross-Rubinstein Binomial Model
# American Option Valuation and impl_vol
#
# 注意：
# 本代码是周宏成为了给东北财经大学的研究生上课时准备的案例，
# 请不要用作它途
###############################################################

import math
import numpy as np
from scipy.optimize import fsolve


# Valuation Function
def getOptionValue(S0, K, T, r, sigma, otype, M=500):
    ''' Cox-Ross-Rubinstein american option valuation.

    Parameters
    ==========
    S0 : float
        stock/index level at time 0
    K : float
        strike price
    T : float
        date of maturity
    r : float
        constant, risk-less short rate
    sigma : float
        volatility
    otype : string
        either 'call' or 'put'
    M : int
        number of time intervals
    '''
    # Time Parameters
    dt = T / M  # length of time interval
    df = math.exp(-r * dt)  # discount per interval

    # Binomial Parameters
    u = math.exp(sigma * math.sqrt(dt))  # up movement
    d = 1 / u  # down movement
    q = (math.exp(r * dt) - d) / (u - d)  # martingale branch probability

    # Array Initialization for Index Levels
    mu = np.arange(M + 1)
    mu = np.resize(mu, (M + 1, M + 1))
    md = np.transpose(mu)
    mu = u ** np.triu((mu - md),1)
    md = d ** np.triu(md,1)
    S = S0 * mu * md

    # Inner Values
    if otype == 'call':
        V = np.maximum(S - K, 0)  # inner values
    else:
        V = np.maximum(K - S, 0)  # inner values


    # 因为美式期权需要比对内涵价值与计算出来的计算价值的大小
    # 所以需要保留最初计算的内涵价值
    Inner_V = np.copy(V);
    #<--

    z = 0
    for t in range(M - 1, -1, -1):  # backwards iteration
        V[0:M - z, t] = (q * V[0:M - z, t + 1] +
                         (1 - q) * V[1:M - z + 1, t + 1]) * df

        # 因为需要考虑提前执行的可能性，、
        # 所以美式期权需要在内涵价值和根据倒推步骤计算出的期权价值之间做比较
        # 取两者中的较大值作为期权价格
        for i in range(0,M-z):
            if(V[i,t]<Inner_V[i,t]):
                V[i, t] = Inner_V[i,t] ;
        z += 1
    return V[0, 0]

def getImpliedVolatility(S0, K, T, r,optionPrice,otype,M=500,sigma_est=0.2):
    '''  Return implied volatility given option price.
    Parameters
    ==========
    S0 : float
        stock/index level at time 0
    K : float
        strike price
    T : float
        date of maturity
    r : float
        constant, risk-less short rate
    optionPrice : float
        the option price from market
    otype : string
        either 'call' or 'put'
    M : int
        number of time intervals
    sigma_est:float
        the first step sigma
    '''
    def difference(sigma):
        optionValue = getOptionValue(S0, K, T, r, sigma, otype, M);
        return optionValue - optionPrice ;

    iv = fsolve(difference, sigma_est)[0];
    return iv;


# if __name__ == '__main__':
#     # just for test
#     S0 = 110.0  # index level
#     K = 100.0  # option strike
#     T = 1.0  # maturity date
#     r = 0.05  # risk-less short rate
#     sigma = 0.3  # volatility
#     callPrice = getOptionValue(S0, K, T, r, sigma, 'call', M=500);
#     print('call optionPrice=', callPrice);

#     callIV = getImpliedVolatility(S0, K, T, r, callPrice, 'call', M=500, sigma_est=0.2);
#     print('call implied volatility=', callIV);

#     putPrice = getOptionValue(S0, K, T, r, sigma, 'put', M=500);
#     print('put optionPrice=', putPrice);

#     putIV = getImpliedVolatility(S0, K, T, r, putPrice, 'put', M=500, sigma_est=0.2);
#     print('put implied volatility=', putIV);
