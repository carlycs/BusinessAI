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


