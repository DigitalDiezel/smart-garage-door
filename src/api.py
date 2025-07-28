from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from src.config import Config
from src.feature_engineering import engineer_features
from src.predict import load_and_predict

app = FastAPI(title="Smart Garage Door Anomaly API")

class TelemetryRequest(BaseModel):
    timestamp: str
    state: int

@app.post("/predict")
def predict_telemetry(data: TelemetryRequest):
    try:
        df = pd.DataFrame([{"timestamp": data.timestamp, "state": data.state}])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = engineer_features(df)
        result = load_and_predict(df, Config.MODEL_PATH, threshold=0.2)
        return {"anomaly": int(result.iloc[0]["anomaly"]), "score": float(result.iloc[0]["anomaly_score"])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
