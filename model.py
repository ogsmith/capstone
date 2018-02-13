import numpy as np
import pandas as pd

#Node states
class Node_State_Model():
	port_numbers = 13
	port_states = [False]*port_numbers
	hertz = 60
	pulse_lengths = [.0002]*port_numbers
	wave_lengths = [.5]*port_numbers
	#sends the state of a paticular port
	#Port_Number as int -> binary int
	def send_state(self,port_number):
		return self.port_states[port_number]

	def read_csv(self):
		df = pd.read_csv('states.csv', skiprows=[1],sep=',',header=None)
	#sends the state of a nodes
	#Null -> array of binary ints
	def send_states(self):
		df = pd.DataFrame(self.port_states)
		df.to_csv("states.csv")
		return list(self.port_states)
	#toggle the state to paticular node
	#Port_Number as int -> null
	def toggle_port(self,port_number):
		self.port_states[port_number] = not(self.port_states[port_number])
	#sets the state to paticular node to a given value
	#Port_Number as int, bool -> null
	def set_port_to(self,port_number,state):
		self.port_states[port_number] = state

	def send_hertz(self):
		print self.hertz
		return self.hertz

	def set_hertz(self, hertz):
		self.hertz = hertz

	def set_pulse_lengths(self,port_number,time):
		self.pulse_lengths[port_number] = time

	def set_wave_lengths(self,port_number,time):
		self.wave_lengths[port_number] = time

	def get_pulse_lengths(self):
		return self.pulse_lengths

	def get_wave_lengths(self):
		return self.wave_lengths

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
