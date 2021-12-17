#%%
#
# European Call Option Inner Value Plot
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Option Strike
K = 3000

# Graphical Output
S = np.linspace(2500, 3500, 100)  # index level values


# inner value of European call option
plt.figure();
hcall = np.maximum(S - K, 0)  # inner values of call option
plt.plot(S, hcall, lw=2.5)  # plot inner values at maturity
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of European call option')
plt.grid(True)
plt.show()


# inner value of European put option
plt.figure()
hput = np.maximum(K-S, 0)  # inner values of call option
plt.plot(S, hput, lw=2.5)  # plot inner values at maturity
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of European put option')
plt.grid(True)
plt.show()

#%%




