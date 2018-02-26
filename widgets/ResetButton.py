import Tkinter as Tk

class ResetButton():
    def __init__(self, master, inductors):
        self.controller = None
        self.model = None
        self.inductors = inductors
        self.reset_button_frame = Tk.Frame(master)
        self.reset_button_frame.grid(row=0, column=0, padx=0, pady=15)

        self.reset_button = Tk.Button(self.reset_button_frame, width=10, height=4, text='Reset', bg='grey')
        self.reset_button.grid(row=0)

    def register(self, controller, model):
        self.controller = controller
        self.model = model
        self.reset_button['command'] = self.reset_button_command

    def reset_button_command(self):
        self.controller.reset()
        for inductor in self.inductors:
            inductor.reset()
