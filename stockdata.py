import requests 
import pandas as pd
import time

def telegrambot(note):
       bot_token="**"
       chat_id="***"
       url=f"https://api.telegram.org/bot{ bot_token}/sendMessage"
       data={"chat_id":chat_id, "text": note }
      

       response= requests.post(url, data=data)
       


api_key="***"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM","META","NFLX","BABA","BAC","JNJ","WMT","BTI"]
#alarm target
alarm={
    "AAPL":201.56,
    "MSFT":492.27,
    "GOOGL":170.68

}

while True:
   note=""
   clm=[]

   for stock  in stocks:
       url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
       get=requests.get(url).json()
   
       if 'c' in get:
            price=get['c'] #current prices
            print(f"{stock}: ${price:.2f}")
            note += f"{stock}: ${price:.2f} \n"
            clm.append({"Name":stock , "Price":price})

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
    #exel bölümü
  
   ecl=pd.DataFrame(clm )
   ecl.to_excel("abd_hisse.xlsx", index=True)
   telegrambot(note)
   time.sleep(10)