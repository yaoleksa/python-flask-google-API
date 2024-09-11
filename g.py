import pandas as pd
import pygsheets
import requests

client = (
    pygsheets
    .authorize(service_file='./currencyapi-435306-73cfd4ea9d84.json')
    .open_by_key('14nKyYCD0SOunCobchyeXjuaxAWyUpOjf_AMu6_swcrs')
)

# get currency exchange rate
exchange_rates = requests.get('https://api.monobank.ua/bank/currency').json()
dollar_exchange_rate = [rate for rate in exchange_rates if rate['currencyCodeA'] == 840]
dollar = dollar_exchange_rate[0]

# Create empty dataframe
df = pd.DataFrame(data={
    'currency_name': 'Dollar US',
    'date': dollar['date'],
    'rateBuy': dollar['rateBuy'],
    'rateSell': dollar['rateSell']
}, index=[0])

client[2].set_dataframe(df, (1, 1))