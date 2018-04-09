from copy import copy
import os
import Tkinter as Tk

BRAIN_IMAGE = 'brain_375_{}.gif'

# LEFT_INDUCTOR_LOCATIONS = {
    # 1: (10, 190),
    # 2: (80, 70),
    # 3: (250, 30),
    # 4: (400, 70),
    # 5: (460, 175),
    # 6: (120, 110),
    # 7: (250, 110),
    # 8: (360, 110),
    # 9: (80, 190),
    # 10: (250, 190),
    # 11: (400, 190)	
# }

# RIGHT_INDUCTOR_LOCATIONS = {
    # 12: (620, 110),
    # 13: (750, 110),
    # 14: (860, 110),
    # 15: (580, 190),
    # 16: (750, 190),
    # 17: (900, 190)	
# }
LEFT_INDUCTOR_LOCATIONS = {
    1: (7, 142),
    2: (60, 52),
    3: (187, 22),
    4: (300, 54),
    5: (345, 131),
    6: (100, 82),
    7: (187, 82),
    8: (260, 82),
    9: (60, 142),
    10: (187, 142),
    11: (300, 142)	
}

RIGHT_INDUCTOR_LOCATIONS = {
    12: (465, 82),
    13: (562, 82),
    14: (645, 82),
    15: (435, 142),
    16: (562, 142),
    17: (675, 142)	
}

class BrainImageWidget():

    def __init__(self, master, side='right', wave_widget=None):
        self.wave_widget = wave_widget
        self.master = master
        self.side = side
        self.controller = None
        self.model = None
        current_path = os.path.dirname(os.path.abspath(__file__))
        brain_image_name = copy(BRAIN_IMAGE)
        brain_image_name = brain_image_name.format(self.side)
        brain_image_path = os.path.join(os.path.split(current_path)[0], brain_image_name)
        self.brain_image = Tk.PhotoImage(file=brain_image_path)
        self.brain_image.zoom(1, 2)

        frame_text = 'Right ' if self.side.lower() == 'right' else 'Left '
        frame_text += 'Side of Brain'
        self.frame = Tk.LabelFrame(master, text=frame_text, padx=10, pady=10)
        self.frame.configure(background='white')
        self.brain = Tk.Label(self.frame, image=self.brain_image)
        self.brain.grid(row=1, column=0)
        if side == 'left':
            self.frame.grid(row=0, column=0)
        else:
            self.frame.grid(row=0, column=1)
        self.buttons = {}
        self.create_buttons()

    def create_buttons(self):
        inductors = RIGHT_INDUCTOR_LOCATIONS if self.side == 'right' else LEFT_INDUCTOR_LOCATIONS
        for number, location in inductors.iteritems():
            button = Tk.Button(self.master, text=number, height=2, width=4, border=1, bg='red')
            button.place(x=location[0], y=location[1])
            button['command'] = lambda number=number: self.button_command(number)
            self.buttons[number] = button

    def button_command(self, number):
        self.wave_widget.change_focused_inductor(number)

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