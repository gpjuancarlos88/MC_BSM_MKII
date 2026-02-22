import numpy as np
from .config import S0, r, sigma, T, n_paths, seed

def monte_carlo():

    ## The underlying is assumed to follow GBM under the risk neutral measure:
    ## dSt = rStdt + sigmaStdWt; drift = risk free rate
    ## Closed form solution: S_T = S0exp((r-1/2sigma^2)T + sigma*sqrt(T)Z)

    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(n_paths)
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    return S_T