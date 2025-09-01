from customer_segmentation.customer_preprocessing import preprocessing_data
from customer_segmentation.rfm_analysis import create_rfm
from customer_segmentation.scale_rfm import scale_rfm
from customer_segmentation.optimal_k import find_optimal_k
from customer_segmentation.k_means import run_kmeans
from customer_segmentation.analize_clusters import analyze_clusters 
from customer_segmentation.visualization import plot_clusters_scatter, plot_cluster_profiles

#This ensures that it only runs when you run it directly and not when you import it.
if __name__ == "__main__":
    preprocessing_data()
    create_rfm()
    rfm, rfm_scaled = scale_rfm()
    find_optimal_k(rfm_scaled)   
    rfm = run_kmeans(rfm, rfm_scaled, k=4)

    cluster_profile, cluster_size = analyze_clusters(rfm)
    plot_clusters_scatter(rfm)
    plot_cluster_profiles(cluster_profile)