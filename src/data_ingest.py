import pandas as pd
from datetime import datetime
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

def parse_telemetry(payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        ts = datetime.fromisoformat(payload["timestamp"])
        state = int(payload["state"])
        return {"timestamp": ts, "state": state}
    except (KeyError, ValueError) as e:
        logger.error(f"Bad payload: {payload} | {e}")
        raise

def load_telemetry_log(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, parse_dates=["timestamp"])
    assert "state" in df.columns
    return df.sort_values("timestamp")
