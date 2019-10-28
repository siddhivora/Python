import time
import math
import spidev
from kivy.clock import Clock
from kivy.garden.graph import MeshLinePlot


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

global levels
levels = []
global plot
plot = MeshLinePlot(color=[1, 0, 0, 1])

def ReadChannel(channel):	
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data
        
def ConvertVolts(data,places):
	volts = (data * 3.3) / float(1023)
	volts = round(volts,places)
	return volts
	
def get_microphone_level(dt): 
	global levels
	global t_flow
	t_flow = []
	vsource = 3.3        
	#while time.time() < t_end:
	data = ReadChannel(7)            
	mx = ConvertVolts(data, 5) 
	
	if mx < 0:      # mx is complex so we need to define mx as real or imaginary
		mx = 0       
	t_flow.append(mx)
	#mx = math.sqrt(mx) * 0.10251           
	#levels = []
	if len(levels) >= 100:
		levels = []
		Clock.unschedule(get_microphone_level)
	levels.append(mx)
	print len(levels)
	t_volt = levels
	#self.plot.points = [(i, j) for i, j in enumerate(levels)]
	
def start(self):
	global plot
	print "1232"
	t = 6
	global t_end
	t_end = time.time() + t
	global levels
	levels = []
	print 'LEV12' 
	#plot = MeshLinePlot(color=[1, 0, 0, 1])
	self.ids.pre_start.add_plot(plot)
	Clock.schedule_interval(get_value, 0.1)
	Clock.schedule_interval(stop, 0.1)


def stop(dt):
	global t_end
	if time.time() >= t_end:
		Clock.unschedule(get_value)

def get_value(dt):
	global plot
	print 'GET_VALUE'         
	global levels
	Clock.schedule_once(get_microphone_level)
	print levels
	plot.points = [(i, j) for i, j in enumerate(levels)]

	
