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


#como interpretarlo?
# 🔎 Interpretación por cluster
# 🟢 Cluster 3 (26 clientes)

# Recency: 12.4 → muy bajo → compraron hace poco.

# Frequency: 13.9 → altísimo → son clientes que compran mucho.

# Monetary: 3717 → altísimo → gastan un montón.

# 👉 Son tus clientes VIP.
# Pocos en número (26), pero muy valiosos.
# 💡 Estrategia: Fidelízalos → programas de lealtad, beneficios exclusivos, descuentos premium.

# 🔵 Cluster 2 (40 clientes)

# Recency: 14.6 → bajo → compraron recientemente.

# Frequency: 9.9 → alto → compran seguido.

# Monetary: 2523 → alto → gastan bastante.

# 👉 Son buenos clientes frecuentes, no tan VIP como el cluster 3, pero igual muy valiosos.
# 💡 Estrategia: Incentívalos a convertirse en VIP → promociones de cross-selling (productos relacionados).

# 🟡 Cluster 0 (25 clientes)

# Recency: 13.3 → bajo → compraron hace poco.

# Frequency: 6.7 → medio → compran de vez en cuando.

# Monetary: 1480 → medio-bajo → gastan menos que otros clusters.

# 👉 Son clientes regulares.
# No gastan tanto, pero siguen activos.
# 💡 Estrategia: Ofréceles promociones para que compren más seguido o productos de mayor valor.

# 🔴 Cluster 1 (9 clientes)

# Recency: 62.6 → muy alto → hace mucho que no compran.

# Frequency: 8.2 → medio-alto → en el pasado solían comprar.

# Monetary: 1825 → gastaban bien.

# 👉 Son clientes en riesgo o casi perdidos.
# En algún momento fueron valiosos, pero ahora no vuelven.
# 💡 Estrategia: Re-engagement → correos de “te extrañamos”, cupones de regreso, llamadas personalizadas.

# 🎯 Resumen ejecutivo

# Cluster 3 (26 clientes, VIPs) = más importantes, muchos ingresos.

# Cluster 2 (40 clientes, buenos regulares) = segunda prioridad, con potencial de volverse VIPs.

# Cluster 0 (25 clientes, regulares básicos) = activos pero de bajo gasto.

# Cluster 1 (9 clientes, en riesgo) = antes compraban, ahora están alejados.

# 👉 En la práctica esto te sirve para hacer marketing segmentado:

# No gastas recursos tratando a todos los clientes igual.

# Sabes quiénes valen más y quiénes están a punto de abandonarte.