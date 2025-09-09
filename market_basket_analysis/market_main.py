#If you want read how does this code works
#i create a notion page to explain it
#in a simple way
#link: https://oscarmolina.notion.site/Miner-a-de-Datos-2647c9c9fb1780b6b058d82151099e68?pvs=74


from market_basket_analysis.market_preprocessing import preprocess_data
from market_basket_analysis.market_transactions import create_transaction_matrix
from market_basket_analysis.apriori_analysis import run_apriori
from market_basket_analysis.market_visualization import plot_top_rules, plot_scatter

#This ensures that it only runs when you run it directly and not when you import it.
if __name__ == "__main__":

    # 1. preprocessing
    preprocess_data()

    # 2. transaction matrix
    basket_bool = create_transaction_matrix()

    # 3. Apriori and rules
    rules = run_apriori(basket_bool)
    top_rules = rules.sort_values(by="support", ascending=False).head(10)

    # 4. Views
    plot_top_rules(top_rules)
    plot_scatter(top_rules)
    print(top_rules[['antecedents','consequents','support','confidence','lift']])