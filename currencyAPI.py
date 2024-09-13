# A very simple API call to Google Sheet
import pygsheets

import pandas as pd

from requests import get
from flask import Flask, request
from collections import defaultdict
from datetime import datetime, date

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():

    # define POST HTTP HANDLER
    if request.method == 'POST':
        today = date.today()
        update_from = datetime.strftime(today, '%Y-%m-%d')
        update_to = update_from
        data = request.get_json()
        if 'update_from' in data:
            update_from = data['update_from']
        if 'update_to' in data:
            update_to = data['update_to']
        update_from = str(update_from).replace('-', '')
        update_to = str(update_to).replace('-', '')
        # get currency rate for period
        exchange_rates = get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={update_from}&end={update_to}&valcode=usd&sort=exchangedate&order=desc&json').json()
        # data to insert into sheet
        to_insert = defaultdict(list)
        for item in exchange_rates:
            to_insert['exchangedate'].append(item['exchangedate'])
            to_insert['rate'].append(str(item['rate']).replace('.', ','))
        return to_insert

    return 'oki'
