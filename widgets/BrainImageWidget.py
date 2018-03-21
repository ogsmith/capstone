import os
import Tkinter as Tk

BRAIN_IMAGE = 'brain_75.gif'

INDUCTOR_LOCATIONS = {
    0: (250, 300),
    1: (200, 200),
    2: (400, 100),
    3: (500, 400)
}

class BrainImageWidget():

    def __init__(self, master):
        self.master = master
        self.controller = None
        self.model = None
        current_path = os.path.dirname(os.path.abspath(__file__))
        brain_image_path = os.path.join(os.path.split(current_path)[0], BRAIN_IMAGE)
        self.brain_image = Tk.PhotoImage(file=brain_image_path)
        self.brain_image.zoom(1, 2)

        self.brain_label = Tk.Label(master, image=self.brain_image)
        self.brain_label.grid(row=0)
        self.buttons = {}
        self.create_buttons()

    def create_buttons(self):
        for number, location in INDUCTOR_LOCATIONS.iteritems():
            button = Tk.Button(self.master, text=number, height=4, width=8, border=1, bg='red')
            button.place(x=location[0], y=location[1])
            button['command'] = self.button_command
            self.buttons[number] = button

    def button_command(self):
        print 'press'

    def register(self, controller, model):
        self.controller = controller
        self.model = model

    def change_inductor_state(self, number, value):
        try:
            button = self.buttons[number]
            button['bg'] = 'red' if value is False else 'green'
        except KeyError:
            pass

if __name__ == '__main__':
    tk = Tk.Tk()
    tk.title('GUI')
    tk.resizable(width=False, height=False)
    tk.minsize(width=700, height=500)
    b = BrainImageWidget(tk)
    tk.mainloop()