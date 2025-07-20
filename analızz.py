import pandas as pd
import matplotlib.pyplot as plt
stock=pd.read_excel("C:\\Users\\buğra\\Desktop\\abd_hisse.xlsx")
""" new colum """
stock['Volatilite']=stock['En yüksek'] - stock['En-düşük']
stock=stock.loc[:, ~stock.columns.str.contains('^Unnemed')]
""" hata bulma """
print("hata: ",stock.isnull().sum())
start20=stock.sort_values(by='Price', ascending=False).head(20)
end20=stock.sort_values(by='Price', ascending=True).head(20)
""" veri türü """
print(stock.dtypes)
""" columlar """
print(stock.columns)

kolo=stock[['En yüksek','En-düşük','Dünkü-fiyat','Volatilite']]
kk=kolo.corr()
print(f"kolorosyon",kk)
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


stock.to_excel("C:\\Users\\buğra\\Desktop\\abd_hisse.xlsx" , index=False)
