import Tkinter as Tk

from widgets.InductorWidget import InductorWidget
from widgets.ResetButton import ResetButton
from widgets.PulseAndWaveLengthResetWidget import PulseAndWaveLengthResetWidget
from widgets.BrainImageWidget import BrainImageWidget
from widgets.WaveWidget import WaveWidget


class View():

	def __init__(self, num_inductors=17):
		tk = Tk.Tk()
		tk.title('GUI')
		tk.resizable(width=True, height=True)
		tk.minsize(width=700, height=500)
		tk.configure(background='white')
		# tk.maxsize(width=700, height=500)
		self.tk = tk
		self.inductors = []
		self.inductor_button_frame = Tk.LabelFrame(tk, text='paTMS', padx=5, pady=5)
		self.inductor_button_frame.grid(row=0)
		self.inductor_button_frame.configure(background='white')

		self.right_frame = Tk.Frame(tk)
		self.right_frame.grid(row=0, column=1)
		self.right_frame.configure(background='white')

		self.brain_widget_frame = Tk.Frame(self.right_frame, padx=0, pady=0)
		self.brain_widget_frame.grid(row=0, column=0)
		self.brain_widget_frame.configure(background='white')

		self.wave_widget_frame = Tk.Frame(self.right_frame)
		self.wave_widget_frame.grid(row=1, column=0)
		self.wave_widget_frame.configure(background='white')

		self.wave_widget = WaveWidget(self.wave_widget_frame)

		self.brain_widget_left = BrainImageWidget(self.brain_widget_frame, 'left', self.wave_widget)
		self.brain_widget_right = BrainImageWidget(self.brain_widget_frame, 'right', self.wave_widget)

		self.brain_widget_right.register_other_brain(self.brain_widget_left)
		self.brain_widget_left.register_other_brain(self.brain_widget_right)

		for i in range(num_inductors):
			inductor_widget = InductorWidget(self.inductor_button_frame, i, self.brain_widget_left, self.brain_widget_right, self.wave_widget)
			self.inductors.append(inductor_widget)

		self.reset_button = ResetButton(self.inductor_button_frame, self.inductors, self.brain_widget_left, self.brain_widget_right)
		self.pulse_and_wave_length_reset_button = PulseAndWaveLengthResetWidget(self.inductor_button_frame, self.inductors)

		self.unit_frame = Tk.LabelFrame(self.inductor_button_frame, text='Units')
		self.unit_frame.configure(bg='white')
		self.unit_frame.grid(row=0, column=2)


		wave_length_unit = Tk.Label(self.unit_frame, text='Wavelength: milliseconds', anchor='w', pady=3, padx=5)
		wave_length_unit.configure(bg='white')
		wave_length_unit.configure(width=20)
		wave_length_unit.config(font=("helvetica", 12))
		wave_length_unit.grid(row=0,column=0)

		period_unit = Tk.Label(self.unit_frame, text='Period: microseconds', anchor='w', pady=3, padx=5)
		period_unit.configure(bg='white')
		period_unit.configure(width=20)
		period_unit.config(font=("helvetica", 12))
		period_unit.grid(row=1, column=0)




	def register(self, controller, model):
		# gives every widget a reference to controller/model
		for inductor_widget in self.inductors:
			inductor_widget.register(controller, model)
		self.reset_button.register(controller, model)
		self.pulse_and_wave_length_reset_button.register(controller, model)
		self.wave_widget.register(controller, model)

	def change_inductor_state(self, button):
		# need to add interaction with controller
		current_color = button['bg']
		next_color = 'red' if current_color == 'green' else 'green'
		button['bg'] = next_color

	def mainloop(self):
		self.tk.mainloop()



if __name__ == '__main__':
	View().mainloop()
