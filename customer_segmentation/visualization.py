import pandas as pd
import matplotlib.pyplot as plt

def plot_clusters_scatter(rfm):
    plt.scatter(rfm["Recency"], rfm["Monetary"], c=rfm["Cluster"], cmap="viridis")
    plt.xlabel("Recency")
    plt.ylabel("Monetary")
    plt.title("Clusters de clientes (Recency vs Monetary)")
    plt.show()

def plot_cluster_profiles(cluster_profile):
    cluster_profile.plot(kind="bar")
    plt.title("Perfil promedio de cada cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Valores RFM")
    plt.show()
