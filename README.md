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

## CI/CD
This project uses GitHub Actions for CI/CD:
- Linting (ruff, black)
- Automated tests (pytest)
- Runs on every push and PR (see [.github/workflows/ci.yml](.github/workflows/ci.yml))

## Architecture
+-----------------------+
| Garage Telemetry |
+----------+------------+
|
v
+-----------------------+
| Data Ingest & |
| Feature Engineering |
+----------+------------+
|
v
+-----------------------+
| ML Model (LSTM AE) |
+----------+------------+
|
v
+-----------------------+
| FastAPI REST API |
+-----------------------+

- Data from the garage is parsed and engineered
- Passed through an LSTM autoencoder anomaly model
- Served via FastAPI endpoint for real-time prediction

## Test
`pytest`
