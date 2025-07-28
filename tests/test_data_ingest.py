import pytest
from src.data_ingest import parse_telemetry
from datetime import datetime

def test_parse_telemetry_good():
    payload = {"timestamp": "2024-07-08T17:35:20", "state": 1}
    out = parse_telemetry(payload)
    assert out["state"] == 1
    assert isinstance(out["timestamp"], datetime)

def test_parse_telemetry_bad():
    payload = {"timestamp": "bad", "state": "up"}
    with pytest.raises(Exception):
        parse_telemetry(payload)
