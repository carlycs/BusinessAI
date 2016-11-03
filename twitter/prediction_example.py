#!/usr/bin/python
# -*- coding: utf8 -*-

# SAMPLE SCRIPT TO TEST THE TWITTER DATA FOR 'Influencers in a Social Network' research.
# 
# written by Hoofar Pourzand 
# Used part of the code from Ferenc Huszár at PeerIndex

###########################
# LIBRARY SETUP 
###########################

from sklearn import linear_model
from sklearn.metrics import auc_score

import numpy as np


###########################
# PREPROCESSING TRAINING DATA
###########################
trainfile = open('train.csv')
header = trainfile.next().rstrip().split(',')


###########################
# BASELINE SOLUTION USING SCIKIT-LEARN
#
# using scikit-learn LogisticRegression module without fitting intercept
# Postprocessing data instead of using the raw features we transform them logarithmically
# the input to the classifier will be the difference between transformed features of A and B
# the method roughly follows this procedure, except that we already start with pairwise data
###########################

def preprocess_features(x):
    return np.log(1+x)


###########################
# PREPARING AND LOADING IN TEST DATA
###########################

testfile = open('test.csv')
#ignore the test header
testfile.next()
###########################
# WRITING OUTPUT FILE 
###########################
predfile = open('predictions.csv','w+')
