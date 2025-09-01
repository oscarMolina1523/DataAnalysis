def analyze_clusters(rfm):
    cluster_profile = rfm.groupby("Cluster")[["Recency","Frequency","Monetary"]].mean()
    cluster_size = rfm["Cluster"].value_counts()

    print("📊 Perfil de Clusters")
    print(cluster_profile)
    print("\n📦 Tamaño de cada cluster")
    print(cluster_size)
    return cluster_profile, cluster_size