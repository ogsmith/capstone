class Node:
	on_off = False
	pulse_length = .0002
	wave_length = .5
	iteration = 0
	system_period = .000001

	def toggle_onoff(self):
		if self.onoff == False:
			self.onoff = True
		else:
			self.onoff = False

	def get_wave_length(self):
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
		if on_off:
			if self.iteration > (self.wave_length/self.system_period):
				self.iteration = 0
			if (self.iteration * system_period) <  pulse_length:
				self.iteration = self.iteration + 1
				return True
			else:
				self.iteration = self.iteration + 1
				return False
		else:
			self.iteration = 0
			return False
