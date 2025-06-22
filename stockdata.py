import requests 
import pandas as pd
import time

def telegrambot(note):
       bot_token="****"
       chat_id="****"
       url=f"https://api.telegram.org/bot{ bot_token}/sendMessage"
       data={"chat_id":chat_id, "text": note }
       response= requests.post(url, data=data)
       


api_key="****"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN"]
#alarm target
alarm={
    "AAPL":201,
    "MSFT":460,
    "TSLA":322.16

}


while True:

   for stock  in stocks:
       url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
       get=requests.get(url).json()
   
       if 'c' in get:
            price=get['c'] #current prices
            print(f"{stock}: ${price:.2f}")
    
               #alarm
            if stock in alarm and price >= alarm[stock]:
              print(f"{stock}: fiyat seviyesine ulaşdı {price} >= {alarm[stock]}  GÜNCEL FİYATLAR: {stock}: ${price:.2f}  ")
              note=f" {stock}: fiyat seviyesine ulaşdı {price} >= {alarm[stock]    }  " 
             
              telegrambot(note)
            else:
               print(f"{stock} fiyat seviyesine ulaşmadı ")
       else:
         print(f"{stock}: tekar deneyiniz")
  
   time.sleep(10)

   
    
