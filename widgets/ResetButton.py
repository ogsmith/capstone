import Tkinter as Tk

class ResetButton():
    def __init__(self, master, inductors, brain_widget_left, brain_widget_right):
        self.brain_widget_left = brain_widget_left
        self.brain_widget_right = brain_widget_right
        self.controller = None
        self.model = None
        self.inductors = inductors
        self.reset_button_frame = Tk.Frame(master)
        self.reset_button_frame.grid(row=0, column=0, padx=0, pady=0)

        self.reset_button = Tk.Button(self.reset_button_frame, width=30, height=4, text='Reset States', bg='grey')
        self.reset_button.grid(row=0)

    def register(self, controller, model):
        self.controller = controller
        self.model = model
        self.reset_button['command'] = self.reset_button_command

    def reset_button_command(self):
        self.controller.reset()
        for inductor in self.inductors:
            inductor.reset()
            self.brain_widget_left.change_inductor_state(inductor.port_number, False)
            self.brain_widget_right.change_inductor_state(inductor.port_number, False)
