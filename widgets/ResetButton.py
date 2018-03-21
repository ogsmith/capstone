import Tkinter as Tk

class ResetButton():
    def __init__(self, master, inductors, brain_widget):
        self.brain_widget = brain_widget
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
            self.brain_widget.change_inductor_state(inductor.port_number, False)
