# import time
# import pandas as pd
# import pandas_ta as ta
import ccxt

exchange = ccxt.kraken()

# get numbers of candle
def get_ohlcv(symbol, interval='1m', limit=1):
    # headers
    # columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

    # get candles from exchange
    bars = exchange.fetch_ohlcv(symbol, timeframe=interval, limit=limit,)

    return bars

dataframe = get_ohlcv('BTC/USDT')

print(dataframe[0][-2])


