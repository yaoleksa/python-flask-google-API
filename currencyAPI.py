# A very simple Flask Hello World app for you to get started with...
import pygsheets

import pandas as pd

from requests import get
from flask import Flask, jsonify
from datetime import date, datetime

app = Flask(__name__)

@app.route('/')
def hello_world():

    # init Google Sheets client
    client = (
        pygsheets
        .authorize(service_file='./currencyapi-435306-73cfd4ea9d84.json')
        .open_by_key('1kDmxlJpwOgVEO3h9AStLyVYC3cYtzy30MqV0X2WqnL8')
    )
    try:
        # get currency exchange rate
        exchange_rates = get('https://api.monobank.ua/bank/currency').json()
        dollar_exchange_rate = [rate for rate in exchange_rates if rate['currencyCodeA'] == 840]
        dollar = dollar_exchange_rate[0]
    except:
        return "Too many requests"
    
    # Create dataframe to write to sheet
    df = pd.DataFrame(data={
        'currency_name': 'Dollar US',
        'date': dollar['date'],
        'rateBuy': str(dollar['rateBuy']).replace('.', ','),
        'rateSell': str(dollar['rateSell']).replace('.', ','),
        'time': date.strftime(datetime.now(), '%d.%m.%y %H:%M:%S.%f')
    }, index=[0])

    # write currency info
    client[2].set_dataframe(df, (1, 1))
    
    return jsonify(exchange_rates)
