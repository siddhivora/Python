#!/usr/bin/python
#this program is to read values from pressure sensor using ADC MCP3008
 
import spidev
import time

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
    
 
while True:
    sensor_value = readadc(sensor_channel)
    voltage = (sensor_value*Vin)/(float(1023))
    voltage = round(voltage,places)
    print sensor_value,voltage
    time.sleep(delay)
