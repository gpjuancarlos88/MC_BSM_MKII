from pathlib import Path

Data_Dir = Path(r"C:\Users\Omen\quant\data")

Data_filename = input("Enter the filename (AAPL_DATA.xksx)")

Data_Path = Data_Dir / Data_filename

S0 = 100.0
K = 100.0
r = 0.05
sigma = 0.20
T = 1.0

n_paths = 100_000
seed = 42
use_antithetic = True

##if __name__ == "__main__":



