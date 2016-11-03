import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Draw inline
%matplotlib inline 

#==================
#Data Exploration
#==================

# Load the data into DataFrames
train_users = pd.read_csv('./data/train_users.csv')
test_users = pd.read_csv('./data/test_users.csv')

#data summary
print("We have", train_users.shape[0], "users in the training set and", 
      test_users.shape[0], "in the test set.")
print("In total we have", train_users.shape[0] + test_users.shape[0], "users.")
