import requests 
import pandas as pd
import time

api_key="******"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN"]
#alarm target
alarm={
    "AAPL":220,
    "MSFT":460

}


while True:

   for stock  in stocks:
       url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
       get=requests.get(url).json()
   
       if 'c' in get:
           price=get['c'] #current prices
           print(f"{stock}: ${price:.2f}")
          
       
       else:
           print(f"{stock}: tekar deneyiniz")

    
         #alarm
       if stock in alarm and price >= alarm[stock]:
           print(f"{stock}: fiyat seviyesine ulaşdı {price} >= {alarm[stock]}   ")
       else:
           print(f"{stock} fiyat seviyesine ulaşmadı ")
  
   time.sleep(10)