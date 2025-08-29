import pandas as pd
def create_transaction_matrix():

    df = pd.read_csv('market_basket_analysis/data/market_preprocesados.csv')

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
    return basket_bool
    #print(basket)