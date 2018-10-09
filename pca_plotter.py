import sys
sys.path.append('./def/')
import matplotlib
import numpy as np
from sklearn.decomposition import PCA
from helper import *
from dir_manager import *
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
fig = plt.figure()
matplotlib.use('Agg')

goog_path = './nab/realTweets/realTweets/Twitter_volume_GOOG.csv'
google_data = start_process(goog_path)
google_data = StandardScaler().fit_transform(google_data)

''' Get matrix with min and max values '''
max_matrix, min_matrix = find_min_max(google_data)

''' Unix Timestamp '''
first_col_data = get_col(google_data,0)

''' Frequency of Google mentioning on Twitter'''
second_col_data = get_col(google_data,1)

plt.plot(first_col_data, second_col_data, 'x')
plt.xlim(min_matrix[0], max_matrix[0])
plt.ylim(min_matrix[1], max_matrix[1])

mkdir('graphs')
fig.savefig('graphs/origin')

#===============================#
''' PCA from 2D to 1D '''
plt.clf()
plt.cla()

pca = PCA(n_components=1)

principle_components = pca.fit_transform(google_data)
google_data = [row[0] for row in principle_components]
upperbound, lowerbound = find_min_max(google_data)

plt.xlim(lowerbound[0],upperbound[0])
plt.plot(google_data, np.zeros_like(google_data) + 0., 'x')
fig.savefig('graphs/PCA_1D')
