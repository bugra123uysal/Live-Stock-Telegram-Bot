#                Live-Stock-Telegram-Bot
Developed a real-time stock tracking tool using Python and the Finnhub API. It collects key stock market data including current price, daily high and low, previous closing price, market capitalization, industry classification, and percentage price change. The data is saved to an Excel file, where additional calculations like 20-day volatility and daily price range are performed. Excel is also used to identify the top gainers and losers as well as summarize industry-based performance.

A Telegram bot allows users to interact with the system through commands. For example, /fiyat AAPL returns the latest available stock data for Apple, and /analiz META AAPL compares two stocks by showing detailed information such as price, range, industry, and change percentage. Users can also use /help to view available commands.

The system includes features to send updates of selected stock prices to Telegram. However, the data is not continuously updated — it only refreshes when the Python script is run, making it suitable for on-demand or scheduled use rather than real-time continuous tracking.

This project provides an efficient way to monitor stock performance and perform comparative analysis using both command-line automation and messaging integration..

#  data retrieval API 
 finnhub: https://finnhub.io/dashboard
 
bot_token="***"
chat_id="***"
api_key="***"
url=f"https://api.telegram.org/bot{bot_token}/sendMessage"




#  my telegram Commands

## start
<img width="1299" height="756" alt="Ekran görüntüsü 2025-07-30 185403" src="https://github.com/user-attachments/assets/272a4976-7cc3-4af9-bccf-29607e7cc914" />

  ## priice
- /fiyatt META
- <img width="848" height="110" alt="Ekran görüntüsü 2025-07-15 223903" src="https://github.com/user-attachments/assets/0b14631e-5693-4ce4-ba68-a9fbf38a24dc" />
## analysis
- /analiz AAPL 
- <img width="1043" height="336" alt="Ekran görüntüsü 2025-07-30 190039" src="https://github.com/user-attachments/assets/b2836ea4-2a0e-4d0a-965e-4b5d87c9c646" />

- /help

- <img width="856" height="162" alt="Ekran görüntüsü 2025-07-15 223930" src="https://github.com/user-attachments/assets/5b5c759a-04da-4bcc-aa3a-db620806eba9" />


