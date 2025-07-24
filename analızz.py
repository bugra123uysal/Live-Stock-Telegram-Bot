import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
stock=pd.read_excel("C:\\Users\\buğra\\abd_hisse.xlsx")
verıı=[]
""" new colum """
# 20 günlük volitilite
stock['Volatilite_20']=stock['Price'].rolling(window=20).std()
stock['Volatilite_day']=stock['En yüksek'] - stock['En-düşük']


stock=stock.loc[:, ~stock.columns.str.contains('^Unnamed')]
""" hata bulma """
print("hata: ",stock.isnull().sum())
start20=stock.sort_values(by='Price', ascending=False).head(20)
end20=stock.sort_values(by='Price', ascending=True).head(20)
""" veri türü """
print(stock.dtypes)
""" columlar """
print(stock.columns)

kolo=stock[['En yüksek','En-düşük','Dünkü-fiyat','Volatilite']].corr()

print(f"kolorosyon",kolo)
""" grafik """

plt.plot(end20["Name"], end20['Price'])
plt.title( "hisse grafiği" )
plt.xticks(rotation=90)
plt.show()


""" max-min price """
map=stock['Price'].max()
mip=stock['Price'].min()
"max-min high"
mah=stock['En yüksek'].max()
mih=stock['En yüksek'].min()

""" max-min en-düşük """
mae=stock['En-düşük'].max()
mie=stock['En-düşük'].min()

"max-min  Dünkü-fiyat"
mad=stock['Dünkü-fiyat'].max()
mid=stock['Dünkü-fiyat'].min()

""" yüzde olarak en çok yükselen """
yuzy20=stock.sort_values(by='Değişim%', ascending=False).head(20)


plt.plot(yuzy20['Name'] , yuzy20['Değişim%'])
plt.title("yüzde olarak en çok yükselen")
plt.xticks(rotation=90)
plt.show()

yuzd20=stock.sort_values(by='Değişim%', ascending=True).head(20)
plt.plot(yuzd20['Name'] , yuzd20['Değişim%'])
plt.title("yüzde olarak en az düşen" )
plt.xticks(rotation=90)
plt.show()


ındustury_cou=stock['Industry'].value_counts().reset_index()
ındustury_cou.columns=['Industry', 'Count']
sns.barplot(x='Industry', y='Count', data=ındustury_cou)
plt.xticks(rotation=90)
plt.title("Industry")
plt.show()

yuma=stock['Değişim%'].max()
en_yuks=stock[stock['Değişim%']== yuma]

""" yüzde olarak en çok düşen """

yumid=stock['Değişim%'].min()
en_dusuk=stock[stock['Değişim%']== yumid]



print("yüzde-en_yüksek:\n" , en_yuks[['Name' , 'Değişim%']])

print("yüzde-en_düşük:\n", en_dusuk[['Name', 'Değişim%']] )


""" yüksek volitilite yüksek değişim anlamına mı geliyor  """
cor_vol_yuzde=stock[['Volatilite', 'Değişim%']].corr()
print(f"deneme: ",cor_vol_yuzde)

# sektörlerdeki hisselerin ortalama  fiyatları hangisi daha palı 
ındustury_maxx=stock.groupby('Industry')['Price'].mean().sort_values(ascending=False)
print(f'Ortalama endüstürü ye göre hisse fiyatları' , ındustury_maxx)

sns.barplot(ındustury_maxx)
plt.title("Aaaaaverage price comparison by sector")
plt.xticks(rotation=90)
plt.show()


ındustry_yuzde=stock.groupby('Industry')['Değişim%'].agg('mean','std').sort_values(ascending=False)
sns.barplot(ındustry_yuzde)
plt.title("Average percentage comparison by sector")
plt.xticks(rotation=90)
plt.show()

stock.to_excel("C:\\Users\\buğra\\abd_hisse.xlsx" , index=False)

