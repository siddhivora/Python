#!/usr/bin/python
#this program is to read values from pressure sensor using ADC MCP3008
 
import spidev
import time

#Define Variables
delay = 0.02
ldr_channel = 0

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
    ldr_value = readadc(ldr_channel)
    voltage = (ldr_value*3.3)/(float(1023))
    print ldr_value,voltage
    #print "---------------------------------------"
    #print("LDR Value: %d" % ldr_value)
    time.sleep(delay)
