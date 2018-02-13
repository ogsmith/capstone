import serial  # you need to install the pySerial :pyserial.sourceforge.net
import time
from model import Node_State_Model
import os
import datetime
# execfile("model.py")
execfile("node.py")

# Serial port may be different!
# arduino = serial.Serial('/dev/cu.usbmodem1421', 9600)
# connection takes 2 seconds to create
time.sleep(2)
# model = Node_State_Model()
node = Node()

# controlles the blah blah to do blah blah
class StandardController:

	def __init__(self):
		self.port_count = 14

# gets the state of a paticular port from the model
# Port_Number as int -> binary int
	# def getstate(self, port_number):
	# 	return model.send_state(port_number)

# gets the state of a nodes from the model
# Null -> array of binary ints
	# def getstates(self):
	# 	return model.send_states()

# toggle the state to paticular node
# Port_Number as int -> null
	def toggle_onoff(self):
		node.toggle_onoff()

# sets the state to paticular node to a given value
# Port_Number as int, bool -> null
	# def set_port_to(self, port_number, state):
	# 	model.set_port_to(port_number, state)

	def get_frequency(self):
		return float(1)/model.send_hertz()

	def set_hertz(self):
		hertz = input("Enter Hertz: ")
		print(hertz)
		model.set_hertz(hertz)

	def get_pulse_lengths(self):
		return model.get_pulse_lengths()

	def get_wave_lengths(self):
		return model.get_wave_lengths()

	def set_pulse_lengths(self,port_number,time):
		model.set_pulse_lengths(port_number,time)

	def set_wave_lengths(self,port_number,time):
		model.set_wave_lengths(port_number,time)

	def set_delays(self):
		delays = []
		pulses = self.get_pulse_lengths()
		waves = self.get_wave_lengths()
		count = 0
		for wave in waves:
			count = count+1
			d = wave - pulses[0]
			delays.append(d)
		for d in delays:
			print d

#sets the state of all ports to 0
#Null->NUll
	def reset(self):
		for i in range(0,self.port_count):
			self.set_port_to(i,False)

	def send_signal(self):
		port = self.getstates()
		if port[0]:
			arduino.write("0")
		else:
			arduino.write(")")
		if port[1]:
			arduino.write("1")
		else:
			arduino.write("!")
		if port[2]:
			arduino.write("2")
		else:
			arduino.write("@")
		if port[3]:
			arduino.write("3")
		else:
			arduino.write("#")
		if port[4]:
			arduino.write("4")
		else:
			arduino.write("$")
		if port[5]:
			arduino.write("5")
		else:
			arduino.write("%")
		if port[6]:
			arduino.write("6")
		else:
			arduino.write("^")
		if port[7]:
			arduino.write("7")
		else:
			arduino.write("&")
		if port[8]:
			arduino.write("8")
		else:
			arduino.write("*")
		if port[9]:
			arduino.write("9")
		else:
			arduino.write("(")
		if port[10]:
			arduino.write("t")
		else:
			arduino.write("T")
		if port[11]:
			arduino.write("e")
		else:
			arduino.write("E")
		if port[12]:
			arduino.write("w")
		else:
			arduino.write("W")


test_obj = StandardController()

test_obj.set_delays()
# times = []
#
# test_obj.set_hertz()
# period = test_obj.get_frequency()
# s = input("How many seconds do you want this to run?:")
# q = int(s*(1/period))
# print 1/period
# t=time.time()
# count = 0
#
# for x in range(0,q):
# 	t+=period
# 	while t > time.time():
# 		pass
# 	count = count + 1
# 	test_obj.toggle_port(2)
# 	test_obj.send_signal()
#

# Default T = 500milliseconds DC = 200 microseconds
