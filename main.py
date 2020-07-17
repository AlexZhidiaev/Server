from datetime import datetime, date, timedelta
from time import time
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"Гл.страница"}


@app.get('/return/day')
def return_day():
    return {datetime.now().strftime('%A')}


@app.post('/DbD')
def day_by_date(input_str: str):
    input_arr = input_str.split("/")
    out_date: date = date(int(input_arr[2]), int(input_arr[1]), int(input_arr[0]))
    return out_date.strftime('%A')


@app.get('/DbaD')
def day_by_added_date(year: int = 0, month: int = 0, week: int = 0, day: int = 0, hour: int = 0, minute: int = 0,
                      second: int = 0):
    if year:
        day += year*365 + leap_count(year)
    if month:
        week += month * 4

    dn = datetime.now() + timedelta(weeks=week, days=day, hours=hour, minutes=minute, seconds=second)
    return dn.strftime('%A')


def leap_year(year: int):
    if 0 < year < 9999:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


def leap_count(year: int):
    now = int(datetime.now().strftime('%Y'))
    count: int = 0
    for i in range(now, now + year):
        if leap_year(i):
            count += 1
    return count

