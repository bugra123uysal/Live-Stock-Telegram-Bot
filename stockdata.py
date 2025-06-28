import requests 
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sns
from telegram.ext import Updater, CommandHandler


def telegrambot(note):
       bot_token="****"# bot token
       chat_id="*****" # chat ıd 
       url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
       data={"chat_id":chat_id, "text": note }
       requests.post(url, data=data) #mesajı gönderir
       


api_key="*****" # finnhub api key 

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM","META","NFLX","BABA","BAC","JNJ","WMT","BTI"]
#alarm target
alarm={
    "AAPL":201.56,
    "MSFT":492.27,
    "GOOGL":170.68

}
# telegram komut 
def fiyatt(update, context):     
       try:
          hisse=context.args[0].upper() # komuttan hisse adını alınır
          url=f"https://finnhub.io/api/v1/quote?symbol={hisse}&token={api_key}"
          rege=requests.get(url).json()
          fiyatt=rege.get("c")
          
   
          if fiyatt:
              note=f"{hisse}: ${fiyatt:.2f}"
          else:
              note=f"{hisse} verisine ulaşılamadı"
          
          update.message.reply_text(note)
   
       except:
           update.message.reply_text("kullanım /fiyat")


while True:

   note=""
   clm=[]

   for stock  in stocks:
       url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
       get=requests.get(url).json()
       price=get['c'] #current prices
       
       if 'c' in get:
            
          
            print(f"{stock}: ${price:.2f}")
            note += f"{stock}: ${price:.2f}\n"
            clm.append({"Name":stock , "Price": price})
        

           

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
   ecl=pd.DataFrame(clm)
   ecl.to_excel("abd_hisse.xlsx", index=True )  
   telegrambot(note)
   if __name__ == "__main__":
       bot_token="*****"
       #Telegram bot'unu başlatır ve gelen telegram mesajlarını alıcak updater i tanımlar
       updater=Updater(bot_token, use_context=True)
       dp=updater.dispatcher 
       dp.add_handler(CommandHandler("fiyatt", fiyatt))
       updater.start_polling()

       while True:
            fiyatt()
            time.sleep(3000)
           

 