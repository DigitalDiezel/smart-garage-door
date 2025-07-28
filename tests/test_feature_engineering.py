import pandas as pd
from src.feature_engineering import engineer_features

def test_engineer_features():
    df = pd.DataFrame({
        "timestamp": pd.date_range("2024-07-08", periods=10, freq="T"),
        "state": [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
    })
    out = engineer_features(df)
    assert "delta" in out.columns
    assert "hour" in out.columns
    assert "rolling_mean" in out.columns
