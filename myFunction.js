function myFunction() {
  // Clear previous result
  SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('A:B').clearContent();
  // Fetch params from sheet
  const update_from = new Date(SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('G2').getValues()).toISOString().split('T')[0].replace(/\-/g, '');
  const update_to = new Date(SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('G3').getValues()).toISOString().split('T')[0].replace(/\-/g, '');
  const apiKey = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('G4').getValues()[0][0]
  console.log(`https://yaoleksa.pythonanywhere.com/?update_from${update_from}&update_to=${update_to}`)
  // call to my API
  console.log(UrlFetchApp.fetch(`https://yaoleksa.pythonanywhere.com/?update_from=${update_from}&update_to=${update_to}`, {
    'method': 'post',
    'headers': {
      "X-API-Key": apiKey
    }
  }).getContentText());
}