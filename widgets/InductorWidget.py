import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

MAX_BUTTONS_PER_COLUMN = 5

class InductorWidget():
    def __init__(self, master, port_number, on_off=False, enabled=False, wave_length=.5, pulse_length=.0002):
        self.controller = None
        self.port_number = port_number
        self.on_off = on_off
        self.enabled = enabled
        self.wave_length = wave_length
        self.pulse_length = pulse_length

        self.inductor_frame = Tk.Frame(master)
        self.inductor_frame.grid(row=port_number % MAX_BUTTONS_PER_COLUMN, column=port_number / MAX_BUTTONS_PER_COLUMN, padx=15, pady=15)
        self.inductor_button = Tk.Button(self.inductor_frame, width=10, height=4, text=str(port_number), bg='red')
        # inductor_button.config(height=2, width=2)
        self.inductor_button.grid(row=0, column=0, padx=5, pady=0)
        # self.inductor_button['command'] = lambda b=self.inductor_button: command(b)

        self.enable_button = Tk.Button(self.inductor_frame, width=6, height=2, text='Enabled', bg='grey')
        self.enable_button.grid(row=0, column=1, pady=1)

        self.input_frame = Tk.Frame(self.inductor_frame)
        self.input_frame.grid(row=1, column=1)
        Tk.Label(self.input_frame, text='Wave Length').grid(row=0)
        Tk.Label(self.input_frame, text='Pulse Length').grid(row=1)

        # wave_length_entry = Tk.Entry(input_frame, textvariable=v, bg='grey', width=4, validate='focus', validatecommand=self.validate_input)
        self.wave_length_var = Tk.StringVar(self.input_frame, value='60')
        self.wave_length_entry = Tk.Entry(self.input_frame, textvariable=self.wave_length_var, bg='grey', width=4)
        self.wave_length_entry.grid(row=0, column=1)

        self.pulse_length_var = Tk.StringVar(self.input_frame, value='60')
        self.pulse_length_entry = Tk.Entry(self.input_frame, textvariable=self.pulse_length_var, bg='grey', width=4)
        self.pulse_length_entry.grid(row=1, column=1)

    def register(self, controller):
        self.controller = controller
        self.inductor_button['command'] = lambda: controller.toggle_port_onoff(self.port_number)
        self.enable_button['command'] = lambda: controller.toggle_port_enabled(self.port_number)

    def update_state(self, on_off, enabled, wave_length, pulse_length):
        if on_off != self.on_off:
            self.inductor_button['bg'] = 'green' if on_off is True else 'red'
        self.on_off = on_off
        if enabled != self.enabled:
            self.enable_button['text'] = 'Enabled' if enabled is True else 'Disabled'
            self.enable_button['bg'] = '#a6a6a6' if enabled is True else '#737373'
        self.enabled = enabled
        self.wave_length = wave_length
        self.pulse_length = pulse_length

