import pandas as pd
import os

def preprocessing_data(input='ventas_ejemplo.csv', output='customer_segmentation/data/customer_preprocessed.csv'):
    #if the folder doesnt exist create one
    os.makedirs(os.path.dirname(output), exist_ok=True)

    #First read the csv
    df=pd.read_csv(input)
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
    df.to_csv(output, index=False)
    #print(df)