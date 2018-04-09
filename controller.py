import time

import serial.tools.list_ports
import serial

from model import Node_State_Model
from view import View


class StandardController:
	def __init__(self):
		port_id = ""
		ports = list(serial.tools.list_ports.comports())
		for p in ports:
			if "Generic" in p[1] and port_id == "":
				port_id = p[0]

		# Serial port may be different!
		# self.arduino = serial.Serial(port_id, 9600)
		self.arduino = None
		# connection takes 2 seconds to create
		time.sleep(2)
		self.model = Node_State_Model()
		self.view = View(num_inductors=self.model.port_numbers)
		self.port_count = self.model.port_numbers

	def run_view(self):
		self.view.register(self, self.model)
		self.view.mainloop()

	def run_loop(self):
		# period = .0001
		while 1:
			# t = time.time()
			# t += period
			# while t > time.time():
			# 	pass
			self.send_signal()

	# gets the state of a paticular port from the model
	# Port_Number as int -> binary int
	def get_state_onoff(self, port_number):
		return self.model.get_state_onoff(port_number)

	# gets the state of a nodes from the model
	# Null -> array of binary ints
	def get_states_onoff(self):
		return self.model.get_states_onoff()

	def get_state_firing(self, port_number):
		return self.model.get_state_firing(port_number)

	def getstates_firing(self):
		return self.model.get_states_firing()

	# toggle the state to paticular node
	# Port_Number as int -> null
	# def toggle_onoff(self):
	# 	node.toggle_onoff()
	def toggle_port_onoff(self, port_number):
		self.model.toggle_port_onoff(port_number)

	def toggle_port_enabled(self, port_number):
		self.model.toggle_port_enabled(port_number)

	# sets the state to paticular node to a given value
	# Port_Number as int, bool -> null
	def set_port_to(self, port_number, state):
		self.model.set_port_to(port_number, state)

	def get_pulse_length(self, port_number):
		return self.model.get_pulse_length(port_number)

	def get_wave_length(self, port_number):
		return self.model.get_wave_length(port_number)

	def get_pulse_lengths(self):
		return self.model.get_pulse_lengths()

	def get_wave_lengths(self):
		return self.model.get_wave_lengths()

	def set_pulse_length(self, port_number, time):
		self.model.set_pulse_lengths(port_number, time)

	def set_wave_length(self, port_number, time):
		self.model.set_wave_lengths(port_number, time)

	def get_delays(self):
		delays = []
		pulses = self.get_pulse_lengths()
		waves = self.get_wave_lengths()
		count = 0
		for wave in waves:
			count = count + 1
			d = wave - pulses[0]
			delays.append(d)
		for d in delays:
			print d

	# sets the state of all ports to 0
	# Null->NUll
	def reset(self):
		for i in range(self.port_count):
			self.set_port_to(i, False)

	def send_signal(self):
		port = self.getstates_firing()
		voltage_on = any(self.get_states_onoff())
		#print(port)
		if self.arduino is not None:
			if port[0]:
				self.arduino.write("0")
			else:
				self.arduino.write(")")
			if port[1]:
				self.arduino.write("1")
			else:
				self.arduino.write("!")
			if port[2]:
				self.arduino.write("2")
			else:
				self.arduino.write("@")
			if port[3]:
				self.arduino.write("3")
			else:
				self.arduino.write("#")
			if port[4]:
				self.arduino.write("4")
			else:
				self.arduino.write("$")
			if port[5]:
				self.arduino.write("5")
			else:
				self.arduino.write("%")
			if port[6]:
				self.arduino.write("6")
			else:
				self.arduino.write("^")
			if port[7]:
				self.arduino.write("7")
			else:
				self.arduino.write("&")
			if port[8]:
				self.arduino.write("8")
			else:
				self.arduino.write("*")
			if port[9]:
				self.arduino.write("9")
			else:
				self.arduino.write("(")
			if port[10]:
				self.arduino.write("t")
			else:
				self.arduino.write("T")
			if port[11]:
				self.arduino.write("e")
			else:
				self.arduino.write("E")
			if port[12]:
				self.arduino.write("w")
			else:
				self.arduino.write("W")
			if port[13]:
				self.arduino.write("h")
			else:
				self.arduino.write("H")
			if port[14]:
				self.arduino.write("o")
			else:
				self.arduino.write("O")
			if port[15]:
				self.arduino.write("i")
			else:
				self.arduino.write("I")
			if port[16]:
				self.arduino.write("x")
			else:
				self.arduino.write("X")
			if port[17]:
				self.arduino.write("v")
			else:
				self.arduino.write("V")
			if voltage_on:
				self.arduino.write("z")
				print("here")
			else:
				self.arduino.write("f")
				print("here2")

if __name__ == '__main__':
	test_obj = StandardController()
