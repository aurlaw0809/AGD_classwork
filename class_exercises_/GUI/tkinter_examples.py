import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self,
                            text="RAHHHHHHH!",
                            bg="green yellow",
                            fg="sea green")

        self.btn = tk.Button(self,
                             text="Press me... if you dare..?",
                             bg="sea green",
                             fg="lemon chiffon",
                             activebackground="brown4",
                             activeforeground="misty rose")

        self.edt = tk.Entry(self)

        self.sld = tk.Scale(self,
                            from_=0,
                            to=100,
                            orient=tk.VERTICAL,
                            )

        self.config(bg="green yellow")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}

        self.txt.grid(row = 0,
                      column = 0,
                      **settings
                      )
        self.btn.grid(row = 0,
                      column = 1,
                      **settings
                      )
        self.edt.grid(row = 1,
                      column = 0,
                      **settings
                      )
        self.sld.grid(row = 1,
                      column = 1,
                      **settings
                      )

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Not a Scam!!.gov.uk")
    root.geometry('500x500+100+100')

    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()