from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Якщо потрібно доступ до редагування Google Sheets, обирай ці області доступу (scopes)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Запусти процес авторизації OAuth 2.0
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret_152465323366-u4cscn9cqpkfm7k5h3akuhdhknartmmo.apps.googleusercontent.com.json', SCOPES)  # 'credentials.json' це файл з OAuth 2.0 даними
creds = flow.run_local_server(port=0)

# Збереження токену для подальшого використання
with open('token.json', 'w') as token:
    token.write(creds.to_json())

# Створи сервіс для роботи з Google Sheets API
service = build('sheets', 'v4', credentials=creds)

# ID таблиці та діапазон, у який будемо записувати дані
spreadsheet_id = '1WoJJcRpq8IOGaQZX_z2DtY6B_GeDuHmo0x-bDUPzxy4'
range_name = 'Data!A1'
value_input_option = 'RAW'
values = [
    ['Hello', 'World'],  # Дані, які записуємо в таблицю
]

body = {
    'values': values
}

result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range_name,
    valueInputOption=value_input_option, body=body).execute()

print(f"{result.get('updatedCells')} cells updated.")
