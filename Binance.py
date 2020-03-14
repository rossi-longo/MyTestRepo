
import datetime

from pandas import DataFrame as df



import json

#installations:
#pip install python-binance
#install pandas




#Get Recent trades for specific Pair

def getTrades(Client, Symbol, Limit):
    print("Get Recent Trades for " + Symbol)

    trades = Client.get_recent_trades(symbol = Symbol, limit = Limit)


    return trades
##Access Dict Values in Python:
    ##print((trades[1]["price"]))

    print(trades)


##Delete Keys in Dictionary
#del mydict["price"]






