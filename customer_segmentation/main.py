import pandas as pd

#First read the csv
df=pd.read_csv('ventas_ejemplo.csv')
#print(pd.DataFrame(df))

#clean data
#here delete all the rows with field empty
df= df.dropna(subset=['InvoiceNo', 'StockCode', 'Description','Quantity','InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

#filter the quatities and unitprice if they are minors 0
df=df[(df['Quantity']>0) & (df['UnitPrice'] > 0)]
#create a new col named total price
df['Total Price']=df['Quantity'] * df['UnitPrice']
#convert dates to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print(df)