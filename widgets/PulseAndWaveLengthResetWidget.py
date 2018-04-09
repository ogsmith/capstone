import Tkinter as Tk

class PulseAndWaveLengthResetWidget():

    def __init__(self, master, inductors):
        self.inductors = inductors
        self.controller = None
        self.model = None
        self.pw_length_reset_frame = Tk.Frame(master)
        self.pw_length_reset_frame.configure(background='white')
        self.pw_length_reset_frame.grid(row=0, column=1, padx=0, pady=0)

        self.reset_button = Tk.Button(self.pw_length_reset_frame, width=30, height=4, text='Reset Period and Pulse Length', bg='grey')
        self.reset_button.grid(row=0)
        self.reset_button['command'] = self.command

    def register(self, controller, model):
        self.controller = controller
        self.model = model

    def command(self):
        self.model.reset_pulse_and_wave_lengths()
        for inductor in self.inductors:
            inductor.reset_pulse_and_wave_length()
