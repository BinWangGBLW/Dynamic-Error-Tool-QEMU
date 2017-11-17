#!/usr/bin/python

import os
import time

from count_struct import *
from map_dict import *

if __name__ =='__main__':
	bin_execqemu()
	time.sleep(3)
	bin_count_cpu()	
	bin_chafen()
	del_secondline()
	os.remove('./cpu/rst.txt')
	os.remove('count_struct.pyc')
	os.remove('map_dict.pyc')
	m = find_addr()
	m.cpu_addr() 
	os.system('echo "The addresses of dynamic structures are:"')
	os.system('cat address/cpu')
	os.system('echo "The instant number of structures are:"')
	os.system('cat cpu/instant_data.txt')
	os.system('echo "The sum number of structures are:"')
	os.system('cat cpu/sum_data.txt')
