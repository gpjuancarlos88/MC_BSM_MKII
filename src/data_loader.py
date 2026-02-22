import pandas as pd
from pathlib import Path
from .config import Data_Path


def load_price_data() -> pd.DataFrame:
    """
    Loads price data from the external data directory.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the Excel data.
    """

    if not Data_Path.exists():
        raise FileNotFoundError(
            f"Data file not found at: {Data_Path}"
        )

    try:
        df = pd.read_excel(Data_Path)
    except Exception as e:
        raise RuntimeError(
            f"Failed to load Excel file at {Data_Path}: {e}"
        )

    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    return df