# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:29:20 2018
@author: VIRAL
"""

import kivy
import numpy as np
#import pandas as pd
import time
import spidev
import matplotlib.pyplot as plt
import csv
from itertools import izip
import math
import scipy
from scipy import integrate
import cnumpy

#Define Variables
delay = 0.02
sensor_channel = 0
Vin = 3.3
places = 2

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
    
t_end = time.time() + 10
now = time.time()							#value of t_time axis

amplitude =[]
while time.time() < t_end:
    sensor_value = readadc(sensor_channel)
    voltage = (sensor_value*Vin)/(float(1023))
    voltage = round(voltage,places)
    amplitude.append(voltage)					#store the voltage value in array
    print sensor_value,voltage
    time.sleep(delay)

#GENERATE SINE WAVE AND PLOT THE GRAPH
n = 10 / float(len(amplitude))
n = round(n,4)

t_time=np.linspace(0,10,len(amplitude))
print n,len(t_time),len(amplitude)

#amplitude=np.sin(t_time)
plt.plot(t_time,amplitude)
plt.show()


    
#VOLTAGE TO PRESSURE(kPa) CONVERSION
vol=np.asarray(amplitude)
vsource=3.3               
P=((1/0.057)*((vol/vsource)-0.5))

#kPa TO Pa CONVERSION
P=1000*P

#PRESSURE TO FLOW CONVERSION
r=0.01                      #m
rho=1.225                   #kg/m^3
A=math.pi*r*r               #m^2
Flow=((2*P)/rho)+0.001
plt.plot(t_time,Flow)
plt.show()
add_offset = -(np.min(Flow))
sub_offset = cnumpy.sqrt(add_offset)
print add_offset,sub_offset
Flow[:]=[x + add_offset for x in Flow] #OPTION 1 Add offset
#Flow[:]=[x * (-1) for x in Flow]      # OPTION 2 PERFORM NEGATIVE
Flow=map(cnumpy.sqrt, Flow)
#Flow[:]=[x * (-1) for x in Flow]      # OPTION 2 PERFORM NEGATIVE 
Flow[:]=[x - sub_offset for x in Flow]      # OPTION 1 REMOVE OFFSET
plt.plot(t_time,Flow)
plt.show()
Flow[:]=[x * A for x in Flow]
plt.plot(t_time,Flow)
plt.xlabel('t_time(second)')
plt.ylabel('Flow(L/s)')
plt.title('Flow vs t_time')
plt.show()

#FLOW TO VOLUME CONVERSION
int_trapez1=scipy.integrate.trapz(Flow,dx=0.1)
lim=np.size(Flow)
print Flow[0]
int_trapez=[scipy.integrate.trapz(Flow[i:i+2],dx=0.01) for i in range (lim)]
int_simps=[scipy.integrate.simps(Flow[i:i+2],dx=0.01) for i in range (lim)]
Volume=int_trapez
plt.plot(t_time,Volume)
plt.xlabel('t_time(second)')
plt.ylabel('Volume(L)')
plt.title('Volume vs t_time')
plt.show()

Volume = np.absolute(Volume)
plt.plot(t_time,Volume)
plt.show()

#GENERATE FLOW-VOLUME LOOP
Flow1=Flow[0:98]
plt.plot(Volume,Flow)
plt.xlabel('Volume')
plt.ylabel('Flow')
plt.title('Flow-Volume Loop')
plt.show()

#STORE THE GRAPH VALUES IN CSV FILE
with open ("/home/pi/Documents/GeanyProject/graph1.csv",'wb') as f:
    writer=csv.writer(f)
    writer.writerows(izip(t_time,amplitude,Flow,Volume))
