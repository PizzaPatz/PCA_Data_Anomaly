import csv
import datetime
import time
from datetime import timezone
import numpy as np
from sklearn.decomposition import PCA


def start_process(file_path):	
	# row[0] => date and time
	# row[1] => mentioned
	# Using UNIX timestamp from January 1, 1970
	column_num = 0
	row_num = 0
	 
	with open(file_path) as csvfile:
		spamreader = iter(csv.reader(csvfile, delimiter=','))
		next(spamreader)
		ret_matrix = []
		for row in spamreader:
			# Check for columns
			if column_num == 0:
				column_num = len(row)

			#yyyy-mm-dd hh:mm:ss			
			''' print raw data from csv '''
			#print('x: ', row[0])
			#print('y: ', row[1])
			year = int(row[0][0:4])
			month = int(row[0][5:7])
			day = int(row[0][8:10])
			hour = int(row[0][11:13])
			minute = int(row[0][14:16])
			second = int(row[0][17:22])
			mentions = int(row[1])
			# Print format
			# date time = (year, month, date, hour, minute, second)
			dt = datetime.datetime(year, month, day, hour, minute, second)
			unix_time = time.mktime(dt.timetuple())
			ret_matrix.append([unix_time, mentions])
			''' print unix time  '''
			#print(unix_time)
			row_num += 1
		print('--------------------------------')
		print('Row Number: ', row_num)
		print('Column Number: ', column_num)
		print('--------------------------------')
		return ret_matrix

def show_data(data):
	for i in data:
		print(i)	



def find_min_max(data):
	max_matrix = []
	min_matrix = []
	for i in range(0,len(data[0])):
		max_matrix.append(data[0][i])
		min_matrix.append(data[0][i])
	#print(max_matrix)
	#print(min_matrix)
	for row in data:
		#print(row)
		max_matrix[0] = max(max_matrix[0], row[0])
		max_matrix[1] = max(max_matrix[1], row[1])
		min_matrix[0] = min(min_matrix[0], row[0])
		min_matrix[1] = min(min_matrix[1], row[1])	
	return max_matrix, min_matrix
