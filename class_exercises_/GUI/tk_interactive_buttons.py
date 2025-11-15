import tkinter as tk

from class_exercises_.GUI.tkinter_examples import MainFrame


class ClickApp(tk.Tk):
    """ Button clicker application """

    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()

        self.title('Not a Scam pt2!!.gov.uk')
        self.clicker_frame = ButtonClicker(self)
        self.background_color_frame = BackgroundColorFrame(self)

        self.clicker_frame.pack(side=tk.LEFT)
        self.background_color_frame.pack(side=tk.LEFT)


class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)
        self.counter = 0

        self.txt = tk.Label(self,
                            text="RAHHHHHHH!",
                            bg="green yellow",
                            fg="sea green")

        self.btn = tk.Button(self,
                             text="Press me... if you dare..?",
                             bg="sea green",
                             fg="lemon chiffon",
                             activebackground="brown4",
                             activeforeground="misty rose",
                             command=self.click_button)

        self.counter_label = tk.Label(self,
                            text="No clicks!",
                            bg="green yellow",
                            fg="sea green")


        self.config(bg="green yellow")

        self.place_widgets()


    def click_button(self):

        self.counter += 1
        self.counter_label.config(text=str(self.counter))

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}

        self.txt.grid(row=0,
                      column=0,
                      **settings
                      )
        self.btn.grid(row=1,
                      column=0,
                      **settings
                      )

        self.counter_label.grid(row=2,
                      column=0,
                      **settings
                      )



        self.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)


class BackgroundColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Color choices
        self.colors = ['red bean paste', 'lime green', 'blellow']

        # Create a tk variable which will hold the value of the selcted color
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             #command=self.change_color
                                             )
                              for color in self.colors]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)


if __name__ == '__main__':
    app = ClickApp()

    #root = tk.Tk()
    app.geometry('500x500+100+100')

    app.mainloop()