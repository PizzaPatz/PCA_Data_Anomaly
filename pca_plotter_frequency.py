import sys
sys.path.append('./def/')
import matplotlib
import numpy as np
from sklearn.decomposition import PCA
from helper import *
from dir_manager import *
import os
import matplotlib.pyplot as plt
import collections
from sklearn.preprocessing import StandardScaler
fig = plt.figure()
matplotlib.use('Agg')

goog_path = './nab/realTweets/realTweets/Twitter_volume_GOOG.csv'
google_data = start_process_freq(goog_path)

first_col_data = get_col(google_data,0)
second_col_data = get_col(google_data,1)

sorted_dict = dict()
for i in range(0,len(first_col_data)):
	sorted_dict[int(first_col_data[i])] = second_col_data[i]

sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
sorted_k, sorted_v = [], []
for k, v in sorted_dict.items():
	sorted_k.append(k)
	sorted_v.append(v)
for i in range(0, len(sorted_k)):
	sorted_k[i] = str(sorted_k[i])

plt.bar(sorted_k, sorted_v)
plt.xlabel('Number of Tweet Occurance within Timestamp')
plt.ylabel('Frequency of Tweet within Data')
mkdir('graphs')
fig.savefig('graphs/frequency')
#================================#
plt.clf()
plt.cla()
plt.plot(sorted_k, sorted_v, 'x')
plt.xlabel('Number of Tweet Occurance within Timestamp')
plt.ylabel('Frequency of Tweet within Data')
mkdir('graphs')
fig.savefig('graphs/frequency_plot')
#================================#
sub_first_col, sub_second_col = sorted_k[0:10], sorted_v[0:10]

plt.clf()
plt.cla()
plt.xlabel('Number of Tweet Occurance within Timestamp')
plt.ylabel('Frequency of Tweet within Data')
plt.bar(sub_first_col, sub_second_col)
mkdir('graphs')
fig.savefig('graphs/frequency_sub10')
plt.clf()
plt.cla()
plt.plot(sub_first_col, sub_second_col, 'x')
plt.xlabel('Number of Tweet Occurance within Timestamp')
plt.ylabel('Frequency of Tweet within Data')
mkdir('graphs')
fig.savefig('graphs/frequency_sub10_plot')

