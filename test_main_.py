from datetime import datetime

from fastapi.testclient import TestClient
from main import app, leap_year, leap_count, string_proc

client = TestClient(app)


def test_return_day():
    response = client.get("return/day")
    assert response.status_code == 200
    assert response.json() == "Wednesday"


def test_day_by_added_date_true():
    response = client.get("http://127.0.0.1:8000/DbaD?year=1&month=1&language=en")
    # response.json == {'year': 1, 'month': 1, 'language': "en"}
    assert response.status_code == 200
    assert response.json() == "Friday"


def test_day_by_date_true():
    response = client.post("http://127.0.0.1:8000/DbD?input_str=28%2F07%2F2020&language=en")
    assert response.status_code == 200
    assert response.json() == "Tuesday"


def test_leap_year():
    assert leap_year(2020) == True
    assert leap_year(2019) == False


def test_leap_count():
    assert leap_count(-40) == 10


def test_string_proc():
    d = datetime(2020, 7, 28)
    assert string_proc(d, "en") == "Tuesday"
