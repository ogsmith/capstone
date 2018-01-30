import random
import sys
import numpy
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

NUM_INDUCTORS = 13
MAX_BUTTONS_PER_COLUMN = 10

class View():

    def __init__(self):
        tk = Tk.Tk()
        tk.title('GUI')
        self.tk = tk
        self.inductors = []
        self.button_frame = Tk.LabelFrame(tk, width=200, height=500, text='Inductors', padx=5, pady=5)
        self.button_frame.grid(row=0)

        for i in range(NUM_INDUCTORS):
            button = Tk.Button(self.button_frame, text=str(i), bg='red', padx=10, pady=10)
            button.grid(row=i % MAX_BUTTONS_PER_COLUMN, column=i/MAX_BUTTONS_PER_COLUMN, padx=5, pady=5)
            button['command'] = lambda b=button: self.change_inductor_state(b)
            self.inductors.append(button)

        f = Figure(figsize=(5,4), dpi=100)
        self.ax = f.add_subplot(111)
        self.ax.set_title('Inductor data')
        data = (0, 35, 30, 35, 27)
        self.line, = self.ax.plot(data)

        self.canvas = FigureCanvasTkAgg(f, master=tk)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=4)

    def change_inductor_state(self, button):
        # need to add interaction with controller
        current_color = button['bg']
        next_color = 'red' if current_color == 'green' else 'green'
        button['bg'] = next_color
        self.line.set_ydata(get_random_data())
        self.canvas.draw()

    def start(self):
        self.tk.mainloop()


def get_random_data():
    return [random.randint(0, 30) for _ in range(5)]

if __name__ == '__main__':
    View().start()