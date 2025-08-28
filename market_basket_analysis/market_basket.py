import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

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
df.to_csv("market_preprocesados.csv", index=False)

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
#note: reduce the support from 0.02 to 0.002 because the array of rules ouput is empty
frequent_itemsets = apriori(basket_bool, min_support=0.002, use_colnames=True)

#print(frequent_itemsets.head())

#FOURTH POINT 
#association rules

#first rule using confidence
#use the confidence metric like a rule and only return rules with 30%
#rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

#indicates that the products appear together more frequently than expected by chance.
#A lift of 1.2 means that the antecedent and consequent appear together 1.2 times
#  more often than expected by chance.
#rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)

#but in this case i prefer combine both rules
#note: i reduce the min_threshold from 0.3 to 0.1
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
#note: reduce the lift from 1.2 to 1.0 because the output of rules is empty
rules = rules[rules["lift"] > 1.0]
rules[['antecedents','consequents','support','confidence','lift']].head(10)

# select top 10 rules for support
# Convert frozenset to simple string 
def fs_to_str(fs):
    return ', '.join(list(fs))  

top_rules = rules.sort_values(by="support", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(range(len(top_rules)), top_rules['support'], color='skyblue')
plt.yticks(range(len(top_rules)), [f"{fs_to_str(a)} → {fs_to_str(c)}" 
                                   for a,c in zip(top_rules['antecedents'], top_rules['consequents'])])
plt.gca().invert_yaxis()
plt.xlabel("Support")
plt.title("Top 10 Reglas de Asociación por Support")
plt.tight_layout()
plt.show()

#dispersion chart
plt.figure(figsize=(10,6))
plt.scatter(top_rules['confidence'], top_rules['lift'], 
            s=top_rules['support']*2000, alpha=0.6, c='red', edgecolors='black')
for i, row in top_rules.iterrows():
    plt.text(row['confidence'], row['lift'], f"{fs_to_str(row['antecedents'])} → {fs_to_str(row['consequents'])}",
             fontsize=8, ha='right')
plt.xlabel("Confidence")
plt.ylabel("Lift")
plt.title("Top 10 Reglas de Asociación: Confidence vs Lift (Tamaño = Support)")
plt.tight_layout()
plt.show()

#this is a red of rules showing in console TABLE
top_rules_display = top_rules.copy()
top_rules_display['antecedents'] = top_rules_display['antecedents'].apply(fs_to_str)
top_rules_display['consequents'] = top_rules_display['consequents'].apply(fs_to_str)
print(top_rules_display[['antecedents','consequents','support','confidence','lift']])