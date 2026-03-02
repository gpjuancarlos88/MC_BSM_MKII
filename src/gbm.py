import numpy as np
from .config import S0, r, sigma, T, seed

def monte_carlo(n_paths):

    rng = np.random.default_rng(seed)

    Z_half = rng.standard_normal(n_paths // 2)
    Z_full = np.concatenate([Z_half, -Z_half])

    ST = S0 * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z_full
    )

    return ST, Z_full