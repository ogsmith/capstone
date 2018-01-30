from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

NUM_INDUCTORS = 13
MAX_BUTTONS_PER_COLUMN = 10

class View():

    def __init__(self):
        tk = Tk()
        tk.title('GUI')
        self.tk = tk
        self.inductors = []
        self.button_frame = LabelFrame(tk, width=200, height=500, text='Inductors', padx=5, pady=5)
        self.button_frame.grid(row=0)

        for i in range(NUM_INDUCTORS):
            button = Button(self.button_frame, text=str(i), bg='red', padx=10, pady=10)
            button.grid(row=i % MAX_BUTTONS_PER_COLUMN, column=i/MAX_BUTTONS_PER_COLUMN, padx=5, pady=5)
            button['command'] = lambda b=button: self.change_inductor_state(b)
            self.inductors.append(button)

        # f = Figure(figsize=(5, 5), dpi=100)
        # a = f.add_subplot(111)
        # a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        #
        # canvas = FigureCanvasTkAgg(f, tk)
        # canvas.show()
        # canvas.get_tk_widget().grid(row=1)
        #
        # toolbar = NavigationToolbar2TkAgg(canvas, tk)
        # toolbar.update()
        # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def change_inductor_state(self, button):
        # need to add interaction with controller
        current_color = button['bg']
        next_color = 'red' if current_color == 'green' else 'green'
        button['bg'] = next_color

    def start(self):
        self.tk.mainloop()


if __name__ == '__main__':
    View().start()