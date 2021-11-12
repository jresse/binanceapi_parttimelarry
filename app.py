from flask import Flask, render_template, request, flash, redirect
import binance_keys as keys
import csv
from binance import Client
from binance.enums import *

app = Flask(__name__)
client = Client(keys.BINANCEONE_KEY, keys.BINANCEONE_SECRET)
app.secret_key = b'bjkdslfdjkbinancekdlfjskfsjdl'

@app.route('/')
def index():
    title='CoinView'
    info = client.get_account()
    balances = info['balances']
    # print(balances)
    exchange_info = client.get_exchange_info()
    # print(exchange_info['symbols'])
    return render_template('index.html', title=title, my_balances=balances, symbols=exchange_info['symbols'])
    
@app.route('/watchlist')
def watchlist():
    prices = client.get_all_tickers()
    # exchange_info = client.get_exchange_info()
    # print(prices)
    return render_template('watchlist.html', list=prices)
        
@app.route('/buy', methods = ['POST'])
def buy():
    # print('Buying')
    print(request.form)
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
            flash(e.message, "error")

    return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'