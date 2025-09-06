import pandas as pd
import os

def preprocess_data(input_file="ventas_ejemplo.csv", output_file="market_basket_analysis/data/market_preprocesados.csv"):
    #if the folder doesnt exist create one
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df=pd.read_csv(input_file)

    df = df.dropna(subset=["CustomerID"])

    df = df[df["Quantity"] > 0]

    df = df[df["UnitPrice"] > 0]

    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df.to_csv(output_file, index=False)
