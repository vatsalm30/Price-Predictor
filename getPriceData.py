from requests import Request, Session
import json

url = "http://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


class PriceData():
    def __init__(self, symbol, compareBy):
        params = {
            "symbol": symbol,
            "convert": compareBy
        }
