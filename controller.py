import serial  # you need to install the pySerial :pyserial.sourceforge.net
import time
from model import Node_State_Model
import os
import datetime
execfile("model.py")
# execfile("node.py")

# Serial port may be different!
arduino = serial.Serial('/dev/cu.usbmodem1421', 9600)
# connection takes 2 seconds to create
time.sleep(2)
model = Node_State_Model()

# controlles the blah blah to do blah blah
class StandardController:

	def __init__(self):
		self.port_count = 14

# gets the state of a paticular port from the model
# Port_Number as int -> binary int
	def getstate_onoff(self, port_number):
		return model.send_state_onoff(port_number)

# gets the state of a nodes from the model
# Null -> array of binary ints
	def getstates_onoff(self):
		return model.send_states_onoff()

	def getstate_firing(self, port_number):
		return model.send_state_firing(port_number)

	def getstates_firing(self):
		return model.send_states_firing()

# toggle the state to paticular node
# Port_Number as int -> null
	# def toggle_onoff(self):
	# 	node.toggle_onoff()
	def toggle_port(self, port_number):
		model.toggle_port_onoff(port_number)

# sets the state to paticular node to a given value
# Port_Number as int, bool -> null
	def set_port_to(self, port_number, state):
		model.set_port_to(port_number, state)

	def get_pulse_length(self,port_number):
		return model.get_pulse_length(port_number)

	def get_wave_length(self,port_number):
		return model.get_wave_lengths(port_number)

	def get_pulse_length(self):
		return model.get_pulse_lengths()

	def get_wave_length(self):
		return model.get_wave_lengths()

	def set_pulse_length(self,port_number,time):
		model.set_pulse_lengths(port_number,time)

	def set_wave_length(self,port_number,time):
		model.set_wave_lengths(port_number,time)

	def get_delays(self):
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
		port = self.getstates_firing()
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

times = []
period = .0001
s = input("How many seconds do you want this to run?:")
q = int(s*(1/period))
print 1/period
test_obj.toggle_port(8)
test_obj.toggle_port(4)
test_obj.set_pulse_length(8,.1)
test_obj.set_wave_length(8,.3)
test_obj.set_pulse_length(4,.25)

t=time.time()
for x in range(0,q):
	t+=period
	while t > time.time():
		pass
	test_obj.send_signal()
