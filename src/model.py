import numpy as np
import pandas as pd
from tensorflow.keras import layers, models
from typing import Tuple

def build_lstm_autoencoder(input_dim: int, timesteps: int) -> models.Model:
    model = models.Sequential([
        layers.LSTM(64, activation="relu", input_shape=(timesteps, input_dim), return_sequences=True),
        layers.LSTM(32, activation="relu", return_sequences=False),
        layers.RepeatVector(timesteps),
        layers.LSTM(32, activation="relu", return_sequences=True),
        layers.LSTM(64, activation="relu", return_sequences=True),
        layers.TimeDistributed(layers.Dense(input_dim))
    ])
    model.compile(optimizer="adam", loss="mse")
    return model

def fit_autoencoder(model: models.Model, X_train: np.ndarray, X_val: np.ndarray, epochs: int = 20) -> models.Model:
    model.fit(X_train, X_train, epochs=epochs, batch_size=16, validation_data=(X_val, X_val), verbose=2)
    return model

def predict_anomaly(model: models.Model, X: np.ndarray, threshold: float) -> np.ndarray:
    reconstructed = model.predict(X)
    loss = np.mean(np.square(X - reconstructed), axis=(1, 2))
    return (loss > threshold).astype(int)
