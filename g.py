import pygsheets
import pandas as pd

client = (
    pygsheets
    .authorize(service_file='./currencyapi-435306-73cfd4ea9d84.json')
    .open_by_key('14nKyYCD0SOunCobchyeXjuaxAWyUpOjf_AMu6_swcrs')
)

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

client[2].set_dataframe(df, (1, 1))