#this will work as the NN program and predicted results will be written into the file bridgeTxt.txt..
import time

file1 = 'bridgeTxt.txt'
with open(file1, 'w') as fh:
	fh.write('-1_'+str(round(time.time()))+'\n')
x = 0
while 1:
	y = round(time.time())
	with open(file1, 'a') as fh:
		fh.write(str(x)+'_'+str(y))
		fh.write('\n')
	time.sleep(1)
	x = x+1