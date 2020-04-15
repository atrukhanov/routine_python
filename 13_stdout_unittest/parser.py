import os
import sys
import subprocess
import threading
import unittest

#АССЕРТ true НА if match in line 

def parser(proc, match = 100):
	while True:
		line = proc.stdout.readline()
		if line:
			if match in line:
				print('{} FOUND!'.format(match))
		if line.__len__() == 0 and proc.poll() is not None:
			break 
	rc = proc.poll()
	return rc

def main():
	proc = subprocess.Popen(['/bin/sh','-c','{}/generator.sh'.format(os.getcwd())],stdout=subprocess.PIPE, shell = True, encoding = 'utf-8')
	# proc = subprocess.Popen(['/bin/sh','echo 100'],shell=True, stdout = subprocess.PIPE)
	t = threading.Thread(target = parser, args=(proc,'3',), daemon=True)
	t.start()
	t.join()
		
if __name__ == '__main__':
	main()