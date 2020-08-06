from datetime import datetime
import googletrans
from googletrans import Translator
import urllib


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
    if connected():
        translator = Translator()
        if language in googletrans.LANGUAGES:
            date_str = translator.translate(date_str, dest=language).text
        else:
            date_str = "Такого языка не существует"
    return date_str


def connected(host: str = 'http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
