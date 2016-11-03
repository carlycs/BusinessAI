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

