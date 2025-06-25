import requests 
import pandas as pd
import time

def telegrambot(note):
       bot_token="8151142897:AAGoXgaHGKXZ4gKp2emt2KJ_Kx6dTBs5SJs"
       chat_id="6700567738"
       url=f"https://api.telegram.org/bot{ bot_token}/sendMessage"
       data={"chat_id":chat_id, "text": note }
      

       response= requests.post(url, data=data)
       


api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM"]
#alarm target
alarm={
    "AAPL":201.56,
    "MSFT":492.27,
    "GOOGL":170.68

}

while True:
   note=""

   for stock  in stocks:
       url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
       get=requests.get(url).json()
   
       if 'c' in get:
            price=get['c'] #current prices
            print(f"{stock}: ${price:.2f}")
            note += f"{stock}: ${price:.2f} \n"

            if stock in alarm:
              if price >= alarm[stock]:
                 note +=f"{stock} hedef fiyata ulaşdı - (${price:.2f} >={alarm[stock]:.2f})\n "
                 print(note)
            
              else:
                 note +=f"{stock} hedef fiyata ulaşmadı "
                 print(note)
           

       
       else:
         print(f": tekar deneyiniz ")
         note +=" tekar deneyiniz \n "

       
   telegrambot(note)
   time.sleep(10)