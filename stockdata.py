import requests 
import pandas as pd
import time
import traceback
from telegram.ext import Updater, CommandHandler

#finn hub 
api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"
stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM","META","NFLX","BABA","BAC","JNJ","WMT","BTI"]
#telegram
bot_token="8151142897:AAGoXgaHGKXZ4gKp2emt2KJ_Kx6dTBs5SJs"
chat_id="6700567738"



#sent message telegram 
def send_mes(message):
  teurl=f"https://api.telegram.org/bot{bot_token}/sendMessage"
  data={"chat_id": chat_id, "text": message}
  requests.post(teurl, data=data)
  

 #analiz bölümü /analiz META
def analiz(update , context): 
   
   try:
       hisse=context.args[0].upper()
       url=f"https://finnhub.io/api/v1/quote?symbol={hisse}&token={api_key}"
       response=requests.get(url).json()

       current=response['c']
       higt=response['h']
       low=response['l']
       prev=response['pc']
       change=round((( current - prev)/ prev ) * 100, 2)

    
       mess=(
       f"Anlık fiyat: {hisse} \n"
       f"En yüksek fiyat: {higt}\n" 
       f"En düşük fiyat: {low}\n" 
       f"önceki kapanış  fiyat: {prev}\n" 
       f"Değişim %{change}"
       )
       update.message.reply_text(mess)


   except Exception as e:
       update.message.reply_text(f"veri bulunamadı tekrar deneyiniz {e}") 

#fiyat komutu  /fiyat META 
def fiyat(update, context):
   
   try: 
      aa=context.args[0].upper()
      uurl=f"https://finnhub.io/api/v1/quote?symbol={aa}&token={api_key}"
      respon=requests.get(uurl).json()
      price=respon["c"]
      ppirice=f"{aa}: ${price:.2f}"
      update.message.reply_text(ppirice)
      
   except Exception as e:
     update.message.reply_text(f"tekrar deneyiniz:{e}")

# help komutu 
def help(updater , context):
   try:
      
      ınfırmacion=("-analiz komutu için  /analiz META  \n - fiyat komutu için /fiyat AAPL  \n yardım komutu için /help   ")
      updater.message.reply_text(ınfırmacion)
      
   except Exception as e:
      updater.message.reply_text(f"tekrar deneyinz komutu yanlış yazmış olabilirsiniz {e} ")
   
   

#başlangıç hisse fiyatları
message="hisse fiyatları\n"
for stock in stocks:
 
 try:
   
   
   url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
   response=requests.get(url).json()
   
   fiya=response["c"] #stocks prices
   print(f"{stock}:${response['c']}")
   message +=f"{stock}: ${fiya:.2f} \n"
 except Exception as e:
     message +=f"{stock}: veri bulunamadı tekrar deneyiniz : ({e})\n"

#telegrama başlangıç mesajı gönder
send_mes(message)


#telegram botunun çalıştırıldığı yer
updater=Updater(bot_token , use_context=True)
dp=updater.dispatcher

#analiz
dp.add_handler(CommandHandler("analiz", analiz)) #analiz komutunu çalıştıma
#fiyat price 
dp.add_handler(CommandHandler("fiyat",fiyat))
""" help """
dp.add_handler(CommandHandler("help", help))
updater.start_polling()
updater.idle()

