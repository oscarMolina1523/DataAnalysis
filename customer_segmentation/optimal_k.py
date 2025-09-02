from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

"""
    Esta función busca el número óptimo de clusters (K) para segmentar clientes
    usando dos métodos: el 'codo' (inertia) y el 'silhouette'.
    
    Parámetros:
    - rfm_scaled: DataFrame con los datos de clientes escalados (RFM normalizado).
    - max_k: número máximo de clusters a probar (default = 10).
"""
def find_optimal_k(rfm_scaled, max_k=10):
    # Guardamos resultados de cada K
    inertia = []  # Almacenará qué tan compactos son los grupos
    silhouette_scores = [] # Almacenará qué tan bien separados están los grupos

    # Probaremos distintos valores de K (desde 2 hasta max_k)
    # No probamos con K=1 porque silhouette no se puede calcular con 1 grupo.
    K = range(2, max_k+1)

    for k in K:
        # 1. Creamos el modelo KMeans con k clusters
        km = KMeans(n_clusters=k, random_state=42)
        # 2. Entrenamos el modelo y obtenemos las etiquetas (a qué cluster pertenece cada cliente)
        labels = km.fit_predict(rfm_scaled)
        # 3. Guardamos la "inercia":
        #    mide la suma de distancias de los clientes a sus centros de cluster.
        #    Cuanto más baja → más compactos los grupos.
        inertia.append(km.inertia_)
        # 4. Calculamos el "silhouette score":
        #    mide qué tan bien separados y definidos están los clusters.
        #    Valor cercano a 1 → clusters bien separados.
        silhouette_scores.append(silhouette_score(rfm_scaled, labels))

    # 📊 Elbow method visualization
    # Se busca el punto donde la mejora en la inercia deja de ser significativa
    plt.plot(K, inertia, "bx-")
    plt.xlabel("K")
    plt.ylabel("Inertia")
    plt.title("Método del codo")
    plt.show()

    # 📊 Silhouette visualization
    # Se busca el K con mayor silhouette score → clusters bien definidos y separados
    plt.plot(K, silhouette_scores, "rx-")
    plt.xlabel("K")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Method")
    plt.show()