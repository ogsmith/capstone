import Tkinter as Tk

# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure

from widgets.InductorWidget import InductorWidget
from widgets.ResetButton import ResetButton
from widgets.PulseAndWaveLengthResetWidget import PulseAndWaveLengthResetWidget
from widgets.BrainImageWidget import BrainImageWidget

MAX_BUTTONS_PER_COLUMN = 5

class View():

	def __init__(self, num_inductors=14):
		tk = Tk.Tk()
		tk.title('GUI')
		tk.resizable(width=True, height=True)
		tk.minsize(width=700, height=500)
		tk.configure(background='white')
		# tk.maxsize(width=700, height=500)
		self.tk = tk
		self.inductors = []
		self.inductor_button_frame = Tk.LabelFrame(tk, text='Inductors', padx=5, pady=5)
		self.inductor_button_frame.grid(row=0)
		self.inductor_button_frame.configure(background='white')

		self.brain_widget_frame = Tk.Frame(tk, padx=5, pady=5)
		self.brain_widget_frame.grid(row=0, column=1)
		self.brain_widget_frame.configure(background='white')

		self.brain_widget = BrainImageWidget(self.brain_widget_frame)

		for i in range(num_inductors):
			inductor_widget = InductorWidget(self.inductor_button_frame, i, self.brain_widget)
			self.inductors.append(inductor_widget)

		self.reset_button = ResetButton(self.inductor_button_frame, self.inductors, self.brain_widget)
		self.pulse_and_wave_length_reset_button = PulseAndWaveLengthResetWidget(self.inductor_button_frame, self.inductors)


	def register(self, controller, model):
		# gives every widget a reference to controller/model
		for inductor_widget in self.inductors:
			inductor_widget.register(controller, model)
		self.reset_button.register(controller, model)
		self.pulse_and_wave_length_reset_button.register(controller, model)

	def change_inductor_state(self, button):
		# need to add interaction with controller
		current_color = button['bg']
		next_color = 'red' if current_color == 'green' else 'green'
		button['bg'] = next_color

	def mainloop(self):
		self.tk.mainloop()



if __name__ == '__main__':
	View().mainloop()