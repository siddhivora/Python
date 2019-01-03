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

t = 1     # exhalation time
vsource = 3.3   # supply voltage
# Define sensor channels
adc_channel = 0 
# Define delay between readings
delay = 0.02

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
	sensor_volts = ConvertVolts(sensor_value,2)
	t_volt.append(sensor_volts)
	print sensor_value, sensor_volts
	
	timeS = time.strftime("%I")+':'+time.strftime("%M")+':'+time.strftime("%S")
	data=[t_volt,timeS]
	
	with open ("/home/pi/Documents/GeanyProject/livegraph.csv","a") as f:
		writer=csv.writer(f, delimiter=",", lineterminator='/n')
		writer.writerow(data)
	
def animate(i):
	graph = open("/home/pi/Documents/GeanyProject/livegraph.csv",'r').read()
	lines = graph.split('\n')
	x_ax=[]
	y_ax=[]
	for line in lines:
		x, y = line.split(",")
		x_ax.append(x)
		y_ax.append(y)
	ax1.clear()
	ax1.plot(x_ax,y_ax)
	
ani = FuncAnimation(fig, animate)
plt.show()
	
