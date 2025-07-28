# Smart Garage Door Anomaly Detector

End-to-end Python project to collect, process, and detect anomalies in garage door telemetry using time-series ML.

- FastAPI REST API for real-time predictions
- Feature engineering and LSTM-based anomaly detection
- Unit tested and CI/CD enabled

## Setup
1. `python -m venv venv`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`

## Run API
`uvicorn src.api:app --reload`

## Test
`pytest`