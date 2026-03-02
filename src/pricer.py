import numpy as np
from .config import K, r, T

def pricer(ST):

    payoff = np.maximum(ST - K, 0)
    discounted_payoff = payoff * np.exp(-r * T)

    price = discounted_payoff.mean()
    se = discounted_payoff.std(ddof=1) / np.sqrt(len(discounted_payoff))

    return price, se