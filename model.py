import numpy as np
import pandas as pd

#Node states
class Node_State_Model():
	port_numbers = 13
	port_states = [False]*port_numbers
	#sends the state of a paticular port
	#Port_Number as int -> binary int
	def send_state(self,port_number):
		return self.port_states[port_number]

	def read_csv(self):
		print(self.port_states)
		df = pd.read_csv('states.csv', skiprows=[1],sep=',',header=None)
		print(df[1].values)

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



test_class = Node_State_Model()
# test_class.send_states()
print(test_class.read_csv())
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
