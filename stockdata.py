import requests 
import pandas as pd
import time
import matplotlib.pyplot as plt
import traceback
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

""" 
"AAPL", "AMAT", "APTV", "ACGL", "ADM", "ANET", "AJG", "AIZ", "T", "ATO","ADSK", "ADP", "AZO", "AVB", "AVY", "AXON", "BKR", "BALL", "BAC", "BAX","BDX", "BRK.B", "BBY", "TECH", "BIIB", "BLK", "BX", "BK", "BA", "BKNG","BSX", "BMY", "AVGO", "BR", "BRO", "BF.B", "BLDR", "BG", "BXP", "CHRW",
    "CDNS", "CZR", "CPT", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CAT","CBOE", "CBRE", "CDW", "COR", "CNC", "CNP", "CF", "CRL", "SCHW", "CHTR","CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG","CLX", "CME", "CMS", "KO", "CTSH", "COIN", "CL", "CMCSA", "CAG", "COP",
    "ED", "STZ", "CEG", "COO", "CPRT", "GLW", "CPAY", "CTVA", "CSGP", "COST", "CTRA", "CRWD", "CCI", "CSX", "CMI", "CVS", "DHR", "DRI", "DDOG", "DVA", "DAY", "DECK", "DE", "DELL", "DAL", "DVN", "DXCM", "FANG", "DLR", "DG", "DLTR", "D", "DPZ", "DASH", "DOV", "DOW", "DHI", "DTE", "DUK", "DD","EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "ELV", "EMR", "ENPH",
    "ETR", "EOG", "EPAM", "EQT", "EFX", "EQIX", "EQR", "ERIE", "ESS", "EL","EG", "EVRG", "ES", "EXC", "EXE", "EXPE", "EXPD", "EXR", "XOM", "FFIV","FDS", "FICO", "FAST", "FRT", "FDX", "FIS", "FITB", "FSLR", "FE", "FI","F", "FTNT", "FTV", "FOXA", "FOX", "BEN", "FCX", "GRMN", "IT", "GE",
    "GEHC", "GEV", "GEN", "GNRC", "GD", "GIS", "GM", "GPC", "GILD", "GPN","GL", "GDDY", "GS", "HAL", "HIG", "HAS", "HCA", "DOC", "HSIC", "HSY","HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ","HUBB", "HUM", "HBAN", "HII", "IBM", "IEX", "IDXX", "ITW", "INCY", "IR", "PODD", "INTC", "ICE", "IFF", "IP", "IPG", "INTU", "ISRG", "IVZ", "INVH",
    "IQV", "IRM", "JBHT", "JBL", "JKHY", "J", "JNJ", "JCI", "JPM", "K", "KVUE", "KDP", "KEY", "KEYS", "KMB", "KIM", "KMI", "KKR", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LDOS", "LEN", "LII", "LLY",  "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LULU", "LYB", "MTB", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MTCH", "MKC", "MCD", "MCK",
    "MDT", "MRK", "META", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MRNA", "MHK", "MOH", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS",
    "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NEM", "NWSA", "NWS", "NEE","NKE", "NI", "NDSN", "NSC", "NTRS", "NOC", "NCLH", "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "ON", "OKE", "ORCL", "OTIS","PCAR", "PKG", "PLTR", "PANW", "PARA", "PH", "PAYX", "PAYC", "PYPL","PNR", "PEP", "PFE", "PCG", "PM", "PSX", "PNW", "PNC", "POOL", "PPG","PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PTC", "PSA", "PHM","PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF","RSG", "RMD", "RVTY", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SRE", "NOW", "SHW", "SPG", "SWKS", "SJM","SW", "SNA", "SOLV", "SO", "LUV", "SWK", "SBUX", "STT", "STLD", "STE","SYK", "SMCI", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR","TRGP", "TGT", "TEL", "TDY", "TER", "TSLA", "TXN", "TPL", "TXT", "TMO","TJX", "TKO", "TTD", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TYL","TSN", "USB", "UBER", "UDR", "ULTA", "UNP", "UAL", "UPS", "URI", "UNH","UHS", "VLO", "VTR", "VLTO", "VRSN", "VRSK", "VZ", "VRTX", "VTRS","VICI", "V", "VST", "VMC", "WRB", "GWW", "WAB", "WBA", "WMT", "DIS","WBD", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WY", "WSM","WMB", "WTW", "WDAY", "WYNN", "XEL", "XYL", "YUM", "ZBRA", "ZBH", "ZTS"

 """
#finn hub 
api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"
stocks= [
    "MMM", "AOS", "ABT", "ABBV", "ACN", "ADBE", "AMD", "AES", "AFL", "A","APD", "ABNB", "AKAM", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL","GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AEP", "AXP", "AIG","AMT", "AWK", "AMP", "AME", "AMGN", "APH", "ADI", "AON", "APA", "APO",
    
]

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
       industryb=profileb.get('finnhubIndustry', 'Bilinmiyor')
       
       if 'c' not in response or not responseb:
          update.message.reply_text("tekrar deneyin")
          return
          #hisse 1
       current=response['c']
       higt=response['h']
       low=response['l']
       prev=response['pc']
       change=round((( current - prev)/ prev ) * 100, 2)
       market_cap=profile.get('marketCapitalization', 'Bilinmiyor')
       industry=profile.get('finnhubIndustry', 'Bilinmiyor')
       name=profile.get('name', hisse)

       # hisse 2  
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
message_branch=""
limit=50
count=0
for stock in stocks:
 
 try:
   
   url=f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
   response=requests.get(url).json()
   
   fiya=response["c"] #stocks prices
   
   # print(f"{stock}:${response['c']}")
   message_branch += f"{stock}: ${float(fiya):.2f} \n"
   count +=1

   profile_u=f"https://finnhub.io/api/v1/stock/profile2?symbol={stock}&token={api_key}"
   profile=requests.get(profile_u).json()
   industry=profile.get("finnhubIndustry", "Bilinmiyor")

   current=response['c']
   higt=response['h']
   low=response['l']
   prev=response['pc']
   change=round((( current - prev)/ prev ) * 100, 2)

   clm.append({"Name":stock , "Price":current, "En yüksek": higt ,"En-düşük": low , "Dünkü-fiyat": prev, "Değişim%": change , "Industry": industry})

   if count % count == 0 :
      send_mes(message_branch)
      message_branch = ""
      

 except Exception as e:
     message_branch +=f"{stock}: veri bulunamadı tekrar deneyiniz : ({e})\n"
     
 if message_branch:
    send_mes(message_branch)
 #excel 
ecl=pd.DataFrame(clm)
ecl.to_excel("C:\\Users\\buğra\\abd_hisse.xlsx", index=True)
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
update.start_polling()
update.idle()