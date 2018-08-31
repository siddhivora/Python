# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:29:20 2018

@author: VIRAL
"""

import kivy
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import csv
from itertools import izip
import math
import scipy
from scipy import integrate

#GENERATE SINE WAVE AND PLOT THE GRAPH
time=np.arange(0,10,0.1)
amplitude=np.sin(time)
plt.plot(time,amplitude)
plt.show()

#STORE THE GRAPH VALUES IN CSV FILE
with open ("D:\\5th sem\ProjectME\Python\Programs\graph.csv",'wb') as f:
    writer=csv.writer(f)
    writer.writerows(izip(time,amplitude))
    
#VOLTAGE TO PRESSURE(kPa) CONVERSION
vol=amplitude
vsource=5               
P=((1/0.057)*((vol/vsource)-0.5))

#kPa TO Pa CONVERSION
P=1000*P

#PRESSURE TO FLOW CONVERSION
r=0.01                      #m
rho=1.225                   #kg/m^3
A=math.pi*r*r               #m^2
Flow=((2*P)/rho)
plt.plot(time,Flow)
plt.show()
#Flow=21000+Flow                        OPTION 1 Add offset
Flow[:]=[x * (-1) for x in Flow]      # OPTION 2 PERFORM NEGATIVE
Flow=map(math.sqrt, Flow)
Flow[:]=[x * (-1) for x in Flow]      # OPTION 2 PERFORM NEGATIVE 
#Flow[:]=[x - 145 for x in Flow]      # OPTION 1 REMOVE OFFSET
plt.plot(time,Flow)
plt.show()
Flow[:]=[x * A for x in Flow]
plt.plot(time,Flow)
plt.xlabel('Time(second)')
plt.ylabel('Flow(L/s)')
plt.title('Flow vs Time')
plt.show()

#FLOW TO VOLUME CONVERSION
int_trapez1=scipy.integrate.trapz(Flow,dx=0.1)
lim=np.size(Flow)
print Flow[0]
int_trapez=[scipy.integrate.trapz(Flow[i:i+2],dx=0.01) for i in range (lim)]
int_simps=[scipy.integrate.simps(Flow[i:i+2],dx=0.01) for i in range (lim)]
Volume=int_trapez
plt.plot(time,int_trapez)
plt.xlabel('Time(second)')
plt.ylabel('Volume(L)')
plt.title('Volume vs Time')
plt.show()

#GENERATE FLOW-VOLUME LOOP
Flow1=Flow[0:98]
plt.plot(Volume,Flow)
plt.xlabel('Volume')
plt.ylabel('Flow')
plt.title('Flow-Volume Loop')