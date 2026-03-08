"""
Reusable data loading functions for the project.

Add project-specific loaders here. Import config paths via:
    from config import find_data, LOCAL_RAW, PROCESSED
"""
from pathlib import Path

import pandas as pd

from config import find_data, PROCESSED


def load_csv(filename: str, **kwargs) -> pd.DataFrame:
    """Load a CSV file from the raw data directory."""
    return pd.read_csv(find_data(filename), **kwargs)


def save_processed(df: pd.DataFrame, filename: str, **kwargs) -> Path:
    """Save a DataFrame to the processed data directory."""
    filepath = PROCESSED / filename
    df.to_csv(filepath, index=False, **kwargs)
    print(f"Saved: {filepath}")
    return filepath
