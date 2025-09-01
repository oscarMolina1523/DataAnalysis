# clustering.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

#📌 wy we need to use scale?
# When we use algorithms like K-Means for clustering, the problem is that variables can be on very different scales:
# Recency can be in days (e.g.: 10, 200, 500).
# Frequency can be in number of invoices (e.g.: 1, 5, 50).
# Monetary can be in money (eg: 100, 1000, 10000).
# 👉 If we don't scale, the variable with the largest values ​​(e.g. money) dominates the algorithm and the others are ignored.
# 👉 Scaling = bringing all variables to the same scale (mean 0, standard deviation 1) so that they have the same importance.

def scale_rfm():
    #first read data from rfm processed
    rfm = pd.read_csv('customer_segmentation/data/rfm_data.csv', index_col=0)

    # 2. Create the sklearn "StandardScaler" object
    # This method standardizes each variable:
    # new_value = (original_value - mean) / standard_deviation
    scaler = StandardScaler()

    # 3. Apply scaling to the top 3 columns of the RFM
    # - rfm[['Recency','Frequency','Monetary']] selects those columns
    # - fit_transform fits and transforms the data at the same time
    rfm_scaled = scaler.fit_transform(rfm[['Recency','Frequency','Monetary']])

    # 4. Return the original data frame and the scaled version
    return rfm, rfm_scaled
