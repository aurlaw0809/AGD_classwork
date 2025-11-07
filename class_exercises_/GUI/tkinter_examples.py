import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self,
                            text="Olfana!",
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
        self.txt.grid(row = 0,
                      column = 0,
                      padx=10,
                      pady=10,
                      sticky="NEWS"
                      )
        self.btn.grid(row = 0,
                      column = 1,
                      padx=10,
                      pady=10,
                      sticky="NEWS"
                      )
        self.edt.grid(row = 1,
                      column = 0,
                      padx=10,
                      pady=10,
                      sticky="NEWS"
                      )
        self.sld.grid(row = 1,
                      column = 1,
                      padx=10,
                      pady=10,
                      sticky="NEWS"
                      )


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Olfana!!.gov.uk")

    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()