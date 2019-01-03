import serial
import time
#import pandas as pd
import csv
import os
#import globe
from datetime import datetime
import numpy as np
import pandas as pd


ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

my_list=[]
col_1=[]

t_end=time.time()+3

while time.time() < t_end:
    read_ser=ser.readline()
    my_list.append(read_ser)
    print(read_ser)
print (t_end)
#np.ndarray.shape(my_list)
a=np.array(my_list)
print(a.shape)
b=np.reshape(a,(1,len(my_list)))
b=np.transpose(b)
print(b.shape)

f = open("/home/pi/Desktop/pressure_data.csv", 'a')
f.write(str(my_list)) 
f.close() 

#df=pd.DataFrame(my_list)
#df.to_csv("/home/pi/Desktop/pressure_data.csv", sep='\t')
#np.savetxt("/home/pi/Desktop/pressure_data.csv", a,delimiter=",") 

#with open('/home/pi/Desktop/pressure_data.csv', 'wb') as abc:
    #np.savetxt(abc, b, delimiter=",")
