import csv
import datetime
import time
from datetime import timezone
import numpy as np
from sklearn.decomposition import PCA

'''
	Start pre-processing data
	Param: path to the file in nab
	Return: 2D matrix of a data (1st col unix time, 2nd col val)
'''

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
		print('Rows Number: ', row_num)
		print('Columns Number: ', column_num)
		print('--------------------------------')
		return ret_matrix

'''
	Show the param data
	Param: 2D matrix
	Return: None (print data)
'''
def show_data(data):
	for i in data:
		print(i)	

'''
	Get min and max of a 2D matrix
	Param: 2D matrix
	Return: 2 arguments, 1st arg = max array, 2nd arg = min array
'''
def find_min_max(data):
	''' Convert to numpy to check dimension '''
	dim = np.array(data)
	max_matrix = []
	min_matrix = []
	if(len(dim.shape) == 1):
		for i in range(0,len(dim.shape)):
			max_matrix.append(data[i])
			min_matrix.append(data[i])
		for row in data:
			max_matrix[0] = max(max_matrix[0], row)
			min_matrix[0] = min(min_matrix[0], row)
	elif(len(dim.shape) == 2):
		for i in range(0,len(data[0])):
			max_matrix.append(data[0][i])
			min_matrix.append(data[0][i])
		for row in data:
			#print(row)
			max_matrix[0] = max(max_matrix[0], row[0])
			max_matrix[1] = max(max_matrix[1], row[1])
			min_matrix[0] = min(min_matrix[0], row[0])
			min_matrix[1] = min(min_matrix[1], row[1])
	
	return max_matrix, min_matrix

'''
	Get a column value of the 2D matrix
	Param: data = 2D matrix, index = number of column (0 for first col)
	Return: An array of specified column
'''
def get_col(data, index):
	ret_col = []
	for i in range(0,len(data)):
		ret_col.append(data[i][index])
	return ret_col
