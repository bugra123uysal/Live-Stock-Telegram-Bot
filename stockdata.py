import requests 
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sns
from telegram.ext import Updater, CommandHandler


def telegrambot(note):
       bot_token="8151142897:AAGoXgaHGKXZ4gKp2emt2KJ_Kx6dTBs5SJs"
       chat_id="6700567738"
       url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
       data={"chat_id":chat_id, "text": note }
       requests.post(url,data=data)
       alget=requests.get(url).json()
     






api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"

stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM","META","NFLX","BABA","BAC","JNJ","WMT","BTI"]
#alarm target


def analiz(update , context):
    try:
          
        hisse=context.args[0].upper()
        url=f"https://finnhub.io/api/v1/quote?symbol={hisse}&token={api_key}"
        alget=requests.get(url).json()
        current=alget['c']
        higt=alget['h']
        low=alget['l']
        prev=alget['pc']
        change_pct=round(((current - prev)/ prev)* 100, 2) 
      
            
        note=update.message.reply_text(f"📊 {hisse} Analizi \n" f" 💰 Anlık Fiyat: ${current:.2f}\n" f"📈 Değişim: %{change_pct}\n" f"🔺 En Yüksek: ${higt:.2f}\n" f"🔻 En Düşük: ${low:.2f}\n" f"📈 bir gün önce: %{change_pct:.2f}")
        update.message.reply_text(note)
           
      
        note +="tekrar deneyiniz"
        update.message.reply_text(note)               
    except Exception as e:
       update.message.reply_text(f" hata oluştu: {e}")
       


def helpp(update , context):
        try:
          
          
          if helpp:  

           yardım=("- for helping  : / help   - for  prices  /fiyatt TSM  - for analiz /analiz META ")    
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


def get_stock_data():
   

   note=""
   clm=[]
  
   
   for stock  in stocks:
       url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
       get=requests.get(url).json()
       price=get.get('c', None) #current prices
       try:
             alget=requests.get(url).json()
             current=alget['c'],
             higt=alget['h'],
             low=alget['l'],
             prev=alget['pc'],
             change_pct=round(((current - prev)/ prev)* 100, 2)
           

             clm.append({"Name":stock , "Price": price,  " current": current ,"higt":higt ,"low":low," prev": prev," change_pct": change_pct   }) 
       
       
             note += "tekrar deneyelim"
       except Exception as e:
            note +="veri alınamadı"
       
       if price:
            
          
            print(f"{stock}: ${price:.2f}")
            note += f"{stock}: ${price:.2f}\n"
         
       else:
         print(f": tekar deneyiniz ")
         note +=" tekar deneyiniz \n "
   #exel bölümü
   ecl=pd.DataFrame(clm)
   ecl.to_excel("abd_hisse.xlsx", index=False)    
   
      
      
   
   telegrambot(note)
   if __name__ == "__main__":
       bot_token="8151142897:AAGoXgaHGKXZ4gKp2emt2KJ_Kx6dTBs5SJs"
       #Telegram bot'unu başlatır ve gelen telegram mesajlarını alıcak updater i tanımlar
       updater=Updater(bot_token, use_context=True)
       ater=Updater(bot_token, use_context=True)
       

       # hisse fiyatı komitti
       dp=updater.dispatcher
       dp.add_handler(CommandHandler("fiyatt", fiyatt))
      
       #bilgilendirme komitti
       aa=updater.dispatcher
       aa.add_handler(CommandHandler ("helpp", helpp ))
       
       #analiz komitti
       bb=updater.dispatcher
       bb.add_handler(CommandHandler("analiz", analiz))
     

       updater.start_polling()
       ater.idle()



       while True:
            fiyatt()
            time.sleep(3000)