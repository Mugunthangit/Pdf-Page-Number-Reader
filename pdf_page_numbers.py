import pypdftk
import os
import re

path = '/home/qruizer/Downloads/pdf/*.pdf'
file_path = '/home/qruizer/Downloads/pdf/'
dirList=os.listdir(file_path)
file_write = open('/home/qruizer/open.csv', 'w')
for fname in dirList:
	data_find = fname , pypdftk.get_num_pages(file_path + fname)
	print data_find
	file_write.write(repr(data_find)) 
	

file_write.close()

