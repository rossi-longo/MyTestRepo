from binance.client import Client 
import datetime

from pandas import DataFrame as df

import key

import json

#installations:
#pip install python-binance
#install pandas




#Init the Client with API Key and Secret KEY - create on Binance

print("Start Init Client")

client = Client(key.pkey, key.skey)


print("Client successfully Initialized")



#Get Candle for specific Pair
print("Get candle for 'ETHTUSD'")

candle = client.get_klines(symbol = 'ETHTUSD', interval = Client.KLINE_INTERVAL_1HOUR)

CandleInDataframe = df(candle)

print(CandleInDataframe)




#Get Recent trades for specific Pair

print("Get Recent Trades for ETHTUSD")

trades = client.get_recent_trades(symbol = 'ETHTUSD')

print(df(trades))




#Get Ticker


print("Get Ticker")
ticker = client.get_ticker()

print(df(ticker))


#Get all Ticker

print("Get Prices for All Symbols")

allTicker = client.get_all_tickers()

print(df(allTicker))

myTest = allTicker



print()




