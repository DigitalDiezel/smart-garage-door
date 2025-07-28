import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

def load_and_predict(df: pd.DataFrame, model_path: str, threshold: float) -> pd.DataFrame:
    model = load_model(model_path)
    feature_cols = ["delta", "hour", "dayofweek", "rolling_mean"]
    X = df[feature_cols].values
    X = X.reshape((X.shape[0], 1, X.shape[1]))
    reconstructed = model.predict(X)
    loss = np.mean(np.square(X - reconstructed), axis=(1, 2))
    df["anomaly_score"] = loss
    df["anomaly"] = (loss > threshold).astype(int)
    return df
