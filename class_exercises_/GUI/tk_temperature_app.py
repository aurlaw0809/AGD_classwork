import tkinter as tk
from _ast import Return
from tkinter import ttk
from class_exercises_.GUI.tk_temperature import Temperature

class TemperatureApp(tk.Tk):
    def __init__(self):
       super().__init__()

       self.color = tk.StringVar()

       self.bind('<Return>', lambda _: self.go_frame.btn.invoke())

       #main blocking frames
       self.title("Temperature Convertor App!")

       # blocking in top frame
       self.go_frame = GoFrame(self)
       self.title_frame = TitleFrame(self)

       self.title_frame.grid(row=0, column=0, columnspan=5, rowspan=2, sticky='nsew')
       self.go_frame.grid(row=0, column=5, columnspan=2, rowspan=2, sticky='nsew')

       #blocking in bottom frame
       self.temp_title_frame = TempTitleFrame(self)
       self.select_temp_frame = SelectTempFrame(self)

       self.unit_title_frame = UnitTitleFrame(self)
       self.select_unit_frame = SelectUnitFrame(self)

       self.celsius_frame = CelsiusFrame(self)
       self.fahrenheit_frame = FahrenheitFrame(self)
       self.kelvin_frame = KelvinFrame(self)

       self.background_frame = BackgroundFrame(self)

       self.temp_title_frame.grid(row=2, column=0, columnspan=4, rowspan=1, sticky='nsew')
       self.select_temp_frame.grid(row=3, column=0, columnspan=4, rowspan=1, sticky='nsew')

       self.unit_title_frame.grid(row=4, column=0, columnspan=4, rowspan=1, sticky='nsew')
       self.select_unit_frame.grid(row=5, column=0, columnspan=4, rowspan=1, sticky='nsew')

       self.celsius_frame.grid(row=2, column=4, columnspan=1, rowspan=2, sticky='nsew')
       self.fahrenheit_frame.grid(row=2, column=5, columnspan=1, rowspan=2, sticky='nsew')
       self.kelvin_frame.grid(row=2, column=6, columnspan=1, rowspan=2, sticky='nsew')

       self.background_frame.grid(row=4, column=4, columnspan=3, rowspan=2, sticky='nsew')

class TitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.txt = tk.Label(self,
                            text="TEMPERATURE CONVERTOR",
                            font=("Arial", 24),
                            justify='center')

        self.txt.grid(row=0, column=0, columnspan=5, rowspan=2, sticky='nsew', padx=30, pady=10)

class GoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.btn = tk.Button(self,
                             text="GO!",
                             font=("Arial", 24),
                             command = self.convert)

        self.btn.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='nsew', padx=10, pady=10)
        #self.btn.winfo_geometry()

    def convert(self):
        current_temp = self.master.select_temp_frame.entry.get()
        current_unit = self.master.select_unit_frame.unit_choice.get()

        if current_unit == 'F':
            temp=Temperature(fahrenheit=int(current_temp))
        elif current_unit == 'K':
            temp=Temperature(kelvin=int(current_temp))
        else:
            temp=Temperature(celsius=int(current_temp))

        self.master.celsius_frame.current_temp.set(f'{temp.celsius:.1f}')
        self.master.fahrenheit_frame.current_temp.set(f'{temp.fahrenheit:.1f}')
        self.master.kelvin_frame.current_temp.set(f'{temp.kelvin:.1f}')

class TempTitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.txt = tk.Label(self,
                            text="SELECT TEMP",
                            font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='nsew', padx=10, pady=10)

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

        self.plus.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)
        self.minus.grid(row=0, column=1, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)
        self.entry.grid(row=0, column=2, columnspan=2, rowspan=1, sticky='nsew', padx=10, pady=10)

        #TODO make minus and plus buttons work

class UnitTitleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")

        self.txt = tk.Label(self,
                            text="SELECT UNIT",
                            font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='nsew', padx=10, pady=10)

class SelectUnitFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.options = ['\u00B0C', 'F', 'K']

        # Create a tk variable which will hold the value of the selected unit
        self.unit_choice = tk.StringVar()
        self.unit_choice.set(self.options[0])

        # Create radio buttons (list comprehension)
        self.unit_options = [tk.Radiobutton(self, text=unit,
                                              value=unit,
                                              variable=self.unit_choice,
                                              font=("Arial", 20),
                                              )
                               for unit in self.options]

        self.place_widgets()

    def place_widgets(self):
        i = 0
        for item in self.unit_options:
            item.grid(row=0, column=i, columnspan=1, rowspan=1, sticky='nsew', padx=40, pady=10)
            i += 1

class CelsiusFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")
        self.current_temp = tk.StringVar()
        self.current_temp.set('0')

        self.txt = tk.Label(self,
                            text="\u00B0C",
                            font=("Arial", 20))

        self.temp = tk.Label(self,
                             textvariable=self.current_temp,
                             font=("Arial", 20))


        self.txt.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)
        self.temp.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)


class FahrenheitFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")
        self.current_temp = tk.StringVar()
        self.current_temp.set('0')

        self.txt = tk.Label(self,
                            text="F",
                            font=("Arial", 20))

        self.temp = tk.Label(self,
                             textvariable=self.current_temp,
                             font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)
        self.temp.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)

class KelvinFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="lemon chiffon")
        self.current_temp = tk.StringVar()
        self.current_temp.set('0')

        self.txt = tk.Label(self,
                            text="K",
                            font=("Arial", 20))

        self.temp = tk.Label(self,
                             textvariable=self.current_temp,
                             font=("Arial", 20))

        self.txt.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)
        self.temp.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='nsew', padx=10, pady=10)

class BackgroundFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="medium turquoise")

        self.txt = tk.Label(self,
                            text="FEELS LIKE",
                            font=("Arial", 20))

        self.sld = tk.Scale(self,
                            from_=0,
                            to=16777215,
                            orient=tk.HORIZONTAL,
                            sliderlength=40,
                            command=self.on_change)

        self.txt.grid(row=0, column=0, columnspan=3, rowspan=1, sticky='nsew', padx=10, pady=10)
        self.sld.grid(row=1, column=0, columnspan=3, rowspan=1, sticky='nsew', padx=10, pady=10)

    def on_change(self, value):
        hex_bg = hex(int(value))[2:].upper()
        while len(hex_bg) < 6:
            hex_bg += '0'
        hex_bg = '#' + hex_bg
        self.master.config(bg=hex_bg)

if __name__ == '__main__':
    app = TemperatureApp()
    app.mainloop()
