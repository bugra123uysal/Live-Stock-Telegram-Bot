import requests 
import pandas as pd

api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN"]

ecl=[]
for stock in stocks:
    url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
    get=requests.get(url).json()

    if 'c' in get:
        price=get['c'] #current prices
        print(f"{stock}: ${price:.2f}")
       
    
    else:
        print(f"{stock}: tekar deneyiniz")

