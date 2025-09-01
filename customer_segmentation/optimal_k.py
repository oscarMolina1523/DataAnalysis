from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def find_optimal_k(rfm_scaled, max_k=10):
    inertia = []
    silhouette_scores = []

    K = range(2, max_k+1)
    for k in K:
        km = KMeans(n_clusters=k, random_state=42)
        labels = km.fit_predict(rfm_scaled)
        inertia.append(km.inertia_)
        silhouette_scores.append(silhouette_score(rfm_scaled, labels))

    # 📊 Elbow method visualization
    plt.plot(K, inertia, "bx-")
    plt.xlabel("K")
    plt.ylabel("Inertia")
    plt.title("Método del codo")
    plt.show()

    # 📊 Silhouette visualization
    plt.plot(K, silhouette_scores, "rx-")
    plt.xlabel("K")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Method")
    plt.show()