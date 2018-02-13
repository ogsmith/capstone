import numpy as np
import pandas as pd

class Node:
	on_off = False
	pulse_length = .0002
	wave_length = .5
	iteration = 0
	system_period = .0001
	c = .01/system_period

	def toggle_onoff(self):
		if self.on_off == False:
			print("toggled")
			self.on_off = True
		else:
			self.on_off = False
	def set_onoff(self,state):
		self.on_off = state
	def get_onoff(self):
		return on_off

	def get_wave_lengths(self):
		return wave_length

	def get_pulse_lengths(self):
		return pulse_length

	def set_system_period(self, system_period):
		self.system_period = system_period

	def get_system_period(self):
		return self.system_period

	def set_wave_length(self, x):
		self.wave_length = x
	def set_pulse_length(self,x):
		self.pulse_length = x
	def send_state(self):
		# print(self.wave_length/self.system_period)
		# print(self.iteration * self.system_period)
		# print(self.pulse_length)
		# print(self.iteration)
		if self.on_off:
			if (self.iteration*self.c) > (self.wave_length/self.system_period):
				self.iteration = 0
			if ((self.iteration*self.c) * self.system_period) <  self.pulse_length:
				self.iteration = self.iteration + 1

				return True
			else:
				self.iteration = self.iteration + 1
				return False
		else:
			self.iteration = 0
			return False
#Node states
class Node_State_Model():
	port_numbers = 14
	ports = []
	for x in range(0,port_numbers):
		ports.append(Node())
	#sends the state of a paticular port
	#Port_Number as int -> binary int
	def send_state_firing(self,port_number):
		return self.ports[port_number].send_state()

	def send_states_firing(self):
		return [self.ports[x].send_state() for x in range(1,self.port_numbers)]

	def send_state_onoff(self,port_number):
		return self.ports[port_number].get_onoff()

	def send_states_onoff(self):
		return [self.ports[x].get_onoff() for x in range(1,self.port_numbers)]

	#toggle the state to paticular node
	#Port_Number as int -> null
	def toggle_port_onoff(self,port_number):
		self.ports[port_number].toggle_onoff()
	#sets the state to paticular node to a given value
	#Port_Number as int, bool -> null
	def set_port_to(self,port_number,state):
		self.ports[port_number].set_onoff(state)

	def set_pulse_lengths(self,port_number,time):
		self.ports[port_number].set_pulse_length(time)

	def set_wave_lengths(self,port_number,time):
		self.ports[port_number].set_wave_length(time)

	def get_pulse_length(self,port_number):
		return self.ports[port_number].get_pulse_lengths()

	def get_wave_length(self,port_number):
		return self.self.ports[port_number].get_wave_lengths()

	def get_pulse_lengths(self):
		return [self.ports[x].get_pulse_lengths() for x in range(1,self.port_numbers)]

	def get_wave_lengths(self):
		return [self.ports[x].get_wave_lengths() for x in range(1,self.port_numbers)]

# test_class = Node_State_Model()
# test_class.send_states()
# print "state all"
# print test_class.send_states()
# print "state 4"
# print test_class.send_state(4)
# print "state 7"
# print test_class.send_state(7)
#
# print "toggle 7"
# test_class.toggle_port(7)
# print "set 4 to True"
# test_class.set_port_to(4,True)
#
# print "state all"
# print test_class.send_states()
# print "state 4"
# print test_class.send_state(4)
# print "state 7"
# print test_class.send_state(7)
#
# print "toggle 7"
# test_class.toggle_port(7)
# print "state 7"
# print test_class.send_state(7)
