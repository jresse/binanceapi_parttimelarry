import backtrader as bt

class RSIStratergy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):

        if self.rsi < 30 and not self.position:
            self.buy()

        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()
cerebro.broker.setcash(1000000000)

# data = bt.feeds.GenericCSVData(dataname='01-2015_11-2021_BTCUSDT_Daily.csv', dtformat=2)
data = bt.feeds.GenericCSVData(dataname='2021_BTCUSDT_15Minutes.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes)

cerebro.adddata(data)
cerebro.addstrategy(RSIStratergy)

cerebro.run()


cerebro.plot()

