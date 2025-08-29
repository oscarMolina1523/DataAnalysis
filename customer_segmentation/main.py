import pandas as pd

#First read the csv
df=pd.read_csv('ventas_ejemplo.csv')
#print(pd.DataFrame(df))

#clean data
#here delete all the rows with field empty
df= df.dropna(subset=['InvoiceNo', 'StockCode', 'Description','Quantity','InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

#filter the quatities and unitprice if they are minors 0
df=df[(df['Quantity']>0) & (df['UnitPrice'] > 0)]

print(df)