# stocks
"AAPL", "AMAT", "APTV", "ACGL", "ADM", "ANET", "AJG", "AIZ", "T", "ATO","ADSK", "ADP", "AZO", "AVB", "AVY", "AXON", "BKR", "BALL", "BAC", "BAX","BDX", "BRK.B", "BBY", "TECH", "BIIB", "BLK", "BX", "BK", "BA", "BKNG","BSX", "BMY", "AVGO", "BR", "BRO", "BF.B", "BLDR", "BG", "BXP", "CHRW","GOOG", "MO", "AMZN", "AMCR","ADBE", "AMD", "AES", "AFL", "A","APD", "ABNB"
    "CDNS", "CZR", "CPT", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CAT","CBOE", "CBRE", "CDW", "COR", "CNC", "CNP", "CF", "CRL", "SCHW", "CHTR","CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG","CLX", "CME", "CMS", "KO", "CTSH", "COIN", "CL", "CMCSA", "CAG", "COP","FI","F", "FTNT", "FTV", "FOXA", "FOX", "BEN", "FCX", "GRMN", "IT", "GE","ZTS" "MMM", "AOS", "ABT", "ABBV", "ACN", 
    "ED", "STZ", "CEG", "COO", "CPRT", "GLW", "CPAY", "CTVA", "CSGP", "COST", "CTRA", "CRWD", "CCI", "CSX", "CMI", "CVS", "DHR", "DRI", "DDOG", "DVA", "DAY", "DECK", "DE", "DELL", "DAL", "DVN", "DXCM", "FANG", "DLR", "DG", "DLTR", "D", "DPZ", "DASH", "DOV", "DOW", "DHI", "DTE", "DUK", "DD","EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "ELV", "EMR", "ENPH", "AMGN", "APH", "ADI", "AON", "APA", "APO",
    "ETR", "EOG", "EPAM", "EQT", "EFX", "EQIX", "EQR", "ERIE", "ESS", "EL","EG", "EVRG", "ES", "EXC", "EXE", "EXPE", "EXPD", "EXR", "XOM", "FFIV","FDS", "FICO", "FAST", "FRT", "FDX", "FIS", "FITB", "FSLR", "FE", 
    "GEHC", "GEV", "GEN", "GNRC", "GD", "GIS", "GM", "GPC", "GILD", "GPN","GL", "GDDY", "GS", "HAL", "HIG", "HAS", "HCA", "DOC", "HSIC", "HSY","HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ","HUBB", "HUM", "HBAN", "HII", "IBM", "IEX", "IDXX", "ITW", "INCY", "IR", "PODD", "INTC", "ICE", "IFF", "IP", "IPG", "INTU", "ISRG", "IVZ", "INVH","AKAM", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL","GOOGL", 
    "IQV", "IRM", "JBHT", "JBL", "JKHY", "J", "JNJ", "JCI", "JPM", "K", "KVUE", "KDP", "KEY", "KEYS", "KMB", "KIM", "KMI", "KKR", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LDOS", "LEN", "LII", "LLY",  "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LULU", "LYB", "MTB", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MTCH", "MKC", "MCD", "MCK","AIG","AMT", "AWK", "AMP", "AME"
    "MDT", "MRK", "META", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MRNA", "MHK", "MOH", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS",, "AEE", "AEP", "AXP", 
    "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NEM", "NWSA", "NWS", "NEE","NKE", "NI", "NDSN", "NSC", "NTRS", "NOC", "NCLH", "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "ON", "OKE", "ORCL", "OTIS","PCAR", "PKG", "PLTR", "PANW", "PARA", "PH", "PAYX", "PAYC", "PYPL","PNR", "PEP", "PFE", "PCG", "PM", "PSX", "PNW", "PNC", "POOL", "PPG","PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PTC", "PSA", "PHM","PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF","RSG", "RMD", "RVTY", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SRE", "NOW", "SHW", "SPG", "SWKS", "SJM","SW", "SNA", "SOLV", "SO", "LUV", "SWK", "SBUX", "STT", "STLD", "STE","SYK", "SMCI", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR","TRGP", "TGT", "TEL", "TDY", "TER", "TSLA", "TXN", "TPL", "TXT", "TMO","TJX", "TKO", "TTD", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TYL","TSN", "USB", "UBER", "UDR", "ULTA", "UNP", "UAL", "UPS", "URI", "UNH","UHS", "VLO", "VTR", "VLTO", "VRSN", "VRSK", "VZ", "VRTX", "VTRS","VICI", "V", "VST", "VMC", "WRB", "GWW", "WAB", "WBA", "WMT", "DIS","WBD", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WY", "WSM","WMB", "WTW", "WDAY", "WYNN", "XEL", "XYL", "YUM", "ZBRA", "ZBH", 



# excel file
You can download the file and examine the data.

https://github.com/bugra123uysal/Live-Stock-Telegram-Bot/blob/main/abd_hisse.xlsx

#few charts
<img width="1895" height="932" alt="Ekran görüntüsü 2025-07-30 211209" src="https://github.com/user-attachments/assets/746be857-9445-4817-8feb-8bb82cce5e8b" />

<img width="1909" height="938" alt="Ekran görüntüsü 2025-07-30 211102" src="https://github.com/user-attachments/assets/79ab4069-80b5-4d4c-8550-567b459d8639" />

<img width="1868" height="928" alt="Ekran görüntüsü 2025-07-30 211220" src="https://github.com/user-attachments/assets/6d7775e1-91ba-4efd-9e4d-9d2903c301b6" />


<img width="1857" height="930" alt="Ekran görüntüsü 2025-07-30 211228" src="https://github.com/user-attachments/assets/f1af6914-5a2b-4927-90b0-d8b947fdc1ef" />

<img width="1915" height="938" alt="Ekran görüntüsü 2025-07-30 211240" src="https://github.com/user-attachments/assets/fda1f527-d7aa-4a8e-bdf9-86310f1b4be6" />





