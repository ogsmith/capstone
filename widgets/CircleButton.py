import Tkinter as tk

class CircleButton(tk.Canvas):
    def __init__(self, parent, text, width, height, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1,
            relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = self.create_oval((padding,padding,
            width+padding, height+padding), outline=color, fill=color)
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

        self.create_text((height/2,width/2), text=text)

    def _on_press(self, event):
        self.configure(relief="sunken")
        self.configure(borderwidth=1)

    def _on_release(self, event):
        self.configure(relief="raised")
        self.configure(borderwidth=0)
        if self.command is not None:
            self.command()

if __name__ == '__main__':
    Tk = tk.Tk()
    app = CircleButton(Tk, 'test', 100, 100, 'red')
    app.pack()
    app.mainloop()
