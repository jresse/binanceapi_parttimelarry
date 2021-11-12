from flask import Flask, render_template
import binance_keys as keys
import csv
from binance import Client
from binance.enums import *

app = Flask(__name__)
client = Client(keys.BINANCEONE_KEY, keys.BINANCEONE_SECRET)

@app.route('/')
def index():
    title='CoinView'
    info = client.get_account()
    balances = info['balances']
    # print(balances)
    return render_template('index.html', title=title, my_balances=balances)
    
@app.route('/watchlist')
def watchlist():
    prices = client.get_all_tickers()
    print(prices)
    return render_template('watchlist.html', list=prices)
        
@app.route('/buy')
def buy():
    order = client.create_order(
        symbol='LTC',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=100,
        price='0.00001')  

    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'