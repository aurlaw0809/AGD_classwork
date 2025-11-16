import tkinter as tk
from tkinter import ttk

from class_exercises_.GUI.tkinter_examples import MainFrame

class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Registration Form')
        self.registration_frame = RegistrationFormFrame(self)
        self.gender_choice_frame = GenderChoiceFrame(self)
        self.entry_box_frame = EntryBoxFrame(self)
        self.country_choice_frame = CountryChoiceFrame(self)

        self.registration_frame.grid(row=0, column=0)
        self.entry_box_frame.grid(row=0, column=1)
        self.gender_choice_frame.grid(row=1, column=1)
        self.country_choice_frame.grid(row=2, column=1)

#registration left side labels
class RegistrationFormFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #labels
        self.title = tk.Label(self, text="Registration Form", justify="left", anchor="w")
        self.name_label = tk.Label(self, text="Name", justify="left", anchor="w")
        self.email_label = tk.Label(self, text="Email", justify="left", anchor="w")
        self.gender_label = tk.Label(self, text="Gender", justify="left", anchor="w")
        self.country_label = tk.Label(self, text="Country", justify="left", anchor="w")
        self.programming_label = tk.Label(self, text="Programming", justify="left", anchor="w")

        #submit button
        self.submit = tk.Button(self, text="Submit",)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 20, 'pady': 10, 'sticky': 'nswe'}

        self.name_label.grid(row=0,
                             column=0,
                             **settings)

        self.email_label.grid(row=1,
                              column=0,
                              **settings)

        self.gender_label.grid(row=2,
                               column=0,
                               **settings)

        self.country_label.grid(row=3,
                                column=0,
                                **settings)

        self.programming_label.grid(row=4,
                                    column=0,
                                    **settings)

#email and name entry buttons
class EntryBoxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.name = tk.Entry(self)
        self.email = tk.Entry(self)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 20, 'pady': 10, 'sticky': 'nswe'}

        self.name.grid(row=0,
                       column=0,
                       **settings)

        self.email.grid(row=1,
                        column=0,
                        **settings)

#gender choice buttons
class GenderChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Gender choices
        self.options = ['Male', 'Female']

        # Create a tk variable which will hold the value of the selected gender
        self.gender_choice = tk.StringVar()
        self.gender_choice.set(self.options[0])

        # Create radio buttons (list comprehension)
        self.gender_options = [tk.Radiobutton(self, text=gender,
                                             value=gender,
                                             variable=self.gender_choice,
                                             # command=self.change_color
                                             )
                              for gender in self.options]

        self.place_widgets()

    def place_widgets(self):
        for item in self.gender_options:
            item.pack(side=tk.LEFT, anchor='w', padx=(5, 10), pady=5)

#country choice button
class CountryChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.current_country = tk.StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.current_country)

        self.combobox['values'] = ('United Kingdom', 'UK', 'England', 'Ireland', 'Northern Ireland', 'Wales',
                                           'Scotland', 'Britain')
        self.combobox['state'] = 'readonly'

        self.current_value = self.combobox.get()

        self.place_widgets()

    def place_widgets(self):
        self.combobox.grid(row=0, column=0)
    #
if __name__ == '__main__':

    registration_form = RegistrationForm()
    registration_form.geometry('500x500+100+100')
    registration_form.mainloop()