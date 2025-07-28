import numpy as np
from src.model import build_lstm_autoencoder

def test_model_build():
    model = build_lstm_autoencoder(input_dim=4, timesteps=1)
    assert model.input_shape == (None, 1, 4)
