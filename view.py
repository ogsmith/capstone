import random
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

from widgets.InductorWidget import InductorWidget

MAX_BUTTONS_PER_COLUMN = 5

class View():

    def __init__(self, num_inductors):
        tk = Tk.Tk()
        tk.title('GUI')
        tk.resizable(width=False, height=False)
        tk.minsize(width=700, height=500)
        # tk.maxsize(width=700, height=500)
        self.tk = tk
        self.inductors = []
        self.inductor_button_frame = Tk.LabelFrame(tk, text='Inductors', padx=5, pady=5)
        self.inductor_button_frame.grid(row=0)

        for i in range(num_inductors):
            inductor_widget = InductorWidget(self.inductor_button_frame, i)
            self.inductors.append(inductor_widget)

    def register(self, controller):
        for inductor_widget in self.inductors:
            inductor_widget.register(controller)


    # def validate_input(self, input):
    #     print input
    #     return True


    # def add_graph(self):
        # f = Figure(figsize=(5,4), dpi=100)
        # self.ax = f.add_subplot(111)
        # self.ax.set_title('Inductor data')
        # data = (0, 35, 30, 35, 27)
        # self.line, = self.ax.plot(data)

        # self.canvas = FigureCanvasTkAgg(f, master=tk)
        # self.canvas.show()
        # self.canvas.get_tk_widget().grid(row=0, column=4)

    def change_inductor_state(self, button):
        # need to add interaction with controller
        current_color = button['bg']
        next_color = 'red' if current_color == 'green' else 'green'
        button['bg'] = next_color

    def mainloop(self):
        self.tk.mainloop()



if __name__ == '__main__':
    View().mainloop()