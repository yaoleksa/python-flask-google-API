# A very simple Flask Hello World app for you to get started with...
import pygsheets

import pandas as pd

from requests import get
from datetime import date, datetime

CURRENT_TIME = date.strftime(datetime.now(), '%d.%m.%y %H:%M:%S.%f')

# init Google Sheets client
client = (
    pygsheets
    .authorize(service_file='./currencyapi-435306-73cfd4ea9d84.json')
    .open_by_key('14nKyYCD0SOunCobchyeXjuaxAWyUpOjf_AMu6_swcrs')
)

# get currency exchange rate
exchange_rates = get('https://api.monobank.ua/bank/currency').json()
dollar_exchange_rate = [rate for rate in exchange_rates if rate['currencyCodeA'] == 840]
dollar = dollar_exchange_rate[0]

# Create dataframe to write to sheet
df = pd.DataFrame(data={
    'currency_name': 'Dollar US',
    'date': dollar['date'],
    'rateBuy': dollar['rateBuy'],
    'rateSell': dollar['rateSell'],
    'time': CURRENT_TIME
}, index=[0])

# write currency info
client[2].set_dataframe(df, (1, 1))