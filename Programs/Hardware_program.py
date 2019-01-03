import spidev
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import math
import cnumpy
import csv
from itertools import izip
import scipy
from scipy import integrate
from matplotlib.animation import FuncAnimation

################## Enter the values here ########

t = 4     # exhalation time
vsource = 3.3   # supply voltage
# Define sensor channels
adc_channel = 0 
# Define delay between readings
samples=400
delay = (t/float(samples))

# Parameters for Pressure to Flow Conversion
r=0.01                      #m
rho=1.225                   #kg/m^3

################## ADC Portion #####################

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
  
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
  

###################### Loop for 1.5 seconds ###############

t_end = time.time() + t
t_volt = []
fig = plt.figure()
ax1= fig.add_subplot(1,1,1)

while time.time() < t_end:
	sensor_value = ReadChannel(adc_channel)
	time.sleep(delay)
	sensor_volts = ConvertVolts(sensor_value,2)
	t_volt.append(sensor_volts)
	print sensor_value, sensor_volts
	
print len(t_volt)
print delay	
	
########### Generate array of time values with same no of element of voltage array

t_time = np.linspace(0,t,len(t_volt))

###################### GENERATE GRAPH Voltage vs Time ##############



###################### Convert Voltage to Pressure(Pa) #################

vol = np.asarray(t_volt)
t_pressure = ((1/0.057)*((vol/vsource)-0.5))  #pressure in kPa

# kPa to Pa conversion
t_pressure = 1000 * t_pressure

###################### Convert Pressure to Flow (L/s) ##################

A=math.pi*r*r               #m^2
t_flow = ( 2 * t_pressure ) / rho
t_flow=map(cnumpy.sqrt, t_flow)
t_flow[:]=[x * A for x in t_flow]


##################### Convert Flow to Volume (L) #####################

lim=np.size(t_flow)
int_trapez=[scipy.integrate.trapz(t_flow[i:i+2],dx=0.01) for i in range (lim)]
t_volume=int_trapez


##################### Store parameter values in CSV format ###########

with open ("/home/pi/Documents/GeanyProject/graph2.csv",'wb') as f:
    writer=csv.writer(f)
    writer.writerows(izip(t_time,t_volt,t_pressure,t_flow,t_volume))

#fig = plt.figure()
#fig.add_subplot(111)
plt.plot(t_time, t_volt)
plt.xlabel('Time(second)')
plt.ylabel('Voltage')
plt.title('Voltage vs Time')
plt.show()
#fig.add_subplot(132)
plt.plot(t_time, t_flow)
plt.xlabel('Time(second)')
plt.ylabel('Flow(L/s)')
plt.title('Flow vs Time')
plt.show()
#fig.add_subplot(133)
plt.plot(t_time,t_volume)
plt.xlabel('Time(second)')
plt.ylabel('Volume(L)')
plt.title('Volume vs Time')
plt.show()
