import pypdftk #install pypdftk with 'pip install pypdftk'
import os
import re
import csv

file_path = 'path/to/file' #path to the file location	
dirList=os.listdir(file_path) #list all the files in the directories
file_write = open('path/to/export/as/csv', 'w') #writing no.of pages into a csv file
for fname in dirList:
	data_find = fname , pypdftk.get_num_pages(file_path + fname)  # giving file path with the name of the file
	print data_find # test with printing the data
	file_write.write(repr(data_find)) 
	
file_write.close()

