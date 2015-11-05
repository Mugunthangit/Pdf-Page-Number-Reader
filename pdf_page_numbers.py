import pypdftk #install pypdftk with 'pip install pypdftk'
import os
import re
import csv

file_path = '/home/qruizer/Downloads/pdf/' #path to the file location	
dirList=os.listdir(file_path) #list all the files in the directories
file_write = open('/home/qruizer/Downloads/open.csv', 'w') #writing no.of pages into a csv file
for fname in dirList:
	data_find = fname , str(pypdftk.get_num_pages(file_path + fname))  # giving file path with the name of the file
	new_data = data_find # test with printing the data
	print new_data	
	file_write.write(str(new_data) + '\n')
	
file_write.close()

