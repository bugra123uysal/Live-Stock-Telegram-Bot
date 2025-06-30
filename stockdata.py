import requests 
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sns
from telegram.ext import Updater, CommandHandler


def telegrambot(note):
       bot_token="**"
       chat_id="****"
       url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
       data={"chat_id":chat_id, "text": note }
       requests.post(url, data=data)
       


api_key="****"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM","META","NFLX","BABA","BAC","JNJ","WMT","BTI"]
#alarm target
alarm={
    "AAPL":201.56,
    "MSFT":492.27,
    "GOOGL":170.68

}

def helpp(update , context):
        try:
          
          
          if helpp:  

           yardım=("- for helping  : / help   - for  prices  /fiyatt TSM  ")    
           update.message.reply_text(yardım)
          else:
              update.message.reply_text
           
        except:
            update.message.reply_text

# telegram fiyat komut                
def fiyatt(update, context):     
       try:
          hisse=context.args[0].upper()
          url=f"https://finnhub.io/api/v1/quote?symbol={hisse}&token={api_key}"
          rege=requests.get(url).json()
          fiyatt=rege.get("c")
          
   
          if fiyatt:
              note=f"{hisse}: ${fiyatt:.2f}"
          else:
              note=f"{hisse} verisine ulaşılamadı"
          
          update.message.reply_text(note)
   
       except:
           update.message.reply_text("kullanım /fiyatt")


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
       bot_token="8151142897:AAGoXgaHGKXZ4gKp2emt2KJ_Kx6dTBs5SJs"
       #Telegram bot'unu başlatır ve gelen telegram mesajlarını alıcak updater i tanımlar
       updater=Updater(bot_token, use_context=True)
       ater=Updater(bot_token, use_context=True)
       dp=updater.dispatcher 
       aa=updater.dispatcher
       # hisse fiyatı komitti
       dp.add_handler(CommandHandler("fiyatt", fiyatt))
       #bilgilendirme
       aa.add_handler(CommandHandler ("helpp", helpp ))

       updater.start_polling()
       ater.idle()



       while True:
            fiyatt()
            time.sleep(3000)