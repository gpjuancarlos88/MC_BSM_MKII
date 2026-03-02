import numpy as np
import time

from src.gbm import monte_carlo
from src.pricer import pricer
from src.greeks import delta, vega
from src.analytics import BSM, BSM_delta, BSM_vega


def run_single_experiment(n_paths):

    ST = monte_carlo(n_paths)
    price, se = pricer(ST)

    return price, se


def convergence_study():

    path_list = [10_000, 20_000, 50_000, 100_000, 200_000, 500_000]

    bs_price = BSM()

    print(f"Black–Scholes Price: {bs_price:.6f}\n")
    print("Paths | MC Price | Abs Error | Std Error | SE*sqrt(N)")
    print("-----------------------------------------------------")

    for N in path_list:

        start = time.time()
        mc_price, se = run_single_experiment(N)
        runtime = time.time() - start

        abs_error = abs(mc_price - bs_price)
        scaling_check = se * np.sqrt(N)

        print(f"{N:<7} {mc_price:.6f} {abs_error:.6f} {se:.6f} {scaling_check:.6f}")

def run(n_paths):

    ST, Z = monte_carlo(n_paths)

    price, price_se = pricer(ST)
    delta_mc, delta_se = delta(ST)
    vega_mc, vega_se = vega(ST, Z)

    price_bs = BSM()
    delta_bs = BSM_delta()
    vega_bs = BSM_vega()

    print(f"Paths: {n_paths}\n")

    print(f"Price MC: {price:.6f} | SE: {price_se:.6f}")
    print(f"Price BS: {price_bs:.6f}\n")

    print(f"Delta MC: {delta_mc:.6f} | SE: {delta_se:.6f}")
    print(f"Delta BS: {delta_bs:.6f}\n")

    print(f"Vega  MC: {vega_mc:.6f} | SE: {vega_se:.6f}")
    print(f"Vega  BS: {vega_bs:.6f}")



if __name__ == "__main__":
    convergence_study()
    run(200_000)