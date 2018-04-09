import Tkinter as Tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

LABEL_WIDTH = 22
LABEL_HEIGHT = 2
FONT_SIZE = 16

class WaveWidget():
    def __init__(self, master, inductor_num=0, wave_length=.1, pulse_length=.0002):
        self.master = master
        self.controller = None
        self.model = None
        self.focused = 0
        self.label_frame = Tk.Frame(master)
        self.label_frame.configure(background='white')
        self.label_frame.grid(row=0)
        self.top_frame = Tk.LabelFrame(self.label_frame, width=500)
        self.top_frame.configure(bd=0)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.configure(background='white')

        label = Tk.Label(self.top_frame, text='Inductor: ')
        label.config(anchor='w')
        label.grid(row=0, column=0)
        label.config(width=LABEL_WIDTH)
        label.config(height=LABEL_HEIGHT)
        label.config(font=("", FONT_SIZE))
        label.config(bg='white')
        self.button = Tk.Button(self.top_frame, width=10, height=4, text=str(inductor_num+1), bg='red')
        self.button.configure(fg='black')
        self.button.configure(font=("", 10))
        self.button.grid(row=0, column=1)

        label = Tk.Label(self.top_frame, text='Status: ', justify='left')
        label.config(anchor='w')
        label.config(width=LABEL_WIDTH)
        label.config(height=LABEL_HEIGHT)
        label.config(font=("", FONT_SIZE))
        label.config(bg='white')
        label.grid(row=1, column=0)
        self.status_label = Tk.Label(self.top_frame, text='OFF')
        self.status_label.config(font=("", FONT_SIZE))
        self.status_label.config(bg='white')
        self.status_label.grid(row=1, column=1)

        label = Tk.Label(self.top_frame, text='Pulse Length (microseconds): ')
        label.config(anchor='w')
        label.config(width=LABEL_WIDTH)
        label.config(height=LABEL_HEIGHT)
        label.config(font=("", FONT_SIZE))
        label.config(bg='white')
        label.grid(row=2, column=0)

        self.pulse_label = Tk.Label(self.top_frame, text=str(int(pulse_length * 1000000)))
        self.pulse_label.config(anchor='w')
        self.pulse_label.config(bg='white')
        self.pulse_label.config(font=("", FONT_SIZE))
        self.pulse_label.grid(row=2, column=1)

        label = Tk.Label(self.top_frame, text='Period (milliseconds): ')
        label.config(anchor='w')
        label.config(width=LABEL_WIDTH)
        label.config(height=LABEL_HEIGHT)
        label.config(font=("", FONT_SIZE))
        label.config(bg='white')
        label.grid(row=3, column=0)

        self.wave_label = Tk.Label(self.top_frame, text=str(int(wave_length * 1000)))
        self.wave_label.configure(bg='white')
        self.wave_label.config(font=("", FONT_SIZE))
        self.wave_label.grid(row=3, column=1)

        self.draw_canvas(wave_length, pulse_length)

    def draw_canvas(self, wave_length, pulse_length):
        f = Figure(figsize=(6, 3), dpi=100)
        self.ax = f.add_subplot(111)
        self.ax.set_title('Wave Graph')
        self.ax.set_xlabel('Time (ms)')
        self.ax.set_ylabel('Volts (V)')

        # get data points from wave_length & pulse_length
        x = [0, 50, 50]
        y = [0, 0, 3.3, 3.3]
        x.append(50+(float(pulse_length))*10000)
        x.append(50+(float(pulse_length))*10000)
        y.append(0)

        x.append(x[-1] + (float(wave_length) * 1000) - (float(pulse_length) * 1000))
        y.append(0)

        y.append(3.3)
        x.append(x[-1])

        y.append(3.3)
        x.append(x[-1]+(float(pulse_length))*10000)
        x.append(x[-1])
        y.append(0)

        x.append(x[-1] + 50)
        y.append(0)

        self.line, = self.ax.plot(x, y)

        self.canvas = FigureCanvasTkAgg(f, master=self.label_frame)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=1)

    def change_focused_inductor(self, num):
        self.focused = num
        state = self.model.get_state_onoff(num)
        wave_length = self.model.get_wave_length(num)
        pulse_length = self.model.get_pulse_length(num)
        self.draw_canvas(wave_length, pulse_length)
        status_text = 'OFF' if state == 0 else 'ON'
        self.status_label.configure(text=status_text)
        self.pulse_label.configure(text=str(int(pulse_length * 1000000)))
        self.wave_label.configure(text=str(int(wave_length * 1000)))
        self.button.configure(text=str(num+1))
        background = 'red' if state == 0 else 'green'
        self.button.configure(background=background)

    def update_focused_inductor(self, num):
        if num == self.focused:
            self.change_focused_inductor(num)

    def register(self, controller, model):
        self.controller = controller
        self.model = model

if __name__ == '__main__':
    tk = Tk.Tk()
    w = WaveWidget(tk)
    tk.mainloop()
