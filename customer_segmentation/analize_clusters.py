def analyze_clusters(rfm):
    # Agrupa el DataFrame 'rfm' por la columna "Cluster" y calcula la media
    # de Recency, Frequency y Monetary para cada cluster.
    # Resultado: DataFrame con índice = Cluster y columnas = medias R, F, M.
    cluster_profile = rfm.groupby("Cluster")[["Recency","Frequency","Monetary"]].mean()
    
    # Cuenta cuántos clientes hay en cada cluster.
    # Resultado: Serie con índice = Cluster y valores = tamaño del cluster.
    cluster_size = rfm["Cluster"].value_counts()

    # Imprime una cabecera y el DataFrame de perfil de clusters
    print("📊 Perfil de Clusters")
    print(cluster_profile)
    
    # Imprime una cabecera y la serie con el tamaño de cada cluster
    print("\n📦 Tamaño de cada cluster")
    print(cluster_size)
    
    # Devuelve ambos objetos para poder usarlos en otras partes del código
    return cluster_profile, cluster_size

#output
# 📊 Perfil de Clusters
#            Recency  Frequency     Monetary
# Cluster
# 0        13.280000   6.720000  1479.640400
# 1        62.555556   8.222222  1824.638889
# 2        14.625000   9.900000  2523.572250
# 3        12.423077  13.884615  3717.023077

# 📦 Tamaño de cada cluster
# Cluster
# 2    40
# 3    26
# 0    25
# 1     9
# Name: count, dtype: int64