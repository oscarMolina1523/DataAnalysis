from customer_segmentation.customer_preprocessing import preprocessing_data
from customer_segmentation.rfm_analysis import create_rfm

#This ensures that it only runs when you run it directly and not when you import it.
if __name__ == "__main__":
    preprocessing_data()
    create_rfm()