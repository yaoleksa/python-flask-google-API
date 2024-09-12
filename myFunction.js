function myFunction() {
    // call to my API
    return UrlFetchApp.fetch('https://yaoleksa.pythonanywhere.com/').getContent();
  }