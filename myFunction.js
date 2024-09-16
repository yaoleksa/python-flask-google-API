function myFunction() {
  // Clear previous result
  SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('A:B').clearContent();
  // Get raw date values
  const raw_update_from = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('G2').getValues().toString();
  const raw_update_to = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('G3').getValues().toString();
  // Fetch params from sheet
  const update_from = raw_update_from.length > 0 ? new Date(raw_update_from).toISOString().split('T')[0].replace(/\-/g, '') : new Date().toISOString().split('T')[0].replace(/\-/g, '');
  const update_to = raw_update_to.length > 0 ? new Date(raw_update_to).toISOString().split('T')[0].replace(/\-/g, '') : new Date().toISOString().split('T')[0].replace(/\-/g, '');
  const apiKey = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('G4').getValues().toString();
  if(apiKey.length < 1) {
    SpreadsheetApp.getActiveSpreadsheet().getSheetByName(["exchange_rate"]).getRange('A1').setValue('Missing API KEY');
    return;
  }
  // call to my API
  console.log(UrlFetchApp.fetch(`https://yaoleksa.pythonanywhere.com/?update_from=${update_from}&update_to=${update_to}`, {
    'method': 'post',
    'headers': {
      "X-API-Key": apiKey
    }
  }).getContentText());
}