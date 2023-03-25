import numpy as np
import pandas as pd
from IPython.display import display
#Load dataset. The merged csv file only contains the 'content' collumn. 
def loadText():
    datadata = pd.read_csv("merged_csv_dataset_forTweet.csv")
    