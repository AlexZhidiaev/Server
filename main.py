import math
from datetime import datetime, date, timedelta
from time import time

import googletrans
from fastapi import FastAPI
from googletrans import Translator
import functions

app = FastAPI()


@app.get('/')
def home():
    return {"Главная страница"}


@app.get('/return/day')
def return_day(language: str = 'en'):
    """
    Функция, возвращающая текущий день недели на сервере.
    :param language : язык возвращаемой строки в сокращенном формате.
    :return: строка, возвращающая день недели.
    """
    out: str = functions.string_proc(datetime.now(), language)
    return out


@app.post('/day/byDate')
def day_by_date(input_str: str, language: str = 'en'):
    """
    Функция, возвращающая день недели указанного в параметрах дня.

    :param input_str: строка формата день/месяц/год.
    :param language : язык возвращаемой строки в сокращенном формате.
    :return: строка, возвращающая день недели.
    """
    input_arr = input_str.split("/")
    out_date: date = date(int(input_arr[2]), int(input_arr[1]), int(input_arr[0]))
    out: str = functions.string_proc(out_date, language)
    return out


@app.get('/day/byAddedDate')
def day_by_added_date(year: int = 0, month: int = 0, week: int = 0, day: int = 0, hour: int = 0, minute: int = 0,
                      second: int = 0, language: str = 'en'):
    """
    Функция, возвращающая день недели через указанное в параметрах время от текущей даты.

    :param year: год.
    :param month: месяц.
    :param week: неделя.
    :param day: день.
    :param hour: час.
    :param minute: минуты.
    :param second: секунды.
    :param language: язык возвращаемой строки в сокращенном формате
    :return: строка, возвращающая день недели .
    """
    if math.fabs(year) < 7980:
        day += math.fabs(year) * 365 + functions.leap_count(year)
    else:
        return "год не может принимать такое значение"

    if month:
        week += month * 4

    dn = datetime.now() + timedelta(weeks=week, days=day, hours=hour, minutes=minute, seconds=second)
    out: str = functions.string_proc(dn, language)
    return out



