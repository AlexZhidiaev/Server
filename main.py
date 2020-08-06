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
def return_day_app(language: str = 'en'):
    return functions.return_day(language)


@app.post('/day/byDate')
def day_by_date_app(input_str: str, language: str = 'en'):
    return functions.day_by_date(input_str, language)


@app.get('/day/byAddedDate')
def day_by_added_date_app(year: int = 0, month: int = 0, week: int = 0, day: int = 0, hour: int = 0, minute: int = 0,
                          second: int = 0, language: str = 'en'):

    return functions.day_by_added_date(year, month, week, day,  hour, minute,
                                       second, language)
