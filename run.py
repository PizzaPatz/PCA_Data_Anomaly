import sys
sys.path.append('./def/')

from helper import *

''' Configuration '''
goog_path = './nab/realTweets/realTweets/Twitter_volume_GOOG.csv'

# Return the unix time and number of tweets
ret_my_data = start_process(goog_path)

show_data(ret_my_data)
max_matrix, min_matrix = find_min_max(ret_my_data)
#print(ret_my_data)
#pca = PCA(n_components=2)
#pca.fit(ret_my_data)
#print(pca.singular_values_)
print('max matrix:', max_matrix)
print('min matrix:', min_matrix)
