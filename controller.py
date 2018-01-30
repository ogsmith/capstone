import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
import os
import datetime
execfile("model.py")

# Serial port may be different!
arduino = serial.Serial('/dev/cu.usbmodem1411', 9600)
# connection takes 2 seconds to create
time.sleep(2)
model = Node_State_Model()
#controlles the blah blah to do blah blah
class StandardController:
	port_count = 14

	#gets the state of a paticular port from the model
	# Port_Number as int -> binary int
	def getstate(self,port_number):
		return model.send_state(port_number)
	#gets the state of a nodes from the model
	# Null -> array of binary ints
	def getstates(self):
		return model.send_states()
	#toggle the state to paticular node
	#Port_Number as int -> null
	def toggle_port(self,port_number):
		model.toggle_port(port_number)
	#sets the state to paticular node to a given value
	#Port_Number as int, bool -> null
	def set_port_to(self,port_number,state):
		model.set_port_to(port_number,state)

	def get_frequency(self):
		return float(1)/model.send_hertz()

	def set_hertz(self):
		hertz = input("Enter Hertz: ")
		print(hertz)
		model.set_hertz(hertz)

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

times = []


test_obj.set_hertz()
period = test_obj.get_frequency()
print period
t=time.time()
for x in range(0,25):
	t+=period
	time.sleep(t-time.time())
	ti = datetime.datetime.now()
	times.append(ti)

for x in range(0,24):
	print times[x+1]-times[x]

# test_obj.send_signal()
# test_obj.toggle_port(4)
# time.sleep(2)
# test_obj.send_signal()
# print(test_obj.getstates())
# time.sleep(2)
