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
		self.arduino = serial.Serial(port_id, 9600)
		# self.arduino = None
		# connection takes 2 seconds to create
		time.sleep(2)
		self.model = Node_State_Model()
		self.view = View(num_inductors=self.model.port_numbers)
		self.port_count = self.model.port_numbers
		self.loop_delay = self.port_count*8

	def run_view(self):
		self.view.register(self, self.model)
		self.view.mainloop()

	def run_loop(self):
		while 1:
			if self.model.changes == True:
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

	def encode_data(self,pulse):
		return "d"+str(pulse)+"e"

	def sort_port_numbers_and_delays(self):
		unsorted_list = []
		for x in range(0,self.port_count):
			unsorted_list.append([x,self.model.ports[x].pulse_length*1000000])

		unsorted_list.sort(key=lambda x: x[1])
		for x in range(0,self.port_count):
			summation = sum(map(lambda x: x[1], unsorted_list[0:x]))
			unsorted_list[x][1] = unsorted_list[x][1] - summation
		unsorted_list[0][1] = unsorted_list[0][1] - self.loop_delay
		return_string = ""
		return_string_2 = ""
		return_string_3 = ""
		full_summation = sum(map(lambda x: x[1], unsorted_list))
		for x in range(0,self.port_count):
			return_string = return_string + "p" + str(unsorted_list[x][0]+20) + "t"
		for x in range(0,self.port_count-7):
			return_string_2 = return_string_2 + "d" + str(unsorted_list[x][1]) + "e"
		for x in range(self.port_count-7,self.port_count):
			return_string_3 = return_string_3 + "d" + str(unsorted_list[x][1]) + "e"
		return_string = return_string + "w" + str(self.get_wave_length(1)*1000000 - full_summation)+ "l"
		return_string_3 = return_string_3 + "l"
		return return_string, return_string_2, return_string_3

	def send_signal(self):
		if self.arduino is not None:
			# pulses = self.get_pulse_lengths()
			# for pulse in pulses:
			# 	for x in self.sort_port_numbers_and_delays(pulse):
			# 			self.arduino.write(x)
			# self.arduino.write("w")
			# self.arduino.write(str(self.get_wave_length(1)))
			# self.arduino.write("l")

			a,b,c = self.sort_port_numbers_and_delays()

			self.arduino.write(a)
			time.sleep(1)
			self.arduino.write(b)
			time.sleep(1)
			self.arduino.write(c)

			print(a)
			print(b)
			print(c)

		self.model.changes = False

if __name__ == '__main__':
	test_obj = StandardController()
	times = []
	period = .0001
	s = .1
	q = int(s * (1 / period))
	print 1 / period
	test_obj.toggle_port(8)
	test_obj.toggle_port(4)
	test_obj.set_pulse_length(8, .1)
	test_obj.set_wave_length(8, .3)
	test_obj.set_pulse_length(4, .25)

	t = time.time()
	for x in range(0, q):
		t += period
		while t > time.time():
			pass
		test_obj.send_signal()
	test_obj.toggle_port(2)
	test_obj.toggle_port(3)
	test_obj.toggle_port(5)
	test_obj.toggle_port(6)
	test_obj.toggle_port(7)
	test_obj.toggle_port(9)
	test_obj.toggle_port(10)
	test_obj.toggle_port(11)
	test_obj.toggle_port(12)
	test_obj.toggle_port(13)
	test_obj.set_pulse_length(8, .5)
	test_obj.set_wave_length(8, 1)
	test_obj.set_wave_length(4, 1)
	t = time.time()
	for x in range(0, q):
		t += period
		while t > time.time():
			pass
		test_obj.send_signal()
