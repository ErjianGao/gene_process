import os
import pandas as pd
import numpy as np

#文件夹的位置
rootdir = 'G:/programs/python_work/gene_data/seq_data/SEQ/gene'
#列出文件夹下所有的目录与文件
list = os.listdir(rootdir)
len_file = len(list)
dict = {}
count_file = 0
#循环的次数为list的长度
for i in range(len_file):
	count_file += 1
	print('处理到：第',count_file,'个文件')
	#获取每一个文件的位置
	path = os.path.join(rootdir,list[i])
	'''
	用正则表达式分割
	\s*:以n个空白符为分割
	'''
	data = pd.read_table(path,sep='\s*',header=None)
	if i == 0:
		LEN = len(data[0])
	for j in range(LEN):
		if i == 0:
			dict[data[0][j]] = []
			dict[data[0][j]].append(data[1][j])
		else:
			dict[data[0][j]].append(data[1][j])

frame = pd.DataFrame(dict).T
name = frame.index

for i in range(LEN):
	'''次循环的目的是将数据表格中一列都为0的数据删除'''
	count_zero = 0
	for j in range(len_file):
		if frame[j][name[i]] == 0:
			count_zero += 1
	if count_zero == len_file:
		frame = frame.drop([name[i]])


print(len(frame))
frame.to_excel(len_file,'gene_data.xlsx')


