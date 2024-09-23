# Basic GET request
curl -X GET https://sheets.googleapis.com/v4/spreadsheets/1kDmxlJpwOgVEO3h9AStLyVYC3cYtzy30MqV0X2WqnL8?key={API_KEY}
# GET HTTP request with optional sheet and range parameters
curl -X GET https://sheets.googleapis.com/v4/spreadsheets/1kDmxlJpwOgVEO3h9AStLyVYC3cYtzy30MqV0X2WqnL8/values/data_leads!A1:D5?key={API_KEY}
# Get and store access token
echo $(curl -X POST \
 -d '{
        "token_uri": "https://oauth2.googleapis.com/token", 
        "refresh_token": "{REFRESH_TOKEN}"
 }' "https://developers.google.com/oauthplayground/refreshAccessToken") > token.json
# Write to Google sheet
curl -X POST \
  -H "Authorization: Bearer {ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
        "range": "Data!A1",
        "majorDimension": "ROWS",
        "values": [["New", "Word"]]
      }' \
  "https://sheets.googleapis.com/v4/spreadsheets/1WoJJcRpq8IOGaQZX_z2DtY6B_GeDuHmo0x-bDUPzxy4/values/Data!A1:append?valueInputOption=RAW"
$SHELL