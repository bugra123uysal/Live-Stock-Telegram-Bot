import requests 
import pandas as pd
import time
import matplotlib.pyplot as plt
import traceback
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

#finn hub 
api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"
stocks=["AAPL", "MSFT", "GOOGL","TSLA","TSM","AMZN","PM","META","NFLX","BABA","BAC","JNJ","WMT","BTI"]
#telegram
bot_token="8151142897:AAGoXgaHGKXZ4gKp2emt2KJ_Kx6dTBs5SJs"
chat_id="6700567738"
clm=[]

#sent message telegram 
def send_mes(message):
  teurl=f"https://api.telegram.org/bot{bot_token}/sendMessage"
  data={"chat_id": chat_id, "text": message}
  requests.post(teurl, data=data)
  

 #analiz bölümü /analiz META
def analiz(update , context): 

   
   try:
       
       
       if len(context.args) == 0:
          
          return
       
       hisse=context.args[0].upper()
       hisseb=context.args[1].upper()
       url=f"https://finnhub.io/api/v1/quote?symbol={hisse}&token={api_key}"
       profile_url=f"https://finnhub.io/api/v1/stock/profile2?symbol={hisse}&token={api_key}"
       response=requests.get(url).json()
       profile=requests.get(profile_url).json()

       urlb=f"https://finnhub.io/api/v1/quote?symbol={hisseb}&token={api_key}"
       profile_urlb=f"https://finnhub.io/api/v1/stock/profile2?symbol={hisseb}&token={api_key}"
       responseb=requests.get(urlb).json()
       profileb=requests.get(profile_urlb).json()
       
       



       if 'c' not in response or not responseb:
          update.message.reply_text("tekrar deneyin")
          return
          
       current=response['c']
       higt=response['h']
       low=response['l']
       prev=response['pc']
       change=round((( current - prev)/ prev ) * 100, 2)
       market_cap=profile.get('marketCapitalization', 'Bilinmiyor')
       industry=profile.get('finnhubIndustry', 'Bilinmiyor')
       name=profile.get('name', hisse)

         
       currentb=responseb['c']
       higtb=responseb['h']
       lowb=responseb['l']
       prevb=responseb['pc']
       changeb=round((( currentb - prevb)/ prevb ) * 100, 2)
       market_capb=profileb.get('marketCapitalization', 'Bilinmiyor')
       industryb=profileb.get('finnhubIndustry', 'Bilinmiyor')
       nameb=profileb.get('nameb', hisseb)


       
    
       mess=(
       f"{name} {nameb} ({hisse} {hisseb}) Analiz: \n"
       f"Anlık fiyat: {current} {currentb} \n"
       f"En yüksek fiyat: {higt} {higtb}\n" 
       f"En düşük fiyat: {low} {lowb} \n" 
       f"önceki kapanış  fiyat: {prev} {prevb}\n" 
       f"Değişim %{change} {changeb}\n"
       f"piyasa değeri: {market_cap} {market_capb} \n"
       f"sektör: {industry} {industryb}"
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
def help(update , context):
   try:
      
      ınfırmacion=("-analiz komutu için  /analiz META  \n - fiyat komutu için /fiyat AAPL  \n yardım komutu için /help   ")
      update.message.reply_text(ınfırmacion)
      
   except Exception as e:
      update.message.reply_text(f"tekrar deneyinz komutu yanlış yazmış olabilirsiniz {e} ")
   
   

#başlangıç hisse fiyatları
message="hisse fiyatları\n"

#grafik  /grafik AAPL
def grafik(update, context):

   try:
      sse=context.args[0].upper()
      end_time=int(time.time())
      start_time=end_time - (60 * 60 * 24 * 30)  #son 30 gün

      grfurl=f"https://finnhub.io/api/v1/stock/candle?symbol={sse}&resolution=60&from={start_time}&to={end_time}&token={api_key}"
      ddta=requests.get(grfurl).json() 

      if ddta.get("s") != "ok":  #başarılı bir yanıt gelmesse
        update.message.reply_text("veri alınmadı")
        return
      
      
      pricess=ddta["c"]
      tarihh=[datetime.datetime.fromtimestamp(t) for t in ddta["t"]]

      plt.figure(figsize=(8, 3))
      plt.plot(tarihh , pricess, color="blue")
      plt.title("sa")
      plt.grid(True)
      plt.tight_layout()
      plt.savefig("grafik.png")
      plt.close()
          #grafiği kaydedip telegrama gönderir
      with open("grafik.png", "rb" ) as g:
         update.message.reply_photo(photo=g, caption=f"{sse} fiyat grafiği")

        
   except Exception as e:
     update.message.reply_text(f"bir hata oluştu tekrar deneyin {e} ")


for stock in stocks:
 

 try:
   
   
   url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
   response=requests.get(url).json()
   
   fiya=response["c"] #stocks prices
   print(f"{stock}:${response['c']}")
   message +=f"{stock}: ${fiya:.2f} \n"


   url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"


   response=requests.get(url).json()

   current=response['c']
   higt=response['h']
   low=response['l']
   prev=response['pc']
   change=round((( current - prev)/ prev ) * 100, 2)

   clm.append({"Name":stock , "Price":current, "En yüksek": higt ,"En-düşük": low , "Dünkü-fiyat": prev, "Değişim%": change })   
      
   

 except Exception as e:
     message +=f"{stock}: veri bulunamadı tekrar deneyiniz : ({e})\n"
     
 
 #excel 
ecl=pd.DataFrame(clm)
ecl.to_excel("abd_hisse.xlsx", index=True)
#telegrama başlangıç mesajı gönder
send_mes(message)
 

#telegram botunun çalıştırıldığı yer
update=Updater(bot_token , use_context=True)
dp=update.dispatcher

#analiz
dp.add_handler(CommandHandler("analiz", analiz)) #analiz komutunu çalıştıma
#fiyat price 
dp.add_handler(CommandHandler("fiyat",fiyat))
""" help """
dp.add_handler(CommandHandler("help", help))
#grafik
dp.add_handler(CommandHandler("grafik", grafik))
update.start_polling()
update.idle()

