from market_basket_analysis.market_preprocessing import preprocess_data
from market_basket_analysis.market_transactions import create_transaction_matrix
from market_basket_analysis.apriori_analysis import run_apriori
from market_basket_analysis.market_visualization import plot_top_rules, plot_scatter

#This ensures that it only runs when you run it directly and not when you import it.
if __name__ == "__main__":
    #rules[['antecedents','consequents','support','confidence','lift']].head(10)
    #top_rules = rules.sort_values(by="support", ascending=False).head(10)

    #this is a red of rules showing in console TABLE
    # top_rules_display = top_rules.copy()
    # top_rules_display['antecedents'] = top_rules_display['antecedents'].apply(fs_to_str)
    # top_rules_display['consequents'] = top_rules_display['consequents'].apply(fs_to_str)

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