import os

class Config:
    MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
    MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
    MQTT_TOPIC = os.getenv("MQTT_TOPIC", "garage/door/telemetry")
    MODEL_PATH = os.getenv("MODEL_PATH", "src/model_lstm_autoencoder.h5")
