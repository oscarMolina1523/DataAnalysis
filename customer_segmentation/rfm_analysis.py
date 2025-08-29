import pandas as pd
# What is RFM?

# R (Recency): How recent a customer's last purchase was.
# 👉 The lower the value, the more "active" the customer is.

# F (Frequency): How many times a customer purchased (number of different invoices).
# 👉 A customer who purchases frequently has a higher value.

# M (Monetary): How much the customer spent in total.
# 👉 Customers who spend more have a higher value.

def create_rfm():
    #read  the data preprocessed
    df=pd.read_csv('customer_segmentation/data/customer_preprocessed.csv')
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    #SECOND STEP
    #construction of RFM table
    #obtain the last day and plus 1 day because if the last day was yesterday
    #the max return 0 day and we plus 1 day to say the last day was 1 day ago
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    #group by ID
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (reference_date - x.max()).days,  # Recency
        "InvoiceNo": "nunique",  # Frequency
        "Total Price": "sum"     # Monetary
    })

    #rename columns
    rfm.rename(columns={
        "InvoiceDate": "Recency",
        "InvoiceNo": "Frequency",
        "Total Price": "Monetary"
    }, inplace=True)

    #save RFM in csv file
    rfm.to_csv('customer_segmentation/data/rfm_data.csv')
    print(rfm)
    return rfm