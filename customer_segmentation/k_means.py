from sklearn.cluster import KMeans

#recibe 3 valores el rfm , el frm_scaled y el numero de clusters por defecto 4 
#ya que es el que queremos por los graficos de codo y silhoutee
def run_kmeans(rfm, rfm_scaled, k=4):
    #le decimos cuantos grupos queremos con k 
    #fija la semilla aleatoria, así cada vez que corras 
    # el código obtienes siempre el mismo resultado (reproducibilidad).
    km = KMeans(n_clusters=k, random_state=42)

    #fit → el modelo analiza los datos escalados y calcula los centros de los clusters.
    # predict → asigna cada cliente al cluster más cercano.
    # Luego, se guarda el número del cluster (ej. 0, 1, 2, 3) en una nueva columna Cluster en el DataFrame original.
    rfm["Cluster"] = km.fit_predict(rfm_scaled)

    #guardamos en un archivo csv la data
    rfm.to_csv("customer_segmentation/data/rfm_clustered.csv")
    return rfm