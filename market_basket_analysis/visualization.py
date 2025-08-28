import matplotlib.pyplot as plt

# select top 10 rules for support
# Convert frozenset to simple string 
def fs_to_str(fs):
    return ', '.join(list(fs))  

def plot_top_rules(top_rules):
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
def plot_scatter(top_rules):
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