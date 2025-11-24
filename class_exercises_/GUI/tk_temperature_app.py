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

        self.txt = tk.Label(self,
                            text="SELECT TEMP",
                            font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='nsew')

class SelectTempFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.plus = tk.Button(self,
                             text = "+",
                             font=("Arial", 24))

        self.minus = tk.Button(self,
                               text = "-",
                               font=("Arial", 24))

        self.entry = tk.Entry(self,
                              font=("Arial", 18))

        self.plus.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew')
        self.minus.grid(row=0, column=1, columnspan=1, rowspan=1, sticky='nsew')
        self.entry.grid(row=0, column=2, columnspan=2, rowspan=1, sticky='nsew')

class UnitTitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.txt = tk.Label(self,
                            text="SELECT UNIT",
                            font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='nsew')

class SelectUnitFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.options = ['C', 'F', 'K', '?']

        # Create a tk variable which will hold the value of the selected unit
        self.unit_choice = tk.StringVar()
        self.unit_choice.set(self.options[0])

        # Create radio buttons (list comprehension)
        self.unit_options = [tk.Radiobutton(self, text=unit,
                                              value=unit,
                                              variable=self.unit_choice,
                                              )
                               for unit in self.options]

        self.place_widgets()

    def place_widgets(self):
        i = 0
        for item in self.unit_options:
            item.grid(row=0, column=i, columnspan=1, rowspan=1, sticky='nsew')
            i += 1

class CelsiusFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.txt = tk.Label(self,
                            text="C",
                            font=("Arial", 20))

        self.temp = tk.Label(self,
                             text=0,
                             font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew')
        self.temp.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='nsew')

class FahrenheitFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.txt = tk.Label(self,
                            text="F",
                            font=("Arial", 20))

        self.temp = tk.Label(self,
                             text=0,
                             font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew')
        self.temp.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='nsew')

class KelvinFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.txt = tk.Label(self,
                            text="K",
                            font=("Arial", 20))

        self.temp = tk.Label(self,
                             text=0,
                             font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew')
        self.temp.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='nsew')

class BackgroundFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.txt = tk.Label(self,
                            text="FEELS LIKE",
                            font=("Arial", 20))

        self.sld = tk.Scale(self,
                            from_=0,
                            to=100,
                            orient=tk.HORIZONTAL,
                            )

        self.txt.grid(row=0, column=0, columnspan=3, rowspan=1, sticky='nsew')
        self.sld.grid(row=1, column=0, columnspan=3, rowspan=1, sticky='nsew')

if __name__ == '__main__':
    app = TemperatureApp()
    app.mainloop()
