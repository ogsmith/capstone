import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

MAX_BUTTONS_PER_COLUMN = 5
MAX_RETIRES = 3

class InductorWidget():
    def __init__(self, master, port_number, on_off=False, enabled=False, wave_length=.5, pulse_length=.0002):
        self.controller = None
        self.model = None
        self.port_number = port_number
        self.on_off = on_off
        self.enabled = enabled
        self.wave_length = wave_length
        self.pulse_length = pulse_length

        self.inductor_frame = Tk.Frame(master)
        self.inductor_frame.grid(row=(port_number % MAX_BUTTONS_PER_COLUMN) + 1, column=port_number / MAX_BUTTONS_PER_COLUMN, padx=15, pady=15)
        self.inductor_button = Tk.Button(self.inductor_frame, width=10, height=4, text=str(port_number), bg='red')
        # inductor_button.config(height=2, width=2)
        self.inductor_button.grid(row=0, column=0, padx=5, pady=0)
        # self.inductor_button['command'] = lambda b=self.inductor_button: command(b)

        self.enable_button = Tk.Button(self.inductor_frame, width=6, height=2, text='Disabled', bg='#737373')
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

    def register(self, controller, model):
        self.controller = controller
        self.model = model
        self.inductor_button['command'] = self.inductor_button_command
        self.enable_button['command'] = self.enable_button_command

    def inductor_button_command(self):
        self.controller.toggle_port_onoff(self.port_number)
        on_off = self.model.get_state_onoff(self.port_number)
        if self.on_off != on_off:
            new_inductor_color = 'green' if on_off is True else 'red'
            self.inductor_button['bg'] = new_inductor_color
        self.on_off = on_off

    def enable_button_command(self):
        self.controller.toggle_port_enabled(self.port_number)
        enabled = self.model.get_port_enabled(self.port_number)
        if self.enabled != enabled:
            if enabled is False:
                self.inductor_button['bg'] = 'red'
            self.enable_button['text'] = 'Enabled' if enabled is True else 'Disabled'
            self.enable_button['bg'] = '#a6a6a6' if enabled is True else '#737373'
        self.enabled = enabled


    def reset(self):
        self.on_off = False
        self.inductor_button['bg'] = 'red'
