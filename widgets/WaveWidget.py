import Tkinter as Tk

class WaveWidget():
    def __init__(self, master, inductor_num=0, wave_length=.5, pulse_length=.0002):
        self.master = master
        self.controller = None
        self.model = None
        self.label_frame = Tk.Frame(master)
        self.label_frame.configure(background='white')
        self.label_frame.grid(row=0)
        self.canvas = Tk.Canvas(self.label_frame, width=500, height=300)
        self.canvas.configure(background='white')
        self.top_frame = Tk.LabelFrame(self.label_frame, width=500)
        self.top_frame.grid(row=0)
        self.canvas.grid(row=1)

        label = Tk.Label(self.top_frame, text='Inductor: ')
        label.grid(row=0, column=0)
        self.button = Tk.Button(self.top_frame, width=10, height=4, text=str(inductor_num), bg='red')
        self.button.grid(row=0, column=1)

        label = Tk.Label(self.top_frame, text='Status: ')
        label.grid(row=0, column=2)
        self.status_label = Tk.Label(self.top_frame, text='OFF')
        self.status_label.grid(row=0, column=3)

        label = Tk.Label(self.top_frame, text='Pulselength: ')
        label.grid(row=0, column=4)

        self.pulse_label = Tk.Label(self.top_frame, text=str(pulse_length))
        self.pulse_label.grid(row=0, column=5)

        label = Tk.Label(self.top_frame, text='Wavelength: ')
        label.grid(row=0, column=6)

        self.wave_label = Tk.Label(self.top_frame, text=str(wave_length))
        self.wave_label.grid(row=0, column=7)
        self.draw_canvas(wave_length, pulse_length)

    def draw_canvas(self, wave_length, pulse_length):
        # main wave shape
        self.canvas.create_line(0, 250, 100, 250, 100, 100, 200, 100, 200, 250, 300, 250, 300, 100, 400, 100, 400, 250, 500, 250)
        # wavelength
        self.canvas.create_line(100, 30, 300, 30)
        self.canvas.create_line(100, 20, 100, 40)
        self.canvas.create_line(300, 20, 300, 40)
        self.canvas.create_text(200, 20, text='Wavelength = {}'.format(wave_length))
        # pulselength
        self.canvas.create_line(200, 70, 300, 70)
        self.canvas.create_line(200, 80, 200, 60)
        self.canvas.create_line(300, 80, 300, 60)
        self.canvas.create_text(250, 50, text='Pulselength = {}'.format(pulse_length))

    def change_focused_inductor(self, num):
        state = self.model.get_state_onoff(num)
        wave_length = self.model.get_wave_length(num)
        pulse_length = self.model.get_pulse_length(num)
        self.clear_canvas()
        self.draw_canvas(wave_length, pulse_length)
        status_text = 'OFF' if state == 0 else 'ON'
        self.status_label.configure(text=status_text)
        self.pulse_label.configure(text=str(pulse_length))
        self.wave_label.configure(text=str(wave_length))
        self.button.configure(text=str(num))
        background = 'red' if state == 0 else 'green'
        self.button.configure(background=background)

    def register(self, controller, model):
        self.controller = controller
        self.model = model

    def clear_canvas(self):
        self.canvas.delete('all')

if __name__ == '__main__':
    tk = Tk.Tk()
    w = WaveWidget(tk)
    tk.mainloop()
