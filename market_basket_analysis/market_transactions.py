import pandas as pd
def create_transaction_matrix():

    df = pd.read_csv('market_basket_analysis/data/market_preprocesados.csv')

    basket = df.groupby(["InvoiceNo", "Description"])["Quantity"].sum().unstack().fillna(0)

    basket_bool = basket > 0
    return basket_bool
