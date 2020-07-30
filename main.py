import math
from datetime import datetime, date, timedelta
from time import time

import googletrans
from fastapi import FastAPI
from googletrans import Translator

app = FastAPI()


@app.get('/')
def home():
    return {"Гл.страница"}


@app.get('/return/day')
def return_day(language: str = 'en'):
    """
    Функция, возвращающая текущий день недели на сервере.
    :param language : язык возвращаемой строки в сокращенном формате.
    :return: строка, возвращающая день недели.
    """
    out: str = string_proc(datetime.now(), language)
    return out


@app.post('/DbD')
def day_by_date(input_str: str, language: str = 'en'):
    """
    Функция, возвращающая день недели указанного в параметрах дня.

    :param input_str: строка формата день/месяц/год.
    :param language : язык возвращаемой строки в сокращенном формате.
    :return: строка, возвращающая день недели.
    """
    input_arr = input_str.split("/")
    out_date: date = date(int(input_arr[2]), int(input_arr[1]), int(input_arr[0]))
    out: str = string_proc(out_date, language)
    return out


@app.get('/DbaD')
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
        day += math.fabs(year) * 365 + leap_count(year)
    else:
        return "год не может принимать такое значение"

    if month:
        week += month * 4

    dn = datetime.now() + timedelta(weeks=week, days=day, hours=hour, minutes=minute, seconds=second)
    out: str = string_proc(dn, language)
    return out


def leap_year(year: int):
    """
    Функция, возвращающая true или false в зависимости от викососности года.

    :param year: год, проверяемый на високосность.
    :return: истина, если викосоный, ложь, если нет.
    """
    if year:
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
    """
    Функция, возвращающая количество високосных лет за количество лет от текущего года, передаваемое в параметре

    :param year: количество лет от текущего, для которого нужно подсчитать число високосных
    :return: число високосных лет.
    """
    now = int(datetime.now().strftime('%Y'))
    count: int = 0
    if year >= 0:
        for i in range(now, now + year):
            if leap_year(i):
                count += 1
    elif year < 0:
        for i in range(now + year, now):
            if leap_year(i):
                count += 1
    return count


def string_proc(dt: datetime, language: str):
    """
    Функция, возвращающая строковое представление дня недели указанной даты.

    :param dt: дата, день недели которой требуется вернуть.
    :param language: язык, на который будет переведена строка
    :return:  строка, возвращающая день недели.
    """
    date_str: str = dt.strftime('%A')
    translator = Translator()
    if language in googletrans.LANGUAGES:
        date_str = translator.translate(date_str, dest=language).text
        return date_str
    else:
        return "Такого языка не существует"
