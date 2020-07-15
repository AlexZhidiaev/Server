from datetime import datetime, date, timedelta
from fastapi import FastAPI
from time import time

import gettext
import os

app = FastAPI()


@app.get('/')
def home():
    return {"Гл.страница"}


@app.get('/return/day')
def returnday():
    return {datetime.now().strftime('%A')}

@app.post('/DbD')
def daybydate(dbd: date):
    return dbd.strftime('%A')

@app.get('/DbaD')
def daybyaddeddate(day: int, hour: int, minute: int, second: int):

    dn=datetime.now()+timedelta(days=day, hours=hour, minutes=minute, seconds=second)
    return dn.strftime('%A')

#@app.post('/dateadd')
