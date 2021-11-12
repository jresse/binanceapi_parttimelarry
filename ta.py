import talib
import numpy

from numpy import genfromtxt

data = genfromtxt('15MinutesCandles.csv', delimiter=',')
# print(data)

close = data[:,4]
# print(close)

# close = numpy.random.random(100)
# print(close)

# sma = talib.SMA(close)
# print(sma)


rsi = talib.RSI(close)
print(rsi)