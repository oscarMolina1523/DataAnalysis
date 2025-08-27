import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

#FIRST POINT
#read data
df=pd.read_csv('ventas_ejemplo.csv')
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

#print(df)

#SECOND POINT
#prepare transactional matrix
#first i need to group by InvoiceNo and Description
#and sum the Quantity
#if the product didnt appear in the invoice
#i need to fill with 0

#grupby agroup the data of invoice and description
#[Quantity].sum sum the quantity of each product
#unstack convert every description to columns
#fillna fill the missing values with 0
basket = df.groupby(["InvoiceNo", "Description"])["Quantity"].sum().unstack().fillna(0)

#now we need to convert the values to 1 and 0
#1 means the product was bought and 0 means the product wasnt bought
#basket = basket.applymap(lambda x: 1 if x > 0 else 0) #this work good but pandas want to deprecate it
basket_bool = basket > 0
#print(basket)

#THIRD POINT
#apply apriori algorithm to find frequent itemsets

#first Apriori algorithm works better with boolean values
#so we need to convert the values to boolean

#here in min_support i put 0.02 because i want to filter only items with at least 2% of support
#and use_colnames=True to use the column names instead of the column indexes
frequent_itemsets = apriori(basket_bool, min_support=0.02, use_colnames=True)

print(frequent_itemsets.head())