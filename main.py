import Binance
from binance.client import Client 
import key

import pandas
import json

import datetime


from pyti.smoothed_moving_average import smoothed_moving_average as sma

#Fiktiver smoothedMovingAverage - 5%
PriceIWantToBuy = 9100

#Init the Client with API Key and Secret KEY - create on Binance

print("Start Init Client")

myClientBinance = Client(key.pkey, key.skey)


print("Client successfully Initialized")

print("Accepted Price: " + str(PriceIWantToBuy))





#print("Actual Price: " + myTrades[0]["price"])


#myHistoricData = myClientBinance.get_historical_trades(symbol = "BTCTUSD", limit = 500)

#print(myHistoricData)

while True:

    print("Asking price at" + str(datetime.datetime.now()))
    myTrades = Binance.getTrades(myClientBinance, "BTCUSDT", 10)

   

    if float(myTrades[0]["price"]) < PriceIWantToBuy:
        print("Lets buy That ShitCoin at " + str(myTrades[0]["price"]))
        break

    else:
        print(str(myTrades[0]["time"]) + ": The Coin is still to expensive at "+ str(myTrades[0]["price"]))
        


