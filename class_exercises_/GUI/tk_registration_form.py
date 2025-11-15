import tkinter as tk
from tkinter import ttk

from class_exercises_.GUI.tkinter_examples import MainFrame

class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Registration Form')
        self.registration_frame = RegistrationFormFrame(self)
        self.background_color_frame = RegistrationFormFrame(self)

        self.registration_frame.pack(side=tk.LEFT)
        self.background_color_frame.pack(side=tk.LEFT)

class RegistrationFormFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}

if __name__ == '__main__':

    registration_form = RegistrationForm()
    registration_form.geometry('500x500+100+100')
    registration_form.mainloop()