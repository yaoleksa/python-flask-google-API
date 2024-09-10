# A very simple Flask Hello World app for you to get started with...
from requests import get
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(get('https://api.monobank.ua/bank/currency').json())