import binance_keys as keys
import csv
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(keys.BINANCEONE_KEY, keys.BINANCEONE_SECRET)

# get all symbol prices
prices = client.get_all_tickers()

# print(prices)

# for price in prices:
#     print(price)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# # print(candles)

# csvfile = open('15MinutesCandles.csv', 'w', newline='')

# candlestick_write = csv.writer(csvfile, delimiter=',')



# for candle in candles:
#     print(candle)
#     candlestick_write.writerow(candle)

# print(len(candles))

historical_candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2015", "1 Nov, 2021")

csvfile = open('01-2015_11-2021_BTCUSDT.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

for candle in historical_candlesticks:
    candlestick_writer.writerow(candle)

csvfile.close()

