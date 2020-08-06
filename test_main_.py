from datetime import datetime

from fastapi.testclient import TestClient
import functions
import main

client = TestClient(main.app)


def test_return_day():
    response = client.get("return/day")
    assert response.status_code == 200
    assert response.json() == main.return_day


def test_day_by_added_date_true():
    response = client.get("http://127.0.0.1:8000/DbaD?year=1&month=1&language=en")
    # response.json == {'year': 1, 'month': 1, 'language': "en"}
    assert response.status_code == 200
    assert response.json() == main.day_by_added_date(1, 1)


def test_day_by_date_true():
    response = client.post("http://127.0.0.1:8000/DbD?input_str=28%2F07%2F2020&language=en")
    assert response.status_code == 200
    assert response.json() == main.day_by_date('28/07/2020')


def test_leap_year():
    assert functions.leap_year(2020) == True
    assert functions.leap_year(2019) == False


def test_leap_count():
    assert functions.leap_count(-40) == 10


def test_string_proc():
    d = datetime(2020, 7, 28)
    assert functions.string_proc(d, "en") == "Tuesday"
