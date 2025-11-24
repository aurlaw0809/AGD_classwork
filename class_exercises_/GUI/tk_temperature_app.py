import tkinter as tk
from tkinter import ttk
from class_exercises_.GUI.tk_temperature import Temperature

class TemperatureApp(tk.Tk):
    def __init__(self):
       super().__init__()

       #main blocking frames
       self.title("Temperature Convertor App!")
       self.top_frame = tk.Frame(self)
       self.bottom_frame = tk.Frame(self)

       self.top_frame.grid(row=0, column=0, columnspan=7, rowspan=2, sticky='nsew')
       self.bottom_frame.grid(row=2, column=0, columnspan=7, rowspan=4, sticky='nsew')

       # blocking in top frame
       self.go_frame = GoFrame(self.top_frame)
       self.title_frame = TitleFrame(self.top_frame)

       self.title_frame.grid(row=0, column=0, columnspan=5, rowspan=2, sticky='nsew')
       self.go_frame.grid(row=0, column=5, columnspan=2, rowspan=2, sticky='nsew')

       #blocking in bottom frame
       self.temp_title_frame = TempTitleFrame(self.bottom_frame)
       self.select_temp_frame = SelectTempFrame(self.bottom_frame)

       self.unit_title_frame = UnitTitleFrame(self.bottom_frame)
       self.select_unit_frame = SelectUnitFrame(self.bottom_frame)

       self.celsius_frame = CelsiusFrame(self.bottom_frame)
       self.fahrenheit_frame = FahrenheitFrame(self.bottom_frame)
       self.kelvin_frame = KelvinFrame(self.bottom_frame)

       self.background_frame = BackgroundFrame(self.bottom_frame)

       self.temp_title_frame.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='nsew')
       self.select_temp_frame.grid(row=1, column=0, columnspan=4, rowspan=1, sticky='nsew')

       self.unit_title_frame.grid(row=2, column=0, columnspan=4, rowspan=1, sticky='nsew')
       self.select_unit_frame.grid(row=3, column=0, columnspan=4, rowspan=1, sticky='nsew')

       self.celsius_frame.grid(row=0, column=4, columnspan=1, rowspan=2, sticky='nsew')
       self.fahrenheit_frame.grid(row=0, column=5, columnspan=1, rowspan=2, sticky='nsew')
       self.kelvin_frame.grid(row=0, column=6, columnspan=1, rowspan=2, sticky='nsew')

       self.background_frame.grid(row=2, column=4, columnspan=3, rowspan=2, sticky='nsew')
       #end thing cause weird spacing

class TitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.txt = tk.Label(self,
                            text="TEMPERATURE CONVERTOR",
                            font=("Arial", 24))

        self.txt.grid(row=0, column=0, columnspan=5, rowspan=2, sticky='nsew')

class GoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.btn = tk.Button(self,
                             text="GO!",
                             font=("Arial", 24))

        self.btn.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='nsew')

class TempTitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

class SelectTempFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

class UnitTitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

class SelectUnitFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

class CelsiusFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

class FahrenheitFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

class KelvinFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

class BackgroundFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

if __name__ == '__main__':
    app = TemperatureApp()
    app.mainloop()
