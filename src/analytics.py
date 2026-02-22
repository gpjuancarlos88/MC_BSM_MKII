import numpy as np
from .config import S0, K, T, sigma, r
from scipy.stats import norm

def BSM():

    d1 = ((np.log(S0/K) + (r + 0.5*sigma**2))* T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    Call = S0*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

    return Call