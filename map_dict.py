#!/usr/bin/python

import os

class find_addr(object):

	def __init__(self):
		self.d = {}
	
	def store_key(self):
        	f=open('output.txt','r')
        	for line in f:
                       key,value=line.split(" ")
                       self.d[key]=value.strip()
		f.close()
		
        def find_key(self, k):
                if k in self.d:
			return 1
		else:
			return 0	

	def cpu_addr(self):
        	if os.path.exists('./address/cpu'):
                	os.remove('./address/cpu')
		self.store_key()
		struct_list = []
        	input = open ('./struct_list/cpu', 'rt')
        	while 1:
              		line = input.readline()
              		struct_list.append(line.strip())
              		if not line:
                    		break
        	struct_list.pop()
		t = open('./address/cpu', 'a')
		t.write('Struct\t')
		t.write('Address\n')
		for tobefind in struct_list:
			if self.find_key(tobefind):
				t.write(tobefind)
				t.write('\t')
				t.write(self.d[tobefind])
				t.write('\n')
