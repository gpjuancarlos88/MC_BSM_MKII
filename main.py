from src.gbm import monte_carlo
from src.analytics import BSM
from src.pricer import pricer
from src.config import S0, K, r, T, sigma

St = monte_carlo()
gbm_price, se = pricer()
BSM_price = BSM()
CI_D = gbm_price - 1.96*se
CI_U = gbm_price + 1.96*se

print(f'The option value using GBM is: {gbm_price}')
print(f'The option value using BSM is: {BSM_price}')
print(f'The standard error of the simulation is: {se}')
print(f'The 95% CI Interval for the option price is : [{CI_D} : {CI_U}]')