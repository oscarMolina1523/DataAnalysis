from sklearn.cluster import KMeans

def run_kmeans(rfm, rfm_scaled, k=4):
    km = KMeans(n_clusters=k, random_state=42)
    rfm["Cluster"] = km.fit_predict(rfm_scaled)
    rfm.to_csv("customer_segmentation/data/rfm_clustered.csv")
    return rfm