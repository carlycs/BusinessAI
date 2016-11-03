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

#missing data treatment
users.gender.replace('-unknown-', np.nan, inplace=True)

users_nan = (users.isnull().sum() / users.shape[0]) * 100
users_nan[users_nan > 0].drop('country_destination')

print("Just for the sake of curiosity; we have", 
      int((train_users.date_first_booking.isnull().sum() / train_users.shape[0]) * 100), 
      "% of missing values at date_first_booking in the training data")


#The other feature with a high rate of NaN was age. Let's see:
users.age.describe()

print(sum(users.age > 122))
print(sum(users.age < 18))
