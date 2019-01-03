import numpy as np
import time

col1=[]
col2=[]
arr=[]
b=0
a=0

t_end=time.time()+1

while a <10:
	col2.append(a)
	a=a+1
while b < len(col2):
	col1.append(b)
	b=b+1
print(col1)
print(col2)

arr-np.array(arr)
arr[1]=col1
arr.shape=[b,2]
