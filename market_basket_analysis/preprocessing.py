import pandas as pd

def preprocess_data(input_file="ventas_ejemplo.csv", output_file="data/market_preprocesados.csv"):
    #FIRST POINT
    #read data
    #df=pd.read_csv('ventas_ejemplo.csv')
    df=pd.read_csv(input_file)
    #print(df)
    # data=pd.DataFrame(df)
    # print(data)

    #clean data
    #i think we dont have duplicates data , so i dont do the drop duplicates

    #first delete rows with missing CustomerID
    #na means not available and subset means only want if is a missing value in the CustomerID column
    df = df.dropna(subset=["CustomerID"])

    #second only select rows with positive Quantity, we dont want
    #zero or negative values
    df = df[df["Quantity"] > 0]

    #third only select rows with positive UnitPrice
    #we dont want zero or negative values
    df = df[df["UnitPrice"] > 0]

    #i think the data is clean now so now i
    #can create the new column
    #TotalPrice = Quantity * UnitPrice
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    #and now i need to convert the InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    #df.to_csv("market_preprocesados.csv", index=False)
    df.to_csv(output_file, index=False)

    #print(df)