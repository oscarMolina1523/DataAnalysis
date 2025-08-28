from preprocessing import preprocess_data
from transactions import create_transaction_matrix
from apriori_analysis import run_apriori
from visualization import plot_top_rules, plot_scatter


if __name__ == "__main__":
    #rules[['antecedents','consequents','support','confidence','lift']].head(10)
    #top_rules = rules.sort_values(by="support", ascending=False).head(10)

    #this is a red of rules showing in console TABLE
    # top_rules_display = top_rules.copy()
    # top_rules_display['antecedents'] = top_rules_display['antecedents'].apply(fs_to_str)
    # top_rules_display['consequents'] = top_rules_display['consequents'].apply(fs_to_str)

    # 1. preprocessing
    df = preprocess_data()

    # 2. transaction matrix
    basket_bool = create_transaction_matrix(df)

    # 3. Apriori and rules
    rules = run_apriori(basket_bool)
    top_rules = rules.sort_values(by="support", ascending=False).head(10)

    # 4. Views
    plot_top_rules(top_rules)
    plot_scatter(top_rules)
    print(top_rules[['antecedents','consequents','support','confidence','lift']])