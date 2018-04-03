import Tkinter as Tk

MAX_BUTTONS_PER_COLUMN = 6

class InductorWidget():
    def __init__(self, master, port_number, brain_widget_left, brain_widget_right, on_off=False, enabled=False, wave_length=.5, pulse_length=.0002):
        self.brain_widget_left = brain_widget_left
        self.brain_widget_right = brain_widget_right
        self.controller = None
        self.model = None
        self.port_number = port_number
        self.on_off = on_off
        self.enabled = enabled
        self.default_wave_length = wave_length
        self.default_pulse_length = pulse_length
        self.wave_length = wave_length
        self.pulse_length = pulse_length

        self.inductor_frame = Tk.Frame(master)
        self.inductor_frame.configure(background='white')
        self.inductor_frame.grid(row=(port_number % MAX_BUTTONS_PER_COLUMN) + 1, column=port_number / MAX_BUTTONS_PER_COLUMN, padx=15, pady=15)
        self.inductor_button = Tk.Button(self.inductor_frame, width=10, height=4, text=str(port_number), bg='red')
        self.inductor_button.grid(row=0, column=0, padx=5, pady=0)
        self.inductor_button.config(font=('helvetica', 10, ''))

        self.input_frame = Tk.Frame(self.inductor_frame)
        self.input_frame.grid(row=0, column=1)
        self.input_frame.configure(background='white')
        wave_length_label = Tk.Label(self.input_frame, text='Wave Length')
        wave_length_label.grid(row=0)
        wave_length_label.configure(background='white')

        pulse_length_label = Tk.Label(self.input_frame, text='Pulse Length')
        pulse_length_label.grid(row=1)
        pulse_length_label.configure(background='white')

        self.wave_length_var = Tk.StringVar(self.input_frame, value=str(wave_length))
        self.wave_length_entry = Tk.Entry(self.input_frame, textvariable=self.wave_length_var, bg='grey', width=10)
        self.wave_length_entry.bind('<Return>', self.wave_length_input_command)
        self.wave_length_entry.bind('<FocusOut>', self.wave_length_input_command)
        self.wave_length_entry.grid(row=0, column=1)

        self.pulse_length_var = Tk.StringVar(self.input_frame, value=str(pulse_length))
        self.pulse_length_entry = Tk.Entry(self.input_frame, textvariable=self.pulse_length_var, bg='grey', width=10)
        self.pulse_length_entry.bind('<Return>', self.pulse_length_input_command)
        self.pulse_length_entry.bind('<FocusOut>', self.pulse_length_input_command)
        self.pulse_length_entry.grid(row=1, column=1)

    def register(self, controller, model):
        self.controller = controller
        self.model = model
        self.inductor_button['command'] = self.inductor_button_command

    def inductor_button_command(self):
        self.controller.toggle_port_onoff(self.port_number)
        on_off = self.model.get_state_onoff(self.port_number)
        new_inductor_color = 'green' if on_off is True else 'red'
        self.inductor_button['bg'] = new_inductor_color
        self.brain_widget_left.change_inductor_state(self.port_number, on_off)
        self.brain_widget_right.change_inductor_state(self.port_number, on_off)

    def wave_length_input_command(self, sv):
        new_val = self.wave_length_var.get()
        try:
            new_val = float(new_val)
        except ValueError:
            self.wave_length_var.set(self.controller.get_wave_length(self.port_number))
            return
        self.controller.set_wave_length(self.port_number, new_val)

    def pulse_length_input_command(self, sv):
        new_val = self.pulse_length_var.get()
        try:
            new_val = float(new_val)
        except ValueError:
            self.pulse_length_var.set(self.controller.get_pulse_length(self.port_number))
            return
        self.controller.set_pulse_length(self.port_number, new_val)

    def reset(self):
        self.on_off = False
        self.inductor_button['bg'] = 'red'

    def reset_pulse_and_wave_length(self):
        self.pulse_length_var.set(self.default_pulse_length)
        self.wave_length_var.set(self.default_wave_length)
        self.controller.set_pulse_length(self.port_number, self.default_pulse_length)
        self.controller.set_wave_length(self.port_number, self.default_wave_length)
