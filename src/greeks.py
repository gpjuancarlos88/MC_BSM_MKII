import numpy as np
from .config import S0, K, r, T, sigma

def delta(ST):

    indicator = (ST > K).astype(float)

    delta_paths = np.exp(-r * T) * indicator * (ST / S0)

    delta_est = delta_paths.mean()
    se = delta_paths.std(ddof=1) / np.sqrt(len(delta_paths))

    return delta_est, se


def vega(ST, Z):

    indicator = (ST > K).astype(float)

    dST_dsigma = ST * (-sigma * T + np.sqrt(T) * Z)

    vega_paths = np.exp(-r * T) * indicator * dST_dsigma

    vega_est = vega_paths.mean()
    se = vega_paths.std(ddof=1) / np.sqrt(len(vega_paths))

    return vega_est, se