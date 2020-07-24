from datetime import datetime, date, timedelta

from fastapi import FastAPI

from googletrans import Translator

app = FastAPI()


@app.get('/')
def home():
    return {"Гл.страница"}


@app.get('/return/day')
def return_day():
    """
    Функция, возвращающая текущий день недели на сервере.

    :return: строка, возвращающая день недели.
    """
    out: str = string_proc(datetime.now)
    return out


@app.post('/DbD')
def day_by_date(input_str: str):
    """
    Функция, возвращающая день недели указанного в параметрах дня.

    :param input_str: строка формата день/месяц/год.
    :return: строка, возвращающая день недели.
    """
    input_arr = input_str.split("/")
    out_date: date = date(int(input_arr[2]), int(input_arr[1]), int(input_arr[0]))
    out: str = string_proc(out_date)
    return out


@app.get('/DbaD')
def day_by_added_date(year: int = 0, month: int = 0, week: int = 0, day: int = 0, hour: int = 0, minute: int = 0,
                      second: int = 0):
    """
    Функция, возвращающая день недели через указанное в параметрах время от текущей даты.

    :param year: год.
    :param month: месяц.
    :param week: неделя.
    :param day: день.
    :param hour: час.
    :param minute: минуты.
    :param second: секунды.
    :return: строка, возвращающая день недели .
    """
    if year:
        day += year * 365 + leap_count(year)
    if month:
        week += month * 4

    dn = datetime.now() + timedelta(weeks=week, days=day, hours=hour, minutes=minute, seconds=second)
    out: str = string_proc(dn)
    return out


def leap_year(year: int):
    """
    Функция, возвращающая true или false в зависимости от викососности года.

    :param year: год, проверяемый на високосность.
    :return: истина, если викосоный, ложь, если нет.
    """
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
    """
    Функция, возвращающая количество високосных лет в интервале от текущего до указанного в параметре года.

    :param year: год, до которого нужно подсчитать количество високосных.
    :return: число високосных лет.
    """
    now = int(datetime.now().strftime('%Y'))
    count: int = 0
    for i in range(now, now + year):
        if leap_year(i):
            count += 1
    return count


def string_proc(date: datetime):
    """
    Функция, возвращающая строковое представление дня недели указанной даты.

    :param date: дата, день недели которой требуется вернуть.
    :return:  строка, возвращающая день недели.
    """
    date_str: str = date.strftime('%A')
    return date_str
