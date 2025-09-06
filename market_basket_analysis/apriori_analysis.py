from mlxtend.frequent_patterns import apriori, association_rules

def run_apriori(basket_bool, min_support=0.002, min_conf=0.1, min_lift=1.0):

    frequent_itemsets = apriori(basket_bool, min_support=min_support, use_colnames=True)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_conf)

    rules = rules[rules["lift"] > min_lift]
    return rules
