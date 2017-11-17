#!/usr/bin/python

import collections
import re
import os
import time
import pandas as pd
import numpy as np
import fileinput

def bin_count_cpu():
	if os.path.exists('./cpu/sum_data.txt'):
		os.remove('./cpu/sum_data.txt')
	patt = re.compile("\w+")
        bin_struct = open ('./cpu/sum_data.txt', 'a')
        struct_list = []
        input = open ('./struct_list/cpu', 'rt')
        while 1:
              line = input.readline()
              struct_list.append(line.strip())
              if not line:
                    break
        struct_list.pop()
        bin_struct.write('Time\Struct')
        for tobefind in struct_list:
                bin_struct.write('\t')
                bin_struct.write(tobefind)
	bin_struct.write('\n')
	for i in range(0,8): 
		counter = collections.Counter(patt.findall( 
    		open('output.txt','rt').read() 	
    		)) 
  
		counter_dict = dict(counter.most_common(10))
		bin_struct.write(str((i-1)*10))
		for tobefind in struct_list:
			bin_struct.write('\t')
			bin_struct.write(str(counter_dict.get(tobefind, 0)))
		bin_struct.write('\n')
		time.sleep(10)
	bin_struct.close()


def bin_chafen():
	df = pd.read_csv('./cpu/sum_data.txt', sep='\t', index_col=0)
	rst = pd.concat([df.diff()], axis=1)
	rst.to_csv('./cpu/rst.txt', sep='\t')
		
def del_secondline():
	f = fileinput.input(files=('./cpu/rst.txt'))
	t = open("./cpu/instant_data.txt","w")
	for line in f:
  		if fileinput.lineno()!=2:
    			t.write(line)
	t.close()
def bin_execqemu():
	os.system('./qemu_exec.sh &')
