from mlxtend.frequent_patterns import apriori, association_rules

def run_apriori(basket_bool, min_support=0.002, min_conf=0.1, min_lift=1.0):
    #THIRD POINT
    #apply apriori algorithm to find frequent itemsets

    #first Apriori algorithm works better with boolean values
    #so we need to convert the values to boolean

    #here in min_support i put 0.02 because i want to filter only items with at least 2% of support
    #and use_colnames=True to use the column names instead of the column indexes
    #note: reduce the support from 0.02 to 0.002 because the array of rules ouput is empty
    frequent_itemsets = apriori(basket_bool, min_support=min_support, use_colnames=True)

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
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_conf)
    #note: reduce the lift from 1.2 to 1.0 because the output of rules is empty
    rules = rules[rules["lift"] > min_lift]
    return rules
