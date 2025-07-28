import pandas as pd
from typing import Tuple

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["delta"] = df["timestamp"].diff().dt.total_seconds().fillna(0)
    df["hour"] = df["timestamp"].dt.hour
    df["dayofweek"] = df["timestamp"].dt.dayofweek
    df["rolling_mean"] = df["state"].rolling(window=5, min_periods=1).mean()
    return df

def train_val_split(df: pd.DataFrame, val_ratio: float = 0.2) -> Tuple[pd.DataFrame, pd.DataFrame]:
    idx = int(len(df) * (1 - val_ratio))
    return df.iloc[:idx], df.iloc[idx:]
